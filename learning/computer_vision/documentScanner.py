import cv2 as cv
import numpy as np
#########################################
frameWidth = 480
frameHeight = 640
#########################################
capture = cv.VideoCapture(0)
capture.set(3,frameWidth)
capture.set(4,frameHeight)
capture.set(10,150)

def stackImages(scale,imgArray):
    rows,cols= len(imgArray),len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width,height = imgArray[0][0].shape[1],imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv.cvtColor( imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def preprocessing(img):
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),1)
    imgCanny = cv.Canny(imgBlur,200,200)
    kernal = np.ones((5,5))
    imgDialation = cv.dilate(imgCanny,kernal,iterations=2)
    imgErode = cv.erode(imgDialation,kernal,iterations=1)
    return imgErode

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    biggest = np.array([])
    maxArea = 0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 5000:
            # cv.drawContours(imgContours,cnt,-1,(255,0,0),3)
            perimeter = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*perimeter,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
    cv.drawContours(imgContours,biggest,-1,(255,0,0),20)
    return biggest

def reorder(mypoints):
    mypoints = mypoints.reshape((4,2))
    mypointsNew = np.zeros((4,1,2),np.int32)
    add = mypoints.sum(1)

    mypointsNew[0] = mypoints[np.argmin(add)]
    mypointsNew[3] = mypoints[np.argmax(add)]
    diff = np.diff(mypoints,axis=1)
    mypointsNew[1] = mypoints[np.argmin(diff)]
    mypointsNew[2] = mypoints[np.argmax(diff)]
    return mypointsNew
        
def getWarp(img,biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[frameWidth,0],[0,frameHeight],[frameWidth,frameHeight]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv.warpPerspective(img,matrix,(frameWidth,frameHeight))
    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv.resize(imgCropped,(frameWidth,frameHeight))
    return imgCropped

while True:
    success,img = capture.read()
    img = cv.resize(img,(frameWidth,frameHeight))
    imgContours = img.copy()
    imgThresold = preprocessing(img)
    biggest = getContours(imgThresold)
    if biggest.size != 0:
        imgWarpped = getWarp(img,biggest)
        imgArray = stackImages(0.6,([img,imgThresold],[imgContours,imgWarpped]))
    else:
        imgArray = stackImages(0.6,([img,imgThresold],[img,img]))
    cv.imshow("Result",imgArray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
