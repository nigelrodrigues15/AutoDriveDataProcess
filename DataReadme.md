# Sensory Description

For each episode, we have collected sensory inputs from central, left and right camera.

The image size is 200 x 200, and since the image are sampled every 2 frames, so the number of the images are all even. Besides RGB, we also included the Depth map and Semantic segmentation for the central image.

### Depth Map
The "depth map" camera provides an image with 24 bit floating precision point codified in the 3 channels of the RGB color space. The order from less to more significant bytes is R -> G -> B.

To decodify the depth map:
1. we get the int24 by 
```
R + G*256 + B*256*256
```
2. Normalize it in the range [0, 1] by 
```
Ans / ( 256*256*256 - 1 )
```
3.  Finally multiply for the units that we want to get. We have set the far plane at 1000 metres.
```
Ans * far # far = 1000 is a constant for largest depth
```

### Semantic Segmentation
The "semantic segmentation" camera classifies every object in the view by displaying it in a different color according to the object class. E.g., pedestrians appear in a different color than vehicles.

The server provides an image with the tag information encoded in the red channel. A pixel with a red value of x displays an object with tag x. The following tags are currently available
- 0 = None
- 1 = Buildings
- 2 = Fences
- 3 = Other
- 4 = Pedestrians
- 5 = Poles
- 6 = RoadLines
- 7 = Roads
- 8 = Sidewalks
- 9 = Vegetation
- 10 = Vehicles
- 11 = Walls
- 12 = TrafficSigns

# Data Label Description

Measurements represent all the float data collected for each simulation step. Each measurement is associated with the respective sensor data (RGB image/Depth/semantic). The units of the measurements are on SI format, otherwise we specify the format. All measurements are stored in json files and contain the following information:

### Time-stamps
- frameNumber: uint64, frame counter number (not restarted on each episode)
- game_timestamp: uint32 (ms), In-game time-stamp, elapsed since the beginning of the current episode
- platform_timestamp: uint32 (ms), Time-stamp of the current frame, as given by the OS.

### Player Measurements
- acceleration: (m/s^2)
- forwardSpeed: (m/s)
- transform
    + location (x,y,z), Cartesian coordiantes
    + orientation [deprecated] (x,y,z). Orientation in Cartesian coordinates 
    + rotation (degrees) Pitch, roll, and yaw.

### Control
- steer/steer_noise: float, Steering angle between [-1.0, 1.0]
- throttle/throttle_noise: float, Throttle input between [ 0.0, 1.0]

**Note:** The actual steering angle depends on the vehicle used. In this work, we use the default Mustang with a maximum steering angle of 70 degrees. Hence the range of steer angle in terms of degree is [-70, 70]

**Note:** The <autopilotControl> in json is not used, it is not the real steer and throttle, please use steer_noise and throttle_noise.





