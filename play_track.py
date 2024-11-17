import tkinter as tk
import track_library as lib
import font_manager as fonts
import tkinter.scrolledtext as tkst
import webbrowser


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class PlayTrack:
    def __init__(self, window):
        window.geometry("820x380")
        window.title("Play Track")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        header_lbl = tk.Label(window, text="Select a track by clicking on it")
        header_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.list_txt.bind("<Button-1>", self.track_clicked)

        self.track_txt = tk.Text(window, width=24, height=6, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        play_btn = tk.Button(window, text="Play", command=lambda: self.open_yt())
        play_btn.grid(row=2, column=3, padx= 10, pady= 10)
        
        self.list_tracks_clicked()


    def list_tracks_clicked(self): 
        track_list = lib.list_all() # Get the list of all tracks
        set_text(self.list_txt, track_list) # Set the text of the list text box to the track list
        self.status_lbl.configure(text="List Tracks button was clicked!") # Set the status label when the list tracks button was clicked

    def track_clicked(self, event):
        index = self.list_txt.index("@%s,%s" % (event.x, event.y)) # Get the index of the text at the position of the mouse click event
        line = self.list_txt.get(index + " linestart", index + " lineend") # Get the entire line of text at the specified index
        self.set_current_track(line) # Set the current track using the retrieved line of text

    def set_current_track(self, track):
        self.current_key = key = int(track.split()[0]) - 1 # Get the key of the track from the first word of the track string
        name = lib.get_name(key) # Get the name of the track using the key
        if name is not None:
            artist = lib.get_artist(key) # Get the artist of the track using the key
            composer = lib.get_composer(key) # Get the composer of the track using the key
            music_instrument = lib.get_music_instrument(key) # Get the music instrument of the track using the key
            rating = lib.get_rating(key) # Get the rating of the track using the key
            play_count = lib.get_play_count(key) # Get the play count of the track using the key
            track_details = f"song: {name}\nartist: {artist}\ncomposer: {composer}\nmusic instrument: {music_instrument}\nrating: {rating}\nplays: {play_count}"  # Create a string with the track details
            set_text(self.track_txt, track_details) # Set the text of the track text box to the track details


    def open_yt(self): # declare a function openning the youtube link of the current track
        key = self.current_key  # Get the current key
        link = lib.get_link(key) # Get the link of the track using the key
        if link is None:    # If no link was found for the track
            self.status_lbl.configure(text="No link found for this track")  # Set the status label to indicate that no link was found
        elif link.startswith("https://www.youtube.com/"):    # If the link is a valid youtube link as "https://www.youtube.com/..."
            webbrowser.open(link)  # Open the link in the web browser
            self.status_lbl.configure(text="Play Track button was clicked!") # Set the status label when the play track button was clicked
        else:
            self.status_lbl.configure(text="Invalid link for this track")   # Set the status label when the link is invalid


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    PlayTrack(window)       # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc

