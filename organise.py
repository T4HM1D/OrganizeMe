import os
from pathlib import Path
# dictionary with key value pairs
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDictionary(ext): # takes in a extension type
    for category, fileTypes in SUBDIRECTORIES.items(): # loops through each file types in each category in the key-value pair
        for fileType in fileTypes: # iterates through the filetypes list
            if fileType == ext: # checks if extension exist in the file type list
                return category # returns category if extension exist in filetypes list
    return "MISC" # if filetype doesn't exist in dictionary

def organiseDirectory():
    for item in os.scandir(): # os.scandir iterator object all the items in the current working directory
        if item.is_dir() or item.name == Path(__file__).name: # if item is directory or the script itself, skip it
            continue
        filePath = Path(item) # Returns relative path of the item.
        fileType = filePath.suffix.lower() # Returns the string value of the suffix of the items
        dictionary = pickDictionary(fileType) # calls pickDiectory function, returns the category of the filetype
        dictionaryPath = Path(dictionary) # creates a path for the category.
        if dictionaryPath.is_dir() == False: 
            dictionaryPath.mkdir() # If category directory doesn't exist, make it.
        filePath.rename(dictionaryPath.joinpath(filePath)) # moves file into the category directory

organiseDirectory()