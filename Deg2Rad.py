import math
import csv
from Quaternion import Quat

with open('CartesianOut.csv', 'rt') as f:
    reader = csv.reader(f)
    outFile = open("ConvertedCartesianRadians.csv", 'w')
    writer = csv.writer(outFile, delimiter= ",")
    writer.writerow(["Time","X","Y","Z","A","B","C","D"])
    # writer = csv.duictWriter(outFile, fieldnames = ["Time","X","Y","Z","A","B","C","S","T"], delimiter= ",")
    # dictWriter.writeheader()

    next(reader, None)

    for row in reader:
        # get vec3 rotation
        x = float(row[4])
        y = float(row[5])
        z = float(row[6])

        newQuat = Quat((x,y,z))

        a = newQuat.q[0]
        b = newQuat.q[1]
        c = newQuat.q[2]
        d = newQuat.q[3]

        newRow = [row[0],row[1],row[2],row[3],a,b,c,d]
        writer.writerow(newRow)
        print newRow
