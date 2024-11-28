import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts
from database.songs_database import get_item, set_item
from tkinter import filedialog

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)

class UpdateTracks():
    def __init__(self, window):
        window.geometry("990x610")
        window.title("Update Tracks")
        window.configure(bg="light blue")

        list_tracks_btn = tk.Button(window, text="List All Tracks",activebackground='red', command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        enter_lbl = tk.Label(window, text="Select a track by clicking on it")
        enter_lbl.grid(row=0, column=2, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(window, width=55, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.list_txt.bind("<Button-1>", self.track_clicked)

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

        self.image_path_lb = tk.Label(window, text="image path:")
        self.image_path_lb.grid(row=4, column=3, padx=10, pady=10)

        self.input_image_path = tk.Entry(window, width=27)
        self.input_image_path.grid(row=4, column=4, padx=5, pady=5)

        browse_image_path=tk.Button(window, text="Browse",font=40,command=self.browse_image_path)
        browse_image_path.grid(row=4,column=5)

        self.file_path_lb = tk.Label(window, text="file path:")
        self.file_path_lb.grid(row=5, column=3, padx=10, pady=10)

        self.input_file_path = tk.Entry(window, width=27)
        self.input_file_path.grid(row=5, column=4, padx=5, pady=5)

        browse_image_path=tk.Button(window, text="Browse",font=40,command=self.browse_file_path)
        browse_image_path.grid(row=5,column=5)

        self.rating_lb = tk.Label(window, text="rating:")
        self.rating_lb.grid(row=6, column=3, padx=10, pady=10)

        self.input_rating = tk.Entry(window, width=27)
        self.input_rating.grid(row=6, column=4, padx=5, pady=5)

        self.btn_update = tk.Button(window, text="update",activebackground='red', command=self.update_track)
        self.btn_update.grid(row=7, column=4, padx=5, pady=5)

        self.list_tracks_clicked()
        self.current_key = None

    def track_clicked(self, event):
        index = self.list_txt.index("@%s,%s" % (event.x, event.y))
        line = self.list_txt.get(index + " linestart", index + " lineend")
        self.set_current_track(line)
        self.edit_tracks_clicked()
        self.status_lbl.configure(text=f"Current track is: {line}")

    def set_current_track(self, track):
        self.current_key = key = int(track.split()[0]) - 1

    def browse_image_path(self):
        self.input_image_path.delete(0, tk.END)
        filename = filedialog.askopenfilename(filetypes=(("mp3 files","*.mp3"),("All files","*.*")))
        new_path = "./" + "/".join(filename.replace("\\", "/").split("/")[-2:])
        self.input_image_path.insert(tk.END, new_path)

    def browse_file_path(self):
        self.input_file_path.delete(0, tk.END)
        filename = filedialog.askopenfilename(filetypes=(("image files","*.jpg"),("All files","*.*")))
        new_path = "./" + "/".join(filename.replace("\\", "/").split("/")[-2:])
        self.input_file_path.insert(tk.END, new_path)

    def edit_tracks_clicked(self):
        key = self.current_key
        name = lib.get_name(key)
        if name is not None:
            #delete old text
            self.input_name.delete(0, tk.END)    
            self.input_artist.delete(0, tk.END)
            self.input_composer.delete(0, tk.END)
            self.input_image_path.delete(0, tk.END)
            self.input_file_path.delete(0, tk.END)
            self.input_rating.delete(0, tk.END)
            self.current_key = key      
            artist = lib.get_artist(key)
            composer = lib.get_composer(key)
            image_path = lib.get_image_path(key)
            file_path = lib.get_file_path(key)
            rating = lib.get_rating(key)
            #insert new text
            self.input_name.insert(0, name)        
            self.input_artist.insert(0, artist)
            self.input_composer.insert(0, composer)
            self.input_image_path.insert(0, image_path)
            self.input_file_path.insert(0, file_path)
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
            image_path = self.input_image_path.get()
            file_path = self.input_file_path.get()
            rating = self.input_rating.get()
            new = get_item(self.current_key)
            new["name"] = name
            new["artist"] = artist
            new["composer"] = composer
            new["image_path"] = image_path
            new["file_path"] = file_path
            try:
                new["rating"] = int(rating)
            except ValueError:
                self.status_lbl.configure(text="Rating must be a number!")
                return
            set_item(self.current_key , new)
            track_list = lib.list_all()
            set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="Update Tracks button was clicked!")



if __name__ == "__main__":  
    window = tk.Tk()       
    fonts.configure()      
    UpdateTracks(window)    
    window.mainloop()      
