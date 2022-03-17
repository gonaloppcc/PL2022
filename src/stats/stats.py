import statistics

from csv_parser.parser import parse_emd

emd_path = 'files/emd.csv'

athletes = parse_emd(emd_path)

print_athletes = False
# Temporary code to check if the parsing works
for athlete in athletes:
    if print_athletes:
        print(f'{athlete["fname"]} {athlete["lname"]}: {athlete["email"]}')

print('Data loaded!')