
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:51:25 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import numpy as np
import cv2
d = 400

#黑底
imgb = np.zeros((d,d),dtype="uint8")
imgg = np.zeros((d,d),dtype="uint8")
imgr = np.zeros((d,d),dtype="uint8")

cv2.circle(imgb,(200,150),100,255,-1)#畫布,圓心座標,半徑,顏色,-1 = 填滿
cv2.circle(imgg,(125,250),100,255,-1)
cv2.circle(imgr,(275,250),100,255,-1)
imgk = np.stack((imgb, imgg, imgr), axis = 2)
imgk[np.all((imgk==[0,0,0]),axis =2)] = 255 #把背景變白色

#放文字
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imgk,'B',(190,130),font, 1,(0,0,0),2) #圖,文字內容,繪製位置,字型,字體大小,顏色,粗度
cv2.putText(imgk,'G',(110,275),font, 1,(0,0,0),2)
cv2.putText(imgk,'R',(265,275),font, 1,(0,0,0),2)
cv2.putText(imgk,'C',(145,210),font, 1,(0,0,0),2) #圖,文字內容,繪製位置,字型,字體大小,顏色,粗度
cv2.putText(imgk,'M',(240,210),font, 1,(0,0,0),2)
cv2.putText(imgk,'Y',(190,280),font, 1,(0,0,0),2)
cv2.putText(imgk,'W',(190,235),font, 1,(0,0,0),2)

#白底
imgy = np.ones((d,d),dtype="uint8") *255
imgm = np.ones((d,d),dtype="uint8") *255
imgc = np.ones((d,d),dtype="uint8") *255

cv2.circle(imgy,(200,150),100,0,-1)
cv2.circle(imgm,(125,250),100,0,-1)
cv2.circle(imgc,(275,250),100,0,-1)
imgw = np.stack((imgy, imgm, imgc),axis =2)

#放文字
cv2.putText(imgw,'Y',(190,130),font, 1,(0,0,0),2) #圖,文字內容,繪製位置,字型,字體大小,顏色,粗度
cv2.putText(imgw,'M',(110,275),font, 1,(0,0,0),2)
cv2.putText(imgw,'C',(265,275),font, 1,(0,0,0),2)
cv2.putText(imgw,'R',(145,210),font, 1,(0,0,0),2) #圖,文字內容,繪製位置,字型,字體大小,顏色,粗度
cv2.putText(imgw,'G',(240,210),font, 1,(0,0,0),2)
cv2.putText(imgw,'B',(190,280),font, 1,(0,0,0),2)
cv2.putText(imgw,'K',(190,235),font, 1,(255,255,255),2)


#合併兩張圖
img = np.concatenate((imgk,imgw), axis = 1)

#Show圖
#cv2.imshow("color",imgw)
#cv2.imshow("color2",imgk)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
