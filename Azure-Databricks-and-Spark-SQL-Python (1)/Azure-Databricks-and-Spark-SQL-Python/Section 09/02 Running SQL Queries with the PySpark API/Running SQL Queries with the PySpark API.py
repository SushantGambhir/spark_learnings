# Databricks notebook source
# MAGIC %md
# MAGIC ### 🔗 Links and Resources
# MAGIC - [sql()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.SparkSession.sql.html)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Running SQL SELECT Statements in an SQL Code Cell renders an interactive Table (not a DataFrame)

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Simple SQL select statement
# MAGIC SELECT * FROM population_metrics.default.countries_population

# COMMAND ----------

# MAGIC %md
# MAGIC ### 📌 Using SQL SELECT Statements in spark.sql() returns a Spark DataFrame

# COMMAND ----------

# Running SQL code using Python
# It returns a dataframe
spark.sql("SELECT * FROM population_metrics.default.countries_population").display()

# COMMAND ----------

# Storing the SQL statement as a string variable and passing it into the sql() function
sql_string = "SELECT * FROM population_metrics.default.countries_population"

spark.sql(sql_string).display()

# COMMAND ----------

# Storing the SQL statement as a multi-line string variable and passing it into the sql() function

sql_string = """
SELECT 
    * 
FROM 
    population_metrics.default.countries_population
"""

spark.sql(sql_string).display()
