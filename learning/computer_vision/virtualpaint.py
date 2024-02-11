import cv2 as cv
import numpy as np
######################################################
frameWidth = 640
frameHeight = 480
######################################################
capture = cv.VideoCapture(1)
capture.set(3,frameWidth)
capture.set(4,frameHeight)
capture.set(10,150)

colors = [[0,118,226,179,255,255],
         [92,159,156,179,245,255],
         [0,36,178,88,255,255]]
mycolorValues = [[51,153,255],[255,0,255],[0,255,0]]

myPoints = []
def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            # cv.drawContours(imgResult,cnt,-1,(255,0,0),3)
            perimeter = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*perimeter,True)
            x,y,w,h = cv.boundingRect(approx)
    return x+w//2,y

def findColor(img,colors,mycolorValues):
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in colors:
        lower = np.array([color[0:3]])
        high = np.array([color[3:6]])
        mask = cv.inRange(imgHSV,lower,high)
        x,y = getContours(mask)
        cv.circle(imgResult,(x,y),10,mycolorValues[count],cv.FILLED)
        if x != 0 and y!=0:
            new_points.append([x,y,count])
        count+=1
    return new_points
        # cv.imshow(str(color[1]),mask)


def drawOnCanvas(myPoints,mycolorValues):
    for point in myPoints:
        cv.circle(imgResult,(point[0],point[1]),10,mycolorValues[point[2]],cv.FILLED)

while True:
    success,img = capture.read()
    imgResult = img.copy()
    new_points = findColor(img,colors,mycolorValues)
    if len(new_points)!=0:
        for newP in new_points:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,mycolorValues)
    cv.imshow("Result",imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break