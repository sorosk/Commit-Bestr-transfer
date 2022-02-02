import csv
from datetime import date

def makefile(I1, I2, I3, I4, I5, I6, I7, I8, Tid, Crawl, Egen, Kick, Bein, Arm, Andre, Teknikkdrill):
    #Just for debug
    I1 = 1000
    I2 = 2000
    I3 = 3000
    I4 = 4000
    I5 = 5000
    I6 = 6000
    I7 = 7000
    I8 = 8000
    Tid_svømming = "2:02"
    Crawl = 1100
    Egen = 1200
    Kick = 1300
    Bein = 1400
    Arm = 1500
    Andre = 1600
    Teknikkdrill = 1700

    #List of data
    data = [
        date.today(),
        I1,
        I2,
        I3,
        I4,
        I5,
        I6,
        I7,
        I8,
        Tid,
        Crawl,
        Egen,
        Kick,
        Bein,
        Arm,
        Andre,
        Teknikkdrill
        ]

    #List of names
    header = [
        'Dato',
        'I1',
        'I2',
        'I3',
        'I4',
        'I5',
        'I6',
        'I7',
        'I8',
        'Tid svømming',
        'Crawl',
        'Egen',
        'Kick',
        'Bein',
        'Arm',
        'Andre',
        'Teknikkdrill']

    #Creating filename of todays date
    current_date = date.today()
    current_date_string = str(current_date)+ '.csv'

    #Creating CSV file
    with open(current_date_string, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header)
        filewriter.writerow(data)
