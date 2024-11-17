from library_item import LibraryItem  # Import the LibraryItem class from the library_item module
from database import get_item, get_len, has # Import the get_item, get_len, and has functions from the database module

library = [] # Initialize an empty list to store library items

def update(): # Define the update function to refresh the library list
    global library # Declare the library variable as global to modify the global list
    library = [] # Reset the library list to empty
    for key in range(get_len()): # Loop through each index from 0 to the length of the library
        song = get_item(key) # Retrieve the song dictionary from the database using the current index
        library.append(LibraryItem(name = song["name"],artist = song["artist"], composer = song["composer"], music_instrument = song["music_instrument"], link = song["link"], rating = song["rating"]))
        # Create a new LibraryItem object and add it to the library list

def list_all():  # Define the list_all function to list all library items
    update()     # Call the update function to refresh the library list
    output = ""  # Initialize an empty string to store the output
    for key in range(len(library)):  # Loop through each index in the library list
        item = library[key]          # Get the LibraryItem object at the current index
        output += f"{key + 1} {item.info()}\n"  # Append the item's info to the output string with a line break
    return output  # Return the complete output string


def get_name(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None
    
def get_composer(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.composer
    except KeyError:
        return None
    
def get_music_instrument(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.music_instrument
    except KeyError:
        return None

def get_link(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.link
    except KeyError:
        return None

def get_rating(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    if not has(key): return None
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    if not has(key): return None
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
