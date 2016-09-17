import math
import csv

with open('CartesianOut.csv', 'rt') as f:
    reader = csv.reader(f)
    outFile = open("ConvertedCartesianRadians.csv", 'w')
    writer = csv.writer(outFile, delimiter= ",")
    writer.writerow(["Time","X","Y","Z","A","B","C","D","T"])
    # writer = csv.duictWriter(outFile, fieldnames = ["Time","X","Y","Z","A","B","C","S","T"], delimiter= ",")
    # dictWriter.writeheader()

    next(reader, None)

    for row in reader:
        a = float(row[4])
        b = float(row[5])
        c = float(row[6])
        d = float(row[7])

        row[4] = math.radians(a)
        row[5] = math.radians(b)
        row[6] = math.radians(c)
        row[7] = math.radians(d)
        
        writer.writerow(row)
        print(a)
