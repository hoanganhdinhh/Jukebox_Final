import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from database import delete_item

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class DeleteTrackList:
    def __init__(self, window):
        window.geometry("830x380")
        window.title("Delete Track")

        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_num = tk.Entry(window, width=3)
        self.input_num.grid(row=0, column=2, padx=10, pady=10)

        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=58, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

        self.btn_delete = tk.Button(window, text="delete", command=self.delete_track)
        self.btn_delete.grid(row=2, column=3, padx=5, pady=5)

        self.list_tracks_clicked()
        self.current_key = None
    
    def view_tracks_clicked(self):
        key = int(self.input_num.get()) - 1
        self.current_key = key
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

    def delete_track(self):
        if self.current_key is not None:
            num = (int(self.input_num.get()))-1
            delete_item(self.current_key)
            track_list = lib.list_all()
            set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Delete Track button was clicked!")



if __name__ == "__main__":  
    window = tk.Tk()       
    fonts.configure()      
    DeleteTrackList(window)    
    window.mainloop()      