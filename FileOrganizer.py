import os
import shutil

# taking source folder from user and making of all the files in given folder
path = input("Give the path of folder which you want to organize: ")
files = os.listdir(path)


# getting the type of files
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    # if folder already exists
    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

    # if no folder exists, new folder to be made
    else:
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
