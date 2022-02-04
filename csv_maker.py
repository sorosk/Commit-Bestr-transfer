import csv
from datetime import date


def makefile(plan, i1, i2, i3, i4, i5, i6, i7, i8, time, crawl, own, kick, bein, arm, andre, drills):
    # List of names
    header = [
        'Date(dd.mm.yyyy)',
        'TrainingPlan',
        'Long/Short',
        'Endurance - Easy',  # i1
        'Endurance - Moderate',  # i2
        'Endurarance - L-AT',  # i3
        'Endurance - H-AT',  # i4
        'Endurance - Maks O2',  # i5
        'Endurance - Anaerob T',  # i6
        'Endurance - Anaerob P',  # i7
        'Endurance - Speed',  # i8
        'Time Swimming',
        'Strength -Base',
        'Strength Max',
        'Strength Ekspolosive',
        'Mobility / Stretching',
        'Swimming Crawl',
        'Swimming Own',
        'Swimming Kick',
        'Swimming Legs',
        'Swimming Arms',
        'Swimming Other',
        'Swimming Technique',
        'Rest. Drink During Training',
        'Rest. Nutrition during training',
        'Rest. Nutrtion after training',
        'Rest. Sleep/rest after training',
        'Rest. Physical treatment after training',
        'Perceived Excertion',
        'Form 1-10',
        'CompetitionTime',
        'Kommentarer'
    ]

    # List of data
    data = [
        date.today(),
        plan,  # Training plan
        None,  # Long/Shortcourse
        i1,
        i2,
        i3,
        i4,
        i5,
        i6,
        i7,
        i8,
        time,
        None,
        None,
        None,
        None,
        crawl,
        own,
        kick,
        bein,
        arm,
        andre,
        drills,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None
    ]

    # Creating filename of today's date
    current_date = date.today()
    current_date_string = str(current_date) + '.csv'

    # Creating CSV file
    with open(current_date_string, 'w', newline='') as csv_file:  # The CSV file name is todays date
        filewriter = csv.writer(csv_file, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(header)  # Row of names/headers
        filewriter.writerow(data)  # Row of data
