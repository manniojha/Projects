import cv2 as cv
import numpy as np
import util 

webCam = False
path = './data/objectMeasurement1.jpeg'
cap = cv.VideoCapture(0)
cap.set(3,1920)
cap.set(4,1080)
cap.set(10,150)
scale = 3
wP,hP = 297*scale,210*scale

while True:
    if webCam : success,img = cap.read()
    else : img = cv.imread(path)
    img = cv.resize(img,(0,0),None,0.5,0.5)
    img,finalContours = util.genricGetContours(img,minArea=50000,filterr=4)
    if len(finalContours) != 0:
        biggest = finalContours[0][2]
        imgWarp = util.wrapImage(img,biggest,wP,hP,40)
        img2,Contours2 = util.genricGetContours(imgWarp,minArea=1000,filterr=4,cThr=[50,50])
        if len(Contours2) != 0:
            for obj in Contours2:
                #cv.polylines(img2,[obj[2]],True,(0,255,255),2)
                nPoints = util.reorder(obj[2])
                newWidth = round((util.findDistance(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
                newHeight = round((util.findDistance(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
                cv.arrowedLine(img2,(nPoints[0][0][0],nPoints[0][0][1]),(nPoints[1][0][0],nPoints[1][0][1]),(255,0,255),3,8,0,0.05)
                cv.arrowedLine(img2,(nPoints[0][0][0],nPoints[0][0][1]),(nPoints[2][0][0],nPoints[2][0][1]),(255,0,255),3,8,0,0.05)
                x,y,w,h = obj[3]
                cv.putText(img2,'{}cm'.format(newWidth),(x+30,y-10),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
                cv.putText(img2,'{}cm'.format(newHeight),(x-70,y+h // 2),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)
        cv.imshow('Image Wrap',img2)
 

    cv.imshow('Original',img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break