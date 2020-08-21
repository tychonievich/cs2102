import csv
from glob import glob

g = {}
with open('grades.csv') as fh:
    r = csv.reader(fh)
    header = r.__next__()
    for row in r:
        g[row[0]] = row[1:] + ['']*(len(header)-len(row))
        if g[row[0]][4] == '':
            g[row[0]][4] = 0
            g[row[0]][5] = 'did not report attendance; fix that at https://goo.gl/forms/cFJSlj40OzMZMCo92'
        if g[row[0]][6] == '':
            g[row[0]][6] = 50
            g[row[0]][7] = 'supervisor has not yet responded to my request for your grade; grade may change if they do'
            
for f in glob('CS 2910*Responses*.csv'):
    with open(f) as fh:
        r = csv.reader(fh)
        for row in r:
            if '@' in row[1]:
                uid = row[1][:row[1].find('@')]
                req = sum(0 if entry.startswith('Did not') else 5 for entry in row[2:8])
                opt = sum(0 if entry.startswith('Did not') else 5 for entry in row[8:15])
                if uid in g:
                    g[uid][4] = req + min(10,opt)
                    g[uid][5] = ''

with open('grades.csv', 'w') as fh:
    w = csv.writer(fh)
    w.writerow(header)
    for k,v in sorted(g.items()):
        w.writerow([k]+v)
