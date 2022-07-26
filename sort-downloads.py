import os
import shutil

user_path = os.path.expanduser('~')

downloads = user_path + '/Downloads/'
images = user_path + '/Downloads/Images/'
music = user_path + '/Downloads/Music/'
soft = user_path + '/Downloads/Soft/'
books = user_path + '/Downloads/Books/'
torrents = user_path + '/Downloads/Torrents/'


try:
    os.mkdir(music)
except FileExistsError:
    pass
try:
    os.mkdir(images)
except FileExistsError:
    pass
try:
    os.mkdir(soft)
except FileExistsError:
    pass
try:
    os.mkdir(books)
except FileExistsError:
    pass


def sort():
    for file in os.listdir(downloads):
        if file.endswith('.mp3'):
            shutil.move(downloads + file, music + file)

        if file.endswith('.jpg'):
            shutil.move(downloads + file, images + file)
        if file.endswith('.png'):
            shutil.move(downloads + file, images + file)

        if file.endswith('.djvu'):
            shutil.move(downloads + file, books + file)
        if file.endswith('.epub'):
            shutil.move(downloads + file, books + file)
        if file.endswith('.pdf'):
            shutil.move(downloads + file, books + file)
        if file.endswith('.fb2'):
            shutil.move(downloads + file, books + file)

        if file.endswith('.exe'):
            shutil.move(downloads + file, soft + file)
        if file.endswith('.msi'):
            shutil.move(downloads + file, soft + file)

        if file.endswith('.torrent'):
            shutil.move(downloads + file, torrents + file)


if __name__ == '__main__':
    sort()
