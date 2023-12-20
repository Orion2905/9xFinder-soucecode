# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainvgXcgn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

import resources
#font.setLegacyWeight(75)
#font1.setLegacyWeight(75)
#font2.setLegacyWeight(75)
#font3.setLegacyWeight(75)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u":/UI_ICONS/images/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{border-top-left-radius: 10px;\n"
"	border-top-right-radius: 10px;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"	border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"};\n"
"margin: 0;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(3, 4, 94);;\n"
"}\n"
"QPushButton{\n"
"	background-color:transparent;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/UI_ICONS/images/icons/return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.frame_34 = QFrame(self.frame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_34)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"image:url(:/UI_ICONS/images/icons/logo.png);\n"
"min-height: 30px;\n"
"min-width: 30px;\n"
"padding-right: 15px")

        self.horizontalLayout_13.addWidget(self.label_21)

        self.label_20 = QLabel(self.frame_34)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setLegacyWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_20)


        self.horizontalLayout.addWidget(self.frame_34, 0, Qt.AlignHCenter)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/UI_ICONS/images/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy)
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Pages.setFrameShape(QFrame.StyledPanel)
        self.Pages.setFrameShadow(QFrame.Raised)
        self.LoginPage = QWidget()
        self.LoginPage.setObjectName(u"LoginPage")
        self.verticalLayout_12 = QVBoxLayout(self.LoginPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_33 = QFrame(self.LoginPage)
        self.frame_33.setObjectName(u"frame_33")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_33.sizePolicy().hasHeightForWidth())
        self.frame_33.setSizePolicy(sizePolicy1)
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_33)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(60, 60))
        self.label_18.setMaximumSize(QSize(60, 60))
        self.label_18.setStyleSheet(u"\n"
"image: url(:/UI_ICONS/images/icons/logo.png);")

        self.horizontalLayout_11.addWidget(self.label_18, 0, Qt.AlignRight)

        self.label_19 = QLabel(self.frame_33)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setLegacyWeight(75)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(91, 91, 91);\n"
"padding-left: 20px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_19, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.frame_33, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.LoginPage)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_14)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"QFrame{\n"
"	\n"
"}\n"
"\n"
"QLineEdit{\n"
"	min-width: 300px;\n"
"	min-height: 25px;\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	\n"
"	border-color: rgb(3, 4, 94);\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy1.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy1)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_18)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_18)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setLegacyWeight(75)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy2)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.lineEdit_2 = QLineEdit(self.frame_20)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.pushButton_11 = QPushButton(self.frame_20)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"	border-radius: 10px;\n"
"padding:2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:;\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/UI_ICONS/images/icons/eye-slash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_11)


        self.verticalLayout_17.addWidget(self.frame_20)


        self.verticalLayout_15.addWidget(self.frame_18)


        self.verticalLayout_13.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setFont(font2)
        self.frame_16.setStyleSheet(u"QPushButton{\n"
"	background-color:#023E8A;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ErrorLabel = QLabel(self.frame_16)
        self.ErrorLabel.setObjectName(u"ErrorLabel")
        self.ErrorLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(181, 79, 80);\n"
"border-radius: 4px;\n"
"min-height: 15px;")
        self.ErrorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.ErrorLabel)

        self.pushButton_10 = QPushButton(self.frame_16)
        self.pushButton_10.setObjectName(u"pushButton_10")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setLegacyWeight(75)
        self.pushButton_10.setFont(font4)
        self.pushButton_10.setIconSize(QSize(16, 16))

        self.verticalLayout_14.addWidget(self.pushButton_10)


        self.verticalLayout_13.addWidget(self.frame_16)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.Pages.addWidget(self.LoginPage)
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.verticalLayout_5 = QVBoxLayout(self.HomePage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_9 = QFrame(self.HomePage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet(u"background-image: url(:/UI_ICONS/images/icons/logo.png)")

        self.verticalLayout_6.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	background-color:#00B4D8;\n"
"	padding: 12px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color:rgb(0, 157, 188);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy3.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy3)
        self.pushButton_4.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/UI_ICONS/images/icons/upload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(96, 96))

        self.verticalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignBottom)

        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setLegacyWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)


        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1, Qt.AlignLeft|Qt.AlignBottom)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 119, 182);\n"
