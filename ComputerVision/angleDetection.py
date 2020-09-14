import cv2 as cv
import math 

img = cv.imread('./data/angle1.png')
pointList = []

def mousePoints(event,x,y,flag,params):
    if event == cv.EVENT_LBUTTONDOWN:
        size = len(pointList)
        if size != 0 and size %3 != 0:
            cv.line(img,tuple(pointList[round(((size-1)/3)*3)]),(x,y),(255,0,0),2)
        cv.circle(img,(x,y),3,(255,0,0),3,cv.FILLED)
        pointList.append([x,y])

def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getAngle(pointList):
    pt1,pt2,pt3 = pointList[-3:]
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angleR = math.atan((m2-m1)/(1+m1*m2))
    angleD = round(math.degrees(angleR))
    cv.putText(img,str(abs(angleD)),(pt1[0]-40,pt1[1]-20),cv.FONT_HERSHEY_COMPLEX,1.5,(255,0,0),2)

while True:
    if len(pointList)%3==0 and len(pointList) != 0:
        getAngle(pointList)
    cv.imshow("Original",img)
    cv.setMouseCallback('Original',mousePoints)
    if cv.waitKey(1) & 0xFF == ord('r'):
        img = cv.imread('./data/angle1.png')
        pointList = []
    elif cv.waitKey(1) & 0xFF == ord('q'):
        break