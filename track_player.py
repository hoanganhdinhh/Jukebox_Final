import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from play_track import PlayTrack
from configure_tracks import ConfigureTracks

def view_tracks_clicked(): 
    status_lbl.configure(text="View Tracks button was clicked!")   # Update the status label to indicate the View Tracks button was clicked
    TrackViewer(tk.Toplevel(window))    # Open a new window for viewing tracks

def play_tracks_clicked():  
    status_lbl.configure(text="Play Track button was clicked!")   # Update the status label to indicate the Play Track button was clicked
    PlayTrack(tk.Toplevel(window))    # Open a new window for playing tracks

def config_track_clicked():
    status_lbl.configure(text="Configure Track button was clicked!")
    ConfigureTracks(tk.Toplevel(window))
    
window = tk.Tk()
window.geometry("490x160")
window.title("JukeBox")
window.configure(bg="gray")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

config_tracks_btn = tk.Button(window, text="Configure Tracks", command=config_track_clicked)
config_tracks_btn.grid(row=1, column=1, padx=10, pady=10)

play_tracks_btn = tk.Button(window, text="Play Tracks", command=play_tracks_clicked)
play_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
