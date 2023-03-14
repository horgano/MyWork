import json
FILENAME = "test_dict.json"
sample = dict(name = "fred", age = 31, grades = [1, 12, 55])

def write_dict(obj):
    with open (FILENAME, 'wt') as f:
        json.dump(obj,f)

write_dict(sample)