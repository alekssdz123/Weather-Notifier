from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = BASE_DIR / "config.json"

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
    data = read_file(CONFIG_PATH)

    return {
        "city": data["city"],
        "country_code": data["country_code"],
        "api_key": data["api_key"],
        "lang": data["lang"]
    }

def create_config(file_path, city=None, country_code=None, api_key=None, lang=None):
    data = {
        "city": city,
        "country_code": country_code,
        "api_key": api_key,
        "lang": lang
    }

    json_data = json.dumps(data, indent=4)
    with open(file_path, "w") as file:
        file.write(json_data)

def update_config(new_data):
    old_config = read_config()

    if new_data["city"] == "":
        new_data["city"] = old_config["city"]

    if new_data["country_code"] == "":
        new_data["country_code"] = old_config["country_code"]

    if new_data["api_key"] == "":
        new_data["api_key"] = old_config["api_key"]

    if new_data["lang"] == "":
        new_data["lang"] = old_config["lang"]

    create_config(CONFIG_PATH, new_data["city"], new_data["country_code"], new_data["api_key"], new_data["lang"])

