from pyspark.sql import SparkSession
import sys
name=sys.argv[1]
name2=sys.argv[2]
spark = SparkSession \
    .builder \
    .appName("kias_first_db") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df=spark.read.csv(name,header=True)
df2=spark.read.csv(name2,header=True)
park1=df.select(df[6]).filter(df.Nom_parc!='').distinct().sort(df.Nom_parc)
park2=df2.select(df2[6]).filter(df2.Nom_parc!='').distinct().sort(df2.Nom_parc)
intersection=park1.intersect(park2).sort(df.Nom_parc).collect()
for element in intersection:
    print(element[0])

