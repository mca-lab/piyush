from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, col
import os

spark = SparkSession.builder.appName("Load JSON to PySpark").getOrCreate()

def load_json(json_path):
    
    raw_df = spark.read.option("multiline", "true").json(json_path)
    df = raw_df.select(explode(col("value")).alias("record")).select("record.*")
    
    return df

def load_json_files(folder_path):

    dfs = {}
    count=0
    
    for file in os.listdir(folder_path):
        if file.endswith(".json"):

            count += 1

            path = os.path.join(folder_path, file)
            name = file.replace(".json", "")  
            dfs[name] = load_json(path)
            print(f"Loaded {name} with {dfs[name].count()} rows")

    print(f"loaded {count} json files")
    
    return dfs


if __name__ == "__main__":

    folder_path = "../data/raw"
    dataframes = load_json_files(folder_path)
