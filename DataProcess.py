import json
import os
import csv

with open('table.csv', 'wb+') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['episode', 'frameNumber', 'centerImage', 'LeftImage', 'rightImage', 'steer', 'throttle', 'forwardSpeed'])
writeFile.close()

for episode in range(0,10):
    episodeDir = "./CarlaData/episode_0000" + str(episode) + '/'
    for file in os.listdir(episodeDir):
        if file.startswith("measurements_"):
            lastDigit = int(file[-6])
            isOdd = lastDigit % 2

            if isOdd == False:
                with open(episodeDir + file) as json_file:  
                    print(episodeDir + file)
                    data = json.load(json_file)
                    Ep = episodeDir[-6:-1]
                    Fn = data['frameNumber']
                    cCam = 'CameraRGB_'+ file[-11:-5]
                    lCam = 'LeftRGB_'+ file[-11:-5]
                    rCam = 'RightRGB_'+ file[-11:-5]
                    St = data['steer_noise']
                    Th = data['throttle_noise']
                    try:
                        Fs = data['playerMeasurements']['forwardSpeed']
                    except:
                        Fs = "Not Available"

                    with open('table.csv', 'ab') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([Ep, Fn, cCam, lCam, rCam, St, Th, Fs])

csvFile.close()   
                 
