# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledoEzzHa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 633)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(30, 10, 411, 221))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(460, 10, 421, 221))
        self.graphicsView_3 = QGraphicsView(self.centralwidget)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(30, 270, 411, 192))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(480, 300, 191, 31))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(680, 300, 191, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(480, 270, 81, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 350, 71, 16))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(480, 380, 191, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(480, 420, 71, 16))
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(480, 450, 191, 31))
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(680, 450, 191, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 500, 75, 23))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 500, 75, 23))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(460, 500, 75, 23))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(590, 500, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 905, 23))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.textEdit, self.textEdit_2)
        QWidget.setTabOrder(self.textEdit_2, self.textEdit_4)
        QWidget.setTabOrder(self.textEdit_4, self.textEdit_5)
        QWidget.setTabOrder(self.textEdit_5, self.textEdit_6)
        QWidget.setTabOrder(self.textEdit_6, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.graphicsView)
        QWidget.setTabOrder(self.graphicsView, self.graphicsView_2)
        QWidget.setTabOrder(self.graphicsView_2, self.graphicsView_3)

        self.retranslateUi(MainWindow)
        MainWindow.windowTitleChanged.connect(MainWindow.showMaximized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u8eab\u4efd\u8bc1\u6709\u6548\u671f</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u9a7e\u9a76\u8bc1\u7c7b\u578b</p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u9a7e\u9a76\u8bc1\u6709\u6548\u671f</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6682\u5b58", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838\u901a\u8fc7", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u5ba1\u6838\u4e0d\u901a\u8fc7", None))
    # retranslateUi

