# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from radius import Total_Radius
import numpy as np
from scan import radius_update
from threading import Thread
from multiprocessing import Process
import sys, os
import time
import warnings
warnings.filterwarnings("ignore")



class Ui_MainWindow(object):
    def __init__(self):
        self.scanner = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close = QtWidgets.QPushButton(self.centralwidget)
        self.close.setGeometry(QtCore.QRect(350, 480, 111, 31))
        self.close.setObjectName("close")
        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setGeometry(QtCore.QRect(200, 480, 111, 31))
        self.clean.setStyleSheet("")
        self.clean.setObjectName("clean")
        self.analysis = QtWidgets.QPushButton(self.centralwidget)
        self.analysis.setGeometry(QtCore.QRect(50, 480, 111, 31))
        self.analysis.setObjectName("analysis")
        self.inside = QtWidgets.QLabel(self.centralwidget)
        self.inside.setGeometry(QtCore.QRect(560, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.inside.setFont(font)
        self.inside.setObjectName("inside")
        self.outside = QtWidgets.QLabel(self.centralwidget)
        self.outside.setGeometry(QtCore.QRect(551, 200, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.outside.setFont(font)
        self.outside.setObjectName("outside")
        self.health = QtWidgets.QLabel(self.centralwidget)
        self.health.setGeometry(QtCore.QRect(520, 280, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.health.setFont(font)
        self.health.setObjectName("health")
        self.outside_text = QtWidgets.QLabel(self.centralwidget)
        self.outside_text.setGeometry(QtCore.QRect(653, 205, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.outside_text.setFont(font)
        self.outside_text.setObjectName("outside_text")
        self.result_text = QtWidgets.QLabel(self.centralwidget)
        self.result_text.setGeometry(QtCore.QRect(654, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.result_text.setFont(font)
        self.result_text.setObjectName("result_text")
        self.inside_text = QtWidgets.QLabel(self.centralwidget)
        self.inside_text.setGeometry(QtCore.QRect(653, 153, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.inside_text.setFont(font)
        self.inside_text.setObjectName("inside_text")
        self.bfsfilter = QtWidgets.QRadioButton(self.centralwidget)
        self.bfsfilter.setGeometry(QtCore.QRect(323, 310, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.bfsfilter.setFont(font)
        self.bfsfilter.setObjectName("bfsfilter")
        self.Sobelfilter = QtWidgets.QRadioButton(self.centralwidget)
        self.Sobelfilter.setGeometry(QtCore.QRect(323, 347, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.Sobelfilter.setFont(font)
        self.Sobelfilter.setObjectName("Sobelfilter")
        self.Cannyedge = QtWidgets.QRadioButton(self.centralwidget)
        self.Cannyedge.setGeometry(QtCore.QRect(323, 384, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight SemiConde")
        font.setPointSize(14)
        self.Cannyedge.setFont(font)
        self.Cannyedge.setObjectName("Cannyedge")
        self.diameter = QtWidgets.QLabel(self.centralwidget)
        self.diameter.setGeometry(QtCore.QRect(520, 100, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.diameter.setFont(font)
        self.diameter.setObjectName("diameter")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(560, 340, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(20)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(40, 100, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.length = QtWidgets.QLabel(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(40, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.length.setFont(font)
        self.length.setObjectName("length")
        self.filter = QtWidgets.QLabel(self.centralwidget)
        self.filter.setGeometry(QtCore.QRect(323, 260, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.filter.setFont(font)
        self.filter.setObjectName("filter")
        self.Center = QtWidgets.QCheckBox(self.centralwidget)
        self.Center.setGeometry(QtCore.QRect(80, 310, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.Center.setFont(font)
        self.Center.setObjectName("Center")
        self.Report = QtWidgets.QCheckBox(self.centralwidget)
        self.Report.setGeometry(QtCore.QRect(80, 352, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.Report.setFont(font)
        self.Report.setObjectName("Report")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 390, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.function = QtWidgets.QLabel(self.centralwidget)
        self.function.setGeometry(QtCore.QRect(80, 260, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.function.setFont(font)
        self.function.setObjectName("function")
        self.path_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_lineEdit.setGeometry(QtCore.QRect(130, 110, 221, 31))
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.length_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.length_lineEdit.setGeometry(QtCore.QRect(130, 165, 221, 31))
        self.length_lineEdit.setObjectName("length_lineEdit")
        self.inside_2 = QtWidgets.QLabel(self.centralwidget)
        self.inside_2.setGeometry(QtCore.QRect(371, 103, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inside_2.setFont(font)
        self.inside_2.setObjectName("inside_2")
        self.inside_3 = QtWidgets.QLabel(self.centralwidget)
        self.inside_3.setGeometry(QtCore.QRect(371, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.inside_3.setFont(font)
        self.inside_3.setObjectName("inside_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setEnabled(True)
        self.menufile.setGeometry(QtCore.QRect(2242, 256, 164, 126))
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openfile = QtWidgets.QAction(MainWindow)
        self.openfile.setObjectName("openfile")
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.setting = QtWidgets.QAction(MainWindow)
        self.setting.setObjectName("setting")
        self.menufile.addAction(self.openfile)
        self.menufile.addAction(self.save)
        self.menufile.addAction(self.save_as)
        self.menuedit.addAction(self.setting)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.close.setText(_translate("MainWindow", "close"))
        self.clean.setText(_translate("MainWindow", "clean"))
        self.analysis.setText(_translate("MainWindow", "analysis"))
        self.inside.setText(_translate("MainWindow", "inside :"))
        self.outside.setText(_translate("MainWindow", "outside :"))
        self.health.setText(_translate("MainWindow", "health or unhealth"))
        self.outside_text.setText(_translate("MainWindow", "??"))
        self.result_text.setText(_translate("MainWindow", "??"))
        self.inside_text.setText(_translate("MainWindow", "??"))
        self.bfsfilter.setText(_translate("MainWindow", "bfsfilter"))
        self.Sobelfilter.setText(_translate("MainWindow", "Sobelfilter"))
        self.Cannyedge.setText(_translate("MainWindow", "Cannyedge"))
        self.diameter.setText(_translate("MainWindow", "diameter"))
        self.result.setText(_translate("MainWindow", "result :"))
        self.name.setText(_translate("MainWindow", "name"))
        self.length.setText(_translate("MainWindow", "length"))
        self.filter.setText(_translate("MainWindow", "filter :"))
        self.Center.setText(_translate("MainWindow", "Center Adjustment"))
        self.Report.setText(_translate("MainWindow", "Auto Save Report"))
        self.checkBox_3.setText(_translate("MainWindow", "Time Optimizer"))
        self.function.setText(_translate("MainWindow", "function :"))
        self.inside_2.setText(_translate("MainWindow", "ex : graph.bmp"))
        self.inside_3.setText(_translate("MainWindow", "ex : 50um"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.menuedit.setTitle(_translate("MainWindow", "edit"))
        self.openfile.setText(_translate("MainWindow", "open file"))
        self.save.setText(_translate("MainWindow", "save"))
        self.save_as.setText(_translate("MainWindow", "save as"))
        self.setting.setText(_translate("MainWindow", "setting"))
        
    def Analysis(self, name, length):
        self.scanner = False
        self.inside_text.setText("running...")
        self.outside_text.setText("running...")  
        self.result_text.setText("running...")
        time.sleep(5)
        for i in range(len(length)):
            if(length[i].isdigit() == False):
                break
            elif(i == len(length) - 1):
                i += 1
        unit = length[i:]
        length = float(length[:i])   
        if(self.Sobelfilter.isChecked()):
            filter_mode = "Sobelfilter"
        elif(self.Cannyedge.isChecked()):
            filter_mode = "Cannyedge"
        else:
            filter_mode = "bfsfilter"  
        checkbox = {"Center":self.Center.isChecked(), "Report":self.Report.isChecked(), "multiprocess":self.checkBox_3.isChecked()}
        inRadius, outRadius, Radius_data, train_radius_data, train_picture_data = Total_Radius(name, length, filter_mode, checkbox, False)
        self.inside_text.setText(("%.3f " % round(np.average(inRadius), 3)) + str(unit))
        self.outside_text.setText(("%.3f " % round(np.average(outRadius), 3)) + str(unit)) 
        self.result_text.setText("loading...") 
        self.scanner = True
        radius_update(Radius_data, train_radius_data, train_picture_data, name, unit, filter_mode, self)

    def Clean(self):
        self.path_lineEdit.setText("")
        self.length_lineEdit.setText("")  

    def Close(self):
        self.scanner = False
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.analysis.clicked.connect(lambda:ui.Analysis(ui.path_lineEdit.text(), float(ui.length_lineEdit.text())))
    ui.clean.clicked.connect(ui.Clean)
    ui.close.clicked.connect(ui.Close)
    sys.exit(app.exec_())