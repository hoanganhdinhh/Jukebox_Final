import tkinter as tk
import track_library as lib
import font_manager as fonts
from create_track_list import CreateTrackList
from update_tracks import UpdateTracksViewer
from delete_track_list import DeleteTrackList

class ConfigureTracks:
    def __init__(self, window):
        window.geometry("530x150")
        window.title("Configure Tracks")

        self.window = window
        self.header_lbl = tk.Label(self.window, text="Configure the tracks by clicking one of the buttons below")
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.create_track_list_btn = tk.Button(window, text="Create Track List", command=self.create_track_list_clicked)
        self.create_track_list_btn.grid(row=1, column=0, padx=10, pady=10)

        self.update_tracks_btn = tk.Button(window, text="Update Tracks", command=self.update_tracks_clicked)
        self.update_tracks_btn.grid(row=1, column=1, padx=10, pady=10)

        self.delete_tracks_btn = tk.Button(window, text="Delete Tracks", command=self.delete_tracks_clicked)
        self.delete_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def update_tracks_clicked(self):
        self.status_lbl.configure(text="Update Tracks button was clicked!")  # Update the status label to indicate the Update Tracks button was clicked
        UpdateTracksViewer(tk.Toplevel(self.window))   # Open a new window for updating tracks

    def create_track_list_clicked(self):
        self.status_lbl.configure(text="Create Track List button was clicked!")   # Update the status label to indicate the Create Track List button was clicked
        CreateTrackList(tk.Toplevel(self.window))  # Open a new window for creating a track list

    def delete_tracks_clicked(self):
        self.status_lbl.configure(text="Delete Track button was clicked!")
        DeleteTrackList(tk.Toplevel(self.window))

if __name__ == "__main__":  
    window = tk.Tk()       
    fonts.configure()      
    ConfigureTracks(window)    
    window.mainloop()      