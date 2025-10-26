import fetch_data
import clean_data

raw_folder = "../data/raw"
processed_folder = "../data/processed"

if __name__ == "__main__":
    fetch_data.main()
    dataframes = clean_data.load_json_files(raw_folder)
    clean_data.save_dataframes_to_parquet(dataframes, processed_folder)
    
