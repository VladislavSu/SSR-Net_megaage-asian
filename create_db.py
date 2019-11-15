import numpy as np
import cv2
# import scipy.io
import argparse
import os
# from tqdm import tqdm
# from os import listdir
# from os.path import isfile, join
# import sys
# import dlib
# from moviepy.editor import *


def get_args():
    parser = argparse.ArgumentParser(description="This script "
                                                 "creates database for training.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--output", "-o", type=str,
                        help="path to output database mat file")
    parser.add_argument("--img_size", type=int, default=64,
                        help="output image size")
    
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    #output_path = './data/age_dataset_train.npz'
    output_path = './data/age_dataset_test.npz'

    img_size = args.img_size
    
    out_ages = []
    out_imgs = []
    
    #rootDir = 'AgeDataset/train'
    rootDir = 'AgeDataset/test'
    
    for dirName, subdirList, fileList in os.walk(rootDir):
        #if subdirList: print(subdirList)
        age = dirName.split('/')[-1]
        for fname in fileList:
            if fname.endswith(".jpg") or fname.endswith(".JPG"):
                fullname = dirName+"/"+fname
                input_img = cv2.imread(fullname)
                input_img = cv2.resize(input_img,(img_size,img_size))
                im_rgb = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
                out_imgs.append(im_rgb)
                out_ages.append(int(age))
                #print(fname, age)
    
    
    np.savez(output_path,image=np.array(out_imgs), age=np.array(out_ages), img_size=img_size)

if __name__ == '__main__':
    main()
