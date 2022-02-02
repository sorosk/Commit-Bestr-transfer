import csv
from datetime import date

#Creating filename of todays date
current_date_and_time = date.today()
current_date_and_time_string = str(current_date_and_time)

#Creating CSV file
with open(current_date_and_time_string, 'wb') as csvfile:
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
    'Tid',
    'Crawl',
    'Egen',
    'Kick',
    'Bein',
    'Arm',
    'Teknikkdrill'
    ])
    filewriter.writerow(['Derek', 'Software Developer'])
