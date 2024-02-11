import cv2 as cv
import numpy as np

plateCasscade = cv.CascadeClassifier("./data/haarcascadee/haarcascade_russian_plate_number.xml")
count = 0
cap = cv.VideoCapture(1)
cap.set(3,640)
cap.set(4,640)
cap.set(10,150)

while True:
    success,img = cap.read()
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    license = plateCasscade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in license:
        area = w*h
        if area > 500:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv.putText(img,"Number plate",(x,y-5),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            imgROI = img[y:y+h,x:x+w]
            cv.imshow("ROI",imgROI)
    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite("./data/Scanned/No_plate"+str(count)+".jpg",imgROI)
        cv.rectangle(img,(0,200),(640,300),(0,255,0),cv.FILLED)
        cv.putText(img,"Image Saved",(150,265),cv.FONT_HERSHEY_COMPLEX,2,(0,200,55),2)
        cv.imshow("Result",img)
        cv.waitKey(500)
        count+=1
