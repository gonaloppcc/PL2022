import sys
import re

p = re.compile(r'^(?P<id>\w{24}),(?P<index>\d+),(?P<date>\d{4}-\d{2}-\d{2}),(?P<fname>[^\W\d]+),(?P<lname>[^\W\d]+),(?P<age>\d+),(?P<gender>(M|F)),(?P<location>[^\W\d]+),(?P<sport>\w+),(?P<club>\w+),(?P<email>(\w+((\.|-)\w+)?)+@(\w+((\.|-)\w+)?)+),(?P<federated>(true|false)),(?P<result>(true|false))$')

sys.stdin.readline()

db = {}

for line in sys.stdin:
    mo = p.match(line)
    dict = mo.groupdict()

    db[dict["index"]] = dict

for athlete in db.values():
    print(f'{athlete["fname"]} {athlete["lname"]}')