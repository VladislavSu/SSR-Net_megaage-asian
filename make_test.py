import os
import random
import shutil

rootDir = 'AgeDataset/train'
persent = 0.1


for dirName, subdirList, fileList in os.walk(rootDir):
    size = len(fileList)
    random.shuffle(fileList)
    newfileList = fileList[0:int(persent*size + 1)]
    print(dirName, size, len(newfileList))
    for fname in newfileList:
        fullname_src = dirName + "/" + fname
        dirName_test = dirName.replace("train", "test") 
        fullname_dst = dirName_test + "/" + fname
        #print(fullname_src, fullname_dst)
        shutil.move(fullname_src, fullname_dst)