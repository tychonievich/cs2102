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
    print('USAGE:', argv[0], 'when2meet_url')

snum2time = {}

for m in tos.finditer(s):
    struct_time = time.gmtime(int(m.group(2)))
    dow = int(time.strftime("%w",struct_time), 10)
    qh = int(time.strftime("%H",struct_time), 10)*4+int(time.strftime("%M",struct_time), 10)//15
    snum2time[m.group(1)] = (dow,qh)

namesById = {}
for m in pnameid.finditer(s):
    namesById[m.group(4)] = m.group(2)


def setBits(n):
    ans = 0
    while n > 0:
        if (n&1) == 1: ans += 1
        n >>= 1
    return ans

masks = []
openness = {}
for m in hexa.finditer(s):
    num = int(m.group(1),16)
    if num != 0: masks.append(num)
    openness[namesById[m.group(2)]] = setBits(num), setBits(num^(num>>1))

for p in openness:
    if openness[p][0] < 40:
        print(p,'only listed',openness[p][0]/4,'hours of availability')
    if openness[p][1]//2 <= 4:
        print(p,'only listed',openness[p][1]//2,'time slots')
    stdout.flush()

def okForWhom(slots=4):
    ans = []
    mask = (1<<slots)-1
    while mask <= max(masks):
        entry = 0
        for m in masks:
            entry <<= 1
            if (0x0ffff00000f0fffff00ffffff0ffe000ffffffffffffffffffe03ff0 & mask) == mask: # my schedule this term
                if (m&mask) == mask: entry |= 1
        ans.append(entry)
        mask <<= 1
    return ans

def find2Slots(slots=4):
    options = okForWhom(slots)
    answers = []
    for i in range(len(options)):
        for j in range(i):
            okFor = options[i] | options[j]
            if '0' not in bin(okFor)[2:]:
                answers.append((i,j))
    return answers

def find3Slots(slots=4):
    options = okForWhom(slots)
    answers = []
    for i in range(len(options)):
        for j in range(i):
            for k in range(j):
                okFor = options[i] | options[j] | options[k]
                if '0' not in bin(okFor)[2:]:
                    answers.append((i,j,k))
    return answers

def find4Slots(slots=4):
    options = okForWhom(slots)
    answers = []
    for i in range(len(options)):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    okFor = options[i] | options[j] | options[k] | options[l]
                    if '0' not in bin(okFor)[2:]:
                        answers.append((i,j,k,l))
    return answers

def find5Slots(slots=4):
    options = okForWhom(slots)
    answers = []
    for i in range(len(options)):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        okFor = options[i] | options[j] | options[k] | options[l] | options[m]
                        if '0' not in bin(okFor)[2:]:
                            answers.append((i,j,k,l,m))
    return answers


def slotNumsToTime(slots, *slotnums):
    ans = []
    for slotnum in slotnums:
        n = len(snum2time) - slotnum - slots
        dow,tod = snum2time[str(n)]
        week = "sun mon tue wed thu fri sat".split()[dow]
        hour = tod//4
        minute = (tod%4)*15
        ans.append("{} {:#02}:{:#02}".format(week,hour,minute))
    if len(ans) == 1: return ans[0]
    return ans

found = False
for e in find2Slots(3):
    print(slotNumsToTime(3,*e))
    found = True
if not found:
    print('no pairs of slots work')
    stdout.flush()
    for e in find3Slots(3):
        print(slotNumsToTime(3,*e))
        found = True
if not found:
    print('no tripples of slots work')
    stdout.flush()
    for e in find4Slots(3):
        print(slotNumsToTime(3,*e))
        found = True
if not found:
    print('no quads of slots work')
    stdout.flush()
    for e in find5Slots(3):
        print(slotNumsToTime(3,*e))
        found = True
if not found:
    print("No sets of slots work")