"	padding: 12px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(0, 106, 159);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy3.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy3)
        self.pushButton_3.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/UI_ICONS/images/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon5)
        self.pushButton_3.setIconSize(QSize(96, 96))

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_9)

        self.Pages.addWidget(self.HomePage)
        self.ConversionPage = QWidget()
        self.ConversionPage.setObjectName(u"ConversionPage")
        self.verticalLayout_8 = QVBoxLayout(self.ConversionPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 2, -1, 2)
        self.frame_2 = QFrame(self.ConversionPage)
        self.frame_2.setObjectName(u"frame_2")
        font6 = QFont()
        font6.setPointSize(18)
        self.frame_2.setFont(font6)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setMinimumSize(QSize(0, 270))
        self.frame_10.setMaximumSize(QSize(16777215, 300))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        font7 = QFont()
        font7.setBold(True)
        font7.setLegacyWeight(75)
        self.label_14.setFont(font7)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_14)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        sizePolicy4.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy4)
        self.label_6.setMinimumSize(QSize(350, 250))
        self.label_6.setMaximumSize(QSize(350, 250))
        self.label_6.setAcceptDrops(True)
        self.label_6.setStyleSheet(u"image: url(:/UI_ICONS/images/icons/image.png);")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_6, 0, Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.tabWidget_11 = QTabWidget(self.frame_7)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tabWidget_11.setTabPosition(QTabWidget.North)
        self.tabWidget_11.setTabShape(QTabWidget.Rounded)
        self.tabWidget_11.setElideMode(Qt.ElideNone)
        self.tabWidget_11.setUsesScrollButtons(True)
        self.tabWidget_11.setDocumentMode(False)
        self.tabWidget_11.setTabsClosable(False)
        self.tabWidget_11.setMovable(False)
        self.tabWidget_11.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_33 = QVBoxLayout(self.tab)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_46 = QFrame(self.tab)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy1.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy1)
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_46)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.frame_46)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_32.addWidget(self.label_27)


        self.verticalLayout_33.addWidget(self.frame_46)

        self.frame_41 = QFrame(self.tab)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy1.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy1)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_17.setSpacing(3)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_6 = QLineEdit(self.frame_41)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	min-height: 25px;\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	\n"
"	border-color: rgb(3, 4, 94);\n"
"}")
        self.lineEdit_6.setAlignment(Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setClearButtonEnabled(False)

        self.horizontalLayout_17.addWidget(self.lineEdit_6)

        self.pushButton_17 = QPushButton(self.frame_41)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"	border-radius: 10px;\n"
"padding:3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:;\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/UI_ICONS/images/icons/search (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon6)
        self.pushButton_17.setIconSize(QSize(24, 24))

        self.horizontalLayout_17.addWidget(self.pushButton_17)


        self.verticalLayout_33.addWidget(self.frame_41)

        self.frame_11 = QFrame(self.tab)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_35 = QFrame(self.frame_11)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_35)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_14.addWidget(self.label_22, 0, Qt.AlignBottom)


        self.verticalLayout_16.addWidget(self.frame_35)

        self.frame_17 = QFrame(self.frame_11)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: transparent;\n"
"	border-bottom: 1.5px solid rgb(3, 4, 94); \n"
"	border-left: 1.5px solid rgb(3, 4, 94); \n"
"	height: 10px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(2, 62, 138); \n"
"	border: 1.5px solid rgb(2, 62, 138); \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_2 = QSlider(self.frame_17)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setMaximum(12)
        self.horizontalSlider_2.setValue(5)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_15.addWidget(self.horizontalSlider_2)

        self.label_10 = QLabel(self.frame_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_10)


        self.verticalLayout_16.addWidget(self.frame_17)

        self.frame_36 = QFrame(self.frame_11)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.frame_36)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_26.addWidget(self.label_23)

        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: transparent;\n"
