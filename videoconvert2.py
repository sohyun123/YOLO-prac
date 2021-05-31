import cv2
import os

sec = 0
curFrame = 0
frameRate = 1

def writeFrame(sec):
    global curFrame

    video.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    ret, image = video.read()
    if ret:
        cv2.imwrite("images/capture/JOY-" + str(curFrame) + ".jpg", image)
        curFrame += 1
    else:
        print('No frame')
    # print(ret)
    return ret



video = cv2.VideoCapture("images/joy.mp4")
isFrame = writeFrame(sec)
while isFrame:
    sec += frameRate
    sec = round(sec,2)
    isFrame = writeFrame(sec)