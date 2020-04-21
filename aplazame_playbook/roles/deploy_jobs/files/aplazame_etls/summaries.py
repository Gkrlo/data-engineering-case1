from pyspark.sql import SparkSession

POSTGRES_URL = "jdbc:postgresql://aplazame1.vm:5432/postgres"

def store_summary(summaty_df, table_name):
    summaty_df.write.mode("overwrite").format("jdbc").option("url", POSTGRES_URL).option("dbtable", table_name)\
        .option("user", "postgres").option("password", "postgres").save()

spark =SparkSession.builder \
    .master("local") \
    .appName("AplazameSummaries") \
    .getOrCreate()

payment_df = spark.read \
    .format("jdbc") \
    .option("url", POSTGRES_URL) \
    .option("dbtable", "public.stage_payments") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .load()
prepayment_df = spark.read \
    .format("jdbc") \
    .option("url", POSTGRES_URL) \
    .option("dbtable", "public.stage_prepayments") \
    .option("user", "postgres") \
    .option("password", "postgres") \
    .load()

payment_df.createTempView("payment_tmp")
prepayment_df.createTempView("prepayment_tmp")

by_country_df = spark.sql("""select 'payment' as type, country_name, avg(amount) as total_avg, 
                             sum(amount) as total_sum from payment_tmp group by country_name""")\
    .union(spark.sql("""select 'prepayment' as type, country_name, avg(principal_not_accrued + interest) as total_avg, 
                        sum(principal_not_accrued + interest) as total_sum from prepayment_tmp group by country_name"""))
by_merchant_df = spark.sql("""select 'payment' as type, merchant_name, avg(amount) as total_avg, 
                              sum(amount) as total_sum from payment_tmp group by merchant_name""")\
    .union(spark.sql("""select 'prepayment' as type, merchant_name, avg(principal_not_accrued + interest) as total_avg, 
                        sum(principal_not_accrued + interest) as total_sum from prepayment_tmp group by merchant_name"""))
by_industry_df = spark.sql("""select 'payment' as type, industry_name, avg(amount) as total_avg,
                              sum(amount) as total_sum from payment_tmp group by industry_name""")\
    .union(spark.sql("""select 'prepayment' as type, industry_name, avg(principal_not_accrued + interest) as total_avg, 
                        sum(principal_not_accrued + interest) as total_sum from prepayment_tmp group by industry_name"""))

# Store payment Summary
store_summary(by_country_df, "summary_country")
store_summary(by_merchant_df, "summary_merchant")
store_summary(by_industry_df, "summary_industry")



