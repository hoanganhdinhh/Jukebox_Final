import json

# Load the albums data from the JSON file
def load_albums():
    try:
        with open('./data/albums.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def list_albums():
    albums = load_albums()
    output = ""
    for album_name in albums.keys():
        output += f"{album_name}\n"
    return output

def list_songs(album_name):
    albums = load_albums()
    if album_name in albums:
        output = f"Album: {album_name}\n"
        for song in albums[album_name]["songs"]:
            output += f"{song['name']}\n"
        return output
    else:
        return f"No album found with the name '{album_name}'"
    
# Save the albums data to the JSON file
def save_albums(file_path, albums):
    with open(file_path, 'w') as file:
        json.dump(albums, file, indent=4)

# Add a new album
def create_album(albums, album_name):
    if album_name not in albums:
        albums[album_name] = {"songs": []}
        print(f"Album '{album_name}' added.")
    else:
        print(f"Album '{album_name}' already exists.")

# Add a song to an album
def add_song_to_album(albums, album_name, song_name, file_paths):
    if album_name in albums:
        for file_path in file_paths:
            albums[album_name]["songs"].append({"name": song_name, "file_path": file_path})
        print(f"Song '{song_name}' added to album '{album_name}' with file paths {file_paths}.")
    else:
        print(f"Album '{album_name}' does not exist. Please add the album first.")

        # Show all album names
def show_all_album_names(albums):
    if albums:
        print("Albums:")
        for album_name in albums.keys():
            print(f"- {album_name}")
    else:
        print("No albums found.")

def show_songs(albums):
    for album_name, album in albums.items():
        print(f"Album: {album_name}")
        for song in album["songs"]:
            print(f"- {song['name']}")
# Example usage
if __name__ == "__main__":
    file_path = './data/albums.json'
    albums = load_albums(file_path)

    # Add a new album
    create_album(albums, "Album name 3")

    add_song_to_album(albums, "Album name 3", "song5", ["path/to/song5.mp3", "path/to/another_song5.mp3"])
    add_song_to_album(albums, "Album name 3", "song6", ["path/to/song6.mp3", "path/to/another_song6.mp3"])
    add_song_to_album(albums, "Album name 3", "song6", "path/to/song6.mp3")

    # Save the updated albums data
    save_albums(file_path, albums)
