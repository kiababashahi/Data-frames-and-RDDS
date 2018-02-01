from pyspark.sql import SparkSession
import sys
name=sys.argv[1]
spark = SparkSession \
    .builder \
    .appName("kias_first_db") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
df=spark.read.csv(name,header=True)
parks=df.groupBy("Nom_parc").count().filter(df.Nom_parc!='').orderBy("count",ascending=False).head(10)
for element in parks:
    print(element[0]+": "+ str(element[1]))

