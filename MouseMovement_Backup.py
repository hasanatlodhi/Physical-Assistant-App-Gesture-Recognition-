import cv2
import numpy as np
import time
import TrackHand as ht
import pyautogui
import subprocess
import os
import win32api
import win32gui
import win32con
from datetime import datetime

class Gesture_System:
    def __init__(self):
        x_ray_path = os.path.abspath('X_ray')
        last_opened_time=datetime.now()
        last_opened_time = last_opened_time.strftime("%H:%M:%S")

        pTime = 0           
        width = 640             
        height = 480           
        frameR = 100            
        smoothening = 8        
        prev_x, prev_y = 0, 0  
        curr_x, curr_y = 0, 0   
        cap = cv2.VideoCapture(0)  
        cap.set(3, width)          
        cap.set(4, height)

        detector = ht.handDetector(maxHands=1)                 
        screen_width, screen_height = pyautogui.size()   

        pyautogui.FAILSAFE=False
        window_title = "Window Title"
        while True:
            success, img = cap.read()
            img = detector.findHands(img)                       
            lmlist, bbox = detector.findPosition(img)   
            time_now=datetime.now()
            time_now=time_now.strftime("%H:%M:%S")
            time_diff=datetime.strptime(time_now,"%H:%M:%S")-datetime.strptime(last_opened_time,"%H:%M:%S")       

            if len(lmlist)!=0:
                x1, y1 = lmlist[8][1:]
                x2, y2 = lmlist[12][1:]

                fingers = detector.fingersUp()
                cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)   
                if fingers[1] == 1 and fingers[2] == 0:     
                    x3 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
                    y3 = np.interp(y1, (frameR, height-frameR), (0, screen_height))

                    curr_x = prev_x + (x3 - prev_x)/smoothening
                    curr_y = prev_y + (y3 - prev_y) / smoothening

                    pyautogui.moveTo(screen_width - curr_x, curr_y,_pause=False)   
                    cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
                    prev_x, prev_y = curr_x, curr_y

                if fingers[1] == 1 and fingers[2] == 1:    
                    length, img, lineInfo = detector.findDistance(8, 12, img)

                    if length < 40 and time_diff.seconds % 60 >1:   
                        last_opened_time=time_now  
                        cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                        pyautogui.click()

                if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and time_diff.seconds % 60 >1 :
                    last_opened_time=time_now
                    subprocess.Popen(f'explorer "{x_ray_path}"')
                
                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1 and time_diff.seconds % 60 >1 :
                    last_opened_time=time_now
                    handle = win32gui.GetForegroundWindow()
                    window_title = win32gui.GetWindowText(handle)

                    # Minimize the window
                    win32api.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)

                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 1 and fingers[4] == 1 and time_diff.seconds % 60 >1 :
                    last_opened_time=time_now
                    handle = win32gui.FindWindow(None, window_title)
                    if win32gui.IsIconic(handle):
                        win32gui.ShowWindow(handle, win32con.SW_RESTORE)
                if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0 and time_diff.seconds % 60 >1 :
                    last_opened_time=time_now
                    pyautogui.click(clicks=2)
                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and time_diff.seconds % 60 >1:
                    last_opened_time=time_now
                    pyautogui.press('backspace')
                
            cTime = time.time()
            fps = 1/(cTime-pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
            cv2.imshow("Gesture Detection System", img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                cv2.destroyAllWindows()
                break

