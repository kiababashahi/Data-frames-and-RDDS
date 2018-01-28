import sys
import csv
x=sys.argv
park_dictionary={}
with open(x[1],newline='',encoding="utf-8")as csvfile:
    count = -1
    line = csv.reader(csvfile, delimiter=',', quotechar='"')
    index = 0
    for row in line:
        if count > -1:
            index += 1
            if row[6]:
                if row[6] not in park_dictionary.keys():
                    park_dictionary[row[6]] = [row[6]]
                else:
                    park_dictionary[row[6]].append(row[6])
        count += 1
park_count = {}
for key in park_dictionary.keys():
    park_count[key] = len(park_dictionary[key])
for key in sorted(park_count.keys()):
    print("%s: %d \n" % (key, park_count[key]))