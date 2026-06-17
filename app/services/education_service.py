import json

def get_education():
    with open("app/data/education.json", "r", encoding="utf-8") as file:
        education = json.load(file)
    return education

def add_education(education):
    
    data = get_education()
    data.append(education)
    with open("app/data/education.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    return education
