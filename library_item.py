class LibraryItem:
    def __init__(self, name, artist, composer, image_path, file_path, rating=0, play_count=0):
        self.name = name
        self.artist = artist
        self.composer = composer
        self.image_path = image_path
        self.file_path = file_path
        self.rating = rating
        self.play_count = play_count

    def info(self):
        return f" {self.name} - {self.artist} - {self.composer}  {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "⭐️"
        return stars
