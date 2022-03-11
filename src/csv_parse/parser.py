from sys import argv
import re

p = re.compile(r'^(?P<id>\w{24}),(?P<index>\d+),(?P<date>\d{4}-\d{2}-\d{2}),(?P<fname>[^\W\d]+),(?P<lname>[^\W\d]+),(?P<age>\d+),(?P<gender>(M|F)),(?P<location>[^\W\d]+),(?P<sport>\w+),(?P<club>\w+),(?P<email>(\w+((\.|-)\w+)?)+@(\w+((\.|-)\w+)?)+),(?P<federated>(true|false)),(?P<result>(true|false))$')

db = []

with open(argv[1], mode='r') as file:
    file.readline()
    for line in file:
        mo = p.match(line)
        dict = mo.groupdict()

        db.append(dict)

    for athlete in db:
        print(f'{athlete["fname"]} {athlete["lname"]}')