import json

def get_projects():
    with open("app/data/projects.json", "r", encoding="utf-8") as file:
        projects = json.load(file)

    return projects
