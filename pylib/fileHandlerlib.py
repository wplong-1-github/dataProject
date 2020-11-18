from os import listdir
from os.path import isfile, join

def fileNameHandler(fileDir):
    onlyfiles = [f for f in listdir(fileDir) if isfile(join(fileDir, f))]
    newFileList = [fileDir + f for f in onlyfiles]
    print(newFileList)
    return newFileList
