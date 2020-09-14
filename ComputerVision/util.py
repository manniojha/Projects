import cv2 as cv
import numpy as np 


def genricGetContours(img,cThr=[100,100],showCanny=False,minArea=1000,filterr=0,draw=False):
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv.Canny(imgBlur,cThr[0],cThr[1])
    kernal = np.ones((5,5))
    imgDialte = cv.dilate(imgCanny,kernal,iterations=3)
    imgErode = cv.erode(imgDialte,kernal,iterations=2)
    if showCanny : cv.imshow("Canny",imgErode)

    contours,hierarchy = cv.findContours(imgErode,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    finalContours = []
    for cont in contours:
        area = cv.contourArea(cont)
        if area > minArea:
            peri = cv.arcLength(cont,True)
            approx = cv.approxPolyDP(cont,0.02*peri,True)
            bbox = cv.boundingRect(approx)
            if filterr > 0:
                if len(approx) == filterr:
                    finalContours.append([len(approx),area,approx,bbox,cont])
            else:
                finalContours.append([len(approx),area,approx,bbox,cont])

    finalContours = sorted(finalContours,key=lambda x:x[1] , reverse=True)
    if draw:
        for cont in finalContours:
            cv.drawContours(img,cont[4],-1,(255,0,255),3)

    return img,finalContours

def reorder(myPoints):
    myPointsNew = np.zeros_like(myPoints)
    myPoints = myPoints.reshape((4,2))
    add = myPoints.sum(1)
    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]
    return myPointsNew

def wrapImage(img,points,w,h,padding):
    points = reorder(points)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgWarp = cv.warpPerspective(img,matrix,(w,h))
    imgWarp = imgWarp[padding:imgWarp.shape[0]-padding,padding:imgWarp.shape[1]-padding]
    return imgWarp

def findDistance(pt1,pt2):
    return ((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)**0.5