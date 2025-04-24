import json
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.history = []

    @abstractmethod
    def add_to_history(self, song):
        pass

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'history': [song.song_id for song in self.history],
            'downloads': getattr(self, 'downloads', 0)
        }

    @staticmethod
    def from_dict(data):
        if data.get('downloads') is not None:
            user = Member(data['user_id'], data['name'])
            user.downloads = data['downloads']
        else:
            user = Admin(data['user_id'], data['name'])
        return user

class SongItem(ABC):
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.downloads = 0

    def add_to_history(self, song):
        self.history.append(song)

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def add_to_history(self, song):
        self.history.append(song)

class Song(SongItem):
    def __init__(self, song_id, title, artist):
        super().__init__(song_id, title, artist)

    def to_dict(self):
        return {
            'song_id': self.song_id,
            'title': self.title,
            'artist': self.artist
        }

class StreamingManager:
    def __init__(self):
        self.users = {}
        self.songs = {}
        self.load_data()

    def load_data(self):
        try:
            with open('members.json', 'r') as f:
                users_dict = json.load(f)
                self.users = {user_id: User.from_dict(user_data) for user_id, user_data in users_dict.items()}
            
            with open('songs.json', 'r') as f:
                songs_dict = json.load(f)
                self.songs = {song_id: Song(**song_data) for song_id, song_data in songs_dict.items()}
        except FileNotFoundError:
            self.users = {}
            self.songs = {}

    def save_data(self):
        users_dict = {user_id: user.to_dict() for user_id, user in self.users.items()}
        with open('members.json', 'w') as f:
            json.dump(users_dict, f)
        
        songs_dict = {song_id: song.to_dict() for song_id, song in self.songs.items()}
        with open('songs.json', 'w') as f:
            json.dump(songs_dict, f)

    def add_user(self, user):
        self.users[user.user_id] = user
        self.save_data()

    def add_song(self, song):
        self.songs[song.song_id] = song
        self.save_data()

    def stream_song(self, user_id, song_id):
        user = self.users.get(user_id)
        song = self.songs.get(song_id)
        if user and song:
            user.add_to_history(song)
            self.log_action(user_id, song_id, 'stream')
        else:
            print("User or Song not found")

    def download_song(self, user_id, song_id):
        user = self.users.get(user_id)
        song = self.songs.get(song_id)
        if user and song:
            if user.downloads < 10:
                user.downloads += 1
                user.add_to_history(song)
                self.log_action(user_id, song_id, 'download')
            else:
                print("Download limit exceeded")
        else:
            print("User or Song not found")

    def log_action(self, user_id, song_id, action):
        with open('log.txt', 'a') as f:
            f.write(f"{datetime.now()}: User {user_id} {action}ed Song {song_id}\n")

# Example Usage
manager = StreamingManager()
admin = Admin('A1', 'AdminUser')
member = Member('M1', 'MemberUser')
song1 = Song('S1', 'SongTitle1', 'Artist1')

manager.add_user(admin)
manager.add_user(member)
manager.add_song(song1)

manager.stream_song('M1', 'S1')
manager.download_song('M1', 'S1')
