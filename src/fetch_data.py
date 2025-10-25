import requests
import json
import time
import os 

BASE_URL = "https://data360api.worldbank.org/data360/"
OUTPUT_DIR = "../data/raw" 

JSON_FILE_PATH = "INDICATOR_ENDPOINTS.json"

with open(JSON_FILE_PATH, "r", encoding="utf-8") as f:
    INDICATOR_ENDPOINTS = json.load(f)


def fetch_data(indicator_name, database_id, indicatorid, skip_count=0):

    endpoint_path = f"data?DATABASE_ID={database_id}&INDICATOR={indicatorid}&skip={skip_count}"
    url = f"{BASE_URL}{endpoint_path}"

    print(f"-> Fetching data for: {indicator_name}...")
    
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"   [SUCCESS] Data fetched for {indicator_name}.")
        return data

    except requests.exceptions.HTTPError as errh:
    
        print(f"   [ERROR] HTTP Error for {indicator_name}: {errh}")

    except requests.exceptions.ConnectionError as errc:
        print(f"   [ERROR] Connection Error for {indicator_name}: {errc}")

    except requests.exceptions.Timeout as errt:
        print(f"   [ERROR] Timeout Error for {indicator_name}: {errt}")

    except requests.exceptions.RequestException as err:
        print(f"   [ERROR] An unexpected error occurred while fetching {indicator_name}: {err}")

    except json.JSONDecodeError:
        print(f"   [ERROR] Failed to decode JSON response for {indicator_name}.")
    
    return None

def main():

    successful_fetches = 0

    print("--- Starting World Bank Data Fetch ---")

    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        print(f"Ensuring output directory '{OUTPUT_DIR}' exists.")
    except OSError as e:
        print(f"[CRITICAL ERROR] Failed to create directory '{OUTPUT_DIR}': {e}")
        return 

    for name, ids in INDICATOR_ENDPOINTS.items():
        
        data = fetch_data(
            indicator_name=name, 
            database_id=ids["database_id"], 
            indicatorid=ids["indicatorid"]
        )
        
        if data:
            output_filename = f"{name}.json"
            output_filepath = os.path.join(OUTPUT_DIR, output_filename)
            
            try:
                with open(output_filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"   [SAVED] Data saved to '{output_filepath}'.")
                successful_fetches += 1
            except IOError as e:
                print(f"   [CRITICAL ERROR] Could not write to file {output_filename}: {e}")
        
        time.sleep(0.5) 

    print("\n--- Fetching and Saving Complete ---")
    print(f"Successfully created {successful_fetches} JSON files.")

if __name__ == "__main__":
    main()
