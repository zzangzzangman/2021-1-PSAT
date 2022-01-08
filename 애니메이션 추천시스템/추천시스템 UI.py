################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pandas as pd

## ==> SPLASH SCREEN
from ui_splash_screen import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_main import Ui_MainWindow

## ==> 다음페이지
from next_page import Next_Page

from final_page import Final

## ==> GLOBALS
counter = 0

df = pd.read_csv('C:/Users/user/Desktop/피셋/주제분석/venv/실험/final_data_word2vec.csv', encoding='utf-8')
df


# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.next_botton1.clicked.connect(self.pushButton_clicked)

    def pushButton_clicked(self):
        self.second = Next_Page2()
        self.second.show()
        self.close()


class Next_Page2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui2 = Next_Page()
        self.ui2.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui2.next_botton1_2.clicked.connect(self.pushButton_clicked2)

    def pushButton_clicked2(self):
        self.final = final_Page()
        self.final.show()
        self.close()


class final_Page(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui3 = Final()
        self.ui3.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 버튼 클릭
        self.ui3.run_button.clicked.connect(self.runsystem)

    def runsystem(self):
        msg = QMessageBox()
        msg.setWindowTitle("결과")
        msg.setText(
            kimji1[0] + '\n' + kimji1[1] + '\n' + kimji1[2] + '\n' + kimji1[3] + '\n' + kimji1[4] + '\n' +
            kimji1[5])

        '''if count == 1:
            if a == 1:
                msg.setText(
                    kimji1[0] + '\n' + kimji1[1] + '\n' + kimji1[2] + '\n' + kimji1[3] + '\n' + kimji1[4] + '\n' +
                    kimji1[5])
            elif b == 1:
                msg.setText(
                    kimji2[0] + '\n' + kimji2[1] + '\n' + kimji2[2] + '\n' + kimji2[3] + '\n' + kimji2[4] + '\n' +
                    kimji2[5])
            elif c == 1:
                msg.setText(
                    kimji3[0] + '\n' + kimji3[1] + '\n' + kimji3[2] + '\n' + kimji3[3] + '\n' + kimji3[4] + '\n' +
                    kimji3[5])

        if count == 2:
            if a == 1 & b == 1:
                msg.setText(
                    kimji1[0] + '\n' + kimji1[1] + '\n' + kimji1[2] + '\n' + kimji2[0] + '\n' + kimji2[1] + '\n' +
                    kimji2[2])
            if b == 1 & c == 1:
                msg.setText(
                    kimji3[0] + '\n' + kimji3[1] + '\n' + kimji3[2] + '\n' + kimji2[0] + '\n' + kimji2[1] + '\n' +
                    kimji2[2])
            if c == 1 & a == 1:
                msg.setText(
                    kimji3[0] + '\n' + kimji3[1] + '\n' + kimji3[2] + '\n' + kimji1[0] + '\n' + kimji1[1] + '\n' +
                    kimji1[2])

        if count == 3:
            msg.setText(
                kimji1[0] + '\n' + kimji1[1] + '\n' + kimji2[0] + '\n' + kimji2[1] + '\n' + kimji3[0] + '\n' + kimji3[
                    1])'''

        self.close()
        x = msg.exec_()


# SPLASH SCREEN
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # Initial Text
        self.ui.label_description.setText("<strong>행복범주")

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 2


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import platform
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from next_page import Next_Page


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 843)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(56, 58, 89);\n"
                                 "color: rgb(220, 220, 220);\n"
                                 "border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_title = QLabel(self.frame)
        self.label_title.setGeometry(QRect(0, 0, 1091, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.label_title.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_title.setTextFormat(Qt.AutoText)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_title_2 = QLabel(self.frame)
        self.label_title_2.setGeometry(QRect(0, 90, 861, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_title_2.setFont(font)
        self.label_title_2.setLayoutDirection(Qt.LeftToRight)
        self.label_title_2.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_title_2.setTextFormat(Qt.AutoText)
        self.label_title_2.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setGeometry(QRect(10, 150, 1071, 631))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")

        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QRect(240, 90, 162, 496))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_pic2_2 = QLabel(self.layoutWidget_2)
        self.label_pic2_2.setMinimumSize(QSize(160, 160))
        self.label_pic2_2.setText("")
        self.label_pic2_2.setObjectName("label_pic2_2")
        self.verticalLayout_3.addWidget(self.label_pic2_2)
        self.label_pic1_2 = QLabel(self.layoutWidget_2)
        self.label_pic1_2.setMinimumSize(QSize(160, 160))
        self.label_pic1_2.setText("")
        self.label_pic1_2.setObjectName("label_pic1_2")
        self.verticalLayout_3.addWidget(self.label_pic1_2)
        self.label_pic3_2 = QLabel(self.layoutWidget_2)
        self.label_pic3_2.setMinimumSize(QSize(160, 160))
        self.label_pic3_2.setText("")
        self.label_pic3_2.setObjectName("label_pic3_2")
        self.verticalLayout_3.addWidget(self.label_pic3_2)
        self.layoutWidget_3 = QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QRect(30, 90, 162, 496))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_pic2_3 = QLabel(self.layoutWidget_3)
        self.label_pic2_3.setMinimumSize(QSize(160, 160))
        self.label_pic2_3.setText("")
        self.label_pic2_3.setObjectName("label_pic2_3")
        self.verticalLayout_4.addWidget(self.label_pic2_3)
        self.label_pic1_3 = QLabel(self.layoutWidget_3)
        self.label_pic1_3.setMinimumSize(QSize(160, 160))
        self.label_pic1_3.setText("")
        self.label_pic1_3.setObjectName("label_pic1_3")
        self.verticalLayout_4.addWidget(self.label_pic1_3)
        self.label_pic3_3 = QLabel(self.layoutWidget_3)
        self.label_pic3_3.setMinimumSize(QSize(160, 160))
        self.label_pic3_3.setText("")
        self.label_pic3_3.setObjectName("label_pic3_3")
        self.verticalLayout_4.addWidget(self.label_pic3_3)
        self.layoutWidget_4 = QWidget(self.groupBox)
        self.layoutWidget_4.setGeometry(QRect(450, 90, 162, 496))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_pic2_4 = QLabel(self.layoutWidget_4)
        self.label_pic2_4.setMinimumSize(QSize(160, 160))
        self.label_pic2_4.setText("")
        self.label_pic2_4.setObjectName("label_pic2_4")
        self.verticalLayout_5.addWidget(self.label_pic2_4)
        self.label_pic1_4 = QLabel(self.layoutWidget_4)
        self.label_pic1_4.setMinimumSize(QSize(160, 160))
        self.label_pic1_4.setText("")
        self.label_pic1_4.setObjectName("label_pic1_4")
        self.verticalLayout_5.addWidget(self.label_pic1_4)
        self.label_pic3_4 = QLabel(self.layoutWidget_4)
        self.label_pic3_4.setMinimumSize(QSize(160, 160))
        self.label_pic3_4.setText("")
        self.label_pic3_4.setObjectName("label_pic3_4")
        self.verticalLayout_5.addWidget(self.label_pic3_4)
        self.layoutWidget_5 = QWidget(self.groupBox)
        self.layoutWidget_5.setGeometry(QRect(650, 90, 162, 496))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_pic2_5 = QLabel(self.layoutWidget_5)
        self.label_pic2_5.setMinimumSize(QSize(160, 160))
        self.label_pic2_5.setText("")
        self.label_pic2_5.setObjectName("label_pic2_5")
        self.verticalLayout_6.addWidget(self.label_pic2_5)
        self.label_pic1_5 = QLabel(self.layoutWidget_5)
        self.label_pic1_5.setMinimumSize(QSize(160, 160))
        self.label_pic1_5.setText("")
        self.label_pic1_5.setObjectName("label_pic1_5")
        self.verticalLayout_6.addWidget(self.label_pic1_5)
        self.label_pic3_5 = QLabel(self.layoutWidget_5)
        self.label_pic3_5.setMinimumSize(QSize(160, 160))
        self.label_pic3_5.setText("")
        self.label_pic3_5.setObjectName("label_pic3_5")
        self.verticalLayout_6.addWidget(self.label_pic3_5)
        self.layoutWidget_6 = QWidget(self.groupBox)
        self.layoutWidget_6.setGeometry(QRect(860, 90, 162, 496))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_pic2_6 = QLabel(self.layoutWidget_6)
        self.label_pic2_6.setMinimumSize(QSize(160, 160))
        self.label_pic2_6.setText("")
        self.label_pic2_6.setObjectName("label_pic2_6")
        self.verticalLayout_7.addWidget(self.label_pic2_6)
        self.label_pic1_6 = QLabel(self.layoutWidget_6)
        self.label_pic1_6.setMinimumSize(QSize(160, 160))
        self.label_pic1_6.setText("")
        self.label_pic1_6.setObjectName("label_pic1_6")
        self.verticalLayout_7.addWidget(self.label_pic1_6)
        self.label_pic3_6 = QLabel(self.layoutWidget_6)
        self.label_pic3_6.setMinimumSize(QSize(160, 160))
        self.label_pic3_6.setText("")
        self.label_pic3_6.setObjectName("label_pic3_6")
        self.verticalLayout_7.addWidget(self.label_pic3_6)

        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QRect(11, 50, 1030, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pic_button1 = QRadioButton(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_button1.sizePolicy().hasHeightForWidth())
        self.pic_button1.setSizePolicy(sizePolicy)
        self.pic_button1.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pic_button1.setFont(font)
        self.pic_button1.setStyleSheet("color: rgb(206, 207, 255);")
        self.pic_button1.setObjectName("pic_button1")
        self.horizontalLayout.addWidget(self.pic_button1)
        self.pic_button2 = QRadioButton(self.layoutWidget)
        self.pic_button2.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.pic_button2.setFont(font)
        self.pic_button2.setStyleSheet("color: rgb(206, 207, 255);")
        self.pic_button2.setObjectName("pic_button2")
        self.horizontalLayout.addWidget(self.pic_button2)
        self.pic_button3 = QRadioButton(self.layoutWidget)
        self.pic_button3.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.pic_button3.setFont(font)
        self.pic_button3.setStyleSheet("color: rgb(206, 207, 255);")
        self.pic_button3.setObjectName("pic_button3")
        self.horizontalLayout.addWidget(self.pic_button3)
        self.pic_button4 = QRadioButton(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_button4.sizePolicy().hasHeightForWidth())
        self.pic_button4.setSizePolicy(sizePolicy)
        self.pic_button4.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.pic_button4.setFont(font)
        self.pic_button4.setStyleSheet("color: rgb(206, 207, 255);")
        self.pic_button4.setObjectName("pic_button4")
        self.horizontalLayout.addWidget(self.pic_button4)
        self.pic_button4_2 = QRadioButton(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pic_button4_2.sizePolicy().hasHeightForWidth())
        self.pic_button4_2.setSizePolicy(sizePolicy)
        self.pic_button4_2.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.pic_button4_2.setFont(font)
        self.pic_button4_2.setStyleSheet("color: rgb(206, 207, 255);")
        self.pic_button4_2.setObjectName("pic_button4_2")
        self.horizontalLayout.addWidget(self.pic_button4_2)
        self.next_botton1 = QPushButton(self.frame)
        self.next_botton1.setGeometry(QRect(980, 110, 93, 28))
        self.next_botton1.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(123, 15, 166);\n"
                                        "border: none;\n"
                                        "color: rgb(255, 225, 254);\n"
                                        "border-left: 1px solid rgb(37, 1, 59);\n"
                                        "border-right: 1px solid rgb(37, 1, 59);\n"
                                        "border-bottom: 3px solid rgb(37, 1, 59);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(133, 25, 176);\n"
                                        "border-left: 1px solid rgb(37, 1, 59);\n"
                                        "border-right: 1px solid rgb(37, 1, 59);\n"
                                        "border-bottom: 3px solid rgb(37, 1, 59);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(113, 5, 156);\n"
                                        "border-left: 1px solid rgb(37, 1, 59);\n"
                                        "border-right: 1px solid rgb(37, 1, 59);\n"
                                        "border-top: 3px solid rgb(37, 1, 59);\n"
                                        "border-bottom: none;\n"
                                        "}\n"
                                        "")
        self.next_botton1.setObjectName("next_botton1")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        # 사진 부분
        self.qPixmapVar1 = QPixmap()
        self.qPixmapVar2 = QPixmap()
        self.qPixmapVar3 = QPixmap()
        self.qPixmapVar4 = QPixmap()
        self.qPixmapVar5 = QPixmap()
        self.qPixmapVar6 = QPixmap()
        self.qPixmapVar7 = QPixmap()
        self.qPixmapVar8 = QPixmap()
        self.qPixmapVar9 = QPixmap()
        self.qPixmapVar10 = QPixmap()
        self.qPixmapVar11 = QPixmap()
        self.qPixmapVar12 = QPixmap()
        self.qPixmapVar13 = QPixmap()
        self.qPixmapVar14 = QPixmap()
        self.qPixmapVar15 = QPixmap()
        self.qPixmapVar1.load("cluster1_1.jpg")
        self.qPixmapVar2.load("cluster1_2.jpg")
        self.qPixmapVar3.load("cluster1_3.jpg")
        self.qPixmapVar4.load("cluster2_1.jpg")
        self.qPixmapVar5.load("cluster2_2.jpg")
        self.qPixmapVar6.load("cluster2_3.jpg")
        self.qPixmapVar7.load("cluster3_1.jpg")
        self.qPixmapVar8.load("cluster3_2.jpg")
        self.qPixmapVar9.load("cluster3_3.jpg")
        self.qPixmapVar10.load("cluster4_1.jpg")
        self.qPixmapVar11.load("cluster4_2.jpg")
        self.qPixmapVar12.load("cluster4_3.jpg")
        self.qPixmapVar13.load("cluster5_1.jpg")
        self.qPixmapVar14.load("cluster5_2.jpg")
        self.qPixmapVar15.load("cluster5_3.jpg")

        self.qPixmapVar1 = self.qPixmapVar1.scaledToWidth(200)
        self.qPixmapVar2 = self.qPixmapVar2.scaledToWidth(200)
        self.qPixmapVar3 = self.qPixmapVar3.scaledToWidth(200)
        self.qPixmapVar4 = self.qPixmapVar4.scaledToWidth(200)
        self.qPixmapVar5 = self.qPixmapVar5.scaledToWidth(200)
        self.qPixmapVar6 = self.qPixmapVar6.scaledToWidth(200)
        self.qPixmapVar7 = self.qPixmapVar7.scaledToWidth(200)
        self.qPixmapVar8 = self.qPixmapVar8.scaledToWidth(200)
        self.qPixmapVar9 = self.qPixmapVar9.scaledToWidth(200)
        self.qPixmapVar10 = self.qPixmapVar10.scaledToWidth(200)
        self.qPixmapVar11 = self.qPixmapVar11.scaledToWidth(200)
        self.qPixmapVar12 = self.qPixmapVar12.scaledToWidth(200)
        self.qPixmapVar13 = self.qPixmapVar13.scaledToWidth(200)
        self.qPixmapVar14 = self.qPixmapVar14.scaledToWidth(200)
        self.qPixmapVar15 = self.qPixmapVar15.scaledToWidth(200)

        '''self.qPixmapVar = self.qPixmapVar.scaledToHeight(200)
        self.qPixmapVar2 = self.qPixmapVar2.scaledToHeight(200)
        self.qPixmapVar3 = self.qPixmapVar3.scaledToHeight(200)
        self.qPixmapVar4 = self.qPixmapVar4.scaledToHeight(200)
        self.qPixmapVar5 = self.qPixmapVar5.scaledToHeight(200)
        self.qPixmapVar6 = self.qPixmapVar6.scaledToHeight(200)
        self.qPixmapVar7 = self.qPixmapVar7.scaledToHeight(200)
        self.qPixmapVar8 = self.qPixmapVar8.scaledToHeight(200)
        self.qPixmapVar9 = self.qPixmapVar9.scaledToHeight(200)
        self.qPixmapVar10 = self.qPixmapVar10.scaledToHeight(200)
        self.qPixmapVar11 = self.qPixmapVar11.scaledToHeight(200)
        self.qPixmapVar12 = self.qPixmapVar12.scaledToHeight(200)'''

        self.label_pic2_3.setPixmap(self.qPixmapVar1)
        self.label_pic1_3.setPixmap(self.qPixmapVar2)
        self.label_pic3_3.setPixmap(self.qPixmapVar3)
        self.label_pic2_2.setPixmap(self.qPixmapVar4)
        self.label_pic1_2.setPixmap(self.qPixmapVar5)
        self.label_pic3_2.setPixmap(self.qPixmapVar6)
        self.label_pic2_4.setPixmap(self.qPixmapVar7)
        self.label_pic1_4.setPixmap(self.qPixmapVar8)
        self.label_pic3_4.setPixmap(self.qPixmapVar9)
        self.label_pic2_5.setPixmap(self.qPixmapVar10)
        self.label_pic1_5.setPixmap(self.qPixmapVar11)
        self.label_pic3_5.setPixmap(self.qPixmapVar12)
        self.label_pic2_6.setPixmap(self.qPixmapVar13)
        self.label_pic1_6.setPixmap(self.qPixmapVar14)
        self.label_pic3_6.setPixmap(self.qPixmapVar15)

        self.pic_button1.clicked.connect(self.groupboxRadFunction)
        self.pic_button2.clicked.connect(self.groupboxRadFunction)
        self.pic_button3.clicked.connect(self.groupboxRadFunction)
        self.pic_button4.clicked.connect(self.groupboxRadFunction)
        self.pic_button4_2.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self):
        global df2
        if self.pic_button1.isChecked():
            print("1번 체크")
            picture = 0
            df2 = df[df['cluster'] == picture]

        elif self.pic_button2.isChecked():
            print("2번 체크")
            picture = 1
            df2 = df[df['cluster'] == picture]

        elif self.pic_button3.isChecked():
            print("3번 체크")
            picture = 2
            df2 = df[df['cluster'] == picture]

        elif self.pic_button4.isChecked():
            print("4번 체크")
            picture = 3
            df2 = df[df['cluster'] == picture]

        elif self.pic_button4_2.isChecked():
            print("5번 체크")
            picture = 4
            df2 = df[df['cluster'] == picture]

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<strong>Animation recommender"))
        self.label_title_2.setText(_translate("MainWindow", "    1. 원하는 그림체를 선택하세요."))
        self.pic_button1.setText(_translate("MainWindow", "1번"))
        self.pic_button2.setText(_translate("MainWindow", "2번"))
        self.pic_button3.setText(_translate("MainWindow", "3번"))
        self.pic_button4.setText(_translate("MainWindow", "4번"))
        self.pic_button4_2.setText(_translate("MainWindow", "5번"))
        self.next_botton1.setText(_translate("MainWindow", "다음"))


### 2번째 패이지

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'next_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Next_Page(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1133, 843)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(11, 11, 1092, 796))
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(56, 58, 89);\n"
                                 "color: rgb(220, 220, 220);\n"
                                 "border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_title_3 = QLabel(self.frame)
        self.label_title_3.setGeometry(QRect(0, 0, 1091, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title_3.setFont(font)
        self.label_title_3.setLayoutDirection(Qt.LeftToRight)
        self.label_title_3.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_title_3.setTextFormat(Qt.AutoText)
        self.label_title_3.setAlignment(Qt.AlignCenter)
        self.label_title_3.setObjectName("label_title_3")
        self.label_genre = QLabel(self.frame)
        self.label_genre.setGeometry(QRect(0, 340, 861, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_genre.setFont(font)
        self.label_genre.setLayoutDirection(Qt.LeftToRight)
        self.label_genre.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_genre.setTextFormat(Qt.AutoText)
        self.label_genre.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_genre.setObjectName("label_genre")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QRect(10, 430, 1071, 291))
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")

        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QRect(60, 30, 202, 217))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.fantasy = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fantasy.sizePolicy().hasHeightForWidth())
        self.fantasy.setSizePolicy(sizePolicy)
        self.fantasy.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.fantasy.setFont(font)
        self.fantasy.setStyleSheet("color: rgb(224, 211, 255);")
        self.fantasy.setObjectName("fantasy")
        self.verticalLayout.addWidget(self.fantasy)
        self.romance = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.romance.sizePolicy().hasHeightForWidth())
        self.romance.setSizePolicy(sizePolicy)
        self.romance.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.romance.setFont(font)
        self.romance.setStyleSheet("color: rgb(224, 211, 255);")
        self.romance.setObjectName("romance")
        self.verticalLayout.addWidget(self.romance)
        self.daily = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.daily.sizePolicy().hasHeightForWidth())
        self.daily.setSizePolicy(sizePolicy)
        self.daily.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.daily.setFont(font)
        self.daily.setStyleSheet("color: rgb(224, 211, 255);")
        self.daily.setObjectName("daily")
        self.verticalLayout.addWidget(self.daily)
        self.humot = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humot.sizePolicy().hasHeightForWidth())
        self.humot.setSizePolicy(sizePolicy)
        self.humot.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.humot.setFont(font)
        self.humot.setStyleSheet("color: rgb(224, 211, 255);")
        self.humot.setObjectName("humot")
        self.verticalLayout.addWidget(self.humot)
        self.action = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action.sizePolicy().hasHeightForWidth())
        self.action.setSizePolicy(sizePolicy)
        self.action.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.action.setFont(font)
        self.action.setStyleSheet("color: rgb(224, 211, 255);")
        self.action.setObjectName("action")
        self.verticalLayout.addWidget(self.action)
        self.sport = QCheckBox(self.layoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sport.sizePolicy().hasHeightForWidth())
        self.sport.setSizePolicy(sizePolicy)
        self.sport.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.sport.setFont(font)
        self.sport.setStyleSheet("color: rgb(224, 211, 255);")
        self.sport.setObjectName("sport")
        self.verticalLayout.addWidget(self.sport)

        self.layoutWidget1 = QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QRect(320, 30, 202, 217))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.adventure = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adventure.sizePolicy().hasHeightForWidth())
        self.adventure.setSizePolicy(sizePolicy)
        self.adventure.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.adventure.setFont(font)
        self.adventure.setStyleSheet("color: rgb(224, 211, 255);")
        self.adventure.setObjectName("adventure")
        self.verticalLayout_2.addWidget(self.adventure)
        self.age = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.age.sizePolicy().hasHeightForWidth())
        self.age.setSizePolicy(sizePolicy)
        self.age.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.age.setFont(font)
        self.age.setStyleSheet("color: rgb(224, 211, 255);")
        self.age.setObjectName("age")
        self.verticalLayout_2.addWidget(self.age)
        self.BL = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BL.sizePolicy().hasHeightForWidth())
        self.BL.setSizePolicy(sizePolicy)
        self.BL.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.BL.setFont(font)
        self.BL.setStyleSheet("color: rgb(224, 211, 255);")
        self.BL.setObjectName("BL")
        self.verticalLayout_2.addWidget(self.BL)
        self.music = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music.sizePolicy().hasHeightForWidth())
        self.music.setSizePolicy(sizePolicy)
        self.music.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.music.setFont(font)
        self.music.setStyleSheet("color: rgb(224, 211, 255);")
        self.music.setObjectName("music")
        self.verticalLayout_2.addWidget(self.music)
        self.inference = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inference.sizePolicy().hasHeightForWidth())
        self.inference.setSizePolicy(sizePolicy)
        self.inference.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.inference.setFont(font)
        self.inference.setStyleSheet("color: rgb(224, 211, 255);")
        self.inference.setObjectName("inference")
        self.verticalLayout_2.addWidget(self.inference)
        self.mystery = QCheckBox(self.layoutWidget1)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mystery.sizePolicy().hasHeightForWidth())
        self.mystery.setSizePolicy(sizePolicy)
        self.mystery.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.mystery.setFont(font)
        self.mystery.setStyleSheet("color: rgb(224, 211, 255);")
        self.mystery.setObjectName("mystery")
        self.verticalLayout_2.addWidget(self.mystery)
        self.layoutWidget2 = QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QRect(570, 30, 202, 217))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.adult19 = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.adult19.sizePolicy().hasHeightForWidth())
        self.adult19.setSizePolicy(sizePolicy)
        self.adult19.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.adult19.setFont(font)
        self.adult19.setStyleSheet("color: rgb(224, 211, 255);")
        self.adult19.setObjectName("adult19")
        self.verticalLayout_3.addWidget(self.adult19)
        self.SF = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SF.sizePolicy().hasHeightForWidth())
        self.SF.setSizePolicy(sizePolicy)
        self.SF.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.SF.setFont(font)
        self.SF.setStyleSheet("color: rgb(224, 211, 255);")
        self.SF.setObjectName("SF")
        self.verticalLayout_3.addWidget(self.SF)
        self.thrill = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thrill.sizePolicy().hasHeightForWidth())
        self.thrill.setSizePolicy(sizePolicy)
        self.thrill.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.thrill.setFont(font)
        self.thrill.setStyleSheet("color: rgb(224, 211, 255);")
        self.thrill.setObjectName("thrill")
        self.verticalLayout_3.addWidget(self.thrill)
        self.crime = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crime.sizePolicy().hasHeightForWidth())
        self.crime.setSizePolicy(sizePolicy)
        self.crime.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.crime.setFont(font)
        self.crime.setStyleSheet("color: rgb(224, 211, 255);")
        self.crime.setObjectName("crime")
        self.verticalLayout_3.addWidget(self.crime)
        self.idol = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idol.sizePolicy().hasHeightForWidth())
        self.idol.setSizePolicy(sizePolicy)
        self.idol.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.idol.setFont(font)
        self.idol.setStyleSheet("color: rgb(224, 211, 255);")
        self.idol.setObjectName("idol")
        self.verticalLayout_3.addWidget(self.idol)
        self.scary = QCheckBox(self.layoutWidget2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scary.sizePolicy().hasHeightForWidth())
        self.scary.setSizePolicy(sizePolicy)
        self.scary.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.scary.setFont(font)
        self.scary.setStyleSheet("color: rgb(224, 211, 255);")
        self.scary.setObjectName("scary")
        self.verticalLayout_3.addWidget(self.scary)
        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QRect(820, 60, 202, 143))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.GL = QCheckBox(self.layoutWidget3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GL.sizePolicy().hasHeightForWidth())
        self.GL.setSizePolicy(sizePolicy)
        self.GL.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.GL.setFont(font)
        self.GL.setStyleSheet("color: rgb(224, 211, 255);")
        self.GL.setObjectName("GL")
        self.verticalLayout_4.addWidget(self.GL)
        self.kids = QCheckBox(self.layoutWidget3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kids.sizePolicy().hasHeightForWidth())
        self.kids.setSizePolicy(sizePolicy)
        self.kids.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.kids.setFont(font)
        self.kids.setStyleSheet("color: rgb(224, 211, 255);")
        self.kids.setObjectName("kids")
        self.verticalLayout_4.addWidget(self.kids)
        self.healing = QCheckBox(self.layoutWidget3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.healing.sizePolicy().hasHeightForWidth())
        self.healing.setSizePolicy(sizePolicy)
        self.healing.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.healing.setFont(font)
        self.healing.setStyleSheet("color: rgb(224, 211, 255);")
        self.healing.setObjectName("healing")
        self.verticalLayout_4.addWidget(self.healing)
        self.drama = QCheckBox(self.layoutWidget3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.drama.sizePolicy().hasHeightForWidth())
        self.drama.setSizePolicy(sizePolicy)
        self.drama.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        self.drama.setFont(font)
        self.drama.setStyleSheet("color: rgb(224, 211, 255);")
        self.drama.setObjectName("drama")
        self.verticalLayout_4.addWidget(self.drama)
        self.next_botton1_2 = QPushButton(self.frame)
        self.next_botton1_2.setGeometry(QRect(970, 100, 93, 28))
        self.next_botton1_2.setStyleSheet("QPushButton{\n"
                                          "background-color: rgb(123, 15, 166);\n"
                                          "border: none;\n"
                                          "color: rgb(255, 225, 254);\n"
                                          "border-left: 1px solid rgb(37, 1, 59);\n"
                                          "border-right: 1px solid rgb(37, 1, 59);\n"
                                          "border-bottom: 3px solid rgb(37, 1, 59);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "background-color: rgb(133, 25, 176);\n"
                                          "border-left: 1px solid rgb(37, 1, 59);\n"
                                          "border-right: 1px solid rgb(37, 1, 59);\n"
                                          "border-bottom: 3px solid rgb(37, 1, 59);\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed{\n"
                                          "background-color: rgb(113, 5, 156);\n"
                                          "border-left: 1px solid rgb(37, 1, 59);\n"
                                          "border-right: 1px solid rgb(37, 1, 59);\n"
                                          "border-top: 3px solid rgb(37, 1, 59);\n"
                                          "border-bottom: none;\n"
                                          "}\n"
                                          "")
        self.next_botton1_2.setObjectName("next_botton1_2")
        self.label_type = QLabel(self.frame)
        self.label_type.setGeometry(QRect(0, 100, 861, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_type.setFont(font)
        self.label_type.setLayoutDirection(Qt.LeftToRight)
        self.label_type.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_type.setTextFormat(Qt.AutoText)
        self.label_type.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_type.setObjectName("label_type")
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QRect(10, 170, 1071, 101))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.old_button = QRadioButton(self.groupBox_3)
        self.old_button.setGeometry(QRect(80, 40, 108, 19))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.old_button.setFont(font)
        self.old_button.setStyleSheet("color: rgb(224, 211, 255);")
        self.old_button.setObjectName("old_button")
        self.recent_button = QRadioButton(self.groupBox_3)
        self.recent_button.setGeometry(QRect(560, 40, 108, 19))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(11)
        self.recent_button.setFont(font)
        self.recent_button.setStyleSheet("color: rgb(224, 211, 255);")
        self.recent_button.setObjectName("recent_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        ### 출시시기 구분 버튼 함수 연결
        self.old_button.clicked.connect(self.tiemFunction)
        self.recent_button.clicked.connect(self.tiemFunction)

        self.action.stateChanged.connect(self.checkFunction)
        self.daily.stateChanged.connect(self.checkFunction)
        self.fantasy.stateChanged.connect(self.checkFunction)
        self.humot.stateChanged.connect(self.checkFunction)
        self.romance.stateChanged.connect(self.checkFunction)
        self.sport.stateChanged.connect(self.checkFunction)
        self.BL.stateChanged.connect(self.checkFunction)
        self.adventure.stateChanged.connect(self.checkFunction)
        self.age.stateChanged.connect(self.checkFunction)
        self.inference.stateChanged.connect(self.checkFunction)
        self.music.stateChanged.connect(self.checkFunction)
        self.mystery.stateChanged.connect(self.checkFunction)
        self.SF.stateChanged.connect(self.checkFunction)
        self.adult19.stateChanged.connect(self.checkFunction)
        self.crime.stateChanged.connect(self.checkFunction)
        self.idol.stateChanged.connect(self.checkFunction)
        self.scary.stateChanged.connect(self.checkFunction)
        self.thrill.stateChanged.connect(self.checkFunction)
        self.GL.stateChanged.connect(self.checkFunction)
        self.drama.stateChanged.connect(self.checkFunction)
        self.kids.stateChanged.connect(self.checkFunction)

    def checkFunction(self):
        genre = []
        global df3_1
        global df3_2
        global c3
        if self.action.isChecked():
            print("액션 체크")
            genre.append('액션')
        if self.daily.isChecked():
            print("일상 체크")
            genre.append('일상')
        if self.fantasy.isChecked():
            print("판타지 체크")
            genre.append('판타지')
        if self.humot.isChecked():
            print("개그 체크")
            genre.append('개그')
        if self.romance.isChecked():
            print("로맨스 체크")
            genre.append('로맨스')
        if self.sport.isChecked():
            print("스포츠 체크")
            genre.append('스포츠')
        if self.BL.isChecked():
            print("BL 체크")
            genre.append('BL')
        if self.adventure.isChecked():
            print("모험 체크")
            genre.append('모험')
        if self.age.isChecked():
            print("시대물 체크")
            genre.append('시대물')
        if self.inference.isChecked():
            print("추리 체크")
            genre.append('추리')
        if self.music.isChecked():
            print("음악 체크")
            genre.append('음악')
        if self.mystery.isChecked():
            print("미스테리 체크")
            genre.append('미스테리')
        if self.SF.isChecked():
            print("SF 체크")
            genre.append('SF')
        if self.adult19.isChecked():
            print("성인 체크")
            genre.append('성인')
        if self.crime.isChecked():
            print("범죄 체크")
            genre.append('범죄')
        if self.idol.isChecked():
            print("아이돌 체크")
            genre.append('아이돌')
        if self.scary.isChecked():
            print("공포 체크")
            genre.append('공포')
        if self.thrill.isChecked():
            print("스릴러 체크")
            genre.append('스릴러')
        if self.GL.isChecked():
            print("GL 체크")
            genre.append('GL')
        if self.drama.isChecked():
            print("드라마 체크")
            genre.append('드라마')
        if self.healing.isChecked():
            print("치유 체크")
            genre.append('치유')
        if self.kids.isChecked():
            print("아동 체크")
            genre.append('아동')
        df3_1 = df3.drop(['cluster', '출시년도구분', 'genre', 'genre1', 'genre2', '제목'], axis=1)
        c1 = pd.DataFrame(cosine_similarity(df3_1))
        c2 = c1.copy()
        df3_2 = df3[df3['genre1'].isin(genre) | df3['genre2'].isin(genre)]
        name = df3_2['제목']
        c1.index = df3['제목']
        c1.columns = df3['제목']
        for i in range(0, len(c1)):
            if sum(c2.index[i] == name) == 1:
                c2.iloc[i, :] = c2.iloc[i, :] * 300
            else:
                c2.iloc[i, :] = c2.iloc[i, :] * 0
        c3 = (c1.to_numpy() + c2.to_numpy())/ 2
        c3 = pd.DataFrame(c3)
        c3.index = df3['제목']
        c3.columns = df3['제목']

    def tiemFunction(self):
        global df3
        if self.old_button.isChecked():
            print("추억의 만화로 고고~!")
            df3 = df2[df2['출시년도구분'] == 'old']

        elif self.recent_button.isChecked():
            print("요즘 유행을 따르고 싶군요!")
            df3 = df2[df2['출시년도구분'] == 'new']

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_3.setText(_translate("MainWindow", "<strong>Animation recommender"))
        self.label_genre.setText(_translate("MainWindow", "    3. 원하는 장르를 선택하세요. (중복 선택 가능)"))
        self.fantasy.setText(_translate("MainWindow", "판타지"))
        self.romance.setText(_translate("MainWindow", "로맨스"))
        self.daily.setText(_translate("MainWindow", "일상"))
        self.humot.setText(_translate("MainWindow", "개그"))
        self.action.setText(_translate("MainWindow", "액션"))
        self.sport.setText(_translate("MainWindow", "스포츠"))
        self.adventure.setText(_translate("MainWindow", "모험"))
        self.age.setText(_translate("MainWindow", "시대물"))
        self.BL.setText(_translate("MainWindow", "BL"))
        self.music.setText(_translate("MainWindow", "음악"))
        self.inference.setText(_translate("MainWindow", "추리"))
        self.mystery.setText(_translate("MainWindow", "미스터리"))
        self.adult19.setText(_translate("MainWindow", "성인"))
        self.SF.setText(_translate("MainWindow", "SF"))
        self.thrill.setText(_translate("MainWindow", "스릴러"))
        self.crime.setText(_translate("MainWindow", "범죄"))
        self.idol.setText(_translate("MainWindow", "아이돌"))
        self.scary.setText(_translate("MainWindow", "공포"))
        self.GL.setText(_translate("MainWindow", "GL / 백합"))
        self.kids.setText(_translate("MainWindow", "아동"))
        self.healing.setText(_translate("MainWindow", "치유"))
        self.drama.setText(_translate("MainWindow", "드라마"))
        self.next_botton1_2.setText(_translate("MainWindow", "다음"))
        self.label_type.setText(_translate("MainWindow", "    2. 원하는 만화 타입을 고르세요."))
        self.old_button.setText(_translate("MainWindow", "추억의 만화"))
        self.recent_button.setText(_translate("MainWindow", "최신 만화"))


### 3번째 페이지
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Final(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 843)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QRect(11, 11, 1092, 796))
        self.frame.setStyleSheet("QFrame{\n"
                                 "background-color: rgb(56, 58, 89);\n"
                                 "color: rgb(220, 220, 220);\n"
                                 "border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_title = QLabel(self.frame)
        self.label_title.setGeometry(QRect(0, 0, 1091, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.label_title.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_title.setTextFormat(Qt.AutoText)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_title_2 = QLabel(self.frame)
        self.label_title_2.setGeometry(QRect(0, 90, 1091, 71))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.label_title_2.setFont(font)
        self.label_title_2.setLayoutDirection(Qt.LeftToRight)
        self.label_title_2.setStyleSheet("color: rgb(255, 170, 255);")
        self.label_title_2.setTextFormat(Qt.AutoText)
        self.label_title_2.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_title_2.setObjectName("label_title_2")
        self.run_button = QPushButton(self.frame)
        self.run_button.setGeometry(QRect(250, 610, 601, 111))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.run_button.setFont(font)
        self.run_button.setStyleSheet("QPushButton{\n"
                                      "    color: white;\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(10, 242, 251, 255), stop:1 rgba(224, 6, 159, 255));\n"
                                      "    border-radius: 30px;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    color: white;\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(20, 252, 255, 255), stop:1 rgba(234, 26, 179, 255));\n"
                                      "    border-radius: 30px;\n"
                                      "border-left: 1px solid rgb(37, 1, 59);\n"
                                      "border-right: 2px solid rgb(37, 1, 59);\n"
                                      "border-bottom: 3px solid rgb(37, 1, 59);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "color: white;\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:0 rgba(0, 232, 235, 255), stop:1 rgba(214, 6, 149, 255));\n"
                                      "border-radius: 30px;\n"
                                      "border-left: 2px solid rgb(37, 1, 59);\n"
                                      "border-right: 1px solid rgb(37, 1, 59);\n"
                                      "border-top: 3px solid rgb(37, 1, 59);\n"
                                      "border-bottom: none;\n"
                                      "}")
        self.run_button.setObjectName("run_button")

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QRect(10, 160, 1071, 101))
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget = QWidget(self.groupBox_2)
        self.widget.setGeometry(QRect(21, 31, 1061, 32))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ratio = QCheckBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ratio.sizePolicy().hasHeightForWidth())
        self.ratio.setSizePolicy(sizePolicy)
        self.ratio.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(15)
        self.ratio.setFont(font)
        self.ratio.setStyleSheet("color: rgb(224, 211, 255);")
        self.ratio.setObjectName("ratio")
        self.horizontalLayout.addWidget(self.ratio)
        self.num_ratio = QCheckBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_ratio.sizePolicy().hasHeightForWidth())
        self.num_ratio.setSizePolicy(sizePolicy)
        self.num_ratio.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(15)
        self.num_ratio.setFont(font)
        self.num_ratio.setStyleSheet("color: rgb(224, 211, 255);")
        self.num_ratio.setObjectName("num_ratio")
        self.horizontalLayout.addWidget(self.num_ratio)
        self.sexRatio = QCheckBox(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sexRatio.sizePolicy().hasHeightForWidth())
        self.sexRatio.setSizePolicy(sizePolicy)
        self.sexRatio.setMinimumSize(QSize(200, 30))
        font = QFont()
        font.setFamily("a타이틀고딕1")
        font.setPointSize(15)
        self.sexRatio.setFont(font)
        self.sexRatio.setStyleSheet("color: rgb(224, 211, 255);")
        self.sexRatio.setObjectName("sexRatio")
        self.horizontalLayout.addWidget(self.sexRatio)

        self.ratio.stateChanged.connect(self.favorite)
        self.num_ratio.stateChanged.connect(self.favorite)
        self.sexRatio.stateChanged.connect(self.favorite)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def favorite(self):
        global kimji1
        global kimji2
        global kimji3
        global count
        global a
        global b
        global c
        count, a, b, c = 0, 0, 0, 0
        if self.ratio.isChecked():
            print("평점 체크")
            pick_1 = df3.sort_values(by='평점', ascending=False).reset_index().loc[0, '제목']
            c4 = c3[c3.index == pick_1].T
            c4.sort_values(by=c4.columns[0], ascending=False)
            global kimji1
            kimji1 = [c4.columns[0]]
            for i in range(0, 10):
                bbb = 0
                for j in range(0, min(len(c4.columns[0]), len(c4.index[i]))):
                    if c4.columns[0][j] == c4.index[i][j]:
                        bbb += 1
                if bbb < min(len(c4.columns[0]), len(c4.index[i])) / 2:
                    kimji1.append(c4.index[i])
            count += 1
            a = 1
        if self.num_ratio.isChecked():
            print("주인공 체크")
            pick_1 = df3.sort_values(by='주인공감분1', ascending=False).reset_index().loc[0, '제목']
            c4 = c3[c3.index == pick_1].T
            c4.sort_values(by=c4.columns[0], ascending=False)
            #global kimji2
            kimji1 = [c4.columns[0]]
            for i in range(0, 10):
                bbb = 0
                for j in range(0, min(len(c4.columns[0]), len(c4.index[i]))):
                    if c4.columns[0][j] == c4.index[i][j]:
                        bbb += 1
                if bbb < min(len(c4.columns[0]), len(c4.index[i])) / 2:
                    kimji1.append(c4.index[i])

            count += 1
            b = 1
        if self.sexRatio.isChecked():
            print("성우 체크")
            pick_1 = df3.sort_values(by='감분1', ascending=False).reset_index().loc[0, '제목']
            c4 = c3[c3.index == pick_1].T
            c4.sort_values(by=c4.columns[0], ascending=False)
            #global kimji3
            kimji1 = [c4.columns[0]]
            for i in range(0, 10):
                bbb = 0
                for j in range(0, min(len(c4.columns[0]), len(c4.index[i]))):
                    if c4.columns[0][j] == c4.index[i][j]:
                        bbb += 1
                if bbb < min(len(c4.columns[0]), len(c4.index[i])) / 2:
                    kimji1.append(c4.index[i])

            count += 1
            c = 1

            kimji1 = kimji1[0:6]

        '''if count == 1:
            if a == 1:
                kimji1 = kimji1[0:6]
            elif b == 1:
                kimji2 = kimji2[0:6]
            elif c == 1:
                kimji3 = kimji3[0:6]

        if count == 2:
            if a == 1:
                kimji1 = kimji1[0:3]
            if b == 1:
                kimji2 = kimji2[0:3]
            if c == 1:
                kimji3 = kimji3[0:3]

        if count == 3:
            kimji1 = kimji1[0:2]
            kimji2 = kimji2[0:2]
            kimji3 = kimji3[0:2]'''

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "<strong>Animation recommender"))
        self.label_title_2.setText(_translate("MainWindow", "    4. 중요하게 생각하는 요소를 선택하세요. (중복 선택 가능)"))
        self.run_button.setText(_translate("MainWindow", "RUN"))
        self.ratio.setText(_translate("MainWindow", "평점"))
        self.num_ratio.setText(_translate("MainWindow", "주인공"))
        self.sexRatio.setText(_translate("MainWindow", "성우"))


from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
