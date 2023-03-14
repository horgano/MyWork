import json
FILENAME = "test_dict.json"

def read_dict():
    with open (FILENAME) as f:
        return json.load(f)
    
some_dict = read_dict()
print (some_dict)