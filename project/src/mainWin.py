# -*- coding: utf-8 -*-
"""
Created on Sat Dec 05 13:54:12 2015

@author: Administrator
"""


import xlwt
import xlrd
import datetime
import sys, string, os
from PyQt4 import QtCore, QtGui
import matplotlib.pyplot as plt
from bodyDress import bodyDressWindow
from faceDress import faceDressWindow

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 90, 741, 381))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        
        self.textEdit = QtGui.QTextBrowser(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 2)
        
        self.pushButton_score = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_score.setObjectName(_fromUtf8("pushButton_score"))
        self.gridLayout.addWidget(self.pushButton_score, 1, 1, 1, 1)
        self.lineEdit_score = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_score.setObjectName(_fromUtf8("lineEdit_score"))
        self.gridLayout.addWidget(self.lineEdit_score, 1, 0, 1, 1)
        
        
        self.pushButton_search = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_search.setObjectName(_fromUtf8("pushButton_search"))
        self.gridLayout.addWidget(self.pushButton_search, 0, 1, 1, 1)
        self.lineEdit_search = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.gridLayout.addWidget(self.lineEdit_search, 0, 0, 1, 1)
        
        
        self.label_info = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_info.setObjectName(_fromUtf8("label_info"))
        self.gridLayout.addWidget(self.label_info, 2, 0, 1, 1)
        
        self.horizontalLayout.addLayout(self.gridLayout)
        
        self.tableView = QtGui.QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayout.addWidget(self.tableView)
        
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.pushButton_play = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_play.setObjectName(_fromUtf8("pushButton_play"))
        self.verticalLayout.addWidget(self.pushButton_play)
        self.pushButton_face = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_face.setObjectName(_fromUtf8("pushButton_face"))
        self.verticalLayout.addWidget(self.pushButton_face)
        self.pushButton_dress = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_dress.setObjectName(_fromUtf8("pushButton_dress"))
        self.verticalLayout.addWidget(self.pushButton_dress)
        self.pushButton_walk = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_walk.setObjectName(_fromUtf8("pushButton_walk"))
        self.verticalLayout.addWidget(self.pushButton_walk)
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.pushButton_open = QtGui.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(40, 490, 75, 23))
        self.pushButton_open.setObjectName(_fromUtf8("pushButton_open"))
        self.pushButton_save = QtGui.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(140, 490, 75, 23))
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        
        self.pushButton_prev = QtGui.QPushButton(self.centralwidget)
        self.pushButton_prev.setGeometry(QtCore.QRect(40, 520, 75, 23))
        self.pushButton_prev.setObjectName(_fromUtf8("pushButton_prev"))
        self.pushButton_next = QtGui.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(140, 520, 75, 23))
        self.pushButton_next.setObjectName(_fromUtf8("pushButton_next"))
        
        self.pushButton_singleScore = QtGui.QPushButton(self.centralwidget)
        self.pushButton_singleScore.setGeometry(QtCore.QRect(240, 490, 75, 23))
        self.pushButton_singleScore.setObjectName(_fromUtf8("pushButton_singleScore"))
        self.pushButton_totalScore = QtGui.QPushButton(self.centralwidget)
        self.pushButton_totalScore.setGeometry(QtCore.QRect(340, 490, 75, 23))
        self.pushButton_totalScore.setObjectName(_fromUtf8("pushButton_totalScore"))
        
        self.label_modifyScore = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_modifyScore.setGeometry(QtCore.QRect(440, 490, 46, 13))
        self.label_modifyScore.setObjectName(_fromUtf8("label_modifyScore"))

        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(450, 480, 231, 81))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_plus_1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus_1.setObjectName(_fromUtf8("pushButton_plus_1"))
        self.gridLayout_2.addWidget(self.pushButton_plus_1, 0, 0, 1, 1)
        self.pushButton_minus_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus_5.setObjectName(_fromUtf8("pushButton_minus_5"))
        self.gridLayout_2.addWidget(self.pushButton_minus_5, 1, 2, 1, 1)
        self.pushButton_plus_5 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus_5.setObjectName(_fromUtf8("pushButton_plus_5"))
        self.gridLayout_2.addWidget(self.pushButton_plus_5, 0, 2, 1, 1)
        self.pushButton_minus_1 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus_1.setObjectName(_fromUtf8("pushButton_minus_1"))
        self.gridLayout_2.addWidget(self.pushButton_minus_1, 1, 0, 1, 1)
        self.pushButton_plus_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_plus_3.setObjectName(_fromUtf8("pushButton_plus_3"))
        self.gridLayout_2.addWidget(self.pushButton_plus_3, 0, 1, 1, 1)
        self.pushButton_minus_3 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_minus_3.setObjectName(_fromUtf8("pushButton_minus_3"))
        self.gridLayout_2.addWidget(self.pushButton_minus_3, 1, 1, 1, 1)
       
        
        
        self.label_title = QtGui.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(50, 40, 100, 20))
        self.label_title.setObjectName(_fromUtf8("label_title"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.model = QtGui.QStandardItemModel(parent=self)
        self.model.setHorizontalHeaderLabels((u'学号', u'姓名', u'分数'))
        self.tableView.setModel(self.model)
        self.StuList = []
        self.StuScoreList = []
        self.retranslateUi(MainWindow)
        self.connectEvents()
        self.excelInit()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def excelInit(self):   
        self.currentStu = [1001,"liming",101,"math","science",12,"male",10]
        self.StuItem = [u'学号', u'姓名',u'班级',u'专业',u'学院',u'年龄',u'性别',u'分数']
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet(u'sheet1', cell_overwrite_ok=True)
        self.nrows = 0


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", u'仪容仪表实训课程', None))
        self.pushButton_score.setText(_translate("MainWindow", "打分", None))
        self.pushButton_search.setText(_translate("MainWindow", "搜索学号", None))
        self.label_info.setText(_translate("MainWindow", "学生信息：", None))
        self.pushButton_play.setText(_translate("MainWindow", "播放范例", None))
        self.pushButton_face.setText(_translate("MainWindow", "面容", None))
        self.pushButton_dress.setText(_translate("MainWindow", "身装", None))
        self.pushButton_walk.setText(_translate("MainWindow", "步姿", None))
        self.pushButton_open.setText(_translate("MainWindow", "打开文件", None))
        self.pushButton_save.setText(_translate("MainWindow", "保存文件", None))
        self.pushButton_prev.setText(_translate("MainWindow", "上一个", None))
        self.pushButton_next.setText(_translate("MainWindow", "下一个", None))
        
        self.pushButton_singleScore.setText(_translate("MainWindow", "成绩历史", None))
        self.pushButton_totalScore.setText(_translate("MainWindow", "班级成绩", None))
        self.label_modifyScore.setText(_translate("MainWindow", "调整分数", None))
         
        self.pushButton_plus_5.setText(_translate("MainWindow", "+5分", None))
        self.pushButton_minus_5.setText(_translate("MainWindow", "-5分", None))
        self.pushButton_plus_3.setText(_translate("MainWindow", "+3分", None))
        self.pushButton_minus_3.setText(_translate("MainWindow", "-3分", None))
        self.pushButton_plus_1.setText(_translate("MainWindow", "+1分", None))
        self.pushButton_minus_1.setText(_translate("MainWindow", "-1分", None))
        
        self.label_title.setText(_translate("MainWindow", u'上海行政管理学院', None))

    def connectEvents(self):
        self.connect( self.pushButton_open, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonOpen )
        self.connect( self.pushButton_save, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSave )
        self.connect( self.pushButton_prev, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPrev )
        self.connect( self.pushButton_next, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonNext )
        
        self.connect( self.pushButton_search, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSearch )
        self.connect( self.pushButton_score, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSetScore )
        self.connect( self.pushButton_play, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPlay )
        self.connect( self.pushButton_singleScore, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonSingleScore )
        self.connect( self.pushButton_totalScore, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonTotalScore )
        
        self.connect( self.pushButton_plus_5, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPlusFive )
        self.connect( self.pushButton_minus_5, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonMinusFive )
        self.connect( self.pushButton_plus_3, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPlusThree )
        self.connect( self.pushButton_minus_3, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonMinusThree )
        self.connect( self.pushButton_plus_1, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonPlusOne )
        self.connect( self.pushButton_minus_1, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonMinusOne )
        
        self.connect( self.pushButton_face, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonFace )
        self.connect( self.pushButton_dress, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonDress )
        self.connect( self.pushButton_walk, QtCore.SIGNAL( 'clicked()' ), self.ExecButtonWalk )

                
    def ExecButtonPlusFive( self ):
        score = int(self.lineEdit_score.text())
        score = score+5
        self.lineEdit_score.setText(str(score))
        
        
    def ExecButtonMinusFive( self ):
        score = int(self.lineEdit_score.text())
        score = score-5
        self.lineEdit_score.setText(str(score))
        
    def ExecButtonPlusThree( self ):
        score = int(self.lineEdit_score.text())
        score = score+3
        self.lineEdit_score.setText(str(score))
        
    def ExecButtonMinusThree( self ):
        score = int(self.lineEdit_score.text())
        score = score-3
        self.lineEdit_score.setText(str(score))
        
    def ExecButtonPlusOne( self ):
        score = int(self.lineEdit_score.text())
        score = score+1
        self.lineEdit_score.setText(str(score))
        
    def ExecButtonMinusOne( self ):
        score = int(self.lineEdit_score.text())
        score = score-1
        self.lineEdit_score.setText(str(score))
        
    def ExecButtonDress( self ):
        bdDress = bodyDressWindow()
        bdDress.exec_()
        bdDress.destroy()
    
    def ExecButtonFace( self ):
        fcDress = faceDressWindow()
        fcDress.exec_()
        fcDress.destroy()
    
    def ExecButtonWalk( self ):
        import ctypes 
        testlib = ctypes.CDLL("skeletonDll.dll")
        #testlib.mainDLL.restype = ctypes.c_char_p
        a=testlib.mainDll()
        print a
            
        

    def ExecButtonOpen( self ):
        print("button pressed!")
        filename = QtGui.QFileDialog.getOpenFileName(
                   None, 'Open File', '', 'excel (*.xls *.xlsx)')
        self.ws = xlrd.open_workbook(filename)
        self.sheet = self.ws.sheet_by_index(0)
        self.sheet2 = self.ws.sheet_by_index(1)

        self.model.clear()        
        self.StuList = []
        for l in range(1,self.sheet.nrows):
            self.StuList.append(self.sheet.row_values(l)) 
            self.model.appendRow((
                QtGui.QStandardItem(str(int(self.sheet.row_values(l)[0]))),
                QtGui.QStandardItem(self.sheet.row_values(l)[1]),
                #QtGui.QStandardItem(str(int(self.sheet.row_values(l)[2]))),
                QtGui.QStandardItem(str(self.sheet.row_values(l)[-1])),
            ))
        for l2 in range(1,self.sheet2.nrows):
            self.StuScoreList.append(self.sheet2.row_values(l2)) 
        print(self.StuList)
            
    def ExecButtonSave( self ):
        for item in self.StuItem:
            self.worksheet.write(0,self.StuItem.index(item),item)
        rows = 0
        for l in self.StuList:
            rows = rows+1
            for i in l:
                self.worksheet.write(rows,l.index(i),i)
        print(self.StuList)
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title', 'C:\\John\\Mywork\\clothes\\pycloth\\src', selectedFilter='*.xls')
        if fileName:
                print fileName
        self.workbook.save(fileName)
        
    def ExecButtonPrev( self ):
        self.currentStu = self.StuList[self.StuList.index(self.currentStu)-1]
        self.textEdit.setText(u"学号:"+str(int(self.currentStu[0]))+u"\n姓名:"+self.currentStu[1]+ \
            u"\n班级:"+str(int(self.currentStu[2]))+u"\n学院:"+self.currentStu[4]+u"\n年龄:"+str(int(self.currentStu[5])))
        self.lineEdit_search.setText(str(int(self.currentStu[0])))
        
    def ExecButtonNext( self ):
        self.currentStu = self.StuList[self.StuList.index(self.currentStu)+1]
        self.textEdit.setText(u"学号:"+str(int(self.currentStu[0]))+u"\n姓名:"+self.currentStu[1]+ \
            u"\n班级:"+str(int(self.currentStu[2]))+u"\n学院:"+self.currentStu[4]+u"\n年龄:"+str(int(self.currentStu[5])))
        self.lineEdit_search.setText(str(int(self.currentStu[0])))
                    
    def ExecButtonSearch( self ):
        searchNum = int(self.lineEdit_search.text())
        searchSuccess = False
        for l in self.StuList:
            if (l[0] == searchNum):
                self.currentStu = l
                self.textEdit.setText(u"学号:"+str(int(self.currentStu[0]))+u"\n姓名:"+self.currentStu[1]+ \
                u"\n班级:"+str(int(self.currentStu[2]))+u"\n学院:"+self.currentStu[4]+u"\n年龄:"+str(int(self.currentStu[5])))
                searchSuccess = True       
        if searchSuccess == False:
            self.textEdit.setText("no match Student information")

    def ExecButtonSetScore( self ):
        searchNum = int(self.lineEdit_search.text())
        score = int(self.lineEdit_score.text())
        searchSuccess = False
        for l in self.StuList:
            if (l[0] == searchNum):
                s_Index = self.StuList.index(l)
                self.StuList[s_Index][-1] = score
                self.model.setItem(s_Index,2,QtGui.QStandardItem(str(score)))
                searchSuccess = True
        print(self.StuList)
        if searchSuccess == False:
            self.textEdit.setText("no match Student information")

    
    def ExecButtonPlay( self ):
        os.chdir( 'D:\\Program Files (x86)\\KMPlayer' )
        filename = str(QtGui.QFileDialog.getOpenFileName(
                   None, 'Open File', '', 'video(*.avi)'))
        filestr = str(filename)
        print filestr
        filestr = filestr.replace("/","\\\\")
        print filestr
        exe='"D:\\Program Files (x86)\\KMPlayer\\KMPlayer.exe"'
        os.system(exe+' '+filestr)
    
    def ExecButtonSingleScore( self ):
        print(self.StuScoreList) 
        for l in self.StuScoreList:
            if l[0]==self.currentStu[0]:
                scorel = l
        plt.xlabel(u'次数', fontproperties='SimHei')
        plt.ylabel(u'成绩', fontproperties='SimHei')
        plt.title(scorel[1]+u'成绩历史', fontproperties='SimHei')
        plt.axis([0, len(scorel)-2, 0, 100])
        plt.plot(scorel[2:],'r')
        print() 
        plt.show()
        
    def ExecButtonTotalScore( self ):
        scoreList = []
        for i in self.StuList:
            scoreList.append(i[-1])
        plt.xlabel(u'序号', fontproperties='SimHei')
        plt.ylabel(u'成绩', fontproperties='SimHei')
        plt.title(u'班级成绩', fontproperties='SimHei')
        plt.axis([0, len(self.StuList), 0, 100])
        plt.plot(scoreList,'r')
        plt.show() 


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



