import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

cap = cv.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)

while True:
    success,img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,(255,0,255),5)
        pts2 = barcode.rect
        cv.putText(img,myData,(pts2[0],pts2[1]),cv.FONT_HERSHEY_COMPLEX,0.9,(100,120,35),2)
    cv.imshow("Result",img)
    cv.waitKey(1)