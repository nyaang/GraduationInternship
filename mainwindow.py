# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Analyse import num_price,CiJiQuYu_price,Mianji_price,Huxing_price,ZhuangXiu_price,ChaoXiang_price,LouCeng_price,PayWay_price
# from Regression_LR_RFR import LR_predict_price,RFR_predict_price
import webbrowser
from urllib.request import pathname2url
import os
import time
from PyQt5.QtWidgets import QMessageBox,QWidget

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 290, 881, 251))
        self.tableView.setObjectName("tableView")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 221, 51))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 550, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(50, 150, 121, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(300, 70, 271, 201))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 40, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 70, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 100, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 130, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 40, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(150, 70, 93, 28))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 100, 93, 28))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 250, 91, 31))
        self.label_1.setObjectName("label_1")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(720, 550, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(670, 100, 191, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(50, 210, 93, 28))
        self.pushButton_15.setObjectName("pushButton_15")


        self.pushButton_2.clicked.connect(ChaoXiang_price)

        self.pushButton_3.clicked.connect(CiJiQuYu_price)
        self.pushButton_8.clicked.connect(ZhuangXiu_price)
        self.pushButton_9.clicked.connect(Huxing_price)
        self.pushButton_10.clicked.connect(LouCeng_price)
        self.pushButton_11.clicked.connect(Mianji_price)
        self.pushButton_12.clicked.connect(PayWay_price)
        self.pushButton_1.clicked.connect(num_price)
        self.pushButton_15.clicked.connect(self.relitu)
        self.pushButton.clicked.connect(self.jindu)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "58同城房价抓取分析系统"))
        self.label.setText(_translate("MainWindow", "执行进度："))
        self.pushButton_1.setText(_translate("MainWindow", "整体房价分析图"))
        self.groupBox.setTitle(_translate("MainWindow", "单因素分析图"))
        self.pushButton_2.setText(_translate("MainWindow", "朝向"))
        self.pushButton_3.setText(_translate("MainWindow", "区域"))
        self.pushButton_8.setText(_translate("MainWindow", "装修"))
        self.pushButton_9.setText(_translate("MainWindow", "户型"))
        self.pushButton_10.setText(_translate("MainWindow", "楼层"))
        self.pushButton_11.setText(_translate("MainWindow", "面积"))
        self.pushButton_12.setText(_translate("MainWindow", "押金"))
        self.pushButton.setText(_translate("MainWindow", "开始抓取"))
        self.label_1.setText(_translate("MainWindow", "抓取结果："))
        self.groupBox_3.setTitle(_translate("MainWindow", "统计方法分析"))
        self.pushButton_13.setText(_translate("MainWindow", "线性回归"))
        self.pushButton_14.setText(_translate("MainWindow", "随机森林"))
        self.pushButton_15.setText(_translate("MainWindow", "区域热力图"))



    def relitu(self):
        url = 'file:{}'.format(pathname2url(os.path.abspath('hot.html')))
        webbrowser.open(url)
        url = 'file:{}'.format(pathname2url(os.path.abspath('hot1.html')))
        webbrowser.open(url)


    def jindu(self):
        for i in range(101):
            time.sleep(0.1)
            self.progressBar.setProperty("value", i)
        QMessageBox.information(self, "提示", "抓取完毕！", QMessageBox.Yes)


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)

    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())