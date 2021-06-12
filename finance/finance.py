import csv

with open('..\\datafiles\\April2021.csv') as csvFile:
    datareader = csv.reader(csvFile, delimiter=',')
    for row in datareader:
        print(', '.join(row))




