import csv

def toLevel(x):
    if x > 100000:
        return 2
    elif x > 50000:
        return 1
    return 0

def getLevels(name):
    with open('names.csv') as names:
        for row in csv.reader(names):
            if row[0] == name.upper():
                return toLevel(row[2])
        return 0
