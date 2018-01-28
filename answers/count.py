import sys
x=sys.argv
f=open(x[1])
count=-1
for line in f:
    count+=1
print(count)
f.close()