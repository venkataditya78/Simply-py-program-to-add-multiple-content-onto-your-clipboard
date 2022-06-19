import sys
import clipboard
import json

from numpy import save

def save_items(filepath, data):
    with open(filepath,'w') as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

SAVED_DATA = 'clipboard.json'

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input("Please enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA,data)
        print("Data saved successfully!!")
    
    elif command == 'load':
        key = input("Enter a key ?")
        if key in data:
            clipboard.copy(data[key])
            print("Data has been loaded onto the clipboard!!")
        else:
            print("Key does not exist!")
    elif command=='list':
        print(data)
else:
    print("unknown command")
