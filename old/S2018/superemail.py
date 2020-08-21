import csv

graded = {}

with open('grades.csv') as f:
    r = csv.reader(f)
    h = r.__next__()
    for row in r:
        if len(row) >= len(h):
            graded[row[0].strip()] = 'not yet responded' not in row[h.index('supervisor grade notes')]

superof = {}

with open('super.csv') as f:
    r = csv.reader(f)
    h = r.__next__()
    for row in r:
        if row[0].strip() not in graded or not graded[row[0].strip()]:
            superof.setdefault(row[3].strip(), []).append(row[:3]+row[4:5])
            if row[5]:
                superof.setdefault(row[5].strip(), []).append(row[:3]+row[6:7])

for k in superof:
    print(k,'''

As part of their grade for CS 2910, first-time TAs are evaluated by their supervisors. Could you reply with a letter grade (and optionally comments) for each of 

'''+ ('\n'.join('  \t'.join(person) for person in superof[k]))+'''

Thanks in advance,

— Luther

-------------------------------------------------
''')
