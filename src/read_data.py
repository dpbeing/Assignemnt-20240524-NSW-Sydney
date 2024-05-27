import csv

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file, delimiter='|')
        data = [row for row in csv_reader]
    return data
