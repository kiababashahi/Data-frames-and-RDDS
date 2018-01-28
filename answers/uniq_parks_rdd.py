import sys
import csv
name=sys.argv[1]
from pyspark import SparkContext, SparkConf
def splitter(line):
    for column in csv.reader([line],delimiter=','):
        return column[6]

conf = SparkConf().setAppName('Kia_bigdata_lab').setMaster('local')
sc = SparkContext(conf=conf)
txt=sc.textFile(name).map(splitter).filter(lambda x:x).distinct().sortBy(lambda x:x).collect()
for element in txt:
    print(element)
