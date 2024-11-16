import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from update_tracks import UpdateTracksViewer
from create_track_list import CreateTrackList
from play_track import PlayTrack
from delete_track_list import DeleteTrackList

def view_tracks_clicked(): 
    status_lbl.configure(text="View Tracks button was clicked!")   # Update the status label to indicate the View Tracks button was clicked
    TrackViewer(tk.Toplevel(window))    # Open a new window for viewing tracks

def update_tracks_clicked():
    status_lbl.configure(text="Update Tracks button was clicked!")  # Update the status label to indicate the Update Tracks button was clicked
    UpdateTracksViewer(tk.Toplevel(window))   # Open a new window for updating tracks

def create_track_list_clicked():
    status_lbl.configure(text="Create Track List button was clicked!")   # Update the status label to indicate the Create Track List button was clicked
    CreateTrackList(tk.Toplevel(window))  # Open a new window for creating a track list

def play_tracks_clicked():  
    status_lbl.configure(text="Play Track button was clicked!")   # Update the status label to indicate the Play Track button was clicked
    PlayTrack(tk.Toplevel(window))    # Open a new window for playing tracks

def delete_tracks_clicked():
    status_lbl.configure(text="Delete Track button was clicked!")
    DeleteTrackList(tk.Toplevel(window))

window = tk.Tk()
window.geometry("520x210")
window.title("JukeBox")
window.configure(bg="gray")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List", command=create_track_list_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

play_tracks_btn = tk.Button(window, text="Play Tracks", command=play_tracks_clicked)
play_tracks_btn.grid(row=2, column=1, padx=10, pady=10)

delete_tracks_btn = tk.Button(window, text="Delete Tracks", command=delete_tracks_clicked)
delete_tracks_btn.grid(row=2, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
