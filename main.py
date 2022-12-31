from ctypes import windll, Structure, c_long, byref

import time
import cv2
import mss
import numpy as np

import pyautogui

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def click():
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()



title = "Terraria Auto-Fishing"
sct = mss.mss()

print("STARTING after 15 seconds, please adjust your rod!")
time.sleep(15)
print("Started ...")

click()
print("Rod dropped ...")
last_time = time.time()



while True:
    if time.time() - last_time < 2:
        continue

    cur = queryMousePosition()
    mon = {"top": cur['y'] -5, "left": cur['x'] -5, "width": 10, "height": 10}
    img = np.asarray(sct.grab(mon))




    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask0 = cv2.inRange(hsv, lower_red, upper_red)


    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)


    mask = mask0+mask1

    # check
    hasRed = np.sum(mask)
    if hasRed > 0:

        pass
    else:


        # get the stuff
        print("Catch! ...")
        time.sleep(0.3)
        click()

        time.sleep(1) # wait some
        print("New rod dropped ...")
        click()

        last_time = time.time()