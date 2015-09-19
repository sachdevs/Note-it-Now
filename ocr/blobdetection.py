import cv2
import numpy as np
import math
# Read image
def getFilter(minThreshold = 90, maxThreshold = 200, minCircularity = 0, maxCircularity = 1, minConvexity = 0, maxConvexity = 0.95, minInertiaRatio = 0.5):
    params = cv2.SimpleBlobDetector_Params()

    params.filterByArea = False
    params.minArea = 100

    # Change thresholds
    params.minThreshold = minThreshold
    params.maxThreshold = maxThreshold

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = minCircularity
    params.maxCircularity = maxCircularity

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = minConvexity
    params.maxConvexity = maxConvexity

    params.filterByInertia = False
    params.minInertiaRatio = minInertiaRatio
    return params

def getTriangleFilter():
    return getFilter(90, 200, 0.4, 0.7, .91, 1)

def getPointyFilter():
    return getFilter(90, 200, 0, 0.4, 0, 0.65, 0.3)

def getCircleFilter():
    return getFilter(90, 200, 0.7, 1.0, 0.9, 1)

def detectWithFilter(imagePath,filter):
    im = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)
    detector = cv2.SimpleBlobDetector(filter)
    keypoints = detector.detect(im)
    print (keypoints)
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    return keypoints
    # cv2.imshow("Keypoints", im_with_keypoints)
    # cv2.waitKey(0)

class PointTypes:
    POINTY, TRIANGLE, CIRCLE = range(3)

class Landmark:
    def __init__(self, KeyPoint, type):
        self.point = KeyPoint
        self.type = type

def getLandmarks(imagePath):
    landmarks = []
    for x in detectWithFilter(imagePath, getPointyFilter()):
        landmarks.append(Landmark(x, PointTypes.POINTY))
    for x in detectWithFilter(imagePath, getTriangleFilter()):
        landmarks.append(Landmark(x, PointTypes.TRIANGLE))
    for x in detectWithFilter(imagePath, getCircleFilter()):
        landmarks.append(Landmark(x, PointTypes.CIRCLE))
    return landmarks

# l = getLandmarks("blob.jpg")
