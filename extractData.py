import csv

tableData = {}
with open('temp/test.csv') as compliance_data:
    compliance_data_reader = csv.reader(compliance_data, delimiter=',')
    line_count = 0
    for row in compliance_data_reader:
        number_of_columns = len(row)
        if line_count == 0:
            print(f'{"   ".join(row)}')
            line_count += 1
        else:
            # row[1] is the 2nd column, not row
            for column in row:
                print(f'{column}')
            tableData[row[0]] = row[1]
            line_count += 1
    print(f'Done: Processed {line_count} lines.')
