class LibraryItem:
    def __init__(self, name, artist, composer, music_instrument, link, rating=0):
        self.name = name
        self.artist = artist
        self.composer = composer
        self.music_instrument = music_instrument
        self.link = link
        self.rating = rating
        self.play_count = 0

    def info(self):
        return f" {self.name} - {self.artist} - {self.composer} - {self.music_instrument}  {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "⭐️"
        return stars
