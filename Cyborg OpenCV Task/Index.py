import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
path = r"C:\Users\prati\OneDrive\Documents\VS Code Projects\Cyborg OpenCV Task\Task_2.jpeg"

img = cv2.imread(path)

down_width = 700
down_height = 700
down_points = (down_width, down_height)
resized_down = cv2.resize(img, down_points, interpolation = cv2.INTER_LINEAR)

index = ()
for i in range(0,14):
    for j in range(0,14):
        index = index + ((i,j),)

prt = tuple(map(str ,index ))
ctr = 0

for row in range(680,10,-50):
        for column in range(7,700,50):
                cv2.putText(resized_down, prt[ctr], (column ,row ),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1)  
                ctr = ctr + 1                             

cv2.imshow("Result Image",resized_down)
cv2.waitKey(0)
cv2.destroyAllWindows
