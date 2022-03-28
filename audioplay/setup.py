import os
from playsound import playsound

class forward:
    def __init__(self):
        self.path = 'media/forward.mp3'
    def play(self):
        if os.path.isfile(self.path):
            self.path = os.path.realpath(self.path)
            playsound(self.path)

class backward:
    def __init__(self):
        self.path = 'media/backward.mp3'
    def play(self):
        if os.path.isfile(self.path):
            self.path = os.path.realpath(self.path)
            playsound(self.path)

class found:
    def __init__(self):
        self.path = 'media/found.mp3'
    def play(self):
        if os.path.isfile(self.path):
            self.path = os.path.realpath(self.path)
            playsound(self.path)

class kick:
    def __init__(self):
        self.path = 'media/kick.mp3'
    def play(self):
        if os.path.isfile(self.path):
            self.path = os.path.realpath(self.path)
            playsound(self.path)

class lost:
    def __init__(self):
        self.path = 'media/lost.mp3'
    def play(self):
        if os.path.isfile(self.path):
            self.path = os.path.realpath(self.path)
            playsound(self.path)