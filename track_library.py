from library_item import LibraryItem
from database.songs_database import get_item, get_len, has

library = []

def update():
    global library
    library = []
    for key in range(get_len()):
        song = get_item(key)
        library.append(LibraryItem(name = song["name"],artist = song["artist"], composer = song["composer"], image_path = song["image_path"], file_path = song["file_path"], rating = song["rating"], play_count = song["play_count"]))


def list_all():
    update()
    output = ""
    for key in range(len(library)):
        item = library[key]
        output += f"{key + 1} {item.info()}\n"
    return output


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


def get_image_path(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.image_path
    except KeyError:
        return None


def get_file_path(key):
    if not has(key): return None
    try:
        item = library[key]
        return item.file_path
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