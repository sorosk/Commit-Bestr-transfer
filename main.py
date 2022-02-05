import csv_maker

#  Not used yet, caused error when not integrated with GitHub
'''
# Username for BESTR
username = os.environ['username']
pwd = os.environ['pwd']
'''

# CSV writing
plan = 'This is the training program.\r\nThis is newline'
i1 = 1000
i2 = 2000
i3 = 3000
i4 = 4000
i5 = 5000
i6 = 6000
i7 = 7000
i8 = 8000
time = "2:02:00"
crawl = 1100
own = 1200
kick = 1300
bein = 1400
arm = 1500
andre = 1600
drills = 1700

csv_maker.makefile(plan, i1, i2, i3, i4, i5, i6, i7, i8,
                   time, crawl, own, kick, bein, arm, andre, drills)
