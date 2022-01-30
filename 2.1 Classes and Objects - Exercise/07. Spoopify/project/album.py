# from song import Song

class Album:
    def __init__(self, name, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        elif not isinstance(songs, list):
            self.songs = []
            self.songs.append(songs)
        else:
            self.songs = songs
        self.published = False

    def add_song(self, song):  # song : Song
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if self.published:
            return 'Cannot add songs. Album is published.'
        if song in self.songs:
            return 'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name):
        if self.published:
            return f'Cannot remove songs. Album is published.'
        if song_name not in [x.name for x in self.songs]:
            return 'Song is not in the album.'
        song_to_remove = [x for x in self.songs if x.name == song_name][0]
        self.songs.remove(song_to_remove)
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if self.published:
            return f'Album {self.name} is already published.'
        self.published = True
        return f'Album {self.name} has been published.'

    def details(self):
        song_collection = f'Album {self.name}\n'
        for song in self.songs:
            song_collection += f'== {song.get_info()}\n'
        return song_collection
