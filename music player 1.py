
import pygame
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0
        self.volume = 0.5

        pygame.mixer.init()

        self.create_ui()

    def create_ui(self):
        # Create and place UI elements
        self.playlist_label = Label(self.root, text="Playlist")
        self.playlist_label.pack()

        self.playlist_listbox = Listbox(self.root)
        self.playlist_listbox.pack()

        self.add_button = Button(self.root, text="Add Track", command=self.add_track)
        self.add_button.pack()

        self.play_button = Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.next_button = Button(self.root, text="Next", command=self.next_track)
        self.next_button.pack()

        self.prev_button = Button(self.root, text="Previous", command=self.prev_track)
        self.prev_button.pack()

        self.volume_label = Label(self.root, text="Volume")
        self.volume_label.pack()

        self.volume_slider = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)  # Set initial volume to 50
        self.volume_slider.pack()

        self.cover_image = Label(self.root)
        self.cover_image.pack()

        # Update playlist UI
        self.update_playlist_ui()

    def add_track(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.update_playlist_ui()

    def update_playlist_ui(self):
        self.playlist_listbox.delete(0, END)  # Clear the existing list

        for track in self.playlist:
            track_name = os.path.basename(track)
            self.playlist_listbox.insert(END, track_name)

        # Select the currently playing track in the list
        self.playlist_listbox.selection_clear(0, END)
        self.playlist_listbox.selection_set(self.current_track)
        self.playlist_listbox.activate(self.current_track)

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.stop()
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.stop()
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()

    def set_volume(self, value):
        self.volume = value / 100
        pygame.mixer.music.set_volume(self.volume)

if __name__ == "__main__":
    root = Tk()
    player = MusicPlayer(root)
    root.mainloop()
