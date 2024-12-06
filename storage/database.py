import json

def load_data():
    try:
        with open("data/expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"gastos": []}

def save_data(data):
    with open("data/expenses.json", "w") as file:
        json.dump(data, file, indent=4)

