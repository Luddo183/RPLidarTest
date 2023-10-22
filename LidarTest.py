from rplidar import RPLidar
import matplotlib.pyplot as plt

lidar = RPLidar("/dev/ttyUSB0")

fig = plt.figure(dpi=200)
ax = fig.add_subplot(projection="polar")

scans = []
angles = []
distances = []

for i, scan in enumerate(lidar.iter_scans()):
        print("%d: Got %d measurements" % (i, len(scan)))
        scans += scan
        if i == 0: #Change the number at which the loop breaks to do more or less scans
            break

for i in scans:
    q, a, d = i #q = quality of scan, a = angle, d = distance from origin
    angles.append(a)
    distances.append(d/10) #distance comes from the sensor in millimeters, change the value at which d is divided by to change unit

lidar.stop()
lidar.stop_motor()
lidar.disconnect()

c = ax.scatter(angles, distances, marker="o")
ax.set_ylim(0, 40) #use this to constrain the graph to only a certain maximum y-axis value

plt.savefig("lidarGraph.png", bbox_inches = "tight")
