import sys
import csv
x=sys.argv
park_dictionary_2016={}
park_dictionary_2015={}
with open(x[1],newline='',encoding="utf-8")as csvfile:
    count = -1
    line = csv.reader(csvfile, delimiter=',', quotechar='"')
    index = 0
    for row in line:
        if count > -1:
            index += 1
            if row[6]:
                if row[6] not in park_dictionary_2016.keys():
                    park_dictionary_2016[row[6]] = [row[6]]
                else:
                    park_dictionary_2016[row[6]].append(row[6])
        count += 1
with open(x[2],newline='',encoding="utf-8")as csvfile:
    count = -1
    line = csv.reader(csvfile, delimiter=',', quotechar='"')
    index = 0
    for row in line:
        if count > -1:
            index += 1
            if row[6]:
                if row[6] not in park_dictionary_2015.keys():
                    park_dictionary_2015[row[6]] = [row[6]]
                else:
                    park_dictionary_2015[row[6]].append(row[6])
        count += 1
intersection= []
for key in park_dictionary_2016.keys():
    if(key in park_dictionary_2015.keys()):
        intersection.append(key)
intersection.sort()
for parks in intersection:
    print(parks)