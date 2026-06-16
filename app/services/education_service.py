import json

def get_education():
    with open("app/data/education.json", "r", encoding="utf-8") as file:
        education = json.load(file)
    return education
    