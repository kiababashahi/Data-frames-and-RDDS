from pyspark.sql import SparkSession
import sys
name=sys.argv[1]
spark = SparkSession \
    .builder \
    .appName("kias_first_db") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df=spark.read.csv(name,header=True)
parks=df.select(df[6]).filter(df.Nom_parc!='').distinct().sort(df.Nom_parc).collect()
for e in parks:
    print(e[0])

