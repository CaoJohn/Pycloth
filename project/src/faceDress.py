
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 02 10:27:46 2015

@author: John
"""


import sys
import os
from PyQt4 import QtGui, QtCore, uic
import numpy as np
import cv2
from objonshow import ObjonShow, Square, Glass, Eardrop
import datetime
#import numpy as np

class faceDressWindow( QtGui.QDialog ):
    def __init__( self ):
        super( faceDressWindow, self ).__init__()
        
        self.frame=np.zeros((640,480,3),np.int8, order='C')
        self.video_size = QtCore.QSize(640,480)
        self.setup_ui()

        self.video_switch = False
        self.counter = 0

        
    def setup_ui(self):
        
        self.glass = Glass("G:\\StaticDressing\\clothes\\resources\\glass\\g1.png",Square(350,80,50,50),1,1,1)
        self.earDrop = Eardrop("G:\\StaticDressing\\clothes\\resources\\ear\\e1.png",Square(350,80,50,50),1,1,1)        
        
        self.setWindowTitle( u"面容实训" )
        self.resize(1000, 640)
        
        self.image_label = QtGui.QLabel(self)
        self.image_label.setGeometry(QtCore.QRect(290, 80, 240, 180))
        self.image_label.setFixedSize(self.video_size)
        
        #gridlayout = QtGui.QGridLayout()
        self.pushButton_sizePlus = QtGui.QPushButton(u"加大尺寸",self)
        self.pushButton_sizePlus.setGeometry(QtCore.QRect(40, 320, 75, 23))

        self.pushButton_sizeMinus = QtGui.QPushButton(u"缩小尺寸",self)
        self.pushButton_sizeMinus.setGeometry(QtCore.QRect(40, 360, 75, 23))
        
        self.pushButton_up = QtGui.QPushButton(u"上",self)
        self.pushButton_up.setGeometry(QtCore.QRect(170, 310, 41, 21))

        self.pushButton_right = QtGui.QPushButton(u"右",self)
        self.pushButton_right.setGeometry(QtCore.QRect(200, 340, 41, 21))

        self.pushButton_left = QtGui.QPushButton(u"左",self)
        self.pushButton_left.setGeometry(QtCore.QRect(140, 340, 41, 21))

        self.pushButton_down = QtGui.QPushButton(u"下",self)
        self.pushButton_down.setGeometry(QtCore.QRect(170, 370, 41, 21))

        self.pushButton_prev = QtGui.QPushButton(u"上一个",self)
        self.pushButton_prev.setGeometry(QtCore.QRect(50, 430, 75, 23))

        self.pushButton_next = QtGui.QPushButton(u"下一个",self)
        self.pushButton_next.setGeometry(QtCore.QRect(130, 430, 75, 23))

        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(290, 40, 69, 22))
        self.comboBox.addItems(u'耳饰 眼镜'.split())
        #self.comboBox.activated[str].connect(self.onActivatedComBox) 
        
        self.checkBox_track = QtGui.QCheckBox(u"跟踪",self)
        self.checkBox_track.setGeometry(QtCore.QRect(380, 40, 71, 16))
        
        self.checkBox_gestrue = QtGui.QCheckBox(u"手势",self)
        self.checkBox_gestrue.setGeometry(QtCore.QRect(460, 40, 71, 16))

        self.checkBox_earDrop = QtGui.QCheckBox(u"耳饰",self)
        self.checkBox_earDrop.setGeometry(QtCore.QRect(290, 560, 71, 16))

        self.checkBox_glass = QtGui.QCheckBox(u"眼镜",self)
        self.checkBox_glass.setGeometry(QtCore.QRect(340, 560, 71, 16))
        
        self.label_record = QtGui.QLabel(u"录像:off",self)
        self.label_record.setGeometry(QtCore.QRect(40, 140, 50, 20))

        self.pushButton_openCam = QtGui.QPushButton(u"摄像头",self)
        self.pushButton_openCam.setGeometry(QtCore.QRect(40, 200, 75, 23))       
      
        self.pushButton_closeCam = QtGui.QPushButton(u"关闭摄像头",self)
        self.pushButton_closeCam.setGeometry(QtCore.QRect(130, 200, 75, 23))
        
        self.pushButton_photo = QtGui.QPushButton(u"拍照",self)
        self.pushButton_photo.setGeometry(QtCore.QRect(85, 250, 75, 23))
        
        self.pushButton_startRec = QtGui.QPushButton(u"开始记录",self)
        self.pushButton_startRec.setGeometry(QtCore.QRect(40, 170, 75, 23))
        
        self.pushButton_stopRec = QtGui.QPushButton(u"停止记录",self)
        self.pushButton_stopRec.setGeometry(QtCore.QRect(130, 170, 75, 23))

                 
        self.connect( self.pushButton_prev, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPrev )
        self.connect( self.pushButton_next, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonNext )
        
        self.connect( self.pushButton_right, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonRight )
        self.connect( self.pushButton_left, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonLeft )
        self.connect( self.pushButton_up, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonUp )
        self.connect( self.pushButton_down, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonDown )
        
        self.connect( self.pushButton_sizePlus, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSizePlus )
        self.connect( self.pushButton_sizeMinus, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSizeMinus )

        self.connect( self.pushButton_photo, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPhoto )
        self.connect( self.pushButton_openCam, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonOpenCam )
        self.connect( self.pushButton_closeCam, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonCloseCam )
        
        self.connect( self.pushButton_startRec, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonStartRecord )
        self.connect( self.pushButton_stopRec, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonStopRecord )

        self.checkBox_earDrop.stateChanged.connect(self.ExecCheckBoxShowearDrop)
        

    def setup_camera(self):
        """Initialize camera.
        """
        #self.capture = cv2.VideoCapture("G:\\StaticDressing\\demo.avi")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(50)


    def display_video_stream(self):
        """Read frame from camera and repaint QLabel widget.
        """
        _, self.frame = self.capture.read()
        frame = self.frame
        self.counter = self.counter+1
        
        if self.checkBox_gestrue.isChecked():
            if self.counter%50 == 0:
                import ctypes 
                testlib = ctypes.CDLL("OpenNIdll.dll")
                #testlib.mainDLL.restype = ctypes.c_char_p
                a=testlib.addDll(1,2)
                print a
                a=testlib.mainDll()
                print a
                if a==0:
                    self.ExecButtonNext()
        
        if self.checkBox_track.isChecked():
            if self.counter%10 == 0:
                tmpSite = self.faceDetect(frame,32)
                if self.comboBox.currentIndex()==0:                    
                    self.earDrop.site = tmpSite
                if self.comboBox.currentIndex()==1:
                    self.glass.site = tmpSite
                print self.counter
                #self.counter = 0
            
        if self.checkBox_earDrop.isChecked():
            img = self.earDrop.getObj()
            #cv2.imshow('img',img)
            frame = self.earDrop.insertBack(self.frame)
        if self.checkBox_glass.isChecked():
            self.glass.getObj()
            frame = self.glass.insertBack(self.frame)
        
        if self.video_switch:
            self.out.write(frame)

        frame = cv2.cvtColor(self.frame, cv2.cv.CV_BGR2RGB)
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], 
                       frame.strides[0], QtGui.QImage.Format_RGB888)
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(image))

    
    def ExecButtonOpenCam( self ):
        self.setup_camera()
        
    def ExecButtonCloseCam( self ):
        self.ExecButtonStopRecord()
        self.capture.release()
        self.timer.stop()
        
    def ExecButtonPhoto( self ):
        now = datetime.datetime.now()
        cv2.imwrite('photo'+str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+str(now.second)+'.jpg', self.frame)

    def ExecCheckBoxShowearDrop( self ):
        print  self.checkBox_earDrop.isChecked()
        
    def ExecButtonStopRecord( self ):
        self.label_record.setText(u"录像:off")
        self.video_switch = False
        #self.capture.release()
        self.out.release()

    def ExecButtonStartRecord( self ):
        self.label_record.setText(u"录像:on")
        self.video_switch = True
        fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
        now = datetime.datetime.now()
        self.out = cv2.VideoWriter(str(now.year)+str(now.month)+str(now.day)+str(now.hour)+str(now.minute)+'.avi',fourcc, 20.0, (640,480))  
        
        
    def ExecButtonPrev( self ):        
        sqrsite = self.faceDetect(self.frame,8)
        print ("x:"+str(sqrsite.x)+"  y:"+str(sqrsite.y)+"   w:"+str(sqrsite.w)+"   h:"+str(sqrsite.h))
        
        if self.comboBox.currentIndex()==0:
            self.earDrop.site = sqrsite
            self.earDrop.num = self.earDrop.num-1
            
        if self.comboBox.currentIndex()==1:
            self.glass.site = sqrsite
            self.glass.site.y = sqrsite.y+sqrsite.h/2
            self.glass.num = self.glass.num-1


        
    def ExecButtonNext( self ):
        sqrsite = self.faceDetect(self.frame,32)
        print ("x:"+str(sqrsite.x)+"  y:"+str(sqrsite.y)+"   w:"+str(sqrsite.w)+"   h:"+str(sqrsite.h))
        if self.comboBox.currentIndex()==0:
            self.earDrop.site = sqrsite
            self.earDrop.num = self.earDrop.num+1
            
        if self.comboBox.currentIndex()==1:
            self.glass.site = sqrsite
            self.glass.site.x = sqrsite.x
            self.glass.site.y = sqrsite.y+sqrsite.h/2
            self.glass.num = self.glass.num+1
        

        
    def ExecButtonRight( self ):
        if self.comboBox.currentIndex()==0:
            print("earDrop Radio is checked!/n")
            self.earDrop.site.x = self.earDrop.site.x+2
        if self.comboBox.currentIndex()==1:
            print("glass Radio is checked!/n")
            self.glass.site.x = self.glass.site.x+2


          
    def ExecButtonLeft( self ):
        if self.comboBox.currentIndex()==0:
            self.earDrop.site.x = self.earDrop.site.x-2
        if self.comboBox.currentIndex()==1:
            self.glass.site.x = self.glass.site.x-2


    def ExecButtonUp( self ):
        if self.comboBox.currentIndex()==0:
            self.earDrop.site.y = self.earDrop.site.y-2
        if self.comboBox.currentIndex()==1:
            self.glass.site.y = self.glass.site.y-2 
        
    def ExecButtonDown( self ):
        if self.comboBox.currentIndex()==0:
            self.earDrop.site.y = self.earDrop.site.y+2
        if self.comboBox.currentIndex()==1:
            self.glass.site.y = self.glass.site.y+2 
        
    def ExecButtonSizePlus( self ):
        if self.comboBox.currentIndex()==0:
            self.earDrop.ratio = self.earDrop.ratio + 0.1
        if self.comboBox.currentIndex()==1:
            self.glass.ratio = self.glass.ratio + 0.1
        
    def ExecButtonSizeMinus( self ):
        if self.comboBox.currentIndex()==0:
            self.earDrop.ratio = self.earDrop.ratio - 0.1
        if self.comboBox.currentIndex()==1:
            self.glass.ratio = self.glass.ratio - 0.1


    def faceDetect(self, img, divisor):
        classifier=cv2.CascadeClassifier("G:\\StaticDressing\\clothes\\src\\pycloth\\haarcascade_frontalface_alt2.xml")
        size=img.shape[:2]
        gryimage = np.zeros(size, dtype=np.float16)
        gryimage=cv2.cvtColor(img,cv2.cv.CV_BGR2GRAY)
        cv2.equalizeHist(gryimage,gryimage)
        h1,w1=size
        minSize=(w1/divisor,h1/divisor)
        #x,y,w,h = (350,10,40,40)
        for i in range(1,10):
            faceRects=classifier.detectMultiScale(gryimage,1.2,2,cv2.CASCADE_SCALE_IMAGE,minSize)
            if len(faceRects)>0:
                print("face detect!\n")
                for faceRect in faceRects:
                    x,y,w,h=faceRect
                    print ("x:"+str(x)+"  y:"+str(y)+"   w:"+str(w)+"   h:"+str(h))
#                    cv2.circle(self.frame,(x+w/2,y+h/2),min(w/2,h/2),(255,0,0))
#                    cv2.circle(self.frame,(x+w/4,y+h/4),min(w/8,h/8),(255,0,0))
#                    cv2.circle(self.frame,(x+3*w/4,y+h/4),min(w/8,h/8),(255,0,0))
#                    cv2.rectangle(self.frame,(x+3*w/8,y+3*h/4),(x+5*w/8,y+7*h/8),(255,0,0))
                    return Square(x,y,w,h)
                
                    
        return Square(350,10,40,40)
        #cv2.rectangle(self.frame,(x+3*w/8,y+3*h/4),(x+5*w/8,y+7*h/8),(255,0,0))
#
#def main():
#    app = QtGui.QApplication( sys.argv )
#    demo = faceDressWindow()
#    demo.show()
#    sys.exit(app.exec_())
#    
#if __name__ == '__main__':
#    main()