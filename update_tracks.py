import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from database import get_item, set_item


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateTracksViewer():
    def __init__(self, window):
        window.geometry("990x610")
        window.title("Update Tracks")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=2, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=3, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="Edit Track", command=self.edit_tracks_clicked)
        check_track_btn.grid(row=0, column=4, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=55, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=3, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.name_lb = tk.Label(window, text="name:")
        self.name_lb.grid(row=1, column=3, sticky="S", padx=1, pady=1)

        self.input_name = tk.Entry(window, width=27)
        self.input_name.grid(row=1, column=4, sticky="S",padx=5, pady=5)

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

        self.btn_update = tk.Button(window, text="update", command=self.update_track)
        self.btn_update.grid(row=7, column=4, padx=5, pady=5)

        self.list_tracks_clicked()
        self.current_key = None

    def edit_tracks_clicked(self):
        key = int(self.input_txt.get()) - 1
        name = lib.get_name(key)
        if name is not None:
            self.current_key = key      
            artist = lib.get_artist(key)
            composer = lib.get_composer(key)
            link = lib.get_link(key)
            rating = lib.get_rating(key)
            self.input_name.insert(0, name)        
            self.input_artist.insert(0, artist)
            self.input_composer.insert(0, composer)
            self.input_link.insert(0, link)
            self.input_rating.insert(0, rating)
        
           
        self.status_lbl.configure(text="View Track button was clicked!")

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def update_track(self):
        if self.current_key is not None:
            name = self.input_name.get()
            artist = self.input_artist.get()
            composer = self.input_composer.get()
            music_instrument = self.input_music_instrument.get()
            link = self.input_link.get()
            rating = self.input_rating.get()
            new = get_item(self.current_key)
            new["name"] = name
            new["artist"] = artist
            new["composer"] = composer
            new["music_instrument"] = music_instrument
            new["link"] = link
            new["rating"] = int(rating)
            set_item(self.current_key , new)
            track_list = lib.list_all()
            set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Update Tracks button was clicked!")



if __name__ == "__main__":  
    window = tk.Tk()       
    fonts.configure()      
    UpdateTracksViewer(window)    
    window.mainloop()      
