import os
import pathlib

def rename(path, prefix):
    i = 0
    for filename in os.listdir(path):
        fileExtension = pathlib.Path(filename).suffix
        newName = prefix + str(i) + fileExtension
        oldPath = path + filename
        newPath = path + newName
        os.rename(oldPath, newPath)
        i = i + 1
    print("\nYour Files have been renamed!")

print("Mass File Renamer By Don Chacko. To get started just enter the neccessary information below.")
print("\nWARNING: DO NOT DO THIS OPERATION WITH SAME PREFIX MORE THAN ONCE ON THE SAME FILES! FILES MAY BE DELETED!")
fileDirectory = input("\nEnter the directory of the files to rename: ")
filePrefix = input("Enter the renaming prefix: ")
rename(fileDirectory, filePrefix)
