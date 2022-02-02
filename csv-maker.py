import csv
from datetime import date

def makefile(I1, I2, I3, I4, I5, I6, I7, I8, Tid, Crawl, Egen, Kick, Bein, Arm, Andre, Teknikkdrill):
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

    #Creating filename of todays date
    current_date = date.today()
    current_date_string = str(current_date)+ '.csv'

    #Creating CSV file
    with open(current_date_string, 'w', newline='') as csvfile: #The CSV file name is todays date
        filewriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header) #Row of names/headers
        filewriter.writerow(data) #Row of data
