import json  # Import the JSON module

db = []  # Initialize an empty list to store database items

file = open("./data.json", "r+", encoding="utf-8")  # Open the data.json file in read/write mode with UTF-8 encoding

db = json.load(file)  # Load the JSON data from the file into the db list

def get_item(index: int) -> dict[str, str | int]:  # Define a function to get an item from the db by index
    return db[index]  # Return the item at the specified index

def get_all():  # Define a function to get all items from the db
    return db  # Return the entire db list

def get_len():  # Define a function to get the length of the db
    return len(db)  # Return the number of items in the db

def set_item(index: int, value: dict[str, str | int]):  # Define a function to set an item in the db by index
    if has(index):  # Check if the index exists in the db
        db[index] = value  # Update the item at the specified index
        save()  # Save the updated db to the file
    elif index >= get_len():  # If the index is out of range, append the item to the db
        db.append(value)  # Add the new item to the end of the db
        save()  # Save the updated db to the file

def has(index: int):  # Define a function to check if an index exists in the db
    return True if index < get_len() and index >= 0 else False  # Return True if the index is valid, otherwise False

def delete_item(index: int):  # Define a function to delete an item from the db by index
    if has(index):  # Check if the index exists in the db
        del db[index]  # Delete the item at the specified index
        save()  # Save the updated db to the file

def save():  # Define a function to save the db to the file
    file.seek(0)  # Move the file pointer to the beginning of the file
    json.dump(db, file, ensure_ascii=False, indent=4)  # Write the db list to the file as JSON
    file.truncate()  # Truncate the file to the current size to remove any leftover data