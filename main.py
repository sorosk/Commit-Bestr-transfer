import os
import csv_maker

# Username for BESTR
username = os.environ['username']
pwd = os.environ['pwd']

# CSV writing
i1 = 1000
i2 = 2000
i3 = 3000
i4 = 4000
i5 = 5000
i6 = 6000
i7 = 7000
i8 = 8000
tid = "2:02"
crawl = 1100
egen = 1200
kick = 1300
bein = 1400
arm = 1500
andre = 1600
Teknikkdrill = 1700

csv_maker.makefile(i1, i2, i3, i4, i5, i6, i7, i8,
                   tid, crawl, egen, kick, bein, arm, andre, teknikkdrill)
