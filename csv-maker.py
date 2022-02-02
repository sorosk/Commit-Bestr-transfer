import csv
from datetime import date

def makefile(I1, I2, I3, I4, I5, I6, I7, I8, Tid, Crawl, Egen, Kick, Bein, Arm, Andre, Teknikkdrill):
    #Creating filename of todays date
    current_date = date.today()
    current_date_string = str(current_date_and_time)

    #Creating CSV file
    with open(current_date_string, 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([
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
        'Teknikkdrill'
        ])
        filewriter.writerow([
        current_date_string,
        I1,
        I2,
        I3,
        I4,
        I5,
        I6,
        I7,
        I8,
        Tid svømming,
        Crawl,
        Egen,
        Kick,
        Bein,
        Arm,
        Andre,
        Teknikkdrill
        ])
