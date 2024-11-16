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

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="Choose track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)
        
        play_btn = tk.Button(window, text="Play", command=lambda: self.open_yt())
        play_btn.grid(row=2, column=3, padx= 10, pady= 10)
        
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = int(self.input_txt.get()) - 1
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            composer = lib.get_composer(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"song: {name}\nartist: {artist}\ncomposer: {composer}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")


    def open_yt(self):
        key = int(self.input_txt.get()) - 1
        link = lib.get_link(key)
        if link is None:
            self.status_lbl.configure(text="No link found for this track") 
        elif link.startswith("https://www.youtube.com/"):
            webbrowser.open(link)
            self.status_lbl.configure(text="Play Track button was clicked!")
        else:
            self.status_lbl.configure(text="Invalid link for this track")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    PlayTrack(window)       # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc

