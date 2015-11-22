
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
    
def export_songs(songs, file_names):
    f = open(file_names, "w")
    for i in songs:
        t = i[0]
        k = i[1]
        l = i[2]
        n = i[3]
        m = i[4]
        r = i[5]
        f.write(t+"\t"+k+"\t"+l+"\t"+n+"\t"+m+"\t"+r+"\n")
    f.close()
    

