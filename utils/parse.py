import csv

with open('1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(row)
            print('\n')
            line_count += 1
        else:
            print(row)
            print('\n')
            line_count += 1
    print(f'Processed {line_count} lines.')