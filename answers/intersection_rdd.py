import sys
import csv
name1=sys.argv[1]
name2=sys.argv[2]
from pyspark import SparkContext, SparkConf
def splitter(line):
    for column in csv.reader([line],delimiter=','):
        return column[6]

conf = SparkConf().setAppName('Kia_bigdata_lab').setMaster('local')
sc = SparkContext(conf=conf)
txt=sc.textFile(name1).map(splitter).filter(lambda x:x)
header=txt.first()
txt=txt.filter(lambda x:x!=header)
txt1=sc.textFile(name2).map(splitter).filter(lambda x:x).distinct()
txt2=txt.intersection(txt1).sortBy(lambda x:x).collect()
for element in txt2:
    print(element)
