songs_file = "song1.tsv"
names = []
artists = []
albums = []
positions = []
years = []
durations = []


with open(songs_file, "r") as songs:
    data = songs.read().splitlines()

for line in data:
    elements = line.split("\t")
    names.append(elements[0])
    artists.append(elements[1])
    albums.append(elements[2])
    positions.append(elements[3])
    years.append(elements[4])
    durations.append(elements[5])

def most_common_artist(artists_list):
    return max(set(artists_list), key=artists_list.count)

def longest_song(durations_list, artists_list, songs_list):
    longest_duration = max(durations_list)
    index = durations_list.index(longest_duration)
    return songs_list[index] + "\t" + artists_list[index]

def longest_album(durations_list, artists_list, albums_list):
    album_artist_durations = {}
    counter = 0
    for album in albums_list:
        if str(album+"\t"+artists_list[counter]) in album_artist_durations:
            album_artist_durations[str(album+"\t"+artists_list[counter])] += int(durations_list[counter])
        else:
            album_artist_durations[str(album+"\t"+artists_list[counter])] = int(durations_list[counter])
        counter += 1
    return sorted(album_artist_durations, key=album_artist_durations.get, reverse = True)[0]

def most_frequent_words_in_names(songs_list):
    word_freqs = {}
    word_list = []
    for song in songs_list:
        for word in song.lower().split():
            word_list.append(word)
            if word in word_freqs:
                word_freqs[word] += 1
            else:
                word_freqs[word] = 1
    if len(word_freqs) > 9:
        word_list = sorted(word_freqs, key=word_freqs.get, reverse = True)[0:10]
    return "\t".join(word_list)

def most_albums(albums_list, artists_list):
    album_artist_number = {}
    counter = 0
    for album in albums_list:
        album_artist_tuple = (album, artists_list[counter])
        if album_artist_tuple in album_artist_number:
            album_artist_number[album_artist_tuple] += 1
        else:
            album_artist_number[album_artist_tuple] = 1
        counter += 1
    return sorted(album_artist_number, key=album_artist_number.get, reverse = True)[0][1]


print(most_common_artist(artists))
print(longest_song(durations, artists, names))
print(longest_album(durations, artists, albums))
print(most_frequent_words_in_names(names))
print(most_albums(albums, artists))
