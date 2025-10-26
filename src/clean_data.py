from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, explode
import os

spark = SparkSession.builder.appName("Load JSON to PySpark").getOrCreate()

def load_json(json_path):
    df = spark.read.option("multiline", "true").json(json_path)
    if "value" in df.columns:
        df = df.select(explode(col("value")).alias("record")).select("record.*")
    return df

def load_json_files(folder_path):
    dfs = {}
    json_files = [file for file in os.listdir(folder_path) if file.endswith(".json")]

    for file in json_files:
        path = os.path.join(folder_path, file)
        name = file.replace(".json", "")
        try:
            dfs[name] = load_json(path)
            print(f"Loaded {name} with {dfs[name].count()} rows")
        except Exception as e:
            print(f"Failed to load {file}: {e}")

    print(f"Loaded {len(dfs)} JSON files")
    return dfs

def clean_transform_dataframe(df):

    numeric_columns = {
        "OBS_VALUE": "double",
        "DECIMALS": "integer",
        "UNIT_MULT": "integer",
        "LATEST_DATA": "boolean",
        "TIME_PERIOD": "integer"
    }
    for col_name, dtype in numeric_columns.items():
        if col_name in df.columns:
            df = df.withColumn(col_name, col(col_name).cast(dtype))

    string_columns = [
        "INDICATOR", "AGE", "AGG_METHOD", "COMMENT_OBS", "COMMENT_TS",
        "COMP_BREAKDOWN_1", "COMP_BREAKDOWN_2", "COMP_BREAKDOWN_3",
        "DATABASE_ID", "DATA_SOURCE", "FREQ", "OBS_CONF",
        "URBANISATION", "UNIT_TYPE", "UNIT_MEASURE", "TIME_FORMAT",
        "SEX", "REF_AREA", "OBS_STATUS"
    ]

    for c in string_columns:
        if c in df.columns:
            df = df.withColumn(c, trim(upper(col(c))))

    essential_cols = ["OBS_VALUE", "TIME_PERIOD", "INDICATOR", "REF_AREA", "SEX", "AGE", "DATABASE_ID"]
    df = df.dropna(subset=[c for c in essential_cols if c in df.columns])

    comment_cols = ["COMMENT_OBS", "COMMENT_TS"]
    for col_name in comment_cols:
        if col_name in df.columns:
            df = df.fillna({col_name: ""})

    return df

def save_dataframes_to_parquet(dfs, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    for name, df in dfs.items():
        df_cleaned = clean_transform_dataframe(df)
        parquet_path = os.path.join(output_folder, f"{name}.parquet")
        df_cleaned.write.mode("overwrite").parquet(parquet_path)
        print(f"Saved {name} to {parquet_path}")

if __name__ == "__main__":
    raw_folder = "../data/raw"
    processed_folder = "../data/processed"

    dataframes = load_json_files(raw_folder)
    save_dataframes_to_parquet(dataframes, processed_folder)


