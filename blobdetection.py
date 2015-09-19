import cv2
import numpy as np
import math
# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
while True:
    # Create a detector with the parameters
    params = getTriangleFilter()
    detector = cv2.SimpleBlobDetector(params)

    keypoints = detector.detect(im)
    print (keypoints)
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)

def getTriangleFilter():
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 90#input("min threshold:");
    params.maxThreshold = 200#input("max threshold");

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.4
    params.maxCircularity = .55

    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.0
    params.maxConvexity = 0.95
    #
    #      # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

def getSquareFilter():
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 90#input("min threshold:");
    params.maxThreshold = 200#input("max threshold");

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.6
    params.maxCircularity = 0.8

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.0
    params.maxConvexity = 0.95
    #
    #      # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01


def getCircleFilter():
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 90#input("min threshold:");
    params.maxThreshold = 200#input("max threshold");

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.7
    params.maxCircularity = 1.0

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.0
    params.maxConvexity = 0.95
    #
    #      # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01


