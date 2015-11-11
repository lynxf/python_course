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
        #i = i.strip()
        name, artist, album, position, year, duration = i.split("\t")
        t = (name, artist, album, position, year, duration)
        songs.append(t)
    return(songs)
    

