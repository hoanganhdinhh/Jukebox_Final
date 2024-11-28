import tkinter as tk
import font_manager as fonts
from playlist_database import load_playlist, add_track, clear_playlist, get_file_path
import tkinter.scrolledtext as tkst
import track_library as lib
import webbrowser , pygame, PIL
from PIL import Image, ImageTk

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class Playlist:
    def __init__(self, window):
        self.window = window
        window.geometry("1250x480")
        window.title("Playlist")
        window.configure(bg="light blue")

        list_tracks_btn = tk.Button(window, text="List All Tracks",activebackground='red', command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        header_lbl = tk.Label(window, text="Select a track by clicking on it")
        header_lbl.grid(row=0, column=1, padx=10, pady=10)

        list_playlist_btn = tk.Button(window, text="List Playlist",activebackground='red', command=self.load_playlist_clicked)
        list_playlist_btn.grid(row=0, column=4, padx=10, pady=10)
        
        self.list_txt = tkst.ScrolledText(window, width=65, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)
        self.list_txt.bind("<Button-1>", self.track_clicked)

        self.track_txt = tk.Text(window, width=24, height=5, wrap="none")
        self.track_txt.grid(row=1, column=3, padx=10, pady=10)

        #show image
        self.image_label = tk.Label(window)
        self.image_label.grid(row=3,column=1, sticky="NW",padx=10, pady=90)
                              
        #playlist listbox
        self.listbox = tk.Listbox(window, width=23, height=9)
        scrollbar = tk.Scrollbar(window)
        scrollbar.grid(row=1, column=7, sticky='ns')

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(row=1, column=4, columnspan=4, padx=10, pady=10)

        #Album listbox
        self.album_listbox = tk.Listbox(window, width=23, height=9)
        scrollbar = tk.Scrollbar(window)
        scrollbar.grid(row=1, column=11, sticky='ns')

        self.album_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        self.album_listbox.grid(row=1, column=8, columnspan=3, padx=10, pady=10)

        add_btn = tk.Button(window, text="Add to Playlist", activebackground='red', command=self.add_track_clicked)
        add_btn.grid(row=2, column=3, padx= 10, pady= 10)

        play_btn = tk.Button(window, text="Play",activebackground='red', command=self.play_track_in_playlist)
        play_btn.grid(row=2, column=4, padx= 10, pady= 10)

        reset_btn = tk.Button(window, text="Reset",activebackground='red', command=self.reset_playlist_clicked)
        reset_btn.grid(row=2, column=5, padx= 10, pady= 10) 

        self.status_lbl = tk.Label(window, text="")
        self.status_lbl.grid(row=2, column=0, padx=10, pady=10)

        #play music func btn
        play_music_btn = tk.Button(window, text="Play Music", command=self.play_music_clicked)
        play_music_btn.grid(row=3, column=0, padx=10, pady=10)

        previous_track_btn = tk.Button(window, text="⏮️", command=self.previous_track_clicked)
        previous_track_btn.grid(row=4, column=0, padx=10, pady=10)

        play_pause_music_btn = tk.Button(window, text="⏯️", command=self.play_pause_clicked)
        play_pause_music_btn.grid(row=4, column=1, padx=10, pady=10)

        next_track_btn = tk.Button(window, text="⏭️", command=self.next_track_clicked)
        next_track_btn.grid(row=4, column=2, padx=10, pady=10)

        stop_btn = tk.Button(window, text="⏹️", command=self.stop_clicked)
        stop_btn.grid(row=4, column=3, padx=10, pady=10)

        volume_up_btn = tk.Button(window, text="🔊", command=self.volume_up_clicked)
        volume_up_btn.grid(row=3, column=4, padx=10, pady=10)

        volume_down_btn = tk.Button(window, text="🔉", command=self.volume_down_clicked)
        volume_down_btn.grid(row=4, column=4, padx=10, pady=10)

        freq = 44100    # audio CD quality
        bitsize = -16   # unsigned 16 bit
        channels = 2    # 1 is mono, 2 is stereo
        buffer = 1024    # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        self.list_tracks_clicked()
        self.load_playlist_clicked()

    #play music function
    def play_music_clicked(self):
        music_file = lib.get_file_path(self.current_key)
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play()
        lib.increment_play_count(self.current_key)
        self.status_lbl.configure(text="Music is playing")
    
    def volume_up_clicked(self):
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(volume + 0.1)
        self.status_lbl.configure(text=f"Volume now is {pygame.mixer.music.get_volume()}")

    def volume_down_clicked(self):
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(volume - 0.1)
        self.status_lbl.configure(text=f"Volume now is {pygame.mixer.music.get_volume()}")

    def stop_clicked(self):
        pygame.mixer.music.stop()
        self.status_lbl.configure(text="Music stopped")

    def next_track_clicked(self):
        key = self.current_key + 1
        music_file = lib.get_file_path(key)
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_file)
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
        self.show_image(key)
        self.status_lbl.configure(text="Next track")

    def previous_track_clicked(self):
        key = int(self.current_key)
        music_file = lib.get_file_path(key)
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_file)
        volume = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(volume - 0.1)
        pygame.mixer.music.play()
        self.show_image(key)
        self.status_lbl.configure(text="Previous track")

    def play_pause_clicked(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.status_lbl.configure(text="Music paused")
        else:
            pygame.mixer.music.unpause()
            self.status_lbl.configure(text="Music is playing")

    #show image when track is clicked
    def show_image(self, key):
        image = lib.get_image_path(key)
        if image is not None:
            img = Image.open(image)
            img = img.resize((150, 150))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        else:
            self.image_label.config(image="")
            self.status_lbl.configure(text="No image found for this track")

    def load_playlist_clicked(self):
        self.listbox.delete(0, tk.END)
        tracks = load_playlist()
        for track in tracks:
            self.listbox.insert(tk.END, track)

    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

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
            self.show_image(key)

    # def search_name(self):
    #     search_name = self.input_search_name.get()
    #     name = lib.get_name(self.current_key)
    #     self.current_key = lib.get_key_by_name(name)
    #     if name.startswith(search_name):
    #         name = self.input_name.get()
    #         artist = self.input_artist.get()
    #         composer = self.input_composer.get()
    #         music_instrument = self.input_music_instrument.get()
    #         link = self.input_link.get()
    #         rating = self.input_rating.get()
    #         new = get_item(self.current_key)
    #         new["name"] = name
    #         new["artist"] = artist
    #         new["composer"] = composer
    #         new["music_instrument"] = music_instrument
    #         new["link"] = link
    #         new["rating"] = int(rating)
    #         set_item(self.current_key , new)
    #         track_list = lib.list_all()
    #         set_text(self.list_txt, track_list)
    #     self.status_lbl.configure(text="Update Tracks button was clicked!")

    def add_track_clicked(self):
        key = self.current_key
        name = lib.get_name(key)
        if name is not None and name not in self.listbox.get(0, tk.END):
            file_path = lib.get_file_path(key)
            add_track(name, file_path)
            self.load_playlist_clicked()
            self.status_lbl.configure(text="Track added to playlist!")
        else:
            self.status_lbl.configure(text="Track already in playlist!")

    def reset_playlist_clicked(self):
        clear_playlist()
        self.load_playlist_clicked()
        self.status_lbl.configure(text="Playlist reset!")

    def play_track_in_playlist(self):
        selection = self.listbox.curselection()
        name = self.listbox.get(selection)
        file_path = get_file_path(name)
        if file_path is None:
            self.status_lbl.configure(text="No file found for this track")
        else:
            music_file = file_path
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play()
            self.status_lbl.configure(text="Music is playing")
        
        

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    Playlist(window)     # open the CreateTrackList GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
