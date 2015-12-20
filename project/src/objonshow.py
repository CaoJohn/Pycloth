# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 20:40:42 2015

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 04 15:44:23 2015


@author: John
"""
import cv2
import os
import numpy as np

class ObjonShow(object):
    
    imgres = np.zeros((100,80,3),np.int8, order='C')
    
    def __init__(self, res, site, width, ratio, num):
        self.res = res
        self.site = site
        self.width = width
        self.ratio = ratio
        self.num = num

        
    def getObj(self):
        width = int(self.site.w*self.width*self.ratio)
        (filepath,filename) = os.path.split(self.res)
        listfile = os.listdir(filepath)
        #for ls in listfile:
                #print ls
        self.imgres = cv2.imread(filepath+"\\"+listfile[self.num],cv2.IMREAD_COLOR)
        
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
    
        col = [0]
        row = [0]
        for c in range(0,mask.shape[0]):
            if(255 in mask[c,:]):
                col.append(c)
            else:
                pass
        for r in range(0,mask.shape[1]):
            if(255 in mask[:,r]):
                row.append(r)
            else:
                pass
    
        retimg = self.imgres[col[1]:col[-1],row[1]:row[-1]]
        retimg = cv2.resize(retimg,(width,int(width*retimg.shape[0]/retimg.shape[1])),interpolation=cv2.INTER_CUBIC)
        self.imgres = retimg        
        return retimg
    
    def insertBack(self, bimg):
        rows,cols,channels = self.imgres.shape
        site = self.site
        if(site.y+site.h+rows>bimg.shape[0] or site.x+site.w/2+cols/2>bimg.shape[1] or site.x+site.w/2-cols/2<=0):
            print("photo doesn't match!")
            print ("x:"+str(site.x)+"  y:"+str(site.y)+"   w:"+str(site.w)+"   h:"+str(site.h))
            return bimg
        if(cols%2==0):
            roi = bimg[site.y+site.h:site.y+site.h+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)]
        else:
            roi = bimg[site.y+site.h:site.y+site.h+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1]
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
    
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(self.imgres,self.imgres,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        #cv2.imshow('img1_bg',img1_bg)
        #cv2.imshow('img2_fg',img2_fg)

        if(cols%2==0):
            bimg[site.y+site.h:site.y+site.h+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)] = dst
        else:
            bimg[site.y+site.h:site.y+site.h+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1] = dst
        return bimg
        
    

class Square(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
class Hat(ObjonShow):
    def insertBack(self, bimg):
        rows,cols,channels = self.imgres.shape
        site = self.site
        if(site.y+site.h+rows>bimg.shape[0] or site.x+site.w/2+cols/2>bimg.shape[1] or site.x+site.w/2-cols/2<=0):
            print("photo doesn't match!")
            print ("x:"+str(site.x)+"  y:"+str(site.y)+"   w:"+str(site.w)+"   h:"+str(site.h))
            return bimg
        if(cols%2==0):
            roi = bimg[site.y-site.h/2:site.y-site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)]
        else:
            roi = bimg[site.y-site.h/2:site.y-site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1]
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
    
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(self.imgres,self.imgres,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        #cv2.imshow('img1_bg',img1_bg)
        #cv2.imshow('img2_fg',img2_fg)

        if(cols%2==0):
            bimg[site.y-site.h/2:site.y-site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)] = dst
        else:
            bimg[site.y-site.h/2:site.y-site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1] = dst
        return bimg


class Glass(ObjonShow):

    def insertBack(self, bimg):
        rows,cols,channels = self.imgres.shape
        site = self.site
        if(site.y+site.h+rows>bimg.shape[0] or site.x+site.w/2+cols/2>bimg.shape[1] or site.x+site.w/2-cols/2<=0):
            print("photo doesn't match!")
            print ("x:"+str(site.x)+"  y:"+str(site.y)+"   w:"+str(site.w)+"   h:"+str(site.h))
            return bimg
        if(cols%2==0):
            roi = bimg[site.y+site.h/4:site.y+site.h/4+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)]
        else:
            roi = bimg[site.y+site.h/4:site.y+site.h/4+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1]
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
    
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(self.imgres,self.imgres,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        #cv2.imshow('img1_bg',img1_bg)
        #cv2.imshow('img2_fg',img2_fg)

        if(cols%2==0):
            bimg[site.y+site.h/4:site.y+site.h/4+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)] = dst
        else:
            bimg[site.y+site.h/4:site.y+site.h/4+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1] = dst
        return bimg

class Eardrop(ObjonShow):

    def insertBack(self, bimg):
        rows,cols,channels = self.imgres.shape
        site = self.site
        if(site.y+site.h+rows>bimg.shape[0] or site.x+site.w/2+cols/2>bimg.shape[1] or site.x+site.w/2-cols/2<=0):
            print("photo doesn't match!")
            print ("x:"+str(site.x)+"  y:"+str(site.y)+"   w:"+str(site.w)+"   h:"+str(site.h))
            return bimg
        if(cols%2==0):
            roi = bimg[site.y+3*site.h/5:site.y+3*site.h/5+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)]
        else:
            roi = bimg[site.y+3*site.h/5:site.y+3*site.h/5+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1]
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
    
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(self.imgres,self.imgres,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        #cv2.imshow('img1_bg',img1_bg)
        #cv2.imshow('img2_fg',img2_fg)

        if(cols%2==0):
            bimg[site.y+3*site.h/5:site.y+3*site.h/5+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)] = dst
        else:
            bimg[site.y+3*site.h/5:site.y+3*site.h/5+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1] = dst
        return bimg
    
class Tie(ObjonShow):
    def insertBack(self, bimg):
        rows,cols,channels = self.imgres.shape
        site = self.site
        if(site.y+site.h+rows>bimg.shape[0] or site.x+site.w/2+cols/2>bimg.shape[1] or site.x+site.w/2-cols/2<=0):
            print("photo doesn't match!")
            print ("x:"+str(site.x)+"  y:"+str(site.y)+"   w:"+str(site.w)+"   h:"+str(site.h))
            return bimg
        if(cols%2==0):
            roi = bimg[site.y+3*site.h/2:site.y+3*site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)]
        else:
            roi = bimg[site.y+3*site.h/2:site.y+3*site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1]
        img1gray = cv2.cvtColor(self.imgres,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
    
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv2.bitwise_and(self.imgres,self.imgres,mask = mask)
        dst = cv2.add(img1_bg,img2_fg)
        #cv2.imshow('img1_bg',img1_bg)
        #cv2.imshow('img2_fg',img2_fg)

        if(cols%2==0):
            bimg[site.y+3*site.h/2:site.y+3*site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)] = dst
        else:
            bimg[site.y+3*site.h/2:site.y+3*site.h/2+rows, (site.x+site.w/2-cols/2):(site.x+site.w/2+cols/2)+1] = dst
        return bimg
        
    