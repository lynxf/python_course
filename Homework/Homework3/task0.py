def import_song(file_name):
    file = open(file_name, "r")
    songs = []
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
    for i in file:
        name, artist, album, position, year, duration = i.split("\t")
        t = (name, artist, album, position, year, duration)
        songs.append(t)
    return(songs)
    
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
    

