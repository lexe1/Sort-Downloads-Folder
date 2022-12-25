import os
import shutil

user_path = os.path.expanduser('~')

downloads = user_path + '/Downloads/'
images = user_path + '/Downloads/Images/'
music = user_path + '/Downloads/Music/'
soft = user_path + '/Downloads/Soft/'
books = user_path + '/Downloads/Books/'
torrents = user_path + '/Downloads/Torrents/'

folders = [music, images, soft, books, torrents]
for folder in folders:
    try:
        os.mkdir(folder)
    except FileExistsError:
        pass


def sort():
    for file in os.listdir(downloads):
        if file.endswith('.mp3'):
            shutil.move(downloads + file, music + file)

        if file.endswith('.jpg') or file.endswith('.png'):
            shutil.move(downloads + file, images + file)

        if file.endswith('.djvu') or file.endswith('.epub') or file.endswith('.pdf') or file.endswith('.fb2'):
            shutil.move(downloads + file, books + file)

        if file.endswith('.exe') or file.endswith('.msi'):
            shutil.move(downloads + file, soft + file)

        if file.endswith('.torrent'):
            shutil.move(downloads + file, torrents + file)
    print('Downloads Folder Sorted!')


if __name__ == '__main__':
    sort()
