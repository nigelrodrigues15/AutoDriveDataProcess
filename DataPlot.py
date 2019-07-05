import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
# plt.switch_backend('agg')
import csv

steering = []
with open('table.csv') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    next(csv_reader, None)
    for row in csv_reader:
        steering.append(np.float(row[5]))

plt.figure()
plt.hist(steering, bins= 30, color= 'blue', linewidth=0.1)
plt.title('Angle Histogram')
plt.xlabel('Steering Angle')
plt.ylabel('Counts')
# print(steering)

plt.show()