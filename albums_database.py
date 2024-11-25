import json


albums = json.loads('./data/albums.json')

def create_album(album_name):
    if album_name not in albums:
        albums[album_name] = {"songs": []}



def add_track_to_album(album_name,track):
    if album_name in albums:
        albums[album_name]["songs"].append(track)
        print(f"Track '{track}' added to album {album_name}.")
    else:
        print(f"Album {album_name} does not exist.")



# Example usage
# create_album("03")
# add_track_to_album("03", "song5")
# add_track_to_album("01", "song6")

# Print the updated albums
print(json.dumps(albums, indent=4))