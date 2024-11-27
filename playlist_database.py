import csv

def load_playlist():
    tracks = []
    with open('./data/playlist.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            tracks.append(row[0])
    return tracks

def clear_playlist():
    with open('./data/playlist.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name','file_path'])

def add_track(track,file_path):
    with open('./data/playlist.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([track,file_path])

def get_link(track_name):
    with open('./data/playlist.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == track_name:
                return row[1]
    return None