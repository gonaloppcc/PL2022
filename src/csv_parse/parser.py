""" System module used to get the arguments passed."""
from sys import argv
import re

# List where our database will be stored
db = []

p = re.compile(
    r'^(?P<id>\w{24}),(?P<index>\d+),(?P<date>\d{4}-\d{2}-\d{2}),(?P<fname>[^\W\d]+),(?P<lname>[^\W\d]+),(?P<age>\d+),(?P<gender>(M|F)),(?P<location>[^\W\d]+),(?P<sport>\w+),(?P<club>\w+),(?P<email>(\w+((\.|-)\w+)?)+@(\w+((\.|-)\w+)?)+),(?P<federated>(true|false)),(?P<result>(true|false))$'
    )

with open(argv[1], mode='r', encoding='utf-8') as file:
    file.readline() # Skip first line

    for line in file:
        mo = p.match(line)
        exam = mo.groupdict()

        # Change field types
        exam['index'] = int(exam['index'])
        exam['age'] = int(exam['age'])
        exam['federated'] = bool(exam['federated'])
        exam['result'] = bool(exam['result'])

        # Add to database
        db.append(exam)

    # Temporary code to check if the parsing works
    for athlete in db:
        print(f'{athlete["fname"]} {athlete["lname"]}: {athlete["email"]}')
