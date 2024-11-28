import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from songs_database import delete_item

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class DeleteTrackList:
    def __init__(self, window):
        window.geometry("830x380")
        window.title("Delete Track")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Select a track by clicking on it")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.list_txt.bind("<Button-1>", self.track_clicked)

        self.track_txt = tk.Text(window, width=24, height=5, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

        self.btn_delete = tk.Button(window, text="delete", command=self.delete_track)
        self.btn_delete.grid(row=2, column=3, padx=5, pady=5)

        self.list_tracks_clicked()
        self.current_key = None

    def track_clicked(self, event):
        index = self.list_txt.index("@%s,%s" % (event.x, event.y))
        line = self.list_txt.get(index + " linestart", index + " lineend")
        self.set_current_track(line)

    def set_current_track(self, track):
        self.current_key = key = int(track.split()[0]) - 1
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            composer = lib.get_composer(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"song: {name}\nartist: {artist}\ncomposer: {composer}\nrating: {rating}\nplay count: {play_count}"
            set_text(self.track_txt, track_details)

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    def delete_track(self):
        key = self.current_key
        name = lib.get_name(key)
        if name is not None:
            delete_item(key)
            track_list = lib.list_all()
            set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Delete Track button was clicked!")

if __name__ == "__main__":  
    window = tk.Tk()       
    fonts.configure()      
    DeleteTrackList(window)    
    window.mainloop()      