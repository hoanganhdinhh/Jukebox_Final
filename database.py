import json

db = []

file = open("./data.json", "r+", encoding="utf-8")

db = json.load(file)

def get_item(index:int)-> dict[str,str|int]:
    return db[index]

def get_all():
    return db

def get_len():
    return len(db)

def set_item(index:int, value:dict[str,str|int]):
    if has(index):
        db[index] = value
        save()
    elif index >= get_len():
        db.append(value)
        save()

def has(index:int):
    return True if index < get_len() and index >=0 else False

def delete_item(index:int):
    if has(index):
        del db[index]
        save()

def save():
    file.seek(0)
    json.dump(db, file, ensure_ascii=False, indent=4)
    file.truncate()