import tkinter as tk
import track_library as lib
import tkinter.scrolledtext as tkst
import font_manager as fonts
from database import set_item, get_len

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class CreateTrackList:
    def __init__(self, window):
        window.geometry("930x590")
        window.title("Create Track List")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.name_lb = tk.Label(window, text="name:")
        self.name_lb.grid(row=1, column=3, sticky="S", padx=1, pady=1)

        self.input_name = tk.Entry(window, width=27)
        self.input_name.grid(row=1, column=4, sticky="S", padx=5, pady=5)

        self.artist_lb = tk.Label(window, text="artist:")
        self.artist_lb.grid(row=2, column=3, padx=10, pady=10)

        self.input_artist = tk.Entry(window, width=27)
        self.input_artist.grid(row=2, column=4, padx=5, pady=5)

        self.composer_lb = tk.Label(window, text="composer:")
        self.composer_lb.grid(row=3, column=3, padx=10, pady=10)

        self.input_composer = tk.Entry(window, width=27)
        self.input_composer.grid(row=3, column=4, padx=5, pady=5)

        self.music_instrument_lb = tk.Label(window, text="music instrument:")
        self.music_instrument_lb.grid(row=4, column=3, padx=10, pady=10)

        self.input_music_instrument = tk.Entry(window, width=27)
        self.input_music_instrument.grid(row=4, column=4, padx=5, pady=5)

        self.link_lb = tk.Label(window, text="youtube link:")
        self.link_lb.grid(row=5, column=3, padx=10, pady=10)

        self.input_link = tk.Entry(window, width=27)
        self.input_link.grid(row=5, column=4, padx=5, pady=5)

        self.rating_lb = tk.Label(window, text="rating:")
        self.rating_lb.grid(row=6, column=3, padx=10, pady=10)

        self.input_rating = tk.Entry(window, width=27)
        self.input_rating.grid(row=6, column=4, padx=5, pady=5)

        self.btn_create = tk.Button(window, text="create", command=self.create_track)
        self.btn_create.grid(row=7, column=4, padx=5, pady=5)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def create_track(self):
        name = self.input_name.get()
        artist = self.input_artist.get()
        composer = self.input_composer.get()
        music_instrument = self.input_music_instrument.get()
        link = self.input_link.get()
        rating = self.input_rating.get()
        new = {}
        new["name"] = name
        new["artist"] = artist
        new["composer"] = composer
        new["music_instrument"] = music_instrument
        new["link"] = link
        new["rating"] = int(rating)
        set_item(get_len(),new)
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Create Track button was clicked!")
        
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CreateTrackList(window)     # open the CreateTrackList GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