"	border-bottom: 1.5px solid rgb(3, 4, 94); \n"
"	border-left: 1.5px solid rgb(3, 4, 94); \n"
"	height: 10px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(2, 62, 138); \n"
"	border: 1.5px solid rgb(2, 62, 138); \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.doubleSpinBox = QDoubleSpinBox(self.frame_37)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        font8.setLegacyWeight(75)
        self.doubleSpinBox.setFont(font8)
        self.doubleSpinBox.setStyleSheet(u"QDoubleSpinBox {\n"
"    min-height: 20px;\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	\n"
"	border-color: rgb(3, 4, 94);\n"
"}")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.100000000000000)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox)


        self.verticalLayout_26.addWidget(self.frame_37)


        self.verticalLayout_16.addWidget(self.frame_36)


        self.verticalLayout_33.addWidget(self.frame_11)

        self.frame_45 = QFrame(self.tab)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy1.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy1)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_19.setSpacing(3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 2, 0)
        self.pushButton_18 = QPushButton(self.frame_45)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font7)
        self.pushButton_18.setStyleSheet(u"QPushButton{\n"
"	background-color:#023E8A;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.pushButton_18.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.pushButton_18)

        self.pushButton_15 = QPushButton(self.frame_45)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy3.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy3)
        self.pushButton_15.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px;\n"
"	background-color: rgb(181, 79, 80);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(171, 74, 76);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(198, 86, 88);\n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/UI_ICONS/images/icons/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.pushButton_15)


        self.verticalLayout_33.addWidget(self.frame_45, 0, Qt.AlignBottom)

        self.tabWidget_11.addTab(self.tab, "")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setEnabled(True)
        self.verticalLayout_4 = QVBoxLayout(self.page1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page1)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 9, 0, 0)
        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_11.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.frame_13)

        self.frame_22 = QFrame(self.page1)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy1.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy1)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.frame_22)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	min-height: 30px;\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	\n"
"	border-color: rgb(3, 4, 94);\n"
"}")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineEdit_3)

        self.pushButton_5 = QPushButton(self.frame_22)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"	border-radius: 10px;\n"
"padding:3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:;\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"")
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_5)


        self.verticalLayout_4.addWidget(self.frame_22)

        self.frame_30 = QFrame(self.page1)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy1.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy1)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_30)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy1.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy1)
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_32)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.frame_32)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setStyleSheet(u"padding-top: 10px")

        self.verticalLayout_25.addWidget(self.label_16)


        self.verticalLayout_24.addWidget(self.frame_32)

        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy1.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy1)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider = QSlider(self.frame_31)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal { \n"
"	background-color: transparent;\n"
"	border-bottom: 1.5px solid rgb(3, 4, 94); \n"
"	border-left: 1.5px solid rgb(3, 4, 94); \n"
"	height: 10px; \n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal { \n"
"	background-color: rgb(2, 62, 138); \n"
"	border: 1.5px solid rgb(2, 62, 138); \n"
"	width: 16px; \n"
"	height: 20px; \n"
"	line-height: 20px; \n"
"	margin-top: -5px; \n"
"	margin-bottom: -5px; \n"
"	border-radius: 10px; \n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover { \n"
"	border-radius: 10px;\n"
"}")
        self.horizontalSlider.setMinimum(5)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(5)
        self.horizontalSlider.setSliderPosition(5)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.horizontalLayout_10.addWidget(self.horizontalSlider)

        self.label_17 = QLabel(self.frame_31)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_17)


        self.verticalLayout_24.addWidget(self.frame_31)


        self.verticalLayout_4.addWidget(self.frame_30)

        self.frame_12 = QFrame(self.page1)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 16, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_12)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	background-color:#023E8A;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        self.pushButton_6.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.verticalLayout_4.addWidget(self.frame_12, 0, Qt.AlignTop)

        self.tabWidget_11.addTab(self.page1, "")

        self.verticalLayout_3.addWidget(self.tabWidget_11)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_8)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_8)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 270))
        self.frame_23.setMaximumSize(QSize(16777215, 300))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_23)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_13)

        self.label_7 = QLabel(self.frame_23)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(350, 250))
        self.label_7.setMaximumSize(QSize(350, 250))
        self.label_7.setStyleSheet(u"image: url(:/UI_ICONS/images/icons/pictures.png);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_7)


        self.verticalLayout_9.addWidget(self.frame_23, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_24 = QFrame(self.frame_8)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_24)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_24)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_23.addWidget(self.label_12)

        self.listWidget = QListWidget(self.frame_24)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(0, 50))
        self.listWidget.setStyleSheet(u"\n"
"QListWidget{\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	border-color: rgb(3, 4, 94);\n"
"	padding:3px;\n"
"	height: 50px;\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: rgb(176, 196, 246);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgb(176, 196, 246);\n"
"	border-radius:5px;\n"
"}\n"
"")
        self.listWidget.setFrameShadow(QFrame.Sunken)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setProperty("isWrapping", False)

        self.verticalLayout_23.addWidget(self.listWidget)

        self.frame_38 = QFrame(self.frame_24)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_18.setSpacing(2)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_16 = QPushButton(self.frame_38)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"	background-color:#023E8A;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	margin-top:2px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")

        self.horizontalLayout_18.addWidget(self.pushButton_16)

        self.pushButton_19 = QPushButton(self.frame_38)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"QPushButton{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	background-color: rgb(181, 79, 80);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(171, 74, 76);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(198, 86, 88);\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.pushButton_19)


        self.verticalLayout_23.addWidget(self.frame_38)


        self.verticalLayout_9.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_8)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy1.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy1)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_25)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_25)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setStyleSheet(u"padding-top: 10px")

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignBottom)

        self.lineEdit_4 = QLineEdit(self.frame_25)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	min-height: 25px;\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	\n"
