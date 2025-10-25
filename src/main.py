import fetch_data
import clean_data

if __name__ == "__main__":
    fetch_data.main()
    folder_path = "../data/raw"
    clean_data.load_json_files(folder_path)