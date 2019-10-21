import csv

with open('<insert text file here>.csv') as compliance_data:
    compliance_data_reader = csv.reader(compliance_data, delimiter=',')
    line_count = 0
    for row in compliance_data_reader:
        if line_count == 0:
            print(f'Column names are {"   ".join(row)}')
            line_count += 1
        else:
            # row[1] is the 2nd column, not row
            print(f'{row[0]}\t{row[1]}\t{row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')
