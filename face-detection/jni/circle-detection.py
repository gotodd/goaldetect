#!/usr/bin/env python3.9
import cv2
import numpy as np
import sys
import os



#raw_image = cv2.imread('/Users/tzhang/Downloads/rawImage.jpg')
raw_image = cv2.imread('/Users/tzhang/Downloads/frc-ball.jpg')
bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)


hsv = cv2.cvtColor(bilateral_filtered_image, cv2.COLOR_BGR2HSV)
# Threshold of yellow in HSV space
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-yellow regions
result = cv2.bitwise_and(bilateral_filtered_image, bilateral_filtered_image, mask = mask)

cv2.imshow('bilateral_filtered_image', bilateral_filtered_image)
cv2.imshow('mask', mask)
cv2.imshow('result', result)

#while True:
#    key = cv2.waitKey(0)
#    if key in [27, ord('q'), ord('Q')]:
#        cv2.destroyAllWindows()
#        sys.exit()

edge_detected_image = cv2.Canny(result, 75, 200)
contours, h = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)

cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
cv2.imshow('Objects Detected',raw_image)
cv2.setWindowProperty('Objects Detected', cv2.WND_PROP_TOPMOST, 1)
os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
while True:
    key = cv2.waitKey(0)
    if key in [27, ord('q'), ord('Q')]:
        cv2.destroyAllWindows()
        sys.exit()


