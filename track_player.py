import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from play_track import PlayTrack
from create_track_list import CreateTrackList
from update_tracks import UpdateTracks
from delete_track_list import DeleteTrackList
from play_track import Playlist

def view_tracks_clicked(): 
    status_lbl.configure(text="View Tracks button was clicked!")  
    TrackViewer(tk.Toplevel(window))

def play_tracks_clicked():  
    status_lbl.configure(text="Play Track button was clicked!")
    PlayTrack(tk.Toplevel(window))

def playlists_clicked():
    status_lbl.configure(text="Playlists button was clicked!")
    Playlist(tk.Toplevel(window))

def create_track_clicked():
    status_lbl.configure(text="Create Track button was clicked!")
    CreateTrackList(tk.Toplevel(window))

def update_track_clicked():
    status_lbl.configure(text="Update Track button was clicked!")
    UpdateTracks(tk.Toplevel(window))

def delete_track_clicked():
    status_lbl.configure(text="Delete Track button was clicked!")
    DeleteTrackList(tk.Toplevel(window))
    
window = tk.Tk()
window.geometry("520x210")
window.title("JukeBox")
window.configure(bg="gray")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

view_tracks_btn = tk.Button(window, text="View Tracks", activebackground='red', command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

play_tracks_btn = tk.Button(window, text="Play Tracks",activebackground='red', command=play_tracks_clicked)
play_tracks_btn.grid(row=1, column=1, padx=10, pady=10)

playlists_btn = tk.Button(window, text="Playlists",activebackground='red',command=playlists_clicked)
playlists_btn.grid(row=1, column=2, padx=10, pady=10)

create_tracks_btn = tk.Button(window, text="Create Tracks",activebackground='red', command=create_track_clicked)
create_tracks_btn.grid(row=2, column=0, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks",activebackground='red', command=update_track_clicked)
update_tracks_btn.grid(row=2, column=1, padx=10, pady=10)

delete_tracks_btn = tk.Button(window, text="Delete Tracks",activebackground='red', command=delete_track_clicked)
delete_tracks_btn.grid(row=2, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
