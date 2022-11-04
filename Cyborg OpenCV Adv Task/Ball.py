import cv2
from cv2 import erode
import numpy as np
import time

path = r"C:\Users\prati\Documents\VS Code Projects\Cyborg OpenCV Adv Task\red ball green background.mp4"

cap = cv2.VideoCapture(path)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter(r"C:\Users\prati\Documents\VS Code Projects\Cyborg OpenCV Adv Task\Output.avi", fourcc, 30, size)

temp = 0
down = 0
cord = [0,0,0,0,0 ]

while(cap.isOpened()):
    
    low_green = np.array([25,52,72])
    high_green = np.array([102,255,255])
    kernel = np.ones((5,5),np.uint8)

    ret, frame = cap.read()

    if ret == True:
        #cv2.imshow('Original', frame) 
        
        blur = cv2.GaussianBlur(frame, (9, 9), 0)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
            
        mask = cv2.inRange(hsv, low_green , high_green) 
        maskremake = cv2.erode(mask, kernel, iterations = 2)

        res = cv2.bitwise_and(frame, frame, mask = mask)    
        bg_removed = frame - res 
        #cv2.imshow('BG Removed', bg_removed) 

        erosion = cv2.erode(bg_removed, kernel, iterations = 40)
        ret, black = cv2.threshold(erosion, 100, 255, cv2.THRESH_BINARY)
        
        edges = cv2.Canny(mask, threshold1 = 0, threshold2 = 200)
        
        contours, hierarchy = cv2.findContours(maskremake, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in contours:

            area = cv2.contourArea(contour)

            if area > 4000 and area < 50000:

                #cv2.drawContours(frame, contour, -1, (255, 0, 255), thickness = 2)
                M = cv2.moments(contour)
                if M['m00'] != 0:
                    
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])

                    time1 = time.time()

                    
                    cord[0] = cx, cy
                    cord[1] = cx
                    temp = cx
                    print(cord[1],cord[2])

                    speed = int(abs((cord[1]-cord[2])/(time1-time2)))
                    
                    cordinate = tuple(map(str ,cord ))

                    #if (cy>110):
                        #cv2.arrowedLine(black, (cx, cy), (cx , cy + 30), (255, 255, 255), 3, 8, 0, 0.3)    
                        #down = 1            
                    #if (cy<590 and down != 1):
                        #cv2.arrowedLine(black, (cx, cy), (cx , cy - 30), (255, 255, 255), 3, 8, 0, 0.3)
                    #if (cy-cx>0):
                        #cv2.arrowedLine(black, (cx, cy), (cx +30 , cy), (255, 255, 255), 3, 8, 0, 0.3)    
                    #if (cx-cy<0):
                        #cv2.arrowedLine(black, (cx, cy), (cx-30 , cy), (255, 255, 255), 3, 8, 0, 0.3)
                    #down = 0

                    cv2.circle(black, (cx, cy), 7, (255, 255, 255), -1)
                    
                    cv2.putText(black, cordinate[0], (cx - 45, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    cv2.putText(black, str(speed), (cx - 25, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    
        cord[2] = temp
        time2 = time.time()
        cv2.imshow('Output', black)
        result.write(black)
        
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
result.release()
cv2.destroyAllWindows()
