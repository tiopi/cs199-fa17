from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("Amazon Review Classification")
sc = SparkContext(conf=conf)

reviews = sc.textFile("hdfs://dataproc-3ba9e17b-802e-4fec-8f2d-4e0d4167cadb-us-central1/Datasets/amazon/amazon_food_reviews.csv")

with open('amazon_review_classification.txt', 'w+') as f:
    pass
