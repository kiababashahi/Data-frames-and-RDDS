import sys
name=sys.argv[1]
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('Kia_bigdata_lab').setMaster('local')
sc = SparkContext(conf=conf)
txt=sc.textFile(name)
trees=txt.filter(lambda x:x).count()
print(trees-1)
