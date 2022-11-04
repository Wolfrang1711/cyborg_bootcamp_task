import cv2
from cv2 import FONT_HERSHEY_SIMPLEX
path = r"C:\Users\prati\OneDrive\Documents\VS Code Projects\Cyborg OpenCV Task\StockPhoto.jpg"
img = cv2.imread(path)

#Boxes
cv2.rectangle(img, (100,250),(200,350),(255,178,102),-1)
cv2.rectangle(img, (200,250),(300,350),(0,128,255),-1)
cv2.rectangle(img, (300,250),(400,350),(51,51,255),-1)
cv2.rectangle(img, (400,250),(500,350),(51,255,153),-1)
cv2.rectangle(img, (300,150),(400,250),(255,51,255),-1)
cv2.rectangle(img, (300,350),(400,450),(0,255,255),-1)

#2
cv2.circle(img,(130,320),8,(255,255,255),-1)
cv2.circle(img,(170,280),8,(255,255,255),-1)
#6
cv2.circle(img,(225,280),8,(255,255,255),-1)
cv2.circle(img,(250,280),8,(255,255,255),-1)
cv2.circle(img,(275,280),8,(255,255,255),-1)
cv2.circle(img,(225,320),8,(255,255,255),-1)
cv2.circle(img,(250,320),8,(255,255,255),-1)
cv2.circle(img,(275,320),8,(255,255,255),-1)
#5
cv2.circle(img,(325,280),8,(255,255,255),-1)
cv2.circle(img,(375,280),8,(255,255,255),-1)
cv2.circle(img,(350,300),8,(255,255,255),-1)
cv2.circle(img,(325,320),8,(255,255,255),-1)
cv2.circle(img,(375,320),8,(255,255,255),-1)
#1
cv2.circle(img,(450,300),8,(255,255,255),-1)
#4
cv2.circle(img,(325,180),8,(255,255,255),-1)
cv2.circle(img,(375,180),8,(255,255,255),-1)
cv2.circle(img,(325,220),8,(255,255,255),-1)
cv2.circle(img,(375,220),8,(255,255,255),-1)
#3
cv2.circle(img,(330,420),8,(255,255,255),-1)
cv2.circle(img,(350,400),8,(255,255,255),-1)
cv2.circle(img,(370,380),8,(255,255,255),-1)

#Text
cv2.putText(img,"Pratik Kumar Sahoo",(350,525),FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),1)
cv2.putText(img,"Roll No: 121ID0437",(350,550),FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),1)
cv2.putText(img,"Library Ver: ",(350,575),FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),1)
cv2.putText(img,cv2. __version__,(500,575),FONT_HERSHEY_SIMPLEX,0.75,(255,255,255),1)

cv2.imshow("Result Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows
