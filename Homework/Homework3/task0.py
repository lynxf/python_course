
class Song:
    def __init__(self, name, artist, album, position, year, duration):
        self.artist = artist
        self.name = name
        self.album = album
        self.position = position
        self.year = year
        self.duration = duration
    def __repr__(self):
        song = self.name+' '+self.artist+' '+self.album+' '+self.position+' '+self.year+' '+self.duration
        return(song)
    
    def __lt__(self, other):
        if self.artist < other.artist:
            return True
        if self.artist == other.artist and self.album < other.album:
            return True
        return False
    
def import_song(file_name):
    file = open(file_name, "r")
    songs = []
    for i in file:
        i = i.strip()
        for j in i:
            name, artist, album, position, year, duration = i.split("\t")
            t = (name, artist, album, position, year, duration)
            songs.append(t)
        return(songs)
        
def export_songs(songs, file_names):
    with open(file_names, "w") as tsv:
        for i in songs:
            tsv_songs = i.name+'\t'+i.artist+'\t'+i.album+'\t'+i.position+'\t'+i.year+'\t'+i.duration
            tsv.write(tsv_songs)
    

