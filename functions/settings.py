import json
import os
from pathlib import Path

functions_directory = os.path.dirname(__file__)     # os.path.dirname(__file__) = D:\_DEV\Python\31_I_aM_D_bee\functions   //in my case
main_directory = functions_directory.strip("functions")
path_json = Path(main_directory,  "settings_db.json")       # Path functions makes the path OS independent

def open_settings():
    f = open(path_json)
    settings_data = json.load(f)
    return settings_data

def save_settings(settings_data):
    with open(path_json, 'w') as f:
        json.dump(settings_data, f, indent=2)
    return
