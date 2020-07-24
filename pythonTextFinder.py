import os
import shutil
import re

def askInput():
    print("This script will search for text you type in all txt files from the current directory and all its subdirectories. If any .txt files containing your text are found, you can copy them in a folder of your choice if you'd like to.\n")
    text = input('What text are you searching for? ')
    path = input('In what folder (from where the script is located, enter nothing for same folder)? ')
    print()
    path = f'{os.getcwd()}\\{path}'
    return text, path
    
def findAllTxtFilesInDirectoryAndSubdirectories(path):
    txtFiles = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.txt' in file:
                txtFiles.append(os.path.join(r, file))

    return txtFiles

def isTextInFile(text, file):
    return re.search(rf'{text}', file, re.IGNORECASE)

def findTextInFiles(text, files):
    filesWithTextFound = []
    for file in files:
        with open(file) as fileContent:
            try:
                if (isTextInFile(text, fileContent.read())):
                    filesWithTextFound.append(fileContent.name)
            except Exception:
                pass
    return filesWithTextFound

def moveFiles(newFolderPath, files):
    destination = f'{os.getcwd()}\\{newFolderPath}\\'
    try:
        os.mkdir(destination)
    except Exception:
        pass
    for file in files:
        try:
            shutil.copy(file, destination)
        except Exception:
            pass

# Script
text, path = askInput()
txtFiles = findAllTxtFilesInDirectoryAndSubdirectories(path)
filesWithTextFound = findTextInFiles(text, txtFiles)
if (not filesWithTextFound):
    print(f'No files found containing: {text}\n')
else:
    print(f'The files contain: {text}')
    for file in filesWithTextFound:
        print(file)
    copyFiles = input('\nDo you wish to copy the files (y/n)? ')
    if (copyFiles.lower() == 'y' or copyFiles.lower() == 'yes'):
        newFolderPath = input('\nIn what folder would you like to copy the files (can be an existing or a new one)? ')
        moveFiles(newFolderPath, filesWithTextFound)

print('\nDone!\n')
input('Press any key to quit...')