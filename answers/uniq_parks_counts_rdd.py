import sys
import csv
name=sys.argv[1]
from pyspark import SparkContext, SparkConf
def splitter(line):
    for column in csv.reader([line],delimiter=','):
        return column[6]
def sumfunc(x,y):
    return x+y
conf = SparkConf().setAppName('Kia_bigdata_lab').setMaster('local')
sc = SparkContext(conf=conf)
trees=sc.textFile(name).map(splitter).filter(lambda x:x)
header=trees.first()
trees1=trees.filter(lambda x:x!=header).map(lambda x:(x,1))
number=trees1.reduceByKey(lambda  x,y:x+y).sortByKey().collect()
for it in range(len(number)):
    print(number[it][0]+ ': '+str(number[it][1]))