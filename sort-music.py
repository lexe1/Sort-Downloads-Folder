import os
import shutil
from mutagen.mp3 import MP3

user_path = os.path.expanduser('~')

music = user_path + '/Downloads/Music/'
good = user_path + '/Downloads/Music/320kbps/'


try:
    os.mkdir(good)
except FileExistsError:
    pass


def check():
    for file in os.listdir(music):
        if file.endswith('.mp3'):
            bitrate = MP3(music + file).info.bitrate
            if bitrate == 320000:
                shutil.move(music + file, good + file)
    print('Music Files Sorted!')


if __name__ == '__main__':
    check()
