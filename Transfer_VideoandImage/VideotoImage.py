import cv2

interval = 1 
cnt = 0 # save to cnt.jpg
idx = 0 # video index

video = cv2.VideoCapture('video.mp4') 


if video.isOpened():
    tf = True
else:
    tf = False
    print('Fail to open the video')

while(tf):
    _, frame = video.read()
    if frame is None:
        break
    print(idx)
    if idx % interval == 0:
        cv2.imwrite('./data/B_target/%d.jpg' %cnt, frame)
        cnt += 1
    idx += 1
    if idx == 3000:
        break
