import os
from pathlib import Path
# dictionary with key value pairs
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.docx','.pptx'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png','.gif']
}

def pickDictionary(ext): # takes in a extension type
    for category, fileTypes in SUBDIRECTORIES.items(): # loops through each file types in each category in the key-value pair
        for fileType in fileTypes: # iterates through the filetypes list
            if fileType == ext: # checks if extension exist in the file type list
                return category # returns category if extension exist in filetypes list
    return "MISC" # if filetype doesn't exist in dictionary

def organiseDirectory():
    print('Script is running in {} folder'.format(Path(__file__).absolute().parent.name)) # Check which folder script is running from.
    if not Path(__file__).absolute().parent.name == 'Downloads':
        cwd = Path(__file__).absolute().parents[1] # Sets cwd to 1 folder above the folder the script is in.
        print('Sub-directories will be made above sub-folder in:', cwd)
    else:
        cwd = Path(__file__).absolute().parent # Sets cwd to current folder the script is in.
        print('Sub-directories will be made in download folder:', cwd)
    for item in cwd.iterdir(): # os.scandir iterator object all the items in the current working directory / can also use pathlib.Path.itdir()
        if item.is_dir() or item.name == Path(__file__).name or item.name == ".gitignore" or item.name == "README.md": # if item is directory or the script itself, skip it
            continue
        filePath = Path(item) # Returns relative path of the item.
        fileType = filePath.suffix.lower() # Returns the string value of the suffix of the items
        dictionary = pickDictionary(fileType) # calls pickDiectory function, returns the category of the filetype
        dictionaryPath = cwd.joinpath(dictionary) # creates a path for the category.
        if not dictionaryPath.is_dir(): 
            dictionaryPath.mkdir() # If category directory doesn't exist, make it.
        newPath = dictionaryPath.joinpath(filePath.name)
        filePath.rename(newPath) # moves file into the category directory
        print('Old Directory: ', Path(item))
        print('New Directory', newPath)
organiseDirectory()