"	border-color: rgb(3, 4, 94);\n"
"}")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.lineEdit_4)


        self.verticalLayout_9.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_8)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"	border-radius: 10px;\n"
"padding:3px;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(238, 238, 238);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:;\n"
"	background-color: rgb(222, 222, 222);\n"
"}\n"
"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.pushButton_7 = QPushButton(self.frame_26)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon8 = QIcon()
        icon8.addFile(u":/UI_ICONS/images/icons/before.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_26)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon9 = QIcon()
        icon9.addFile(u":/UI_ICONS/images/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon9)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.frame_26)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon10 = QIcon()
        icon10.addFile(u":/UI_ICONS/images/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pushButton_9)


        self.verticalLayout_9.addWidget(self.frame_26)


        self.horizontalLayout_3.addWidget(self.frame_8)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.progressBar_2 = QProgressBar(self.ConversionPage)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setFont(font2)
        self.progressBar_2.setStyleSheet(u"QProgressBar  {\n"
"	color: rgb(2, 62, 138);\n"
"min-height:20px;\n"
"border-bottom-color: rgb(2, 62, 138);\n"
"border-top-color:transparent;\n"
"border-right-color:transparent;\n"
"border-width: 1.5px;\n"
"border-style: solid;\n"
"border-left-color: rgb(2, 62, 138);\n"
"border-radius: 10px;\n"
"padding:1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setValue(0)
        self.progressBar_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.progressBar_2)

        self.Pages.addWidget(self.ConversionPage)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_12 = QHBoxLayout(self.page)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_19 = QFrame(self.page)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.frame_21)
        self.label_15.setObjectName(u"label_15")
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setLegacyWeight(75)
        self.label_15.setFont(font9)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_15)


        self.verticalLayout_18.addWidget(self.frame_21)

        self.frame_27 = QFrame(self.frame_19)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_28)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.listWidget_2 = QListWidget(self.frame_28)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"\n"
