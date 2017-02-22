import csv

if __name__ == '__main__':
    file_name = 'teams.csv'
    file_name = file_name[:-4]
    new_header = []
    with open(file_name + '.csv', 'r') as infile, open(file_name + '-out.csv', 'w') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        new_header = next(reader, None)
        new_header = new_header[:2]
        writer.writerow(new_header)
        for row in reader:
            row = [row[0], str(row[1]) + " " + str(row[2])]
            writer.writerow(row)
