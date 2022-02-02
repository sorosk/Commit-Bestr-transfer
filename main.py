import os
import csv_maker

# Username for BESTR
username = os.environ['username']
pwd = os.environ['pwd']

# CSV writing
I1 = 1000
I2 = 2000
I3 = 3000
I4 = 4000
I5 = 5000
I6 = 6000
I7 = 7000
I8 = 8000
Tid = "2:02"
Crawl = 1100
Egen = 1200
Kick = 1300
Bein = 1400
Arm = 1500
Andre = 1600
Teknikkdrill = 1700

csv_maker.makefile(I1, I2, I3, I4, I5, I6, I7, I8,
Tid, Crawl, Egen, Kick, Bein, Arm, Andre, Teknikkdrill)
