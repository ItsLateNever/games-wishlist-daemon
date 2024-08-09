import json


def read_data():
    with open('data.json', 'r') as file:
        return json.loads(file.read())
