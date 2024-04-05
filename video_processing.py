#packages needed are opencv (pip install opencv-python) and matplotlib
from os import read
import pandas as pd
import numpy as np
import cv2 
import matplotlib.pyplot as plt

from glob import glob
import subprocess

#convert mov files to mp4
input_file= '' #here we will enter the path for the videos from cctv that we want to process
subprocess.run(['ffmpeg','-i', input_file, '-qscale', '0', '', '-log', 'quiet']) #3rd to last simple quote is for the file name and it should be filename.mp4

#read metadata from the video
cap = cv2.VideoCapture('') #here you input the name of the video file
frames = cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT) #total number of frames
fps = cap.get(cv2.cv2.CAP_PROP_FPS)
print(frames, fps)
cap.release() #make sure to release the file after using it so it does not show as being in use

fig, axs = plt.subplot(5, 5, figsize=(30, 20))
axs = axs.flatten()
cap = cv2.VideoCapture('') #filename to analyze
n_frames = int(cap.get(cv2.cv2.CAP_FRAME_COUNT))
img_index = 0
for frame in range(n_frames):
    ret, img = cap.read()
    if ret == False: 
        break()
    if frame % 100 == 0:
        axs[img_index].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[img_index].set_title(f'Frame: {frame}')
        axs[img_index].axis('off')
        img_index += 1
plt.plt.tight_layout()
plt.show()
cap.release()
#add anotations to the videoimages
labels = pd.read_csv('',low_memory=False)
labels.head()




