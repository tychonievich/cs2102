#!/usr/bin/env python3

from sys import argv, stdout
from urllib.request import urlopen
import re, time

pid = re.compile(r'PeopleIDs\[(\d+)\] = (\d+);')
pname = re.compile(r"PeopleNames\[(\d+)\] = '([^']*)';")
slot = re.compile(r"AvailableAtSlot\[(\d+)\].push\((\d+)\)");
tos = re.compile(r"TimeOfSlot\[(\d+)\]=(\d+);")
col = re.compile(r"Col\[TimeOfSlot.indexOf\((\d*)\)\] = (\d+);")
row = re.compile(r"Row\[TimeOfSlot.indexOf\((\d*)\)\] = (\d+);")
hexa = re.compile(r"// hexAvailability: ([0-9a-f]+)[\n\r]+AvailableAtSlot\[\d+\].push\((\d+)\);")

pnameid = re.compile(r"PeopleNames\[(\d+)\] = '([^']*)';PeopleIDs\[(\d+)\] = (\d+);")

if len(argv) > 1:
    s = urlopen(argv[1]).read().decode("utf-8")
else:
    s = open("example.html").read()


# given a slot number, returns the day/time it represents
snum2time = {}

for m in tos.finditer(s):
    struct_time = time.gmtime(int(m.group(2)))
    dow = int(time.strftime("%w",struct_time), 10)
    qh = int(time.strftime("%H",struct_time), 10)*4+int(time.strftime("%M",struct_time), 10)//15
    week = "sun mon tue wed thu fri sat".split()[dow]
    hour = qh//4
    minute = (qh%4)*15
    snum2time[int(m.group(1))] = "{} {:#02}:{:#02}".format(week,hour,minute)

def timesOfMask(mask):
    ans = []
    ts = 1
    cnt = len(snum2time)-1
    while ts <= mask:
        if (ts & mask) != 0:
            ans.append(snum2time[cnt])
        ts <<= 1
        cnt -= 1
    return ans


# learn what we can about people: name and availability
tmp = {} # [name,openLong]

for m in pnameid.finditer(s):
    tmp[m.group(4)] = [m.group(2), None]
for m in hexa.finditer(s):
    num = int(m.group(1),16)
    tmp[m.group(2)][1] = num

people = {}
allfolk = set()
maxTimes = 0
for k in tmp:
    if tmp[k][1] is not None:
        people[tmp[k][0]] = tmp[k][1]
        maxTimes |= tmp[k][1]
        allfolk.add(tmp[k][0])

for k in people:
    print(k,hex(people[k]))

duration=3 # 15-minute segments

openness = {} # openness[x] = people open for at least one of the duration-segment slots starting at each set bit of x


# find the one-time optima
ts = 1<<(duration-1)
while ts < maxTimes:
    tmp = set()
    for person in people:
        mask = people[person]
        ok = (mask & ts) != 0
        for shift in range(1,duration):
            ok &= (mask & (ts>>shift)) != 0
        if ok: tmp.add(person)
    if 'Luther' not in tmp: tmp = set() #######################################
    openness[ts] = tmp
    ts <<= 1

best = 0
for place in openness:
    if len(openness[place]) > best:
        best = len(openness[place])
print('-'*60);
print('Can get',best,'out of',len(people),' at times:')
for place in openness:
    if len(openness[place]) == best:
        print(timesOfMask(place), allfolk - openness[place])

stdout.flush()

for ways in range(3,6):
    # find the two-time optima
    keys = list(openness.keys())
    for base in keys:
        ts = 1<<(duration-1)
        while ts < maxTimes:
            newtime = base | ts
            if ts in openness and newtime not in openness:
                openness[newtime] = openness[base] | openness[ts]
            ts <<= 1

    best = 0
    for place in openness:
        if len(openness[place]) > best:
            best = len(openness[place])
    print('-'*60);
    print('Can get',best,'out of',len(people),' at times:')
    for place in openness:
        if len(openness[place]) == best:
            print(timesOfMask(place), allfolk - openness[place])

    stdout.flush()
    if best == len(people): break

