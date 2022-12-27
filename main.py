import os
import subprocess
import time
import numpy as np
import cv2


def getScreenCap():
    print('take ss')
    subprocess.run('./ADB/adb.exe shell screencap -p /sdcard/screenshot.png')
    time.sleep(1)
    subprocess.run('./ADB/adb.exe pull /sdcard/screenshot.png ./ScreenShot')
    time.sleep(3)

def findPosClick(pattern_path, template_path, threshold):
    template = cv2.imread(template_path)
    pattern = cv2.imread(pattern_path)
    result = cv2.matchTemplate(pattern, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    pos = list(zip(*loc[::-1]))
    if(pos.__len__()):
        return pos
    else:
        return False

def click_pos(pos):
    if(pos):
        command = f'ADB/adb.exe shell input tap {pos[0][0]} {pos[0][1]}'
        subprocess.run(command)
    else:
        print('no pos to click')

resources = list(f'Resources/{x}' for x in os.listdir('Resources'))
getScreenCap()
template = 'ScreenShot/screenshot.png'
for item in resources:
    pos = findPosClick(item, template, 0.89)
    click_pos(pos)




