import sys
import csv
x=sys.argv
with open(x[1],newline='')as csvfile:
    count=-1
    obj=csv.reader(csvfile,delimiter=',',quotechar='"')
    index=0
    for row in obj:
        index+=1
        if row[6]:
            count+=1
print(count)