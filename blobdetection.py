import cv2
import numpy as np;

# Read image
im = cv2.imread("blob.jpg", cv2.IMREAD_GRAYSCALE)
while True:
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    # Change thresholds
    params.minThreshold = 10#input("min threshold:");
    params.maxThreshold = 20#input("max threshold");

    # Filter by Area.
    params.filterByArea = False

    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = input("minCircularity")

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = input("convexity")
    #
    #      # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector(params)

    keypoints = detector.detect(im)
    print (keypoints)
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Keypoints", im_with_keypoints)
    cv2.waitKey(0)
