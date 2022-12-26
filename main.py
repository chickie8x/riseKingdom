import subprocess
import time
import numpy as np
import cv2


def getScreenCap():
    subprocess.run('./ADB/adb.exe shell screencap -p /sdcard/screenshot.png')
    time.sleep(3)
    subprocess.run('./ADB/adb.exe pull /sdcard/screenshot.png ./ScreenShot')
    time.sleep(3)


def findPosClick(partern, template, threshold):
    pass

getScreenCap()
time.sleep(3)
sc = cv2.imread('ScreenShot/screenshot.png')
pat = cv2.imread('Resources/food.png')
cv2.imshow('image',pat)
cv2.waitKey(0)
result = cv2.matchTemplate(pat, sc, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.99)
data = list(zip(*loc[::-1]))
print(data)

