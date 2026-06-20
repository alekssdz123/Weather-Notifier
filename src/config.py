from pathlib import Path
import json

def read_file(file_path):
    try:
        if Path(file_path).is_file() == False:
            create_config(file_path)

        with open(file_path, "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        print(f"Error. File {file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error. Failed to decode JSON from the file {file_path}")
    except Exception:
        print(f"Error. Failed to read file {file_path}")

def read_config():
    config_path = "config.json"
    data = read_file(config_path)

    return {
        "city": data["city"],
        "country_code": data["country_code"],
        "api_key": data["api_key"],
        "lang": data["lang"]
    }

def create_config(file_path):
    data = {
        "city": None,
        "country_code": None,
        "api_key": None,
        "lang": None
    }

    json_data = json.dumps(data, indent=4)
    with open(file_path, "w") as file:
        file.write(json_data)

read_file("config.json")
