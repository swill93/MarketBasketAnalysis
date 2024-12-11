from pyspark.sql import SparkSession 
from pyspark.sql.functions import collect_set
from pyspark.ml.fpm import FPGrowth
from pyspark.sql.functions import col, concat_ws


spark = SparkSession.builder.appName("Market Basket Analysis").getOrCreate()

#Reads in CSV data into a dataframe
transactionData = spark.read.csv('/Users/spenserwilliams/Desktop/COSC473/FinalProject/TransactionData2.csv', header = True, inferSchema = True)

#Select relevant columns "BillNo" and "itemname" from dataset
transactions = transactionData.select("BillNo", "Itemname")

#Grouped transactions by "BillNo" and named new column "items"
groupedTransactions = transactions.groupBy("BillNo").agg(collect_set("Itemname").alias("items"))

#Implements FPGrowth algorithm to find frequent itemsets and sets confidence for association rules
fpGrowth = FPGrowth(itemsCol= "items", minSupport=0.05, minConfidence= 0.4)
model = fpGrowth.fit(groupedTransactions)

freq_itemsets = model.freqItemsets

#Writes results to a csv
freq_itemsets.withColumn("items", concat_ws(", ", freq_itemsets["items"])) \
    .coalesce(1) \
    .write.csv("/Users/spenserwilliams/Desktop/COSC473/FinalProject/frequent_itemsets.csv", header=True, mode="overwrite")


association_rules = model.associationRules

#Write results to a csv
association_rules.withColumn("antecedent", concat_ws(", ", association_rules["antecedent"])) \
    .withColumn("consequent", concat_ws(", ", association_rules["consequent"])).coalesce(1) \
    .write.csv("/Users/spenserwilliams/Desktop/COSC473/FinalProject/association_rules.csv", header= True, mode= "overwrite")








    