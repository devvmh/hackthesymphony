import csv, sys, json

fixtures = []

with open(sys.argv[1], 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ',', quotechar='"')
  for row in csvreader:
    obj = {}
    obj['model'] = "appcode.question"
    obj['pk'] = row[1]
    obj['fields'] = {}
    obj['fields']['question'] = row[0]
    fixtures.append(obj)
pk = 1
with open(sys.argv[2], 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter = ',', quotechar='"')
  for row in csvreader:
    obj = {}
    obj['model'] = "appcode.answer"
    obj['pk'] = pk
    pk += 1
    obj['fields'] = {}
    obj['fields']['answer'] = row[0]
    obj['fields']['old_question'] = row[1]
    obj['fields']['new_question'] = row[2]
    if row[3]:
      obj['fields']['comment'] = row[3]
    fixtures.append(obj)

print json.dumps(fixtures, indent=2)
