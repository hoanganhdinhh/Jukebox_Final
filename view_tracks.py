import tkinter as tk                  # import the tkinter module
import tkinter.scrolledtext as tkst   # import the scrolledtext module
import track_library as lib           # import the track_library module
import font_manager as fonts          # import the font_manager module


def set_text(text_area, content):    # inserts content into the text_area 
    text_area.delete("1.0", tk.END)  # first the existing content is deleted
    text_area.insert(1.0, content)   # then the new content is inserted


class TrackViewer():                # Create a class TrackViewer
    def __init__(self, window):     # Create a constructor for the TrackViewer class
        window.geometry("810x350")  # Set the size of the window
        window.title("View Tracks") # Set the title of the window

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)   # Create a button to list all the tracks
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)                                         # Place the list tracks button in the window

        enter_lbl = tk.Label(window, text="Enter Track Number") # Create a label to enter the track number
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)       # Place the label in the window

        self.input_txt = tk.Entry(window, width=3)              # Create an entry box to enter the track number
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Place the entry box in the window

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)  # Create a button to view the track details
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)                                   # Place the view track button in the window

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")      # Create a scrolled text box to display the list of tracks  
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Place the list text box in the window

        self.track_txt = tk.Text(window, width=24, height=6, wrap="none")     # Create a text box to display the track details
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)   # Place the track text box in the window

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))                 # Create a status label
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)   # Place the status label in the window

        self.list_tracks_clicked()  # Call the list_tracks_clicked function to list all the tracks

    def view_tracks_clicked(self):            # declare a function to view the track details
        key = int(self.input_txt.get()) - 1   # Get the key of the track from the input text box
        name = lib.get_name(key)              # Get the name of the track using the key
        if name is not None:                  # If the name is not None
            artist = lib.get_artist(key)              # Get the artist of the track using the key
            composer = lib.get_composer(key)                  # Get the composer of the track using the key
            music_instrument = lib.get_music_instrument(key)  # Get the music instrument of the track using the key
            rating = lib.get_rating(key)                      # Get the rating of the track using the key 
            play_count = lib.get_play_count(key)              # Get the play count of the track using the key
            # Create a string with the track details  
            track_details = f"song: {name}\nartist: {artist}\ncomposer: {composer}\nmusic instrument: {music_instrument}\nrating: {rating}\nplays: {play_count}" 
            set_text(self.track_txt, track_details)      # Set the text of the track text box to the track details
        else:    # If the name is None
            set_text(self.track_txt, f"Track {key} not found")            # Set the text of the track text box to indicate the track was not found
        self.status_lbl.configure(text="View Track button was clicked!")  # Set the status label when the view track button was clicked

    def list_tracks_clicked(self):            # declare a function to list all the tracks
        track_list = lib.list_all()           # Get the list of all tracks
        set_text(self.list_txt, track_list)   # Set the text of the list text box to the track list
        self.status_lbl.configure(text="List Tracks button was clicked!")   # Set the status label when the list tracks button was clicked

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
