import cv2
import os


rootDir = 'AgeDataset/train'


def isgray(imgpath):
    img = cv2.imread(imgpath)
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    return False
    
    
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        fullname_src = dirName + "/" + fname
        if fname.endswith(".jpg") or fname.endswith(".png"):
            if isgray(fullname_src):
                os.remove(fullname_src)
                print(fullname_src)