"QListWidget{\n"
"	border-radius:10px;\n"
"	border-bottom-width: 1.5px;\n"
"	border-left-width: 1.5px;\n"
"	border-style: solid;\n"
"	border-color: rgb(3, 4, 94);\n"
"	padding:3px;\n"
"}\n"
"\n"
"QListWidget::item:alternate {\n"
"    background: rgb(176, 196, 246);\n"
"}\n"
"\n"
"QListView::item:selected {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background: rgb(55, 157, 241);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgb(176, 196, 246);\n"
"	border-radius:5px;\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.listWidget_2)

        self.pushButton_14 = QPushButton(self.frame_28)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setStyleSheet(u"QPushButton{\n"
"	background-color:#023E8A;\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(5, 8, 179);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/UI_ICONS/images/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon11)
        self.pushButton_14.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.pushButton_14)


        self.horizontalLayout_9.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_29)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.pushButton_12 = QPushButton(self.frame_29)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_12.setAutoFillBackground(False)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"	min-height:130px;\n"
"	min-width:130px;\n"
"	background-color:#00B4D8;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color:rgb(0, 157, 188);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/UI_ICONS/images/icons/add-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon12)
        self.pushButton_12.setIconSize(QSize(32, 32))

        self.verticalLayout_19.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_29)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font2)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"	min-height:130px;\n"
"	min-width:130px;\n"
"	background-color: rgb(0, 119, 182);\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	color: #fff;\n"
"	height: 20px\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(0, 106, 159);\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	background-color:rgb(6, 9, 198);\n"
"}\n"
"\n"
"")
        icon13 = QIcon()
        icon13.addFile(u":/UI_ICONS/images/icons/remove-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon13)
        self.pushButton_13.setIconSize(QSize(32, 32))

        self.verticalLayout_19.addWidget(self.pushButton_13)


        self.horizontalLayout_9.addWidget(self.frame_29, 0, Qt.AlignVCenter)


        self.verticalLayout_18.addWidget(self.frame_27)

        self.progressBar = QProgressBar(self.frame_19)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font2)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar  {\n"
"	color: rgb(2, 62, 138);\n"
"min-height:20px;\n"
"border-bottom-color: rgb(2, 62, 138);\n"
"border-top-color:transparent;\n"
"border-right-color:transparent;\n"
"border-width: 1.5px;\n"
"border-style: solid;\n"
"border-left-color: rgb(2, 62, 138);\n"
"border-radius: 10px;\n"
"padding:1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"	border-radius: 10px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_18.addWidget(self.progressBar)


        self.horizontalLayout_12.addWidget(self.frame_19)

        self.Pages.addWidget(self.page)

        self.verticalLayout.addWidget(self.Pages)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(3, 4, 94);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"9X Finder", None))
        self.pushButton.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.label_21.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"9x Finder", None))
        self.pushButton_2.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.label_18.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"9x Finder", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Activation Key", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.pushButton_11.setText("")
        self.ErrorLabel.setText("")
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(shortcut)
        self.pushButton_10.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IMAGE FINDER", None))
        self.pushButton_4.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_4.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.pushButton_3.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_3.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Search Image", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Upload an image or drag and drop here", None))
        self.label_6.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Selected image", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"your image path here...", None))
        self.pushButton_17.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_17.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Threads", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Starts searching for files", None))
#if QT_CONFIG(shortcut)
        self.pushButton_18.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_15.setText("")
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Image within another image", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Selected image", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"your image path here...", None))
        self.pushButton_5.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_5.setShortcut(QCoreApplication.translate("MainWindow", u"P", None))
#endif // QT_CONFIG(shortcut)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"accuracy", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"5.0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Starts searching for files", None))
#if QT_CONFIG(shortcut)
        self.pushButton_6.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.page1), QCoreApplication.translate("MainWindow", u"Similar Image Finder", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.label_7.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"List of similar images", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Update List", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Clear Stored Data ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Selected image", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"current shown image path here...", None))
        self.pushButton_7.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_7.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_8.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_8.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_9.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton_9.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.progressBar_2.setFormat(QCoreApplication.translate("MainWindow", u"waiting for data", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Update data", None))
#if QT_CONFIG(shortcut)
        self.pushButton_14.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Add URL", None))
#if QT_CONFIG(shortcut)
        self.pushButton_12.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Remove URL", None))
#if QT_CONFIG(shortcut)
        self.pushButton_13.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.progressBar.setFormat("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"9x Finder \u00a9 2023", None))
    # retranslateUi

