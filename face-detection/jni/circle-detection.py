#!/usr/bin/env python3.9
import cv2
import numpy as np
import sys
import os

def show_image_and_exit():
    os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')
    while True:
        key = cv2.waitKey(0)
        if key in [27, ord('q'), ord('Q')]:
            cv2.destroyAllWindows()
            sys.exit()
    sys.exit()

def ball_recog_method1(filtered_image,hsv_img):
    h, s, result = cv2.split(hsv_img)
    result=cv2.medianBlur(result,5)

    circles=cv2.HoughCircles(result, cv2.HOUGH_GRADIENT, 1, 20, param1=130,
            param2=21, minRadius=10, maxRadius=0);
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(filtered_image,(i[0],i[1]),i[2],(0,255,0),1) # draw the outer circle
        cv2.circle(filtered_image,(i[0],i[1]),4,(0,0,255),3) # draw the center of the circle

    cv2.imshow('result', filtered_image)
    #cv2.imshow('result', result)
    show_image_and_exit()

def ball_recog_method2(raw_image,hsv_img):
    edge_detected_image = cv2.Canny(hsv_img, 75, 200)
    contours, h = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
            print(len(approx),area)
            contour_list.append(contour)

    cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
    cv2.imshow('Objects Detected',raw_image)
    show_image_and_exit()



raw_image = cv2.imread('/Users/tzhang/Downloads/frc-ball.jpg')
filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)

hsv = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2HSV)
# Threshold of yellow in HSV space
lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

# preparing the mask to overlay
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# The black region in the mask has the value of 0,
# so when multiplied with original image removes all non-yellow regions
result = cv2.bitwise_and(filtered_image, filtered_image, mask = mask)

#ball_recog_method1(filtered_image,result)
ball_recog_method2(raw_image,result)

# useful links: https://stackoverflow.com/questions/49650772/detecting-silver-and-reflecting-balls-with-opencv
