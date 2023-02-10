# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 23:25:51 2023

@author: Burak
"""

import numpy as np
import cv2

imageFrame=cv2.imread('12.jpg')
		
hsv = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
	
		# kırmızı renk için aralık belirleme
red_lower = np.array([40, 0, 100], np.uint8)
red_upper = np.array([179, 255, 255], np.uint8)
red_mask = cv2.inRange(hsv, red_lower, red_upper)
		
		# Morfolojik işlem
kernal = np.ones((5, 5), "uint8")
		# Kırmızı renk için
red_mask = cv2.dilate(red_mask, kernal)
image_red = cv2.bitwise_and(imageFrame, imageFrame,
								mask = red_mask)
#kırmızı renk tespit edilmişse, daire mi? 

if (image_red !=[] ):    
    gray = cv2.cvtColor(image_red,cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray,5)

    #çember tespit etme 
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,
    param1=300,param2=60,minRadius=0,maxRadius=0)
    if (circles is not None): # kırmızı bölge daire ise
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(image_red,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(image_red,(i[0],i[1]),2,(0,0,255),3)
            print('daire')
    else: #kırmızı bölge daire değilse
       print('daire değil') 

cv2.imshow("frame", imageFrame )
cv2.imshow('tespit',image_red)
cv2.waitKey(0)
cv2.destroyAllWindows()	
