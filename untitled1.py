# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:14:01 2020

@author: Rushi
"""
import cv2
import datetime
import numpy as np
#read,write,show
'''
img=cv2.imread('Blender_Suzanne1.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27: #esc key
    cv2.destroyAllWindows()
elif k==ord('s'):
    print('fcdcf')
    cv2.destroyAllWindows()
'''
#cv2.imwrite('gvaewf.jpg',img)


#video from camera
'''
cap=cv2.VideoCapture(0);

while(True):
    ret,fm=cap.read()
    
    #gray frame
    gray=cv2.cvtColor(fm,cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',gray)
    
    if cv2.waitKey(0) ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
'''


'''
#Geometric shapes on image
#img=np.zeros([512,512,3],np.uint8)
img=cv2.imread('Blender_Suzanne1.jpg',1)
#line
img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
#img=cv2.arrowedLine(img,(0,100),(300,100),(0,0,255),8)

#rectangle

img=cv2.rectangle(img,(360,0),(510,128),(0,300,0),5)
#filledRectangle
img=cv2.rectangle(img,(0,330),(430,255),(0,200,0),-1)
#circle
img=cv2.circle(img,(444,63),70,(0,0,200),-1)
#text
font=cv2.FONT_HERSHEY_COMPLEX
img=cv2.putText(img,'fdfffaewfgtde',(10,500),font,4,(255,255,255),11,cv2.LINE_AA)



cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''



'''
#print on video
cap=cv2.VideoCapture(0);
print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret,fm=cap.read()
    if ret==True:
        
        font=cv2.FONT_HERSHEY_COMPLEX
        dt=str(datetime.datetime.now())
        text='Ht X Wt: '+str(cap.get(3))+' X '+str(cap.get(4))
        fm=cv2.putText(fm,dt,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('video',fm)
        
        if cv2.waitKey(0)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
'''  
    
#mouse events in opencv
#event=[i for i in dir(cv2) if 'EVENT' in i]
#print(event)
def mouse_click(event,x,y,flag,pr):
    if event==cv2.EVENT_LBUTTONDOWN:
        #font=cv2.FONT_HERSHEY_COMPLEX
        #text=str(x)+' , '+str(y)
        
        #cv2.putText(img,text,(x,y),font,0.5,(255,255,0),1,cv2.LINE_AA)
        cv2.circle(img,(x,y),2,(0,0,0),-1)
        pt.append((x,y))
        if len(pt)>=2:
            cv2.line(img,pt[-1],pt[-2],(255,255,0),2)
        cv2.imshow('image',img)
    if event==cv2.EVENT_RBUTTONDOWN:
        b=img[y,x,0]
        g=img[y,x,1]
        r=img[y,x,2]
        #font=cv2.FONT_HERSHEY_COMPLEX
        #BGR=str(b)+' , '+str(g)+' , '+str(r)
        #cv2.putText(img,BGR,(x,y),font,0.5,(255,255,0),1,cv2.LINE_AA)
        cimg=np.zeros([255,255,3],np.uint8)
        cimg[:]=[b,g,r]
        cv2.imshow('color',cimg)
#img=np.zeros([255,255,3],np.uint8)
pt=[]
img=cv2.imread('20190307_153251.jpg',1)
img=cv2.resize(img,(480,480),interpolation=cv2.INTER_AREA)
cv2.imshow('image',img)



cv2.setMouseCallback('image',mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()

    
    
    




