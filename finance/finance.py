import csv

with open('..\\datafiles\\April2021.csv') as csvFile,\
        open('..\\datafiles\\edited\\April2021edited.csv', 'w') as fout:
    datareader = csv.reader(csvFile, delimiter=',')
    datawriter = csv.writer(fout)
    try:
        header = next(datareader)
        header.insert(3, 'category')
        datawriter.writerow(header)
    except StopIteration as e:
        pass

    for row in datareader:
        if len(row) < 1:
            continue
        row.insert(3, "Category Goes Here")
        datawriter.writerow(row[0:5])




