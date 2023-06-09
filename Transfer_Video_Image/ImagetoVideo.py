import cv2
import os
import random

img = cv2.imread('./data/result_img/0.jpg')

video = cv2.VideoCapture('./data/Video/test.mp4') 
fps = video.get(cv2.CAP_PROP_FPS)
video.release()
print('Video FPS: ', fps) # get fps from video

size = (img.shape[1], img.shape[0]) 
print(size)

format = cv2.VideoWriter_fourcc(*"MP4V") # create a blank video
videoWrite = cv2.VideoWriter('./data/result_video/new.mp4', format, fps, size)

files = os.listdir('./data/result_img/') # total number of img
for i in range(0, len(files)):
    imgPath = './data/result_img/' + str(i) + '.jpg'
    img = cv2.imread(imgPath)
    videoWrite.write(img) # write the img to the video

videoWrite.release()
