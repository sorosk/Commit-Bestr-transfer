import csv
from datetime import date


def makefile(i1, i2, i3, i4, i5, i6, i7, i8, tid, crawl, egen, kick, bein, arm, andre, drills):
    # List of names
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

    # List of data
    data = [
        date.today(),
        i1,
        i2,
        i3,
        i4,
        i5,
        i6,
        i7,
        i8,
        tid,
        crawl,
        egen,
        kick,
        bein,
        arm,
        andre,
        drills
    ]

    # Creating filename of todays date
    current_date = date.today()
    current_date_string = str(current_date) + '.csv'

    # Creating CSV file
    with open(current_date_string, 'w', newline='') as csv_file:  # The CSV file name is todays date
        filewriter = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header)  # Row of names/headers
        filewriter.writerow(data)  # Row of data
