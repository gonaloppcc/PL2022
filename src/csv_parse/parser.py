from sys import argv
import re

# List where our database will be stored
db = []

p = re.compile(r'^(?P<id>\w{24}),(?P<index>\d+),(?P<date>\d{4}-\d{2}-\d{2}),(?P<fname>[^\W\d]+),(?P<lname>[^\W\d]+),(?P<age>\d+),(?P<gender>(M|F)),(?P<location>[^\W\d]+),(?P<sport>\w+),(?P<club>\w+),(?P<email>(\w+((\.|-)\w+)?)+@(\w+((\.|-)\w+)?)+),(?P<federated>(true|false)),(?P<result>(true|false))$')
with open(argv[1], mode='r') as file:
    file.readline() # Skip first line
    
    for line in file:
        mo = p.match(line)
        dict = mo.groupdict()

        # Change field types
        dict['index'] = int(dict['index'])
        dict['age'] = int(dict['age'])
        dict['federated'] = bool(dict['federated'])
        dict['result'] = bool(dict['result'])

        # Add to database
        db.append(dict)

    # Temporary code to check if the parsing works
    for athlete in db:
        print(f'{athlete["fname"]} {athlete["lname"]}: {athlete["email"]}')