# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WndMain.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import src.views.icons.rc_icons

class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(1000, 582)
        WndMain.setMinimumSize(QSize(664, 0))
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.centralwidget)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setMinimumSize(QSize(0, 40))
        self.topBar.setMaximumSize(QSize(16777215, 40))
        self.topBar.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none;\n"
"")
        self.topBar.setFrameShape(QFrame.NoFrame)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.topBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle = QFrame(self.topBar)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMaximumSize(QSize(60, 40))
        self.toggle.setStyleSheet(u"background-color: rgb(65, 43, 173);")
        self.toggle.setFrameShape(QFrame.StyledPanel)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.toggle)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnToggle = QPushButton(self.toggle)
        self.btnToggle.setObjectName(u"btnToggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnToggle.sizePolicy().hasHeightForWidth())
        self.btnToggle.setSizePolicy(sizePolicy)
        self.btnToggle.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-color: rgb(122, 100, 189);\n"
"background-image: url(:/icons/toggleIcon.png);\n"
"background-repeat:none;\n"
"background-position: center center;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.btnToggle)


        self.horizontalLayout.addWidget(self.toggle)

        self.description = QFrame(self.topBar)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"border:none;\n"
"")
        self.description.setFrameShape(QFrame.StyledPanel)
        self.description.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.description)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frName = QFrame(self.description)
        self.frName.setObjectName(u"frName")
        self.frName.setFrameShape(QFrame.StyledPanel)
        self.frName.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frName)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbName = QLabel(self.frName)
        self.lbName.setObjectName(u"lbName")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbName.setFont(font)

        self.horizontalLayout_6.addWidget(self.lbName)


        self.horizontalLayout_5.addWidget(self.frName)

        self.frDate = QFrame(self.description)
        self.frDate.setObjectName(u"frDate")
        self.frDate.setFrameShape(QFrame.StyledPanel)
        self.frDate.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frDate)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbDate = QLabel(self.frDate)
        self.lbDate.setObjectName(u"lbDate")
        self.lbDate.setFont(font)
        self.lbDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.lbDate)


        self.horizontalLayout_5.addWidget(self.frDate)

        self.frPageDescription = QFrame(self.description)
        self.frPageDescription.setObjectName(u"frPageDescription")
        self.frPageDescription.setFrameShape(QFrame.StyledPanel)
        self.frPageDescription.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frPageDescription)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbPageDescription = QLabel(self.frPageDescription)
        self.lbPageDescription.setObjectName(u"lbPageDescription")
        self.lbPageDescription.setFont(font)
        self.lbPageDescription.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbPageDescription.setMargin(5)

        self.horizontalLayout_8.addWidget(self.lbPageDescription)


        self.horizontalLayout_5.addWidget(self.frPageDescription)


        self.horizontalLayout.addWidget(self.description)


        self.verticalLayout.addWidget(self.topBar)

        self.mainWidget = QFrame(self.centralwidget)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setFrameShape(QFrame.NoFrame)
        self.mainWidget.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.leftMenu = QFrame(self.mainWidget)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(60, 0))
        self.leftMenu.setMaximumSize(QSize(60, 16777215))
        self.leftMenu.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border:none\n"
"")
        self.leftMenu.setFrameShape(QFrame.StyledPanel)
        self.leftMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.leftMenu)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.StyledPanel)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topMenus)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnHome = QPushButton(self.topMenus)
        self.btnHome.setObjectName(u"btnHome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnHome.sizePolicy().hasHeightForWidth())
        self.btnHome.setSizePolicy(sizePolicy1)
        self.btnHome.setMinimumSize(QSize(60, 40))
        self.btnHome.setFont(font)
        self.btnHome.setLayoutDirection(Qt.LeftToRight)
        self.btnHome.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/homeIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}\n"
"\n"
"")
        self.btnHome.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnHome)

        self.btnFood = QPushButton(self.topMenus)
        self.btnFood.setObjectName(u"btnFood")
        self.btnFood.setMinimumSize(QSize(0, 40))
        self.btnFood.setFont(font)
        self.btnFood.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/food.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnFood.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnFood)

        self.btnStatistic = QPushButton(self.topMenus)
        self.btnStatistic.setObjectName(u"btnStatistic")
        self.btnStatistic.setMinimumSize(QSize(0, 40))
        self.btnStatistic.setFont(font)
        self.btnStatistic.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/statisticIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnStatistic.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnStatistic)

        self.btnSettings = QPushButton(self.topMenus)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setMinimumSize(QSize(0, 40))
        self.btnSettings.setFont(font)
        self.btnSettings.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/settingsIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnSettings.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnSettings)

        self.btnCalendar = QPushButton(self.topMenus)
        self.btnCalendar.setObjectName(u"btnCalendar")
        self.btnCalendar.setMinimumSize(QSize(0, 40))
        self.btnCalendar.setFont(font)
        self.btnCalendar.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/calemdarIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnCalendar.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.btnCalendar)


        self.verticalLayout_2.addWidget(self.topMenus, 0, Qt.AlignTop)

        self.bottonMenus = QFrame(self.leftMenu)
        self.bottonMenus.setObjectName(u"bottonMenus")
        self.bottonMenus.setFrameShape(QFrame.StyledPanel)
        self.bottonMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bottonMenus)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btnLogout = QPushButton(self.bottonMenus)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setMinimumSize(QSize(0, 40))
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/logoutIcon.png);\n"
"background-position: left center;\n"
"background-repeat: no-repeat;\n"
"border: none;\n"
"border-left: 14px solid rgb(155, 127, 240);\n"
"text-align: left;\n"
"padding-left: 45px;\n"
"background-color: rgb(155, 127, 240);\n"
"\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-left: 14px solid rgb(122, 100, 189);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"    border-left: 14px solid rgb(211, 201, 242);\n"
"}")
        self.btnLogout.setIconSize(QSize(25, 25))

        self.verticalLayout_6.addWidget(self.btnLogout)


        self.verticalLayout_2.addWidget(self.bottonMenus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.content = QFrame(self.mainWidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.content)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.pageHome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(143, 126, 230);\n"
"border:none;\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.pageHome)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.topContent = QFrame(self.pageHome)
        self.topContent.setObjectName(u"topContent")
        self.topContent.setMaximumSize(QSize(16777215, 260))
        self.topContent.setFrameShape(QFrame.StyledPanel)
        self.topContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.topContent)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.topContent)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame)

        self.frmProgressBar = QFrame(self.topContent)
        self.frmProgressBar.setObjectName(u"frmProgressBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frmProgressBar.sizePolicy().hasHeightForWidth())
        self.frmProgressBar.setSizePolicy(sizePolicy2)
        self.frmProgressBar.setMinimumSize(QSize(260, 0))
        self.frmProgressBar.setMaximumSize(QSize(16777215, 260))
        font1 = QFont()
        font1.setFamilies([u"Script"])
        self.frmProgressBar.setFont(font1)
        self.frmProgressBar.setFrameShape(QFrame.StyledPanel)
        self.frmProgressBar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frmProgressBar)

        self.frame_3 = QFrame(self.topContent)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.topContent)

        self.bottemContent = QFrame(self.pageHome)
        self.bottemContent.setObjectName(u"bottemContent")
        self.bottemContent.setFrameShape(QFrame.StyledPanel)
        self.bottemContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.bottemContent)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 5)
        self.trackContent = QFrame(self.bottemContent)
        self.trackContent.setObjectName(u"trackContent")
        self.trackContent.setFrameShape(QFrame.StyledPanel)
        self.trackContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.trackContent)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.weightContent = QFrame(self.trackContent)
        self.weightContent.setObjectName(u"weightContent")
        self.weightContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.weightContent.setFrameShape(QFrame.StyledPanel)
        self.weightContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.weightContent)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbWeight = QLabel(self.weightContent)
        self.lbWeight.setObjectName(u"lbWeight")
        self.lbWeight.setFont(font)

        self.horizontalLayout_4.addWidget(self.lbWeight)

        self.leWeight = QLineEdit(self.weightContent)
        self.leWeight.setObjectName(u"leWeight")
        self.leWeight.setMaximumSize(QSize(200, 16777215))
        self.leWeight.setFont(font)
        self.leWeight.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.leWeight)


        self.verticalLayout_9.addWidget(self.weightContent)

        self.stepContent = QFrame(self.trackContent)
        self.stepContent.setObjectName(u"stepContent")
        self.stepContent.setFont(font)
        self.stepContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.stepContent.setFrameShape(QFrame.StyledPanel)
        self.stepContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.stepContent)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbSteps = QLabel(self.stepContent)
        self.lbSteps.setObjectName(u"lbSteps")
        self.lbSteps.setFont(font)
        self.lbSteps.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.lbSteps)

        self.leSteps = QLineEdit(self.stepContent)
        self.leSteps.setObjectName(u"leSteps")
        self.leSteps.setMaximumSize(QSize(200, 16777215))
        self.leSteps.setFont(font)
        self.leSteps.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leSteps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.leSteps)


        self.verticalLayout_9.addWidget(self.stepContent)

        self.bpContent = QFrame(self.trackContent)
        self.bpContent.setObjectName(u"bpContent")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bpContent.sizePolicy().hasHeightForWidth())
        self.bpContent.setSizePolicy(sizePolicy3)
        self.bpContent.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.bpContent.setFrameShape(QFrame.StyledPanel)
        self.bpContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.bpContent)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbBP = QLabel(self.bpContent)
        self.lbBP.setObjectName(u"lbBP")
        self.lbBP.setFont(font)

        self.horizontalLayout_10.addWidget(self.lbBP)

        self.leBPLow = QLineEdit(self.bpContent)
        self.leBPLow.setObjectName(u"leBPLow")
        self.leBPLow.setMaximumSize(QSize(94, 16777215))
        self.leBPLow.setFont(font)
        self.leBPLow.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leBPLow.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.leBPLow)

        self.leBPHigh = QLineEdit(self.bpContent)
        self.leBPHigh.setObjectName(u"leBPHigh")
        self.leBPHigh.setMaximumSize(QSize(100, 16777215))
        self.leBPHigh.setFont(font)
        self.leBPHigh.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leBPHigh.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.leBPHigh)


        self.verticalLayout_9.addWidget(self.bpContent)


        self.verticalLayout_7.addWidget(self.trackContent)

        self.frmButtonSubmit = QFrame(self.bottemContent)
        self.frmButtonSubmit.setObjectName(u"frmButtonSubmit")
        self.frmButtonSubmit.setMaximumSize(QSize(16777215, 40))
        self.frmButtonSubmit.setFrameShape(QFrame.StyledPanel)
        self.frmButtonSubmit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frmButtonSubmit)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bufferLeft = QFrame(self.frmButtonSubmit)
        self.bufferLeft.setObjectName(u"bufferLeft")
        self.bufferLeft.setMinimumSize(QSize(0, 0))
        self.bufferLeft.setFrameShape(QFrame.StyledPanel)
        self.bufferLeft.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.bufferLeft)

        self.frmBtn = QFrame(self.frmButtonSubmit)
        self.frmBtn.setObjectName(u"frmBtn")
        self.frmBtn.setMinimumSize(QSize(140, 0))
        self.frmBtn.setMaximumSize(QSize(140, 16777215))
        self.frmBtn.setFrameShape(QFrame.StyledPanel)
        self.frmBtn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frmBtn)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnSubmit = QPushButton(self.frmBtn)
        self.btnSubmit.setObjectName(u"btnSubmit")
        sizePolicy1.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy1)
        self.btnSubmit.setMinimumSize(QSize(140, 40))
        self.btnSubmit.setMaximumSize(QSize(140, 140))
        self.btnSubmit.setFont(font)
        self.btnSubmit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.verticalLayout_8.addWidget(self.btnSubmit)


        self.horizontalLayout_11.addWidget(self.frmBtn)

        self.bufferRight = QFrame(self.frmButtonSubmit)
        self.bufferRight.setObjectName(u"bufferRight")
        self.bufferRight.setMinimumSize(QSize(0, 0))
        self.bufferRight.setFrameShape(QFrame.StyledPanel)
        self.bufferRight.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.bufferRight)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 371, 21))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.bufferRight)


        self.verticalLayout_7.addWidget(self.frmButtonSubmit)


        self.verticalLayout_5.addWidget(self.bottemContent)

        self.pages.addWidget(self.pageHome)
        self.pageFood = QWidget()
        self.pageFood.setObjectName(u"pageFood")
        self.horizontalLayout_13 = QHBoxLayout(self.pageFood)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frmContentFood = QFrame(self.pageFood)
        self.frmContentFood.setObjectName(u"frmContentFood")
        self.frmContentFood.setFrameShape(QFrame.StyledPanel)
        self.frmContentFood.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frmContentFood)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frmSearchbar = QFrame(self.frmContentFood)
        self.frmSearchbar.setObjectName(u"frmSearchbar")
        self.frmSearchbar.setMinimumSize(QSize(0, 50))
        self.frmSearchbar.setMaximumSize(QSize(16777215, 50))
        self.frmSearchbar.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmSearchbar.setFrameShape(QFrame.StyledPanel)
        self.frmSearchbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frmSearchbar)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lbSearchFood = QLabel(self.frmSearchbar)
        self.lbSearchFood.setObjectName(u"lbSearchFood")
        self.lbSearchFood.setFont(font)

        self.horizontalLayout_23.addWidget(self.lbSearchFood)

        self.leSearchFood = QLineEdit(self.frmSearchbar)
        self.leSearchFood.setObjectName(u"leSearchFood")
        self.leSearchFood.setFont(font)
        self.leSearchFood.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.horizontalLayout_23.addWidget(self.leSearchFood)

        self.btnSearchFood = QPushButton(self.frmSearchbar)
        self.btnSearchFood.setObjectName(u"btnSearchFood")
        sizePolicy1.setHeightForWidth(self.btnSearchFood.sizePolicy().hasHeightForWidth())
        self.btnSearchFood.setSizePolicy(sizePolicy1)
        self.btnSearchFood.setMinimumSize(QSize(140, 0))
        self.btnSearchFood.setMaximumSize(QSize(140, 40))
        self.btnSearchFood.setFont(font)
        self.btnSearchFood.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px ;\n"
"	border: 3px solid rgb(122, 100, 189);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_23.addWidget(self.btnSearchFood)


        self.verticalLayout_10.addWidget(self.frmSearchbar)

        self.frmfoodTbl = QFrame(self.frmContentFood)
        self.frmfoodTbl.setObjectName(u"frmfoodTbl")
        self.frmfoodTbl.setMaximumSize(QSize(16777215, 16777215))
        self.frmfoodTbl.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmfoodTbl.setFrameShape(QFrame.StyledPanel)
        self.frmfoodTbl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frmfoodTbl)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.tbFood = QTableWidget(self.frmfoodTbl)
        if (self.tbFood.columnCount() < 2):
            self.tbFood.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbFood.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbFood.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbFood.setObjectName(u"tbFood")
        self.tbFood.setFont(font2)
        self.tbFood.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.tbFood)


        self.verticalLayout_10.addWidget(self.frmfoodTbl)


        self.horizontalLayout_13.addWidget(self.frmContentFood)

        self.frmContorlAdmin = QFrame(self.pageFood)
        self.frmContorlAdmin.setObjectName(u"frmContorlAdmin")
        self.frmContorlAdmin.setMinimumSize(QSize(250, 0))
        self.frmContorlAdmin.setMaximumSize(QSize(250, 16777215))
        self.frmContorlAdmin.setFrameShape(QFrame.StyledPanel)
        self.frmContorlAdmin.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frmContorlAdmin)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bufferTop = QFrame(self.frmContorlAdmin)
        self.bufferTop.setObjectName(u"bufferTop")
        self.bufferTop.setFrameShape(QFrame.StyledPanel)
        self.bufferTop.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.bufferTop)

        self.frmControlBtns = QFrame(self.frmContorlAdmin)
        self.frmControlBtns.setObjectName(u"frmControlBtns")
        self.frmControlBtns.setFrameShape(QFrame.StyledPanel)
        self.frmControlBtns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frmControlBtns)
        self.verticalLayout_42.setSpacing(5)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 9, 0)
        self.frame_45 = QFrame(self.frmControlBtns)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(0, 150))
        self.frame_45.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_45)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.lbAmount = QLabel(self.frame_45)
        self.lbAmount.setObjectName(u"lbAmount")
        self.lbAmount.setMinimumSize(QSize(0, 0))
        self.lbAmount.setMaximumSize(QSize(16777215, 40))
        self.lbAmount.setFont(font)

        self.verticalLayout_43.addWidget(self.lbAmount)

        self.leCalories = QLineEdit(self.frame_45)
        self.leCalories.setObjectName(u"leCalories")
        font3 = QFont()
        font3.setBold(True)
        font3.setUnderline(False)
        self.leCalories.setFont(font3)
        self.leCalories.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.verticalLayout_43.addWidget(self.leCalories)

        self.label_2 = QLabel(self.frame_45)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_43.addWidget(self.label_2)

        self.leAmount = QLineEdit(self.frame_45)
        self.leAmount.setObjectName(u"leAmount")
        self.leAmount.setFont(font)
        self.leAmount.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);")

        self.verticalLayout_43.addWidget(self.leAmount)


        self.verticalLayout_42.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frmControlBtns)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_48.addWidget(self.frame_47)

        self.btnAddFood = QPushButton(self.frame_46)
        self.btnAddFood.setObjectName(u"btnAddFood")
        sizePolicy1.setHeightForWidth(self.btnAddFood.sizePolicy().hasHeightForWidth())
        self.btnAddFood.setSizePolicy(sizePolicy1)
        self.btnAddFood.setMinimumSize(QSize(140, 40))
        self.btnAddFood.setMaximumSize(QSize(140, 40))
        self.btnAddFood.setFont(font)
        self.btnAddFood.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_48.addWidget(self.btnAddFood)

        self.frame_48 = QFrame(self.frame_46)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_48.addWidget(self.frame_48)


        self.verticalLayout_42.addWidget(self.frame_46)


        self.verticalLayout_11.addWidget(self.frmControlBtns)

        self.bufferBottom = QFrame(self.frmContorlAdmin)
        self.bufferBottom.setObjectName(u"bufferBottom")
        self.bufferBottom.setFrameShape(QFrame.StyledPanel)
        self.bufferBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.bufferBottom)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.lbFoodAdded = QLabel(self.bufferBottom)
        self.lbFoodAdded.setObjectName(u"lbFoodAdded")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.lbFoodAdded.setFont(font4)
        self.lbFoodAdded.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.lbFoodAdded, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.bufferBottom)


        self.horizontalLayout_13.addWidget(self.frmContorlAdmin)

        self.pages.addWidget(self.pageFood)
        self.pageStatKcal = QWidget()
        self.pageStatKcal.setObjectName(u"pageStatKcal")
        self.verticalLayout_13 = QVBoxLayout(self.pageStatKcal)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentKcal = QFrame(self.pageStatKcal)
        self.frmTopContentKcal.setObjectName(u"frmTopContentKcal")
        self.frmTopContentKcal.setMinimumSize(QSize(0, 0))
        self.frmTopContentKcal.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frmTopContentKcal)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat1 = QFrame(self.frmTopContentKcal)
        self.frmTopLeftStat1.setObjectName(u"frmTopLeftStat1")
        self.frmTopLeftStat1.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frmTopLeftStat1)

        self.frmTopBtnKcal = QFrame(self.frmTopContentKcal)
        self.frmTopBtnKcal.setObjectName(u"frmTopBtnKcal")
        self.frmTopBtnKcal.setMinimumSize(QSize(664, 50))
        self.frmTopBtnKcal.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frmTopBtnKcal)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btnKcal1 = QPushButton(self.frmTopBtnKcal)
        self.btnKcal1.setObjectName(u"btnKcal1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnKcal1.sizePolicy().hasHeightForWidth())
        self.btnKcal1.setSizePolicy(sizePolicy4)
        self.btnKcal1.setFont(font)
        self.btnKcal1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnKcal1)

        self.btnSteps1 = QPushButton(self.frmTopBtnKcal)
        self.btnSteps1.setObjectName(u"btnSteps1")
        sizePolicy4.setHeightForWidth(self.btnSteps1.sizePolicy().hasHeightForWidth())
        self.btnSteps1.setSizePolicy(sizePolicy4)
        self.btnSteps1.setFont(font)
        self.btnSteps1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnSteps1)

        self.btnBP1 = QPushButton(self.frmTopBtnKcal)
        self.btnBP1.setObjectName(u"btnBP1")
        sizePolicy4.setHeightForWidth(self.btnBP1.sizePolicy().hasHeightForWidth())
        self.btnBP1.setSizePolicy(sizePolicy4)
        self.btnBP1.setFont(font)
        self.btnBP1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnBP1)

        self.btnWeight1 = QPushButton(self.frmTopBtnKcal)
        self.btnWeight1.setObjectName(u"btnWeight1")
        sizePolicy4.setHeightForWidth(self.btnWeight1.sizePolicy().hasHeightForWidth())
        self.btnWeight1.setSizePolicy(sizePolicy4)
        self.btnWeight1.setFont(font)
        self.btnWeight1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_15.addWidget(self.btnWeight1)


        self.horizontalLayout_14.addWidget(self.frmTopBtnKcal)

        self.frmTopRightStat1 = QFrame(self.frmTopContentKcal)
        self.frmTopRightStat1.setObjectName(u"frmTopRightStat1")
        self.frmTopRightStat1.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.frmTopRightStat1)


        self.verticalLayout_13.addWidget(self.frmTopContentKcal)

        self.frmContentKcal = QFrame(self.pageStatKcal)
        self.frmContentKcal.setObjectName(u"frmContentKcal")
        self.frmContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmContentKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frmContentKcal)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentKcal = QFrame(self.frmContentKcal)
        self.frmLeftContentKcal.setObjectName(u"frmLeftContentKcal")
        self.frmLeftContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentKcal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frmLeftContentKcal)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frmLeftContentKcal)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_2)

        self.frame_11 = QFrame(self.frmLeftContentKcal)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 200))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setSpacing(9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frmAvgKcal = QFrame(self.frame_11)
        self.frmAvgKcal.setObjectName(u"frmAvgKcal")
        self.frmAvgKcal.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmAvgKcal.setFrameShape(QFrame.StyledPanel)
        self.frmAvgKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frmAvgKcal)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lbAvgKcal = QLabel(self.frmAvgKcal)
        self.lbAvgKcal.setObjectName(u"lbAvgKcal")
        self.lbAvgKcal.setFont(font)

        self.horizontalLayout_32.addWidget(self.lbAvgKcal)

        self.lbAvgKcalValue = QLabel(self.frmAvgKcal)
        self.lbAvgKcalValue.setObjectName(u"lbAvgKcalValue")
        self.lbAvgKcalValue.setFont(font)
        self.lbAvgKcalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.lbAvgKcalValue)


        self.verticalLayout_21.addWidget(self.frmAvgKcal)

        self.frmMaxKcal = QFrame(self.frame_11)
        self.frmMaxKcal.setObjectName(u"frmMaxKcal")
        self.frmMaxKcal.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMaxKcal.setFrameShape(QFrame.StyledPanel)
        self.frmMaxKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frmMaxKcal)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lbMaxKcal = QLabel(self.frmMaxKcal)
        self.lbMaxKcal.setObjectName(u"lbMaxKcal")
        self.lbMaxKcal.setFont(font)

        self.horizontalLayout_33.addWidget(self.lbMaxKcal)

        self.lbMaxKcalValue = QLabel(self.frmMaxKcal)
        self.lbMaxKcalValue.setObjectName(u"lbMaxKcalValue")
        self.lbMaxKcalValue.setFont(font)
        self.lbMaxKcalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.lbMaxKcalValue)


        self.verticalLayout_21.addWidget(self.frmMaxKcal)

        self.frmMinKcal = QFrame(self.frame_11)
        self.frmMinKcal.setObjectName(u"frmMinKcal")
        self.frmMinKcal.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMinKcal.setFrameShape(QFrame.StyledPanel)
        self.frmMinKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frmMinKcal)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.lbMinKcal = QLabel(self.frmMinKcal)
        self.lbMinKcal.setObjectName(u"lbMinKcal")
        self.lbMinKcal.setFont(font)

        self.horizontalLayout_34.addWidget(self.lbMinKcal)

        self.lbMinKcalValue = QLabel(self.frmMinKcal)
        self.lbMinKcalValue.setObjectName(u"lbMinKcalValue")
        self.lbMinKcalValue.setFont(font)
        self.lbMinKcalValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_34.addWidget(self.lbMinKcalValue)


        self.verticalLayout_21.addWidget(self.frmMinKcal)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.frame_6 = QFrame(self.frmLeftContentKcal)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_6)


        self.horizontalLayout_16.addWidget(self.frmLeftContentKcal)

        self.frmRightContentKcal = QFrame(self.frmContentKcal)
        self.frmRightContentKcal.setObjectName(u"frmRightContentKcal")
        self.frmRightContentKcal.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentKcal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frmRightContentKcal)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.kcalChart = QFrame(self.frmRightContentKcal)
        self.kcalChart.setObjectName(u"kcalChart")
        self.kcalChart.setFrameShape(QFrame.StyledPanel)
        self.kcalChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.kcalChart)

        self.frmChartSelectionKcal = QFrame(self.frmRightContentKcal)
        self.frmChartSelectionKcal.setObjectName(u"frmChartSelectionKcal")
        self.frmChartSelectionKcal.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionKcal.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frmChartSelectionKcal)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, -1, 0)
        self.frame_4 = QFrame(self.frmChartSelectionKcal)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(100, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_4)

        self.frmSelectionBtnKcal = QFrame(self.frmChartSelectionKcal)
        self.frmSelectionBtnKcal.setObjectName(u"frmSelectionBtnKcal")
        self.frmSelectionBtnKcal.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnKcal.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnKcal.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnKcal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frmSelectionBtnKcal)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lbSelectionKcal = QLabel(self.frmSelectionBtnKcal)
        self.lbSelectionKcal.setObjectName(u"lbSelectionKcal")
        self.lbSelectionKcal.setFont(font)

        self.horizontalLayout_22.addWidget(self.lbSelectionKcal)

        self.cbKcal = QComboBox(self.frmSelectionBtnKcal)
        self.cbKcal.addItem("")
        self.cbKcal.addItem("")
        self.cbKcal.addItem("")
        self.cbKcal.setObjectName(u"cbKcal")
        self.cbKcal.setMinimumSize(QSize(120, 0))
        self.cbKcal.setMaximumSize(QSize(120, 16777215))
        self.cbKcal.setFont(font)
        self.cbKcal.setStyleSheet(u"")
        self.cbKcal.setEditable(False)
        self.cbKcal.setMaxCount(2147483645)

        self.horizontalLayout_22.addWidget(self.cbKcal)


        self.horizontalLayout_17.addWidget(self.frmSelectionBtnKcal)

        self.frame_5 = QFrame(self.frmChartSelectionKcal)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_5)


        self.verticalLayout_16.addWidget(self.frmChartSelectionKcal)


        self.horizontalLayout_16.addWidget(self.frmRightContentKcal)


        self.verticalLayout_13.addWidget(self.frmContentKcal)

        self.pages.addWidget(self.pageStatKcal)
        self.pageStatSteps = QWidget()
        self.pageStatSteps.setObjectName(u"pageStatSteps")
        self.verticalLayout_15 = QVBoxLayout(self.pageStatSteps)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentSteps = QFrame(self.pageStatSteps)
        self.frmTopContentSteps.setObjectName(u"frmTopContentSteps")
        self.frmTopContentSteps.setMinimumSize(QSize(500, 50))
        self.frmTopContentSteps.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frmTopContentSteps)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat2 = QFrame(self.frmTopContentSteps)
        self.frmTopLeftStat2.setObjectName(u"frmTopLeftStat2")
        self.frmTopLeftStat2.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frmTopLeftStat2)

        self.frmTopBtnSteps = QFrame(self.frmTopContentSteps)
        self.frmTopBtnSteps.setObjectName(u"frmTopBtnSteps")
        self.frmTopBtnSteps.setMinimumSize(QSize(664, 50))
        self.frmTopBtnSteps.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frmTopBtnSteps)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.btnKcal2 = QPushButton(self.frmTopBtnSteps)
        self.btnKcal2.setObjectName(u"btnKcal2")
        sizePolicy4.setHeightForWidth(self.btnKcal2.sizePolicy().hasHeightForWidth())
        self.btnKcal2.setSizePolicy(sizePolicy4)
        self.btnKcal2.setFont(font)
        self.btnKcal2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnKcal2)

        self.btnSteps2 = QPushButton(self.frmTopBtnSteps)
        self.btnSteps2.setObjectName(u"btnSteps2")
        sizePolicy4.setHeightForWidth(self.btnSteps2.sizePolicy().hasHeightForWidth())
        self.btnSteps2.setSizePolicy(sizePolicy4)
        self.btnSteps2.setFont(font)
        self.btnSteps2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnSteps2)

        self.btnBP2 = QPushButton(self.frmTopBtnSteps)
        self.btnBP2.setObjectName(u"btnBP2")
        sizePolicy4.setHeightForWidth(self.btnBP2.sizePolicy().hasHeightForWidth())
        self.btnBP2.setSizePolicy(sizePolicy4)
        self.btnBP2.setFont(font)
        self.btnBP2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnBP2)

        self.btnWeight2 = QPushButton(self.frmTopBtnSteps)
        self.btnWeight2.setObjectName(u"btnWeight2")
        sizePolicy4.setHeightForWidth(self.btnWeight2.sizePolicy().hasHeightForWidth())
        self.btnWeight2.setSizePolicy(sizePolicy4)
        self.btnWeight2.setFont(font)
        self.btnWeight2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.btnWeight2)


        self.horizontalLayout_20.addWidget(self.frmTopBtnSteps)

        self.frmTopRightStat2 = QFrame(self.frmTopContentSteps)
        self.frmTopRightStat2.setObjectName(u"frmTopRightStat2")
        self.frmTopRightStat2.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frmTopRightStat2)


        self.verticalLayout_15.addWidget(self.frmTopContentSteps)

        self.frmContentSteps = QFrame(self.pageStatSteps)
        self.frmContentSteps.setObjectName(u"frmContentSteps")
        self.frmContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmContentSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frmContentSteps)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentSteps = QFrame(self.frmContentSteps)
        self.frmLeftContentSteps.setObjectName(u"frmLeftContentSteps")
        self.frmLeftContentSteps.setMinimumSize(QSize(456, 0))
        self.frmLeftContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentSteps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frmLeftContentSteps)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frmLeftContentSteps)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_27)

        self.frame_16 = QFrame(self.frmLeftContentSteps)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 200))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_16)
        self.verticalLayout_22.setSpacing(9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frmAvgSteps = QFrame(self.frame_16)
        self.frmAvgSteps.setObjectName(u"frmAvgSteps")
        self.frmAvgSteps.setMinimumSize(QSize(448, 0))
        self.frmAvgSteps.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmAvgSteps.setFrameShape(QFrame.StyledPanel)
        self.frmAvgSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frmAvgSteps)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.lbAvgSteps = QLabel(self.frmAvgSteps)
        self.lbAvgSteps.setObjectName(u"lbAvgSteps")
        self.lbAvgSteps.setFont(font)

        self.horizontalLayout_35.addWidget(self.lbAvgSteps)

        self.lbAvgStepsValue = QLabel(self.frmAvgSteps)
        self.lbAvgStepsValue.setObjectName(u"lbAvgStepsValue")
        self.lbAvgStepsValue.setFont(font)
        self.lbAvgStepsValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.lbAvgStepsValue)


        self.verticalLayout_22.addWidget(self.frmAvgSteps)

        self.frmMaxSteps = QFrame(self.frame_16)
        self.frmMaxSteps.setObjectName(u"frmMaxSteps")
        self.frmMaxSteps.setMinimumSize(QSize(448, 0))
        self.frmMaxSteps.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMaxSteps.setFrameShape(QFrame.StyledPanel)
        self.frmMaxSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frmMaxSteps)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.lbMaxSteps = QLabel(self.frmMaxSteps)
        self.lbMaxSteps.setObjectName(u"lbMaxSteps")
        self.lbMaxSteps.setFont(font)

        self.horizontalLayout_36.addWidget(self.lbMaxSteps)

        self.lbMaxStepsValue = QLabel(self.frmMaxSteps)
        self.lbMaxStepsValue.setObjectName(u"lbMaxStepsValue")
        self.lbMaxStepsValue.setFont(font)
        self.lbMaxStepsValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.lbMaxStepsValue)


        self.verticalLayout_22.addWidget(self.frmMaxSteps)

        self.frmMinSteps = QFrame(self.frame_16)
        self.frmMinSteps.setObjectName(u"frmMinSteps")
        self.frmMinSteps.setMinimumSize(QSize(448, 0))
        self.frmMinSteps.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMinSteps.setFrameShape(QFrame.StyledPanel)
        self.frmMinSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frmMinSteps)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.lbMinSteps = QLabel(self.frmMinSteps)
        self.lbMinSteps.setObjectName(u"lbMinSteps")
        self.lbMinSteps.setFont(font)

        self.horizontalLayout_37.addWidget(self.lbMinSteps)

        self.lbMinStepsValue = QLabel(self.frmMinSteps)
        self.lbMinStepsValue.setObjectName(u"lbMinStepsValue")
        self.lbMinStepsValue.setFont(font)
        self.lbMinStepsValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.lbMinStepsValue)


        self.verticalLayout_22.addWidget(self.frmMinSteps)


        self.verticalLayout_24.addWidget(self.frame_16)

        self.frame_28 = QFrame(self.frmLeftContentSteps)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_28)


        self.horizontalLayout_26.addWidget(self.frmLeftContentSteps)

        self.frmRightContentSteps = QFrame(self.frmContentSteps)
        self.frmRightContentSteps.setObjectName(u"frmRightContentSteps")
        self.frmRightContentSteps.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentSteps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frmRightContentSteps)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.stepsChart = QFrame(self.frmRightContentSteps)
        self.stepsChart.setObjectName(u"stepsChart")
        self.stepsChart.setFrameShape(QFrame.StyledPanel)
        self.stepsChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_18.addWidget(self.stepsChart)

        self.frmChartSelectionSteps = QFrame(self.frmRightContentSteps)
        self.frmChartSelectionSteps.setObjectName(u"frmChartSelectionSteps")
        self.frmChartSelectionSteps.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionSteps.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frmChartSelectionSteps)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 9, 0)
        self.frame_15 = QFrame(self.frmChartSelectionSteps)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(100, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_15)

        self.frmSelectionBtnSteps = QFrame(self.frmChartSelectionSteps)
        self.frmSelectionBtnSteps.setObjectName(u"frmSelectionBtnSteps")
        self.frmSelectionBtnSteps.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnSteps.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnSteps.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnSteps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frmSelectionBtnSteps)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lbSelectionSteps = QLabel(self.frmSelectionBtnSteps)
        self.lbSelectionSteps.setObjectName(u"lbSelectionSteps")
        self.lbSelectionSteps.setFont(font)

        self.horizontalLayout_27.addWidget(self.lbSelectionSteps)

        self.cbSteps = QComboBox(self.frmSelectionBtnSteps)
        self.cbSteps.addItem("")
        self.cbSteps.addItem("")
        self.cbSteps.addItem("")
        self.cbSteps.setObjectName(u"cbSteps")
        self.cbSteps.setMinimumSize(QSize(120, 0))
        self.cbSteps.setMaximumSize(QSize(120, 16777215))
        self.cbSteps.setFont(font)
        self.cbSteps.setStyleSheet(u"")
        self.cbSteps.setEditable(False)
        self.cbSteps.setMaxCount(2147483645)

        self.horizontalLayout_27.addWidget(self.cbSteps)


        self.horizontalLayout_28.addWidget(self.frmSelectionBtnSteps)

        self.frame_17 = QFrame(self.frmChartSelectionSteps)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(100, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_28.addWidget(self.frame_17)


        self.verticalLayout_18.addWidget(self.frmChartSelectionSteps)


        self.horizontalLayout_26.addWidget(self.frmRightContentSteps)


        self.verticalLayout_15.addWidget(self.frmContentSteps)

        self.pages.addWidget(self.pageStatSteps)
        self.pageStatBP = QWidget()
        self.pageStatBP.setObjectName(u"pageStatBP")
        self.verticalLayout_14 = QVBoxLayout(self.pageStatBP)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentBP = QFrame(self.pageStatBP)
        self.frmTopContentBP.setObjectName(u"frmTopContentBP")
        self.frmTopContentBP.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frmTopContentBP)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat3 = QFrame(self.frmTopContentBP)
        self.frmTopLeftStat3.setObjectName(u"frmTopLeftStat3")
        self.frmTopLeftStat3.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frmTopLeftStat3)

        self.frmTopBtnBP = QFrame(self.frmTopContentBP)
        self.frmTopBtnBP.setObjectName(u"frmTopBtnBP")
        self.frmTopBtnBP.setMinimumSize(QSize(664, 50))
        self.frmTopBtnBP.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frmTopBtnBP)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btnKcal3 = QPushButton(self.frmTopBtnBP)
        self.btnKcal3.setObjectName(u"btnKcal3")
        sizePolicy4.setHeightForWidth(self.btnKcal3.sizePolicy().hasHeightForWidth())
        self.btnKcal3.setSizePolicy(sizePolicy4)
        self.btnKcal3.setFont(font)
        self.btnKcal3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnKcal3)

        self.btnSteps3 = QPushButton(self.frmTopBtnBP)
        self.btnSteps3.setObjectName(u"btnSteps3")
        sizePolicy4.setHeightForWidth(self.btnSteps3.sizePolicy().hasHeightForWidth())
        self.btnSteps3.setSizePolicy(sizePolicy4)
        self.btnSteps3.setFont(font)
        self.btnSteps3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnSteps3)

        self.btnBP3 = QPushButton(self.frmTopBtnBP)
        self.btnBP3.setObjectName(u"btnBP3")
        sizePolicy4.setHeightForWidth(self.btnBP3.sizePolicy().hasHeightForWidth())
        self.btnBP3.setSizePolicy(sizePolicy4)
        self.btnBP3.setFont(font)
        self.btnBP3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnBP3)

        self.btnWeight3 = QPushButton(self.frmTopBtnBP)
        self.btnWeight3.setObjectName(u"btnWeight3")
        sizePolicy4.setHeightForWidth(self.btnWeight3.sizePolicy().hasHeightForWidth())
        self.btnWeight3.setSizePolicy(sizePolicy4)
        self.btnWeight3.setFont(font)
        self.btnWeight3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.btnWeight3)


        self.horizontalLayout_18.addWidget(self.frmTopBtnBP)

        self.frmTopRightStat3 = QFrame(self.frmTopContentBP)
        self.frmTopRightStat3.setObjectName(u"frmTopRightStat3")
        self.frmTopRightStat3.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frmTopRightStat3)


        self.verticalLayout_14.addWidget(self.frmTopContentBP)

        self.frmContentBP = QFrame(self.pageStatBP)
        self.frmContentBP.setObjectName(u"frmContentBP")
        self.frmContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmContentBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frmContentBP)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentBP = QFrame(self.frmContentBP)
        self.frmLeftContentBP.setObjectName(u"frmLeftContentBP")
        self.frmLeftContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentBP.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frmLeftContentBP)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frmLeftContentBP)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_29)

        self.frame_21 = QFrame(self.frmLeftContentBP)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 200))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_21)
        self.verticalLayout_23.setSpacing(9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frmAvgBP = QFrame(self.frame_21)
        self.frmAvgBP.setObjectName(u"frmAvgBP")
        self.frmAvgBP.setMinimumSize(QSize(448, 0))
        self.frmAvgBP.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmAvgBP.setFrameShape(QFrame.StyledPanel)
        self.frmAvgBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frmAvgBP)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.lbAvgBP = QLabel(self.frmAvgBP)
        self.lbAvgBP.setObjectName(u"lbAvgBP")
        self.lbAvgBP.setFont(font)

        self.horizontalLayout_38.addWidget(self.lbAvgBP)

        self.lbAvgBpValue = QLabel(self.frmAvgBP)
        self.lbAvgBpValue.setObjectName(u"lbAvgBpValue")
        self.lbAvgBpValue.setFont(font)
        self.lbAvgBpValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.lbAvgBpValue)


        self.verticalLayout_23.addWidget(self.frmAvgBP)

        self.frmMaxBP = QFrame(self.frame_21)
        self.frmMaxBP.setObjectName(u"frmMaxBP")
        self.frmMaxBP.setMinimumSize(QSize(448, 0))
        self.frmMaxBP.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMaxBP.setFrameShape(QFrame.StyledPanel)
        self.frmMaxBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frmMaxBP)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.lbMaxBP = QLabel(self.frmMaxBP)
        self.lbMaxBP.setObjectName(u"lbMaxBP")
        self.lbMaxBP.setFont(font)

        self.horizontalLayout_39.addWidget(self.lbMaxBP)

        self.lbMaxBpValue = QLabel(self.frmMaxBP)
        self.lbMaxBpValue.setObjectName(u"lbMaxBpValue")
        self.lbMaxBpValue.setFont(font)
        self.lbMaxBpValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.lbMaxBpValue)


        self.verticalLayout_23.addWidget(self.frmMaxBP)

        self.frmMin = QFrame(self.frame_21)
        self.frmMin.setObjectName(u"frmMin")
        self.frmMin.setMinimumSize(QSize(448, 0))
        self.frmMin.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMin.setFrameShape(QFrame.StyledPanel)
        self.frmMin.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frmMin)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.lbMinBP = QLabel(self.frmMin)
        self.lbMinBP.setObjectName(u"lbMinBP")
        self.lbMinBP.setFont(font)

        self.horizontalLayout_40.addWidget(self.lbMinBP)

        self.lbMinBpValue = QLabel(self.frmMin)
        self.lbMinBpValue.setObjectName(u"lbMinBpValue")
        self.lbMinBpValue.setFont(font)
        self.lbMinBpValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.lbMinBpValue)


        self.verticalLayout_23.addWidget(self.frmMin)


        self.verticalLayout_25.addWidget(self.frame_21)

        self.frame_30 = QFrame(self.frmLeftContentBP)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)

        self.verticalLayout_25.addWidget(self.frame_30)


        self.horizontalLayout_29.addWidget(self.frmLeftContentBP)

        self.frmRightContentBP = QFrame(self.frmContentBP)
        self.frmRightContentBP.setObjectName(u"frmRightContentBP")
        self.frmRightContentBP.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentBP.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frmRightContentBP)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bpChart = QFrame(self.frmRightContentBP)
        self.bpChart.setObjectName(u"bpChart")
        self.bpChart.setFrameShape(QFrame.StyledPanel)
        self.bpChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.bpChart)

        self.frmChartSelectionBP = QFrame(self.frmRightContentBP)
        self.frmChartSelectionBP.setObjectName(u"frmChartSelectionBP")
        self.frmChartSelectionBP.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionBP.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frmChartSelectionBP)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 9, 0)
        self.frame_22 = QFrame(self.frmChartSelectionBP)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(100, 16777215))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_22)

        self.frmSelectionBtnBP = QFrame(self.frmChartSelectionBP)
        self.frmSelectionBtnBP.setObjectName(u"frmSelectionBtnBP")
        self.frmSelectionBtnBP.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnBP.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnBP.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnBP.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frmSelectionBtnBP)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lbSelectionBP = QLabel(self.frmSelectionBtnBP)
        self.lbSelectionBP.setObjectName(u"lbSelectionBP")
        self.lbSelectionBP.setFont(font)

        self.horizontalLayout_30.addWidget(self.lbSelectionBP)

        self.cbBP = QComboBox(self.frmSelectionBtnBP)
        self.cbBP.addItem("")
        self.cbBP.addItem("")
        self.cbBP.addItem("")
        self.cbBP.setObjectName(u"cbBP")
        self.cbBP.setMinimumSize(QSize(120, 0))
        self.cbBP.setMaximumSize(QSize(120, 16777215))
        self.cbBP.setFont(font)
        self.cbBP.setStyleSheet(u"")
        self.cbBP.setEditable(False)
        self.cbBP.setMaxCount(2147483645)

        self.horizontalLayout_30.addWidget(self.cbBP)


        self.horizontalLayout_31.addWidget(self.frmSelectionBtnBP)

        self.frame_23 = QFrame(self.frmChartSelectionBP)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(100, 16777215))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_31.addWidget(self.frame_23)


        self.verticalLayout_19.addWidget(self.frmChartSelectionBP)


        self.horizontalLayout_29.addWidget(self.frmRightContentBP)


        self.verticalLayout_14.addWidget(self.frmContentBP)

        self.pages.addWidget(self.pageStatBP)
        self.pageStatWeight = QWidget()
        self.pageStatWeight.setObjectName(u"pageStatWeight")
        self.horizontalLayout_24 = QHBoxLayout(self.pageStatWeight)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.pageStatWeight)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frmTopContentBP_2 = QFrame(self.frame_7)
        self.frmTopContentBP_2.setObjectName(u"frmTopContentBP_2")
        self.frmTopContentBP_2.setMaximumSize(QSize(16777215, 50))
        self.frmTopContentBP_2.setFrameShape(QFrame.StyledPanel)
        self.frmTopContentBP_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frmTopContentBP_2)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frmTopLeftStat3_2 = QFrame(self.frmTopContentBP_2)
        self.frmTopLeftStat3_2.setObjectName(u"frmTopLeftStat3_2")
        self.frmTopLeftStat3_2.setFrameShape(QFrame.StyledPanel)
        self.frmTopLeftStat3_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frmTopLeftStat3_2)

        self.frmTopBtnBP_2 = QFrame(self.frmTopContentBP_2)
        self.frmTopBtnBP_2.setObjectName(u"frmTopBtnBP_2")
        self.frmTopBtnBP_2.setMinimumSize(QSize(664, 50))
        self.frmTopBtnBP_2.setFrameShape(QFrame.StyledPanel)
        self.frmTopBtnBP_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frmTopBtnBP_2)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.btnKcal4 = QPushButton(self.frmTopBtnBP_2)
        self.btnKcal4.setObjectName(u"btnKcal4")
        sizePolicy4.setHeightForWidth(self.btnKcal4.sizePolicy().hasHeightForWidth())
        self.btnKcal4.setSizePolicy(sizePolicy4)
        self.btnKcal4.setFont(font)
        self.btnKcal4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_54.addWidget(self.btnKcal4)

        self.btnSteps4 = QPushButton(self.frmTopBtnBP_2)
        self.btnSteps4.setObjectName(u"btnSteps4")
        sizePolicy4.setHeightForWidth(self.btnSteps4.sizePolicy().hasHeightForWidth())
        self.btnSteps4.setSizePolicy(sizePolicy4)
        self.btnSteps4.setFont(font)
        self.btnSteps4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_54.addWidget(self.btnSteps4)

        self.btnBP4 = QPushButton(self.frmTopBtnBP_2)
        self.btnBP4.setObjectName(u"btnBP4")
        sizePolicy4.setHeightForWidth(self.btnBP4.sizePolicy().hasHeightForWidth())
        self.btnBP4.setSizePolicy(sizePolicy4)
        self.btnBP4.setFont(font)
        self.btnBP4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_54.addWidget(self.btnBP4)

        self.btnWeight4 = QPushButton(self.frmTopBtnBP_2)
        self.btnWeight4.setObjectName(u"btnWeight4")
        sizePolicy4.setHeightForWidth(self.btnWeight4.sizePolicy().hasHeightForWidth())
        self.btnWeight4.setSizePolicy(sizePolicy4)
        self.btnWeight4.setFont(font)
        self.btnWeight4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_54.addWidget(self.btnWeight4)


        self.horizontalLayout_25.addWidget(self.frmTopBtnBP_2)

        self.frmTopRightStat3_2 = QFrame(self.frmTopContentBP_2)
        self.frmTopRightStat3_2.setObjectName(u"frmTopRightStat3_2")
        self.frmTopRightStat3_2.setFrameShape(QFrame.StyledPanel)
        self.frmTopRightStat3_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frmTopRightStat3_2)


        self.verticalLayout_17.addWidget(self.frmTopContentBP_2)

        self.frmContentSteps_2 = QFrame(self.frame_7)
        self.frmContentSteps_2.setObjectName(u"frmContentSteps_2")
        self.frmContentSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmContentSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frmContentSteps_2)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(9, 0, 0, 0)
        self.frmLeftContentSteps_2 = QFrame(self.frmContentSteps_2)
        self.frmLeftContentSteps_2.setObjectName(u"frmLeftContentSteps_2")
        self.frmLeftContentSteps_2.setMinimumSize(QSize(456, 0))
        self.frmLeftContentSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmLeftContentSteps_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frmLeftContentSteps_2)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.frmLeftContentSteps_2)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_49)

        self.frame_50 = QFrame(self.frmLeftContentSteps_2)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 200))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_50)
        self.verticalLayout_45.setSpacing(9)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frmAvgSteps_2 = QFrame(self.frame_50)
        self.frmAvgSteps_2.setObjectName(u"frmAvgSteps_2")
        self.frmAvgSteps_2.setMinimumSize(QSize(448, 0))
        self.frmAvgSteps_2.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmAvgSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmAvgSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frmAvgSteps_2)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.lbAvgWeight = QLabel(self.frmAvgSteps_2)
        self.lbAvgWeight.setObjectName(u"lbAvgWeight")
        self.lbAvgWeight.setFont(font)

        self.horizontalLayout_49.addWidget(self.lbAvgWeight)

        self.lbAvgWeightValue = QLabel(self.frmAvgSteps_2)
        self.lbAvgWeightValue.setObjectName(u"lbAvgWeightValue")
        self.lbAvgWeightValue.setFont(font)
        self.lbAvgWeightValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.lbAvgWeightValue)


        self.verticalLayout_45.addWidget(self.frmAvgSteps_2)

        self.frmMaxSteps_2 = QFrame(self.frame_50)
        self.frmMaxSteps_2.setObjectName(u"frmMaxSteps_2")
        self.frmMaxSteps_2.setMinimumSize(QSize(448, 0))
        self.frmMaxSteps_2.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMaxSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmMaxSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frmMaxSteps_2)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.lbMaxWeight = QLabel(self.frmMaxSteps_2)
        self.lbMaxWeight.setObjectName(u"lbMaxWeight")
        self.lbMaxWeight.setFont(font)

        self.horizontalLayout_50.addWidget(self.lbMaxWeight)

        self.lbMaxWeightValue = QLabel(self.frmMaxSteps_2)
        self.lbMaxWeightValue.setObjectName(u"lbMaxWeightValue")
        self.lbMaxWeightValue.setFont(font)
        self.lbMaxWeightValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.lbMaxWeightValue)


        self.verticalLayout_45.addWidget(self.frmMaxSteps_2)

        self.frmMinSteps_2 = QFrame(self.frame_50)
        self.frmMinSteps_2.setObjectName(u"frmMinSteps_2")
        self.frmMinSteps_2.setMinimumSize(QSize(448, 0))
        self.frmMinSteps_2.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;\n"
"")
        self.frmMinSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmMinSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frmMinSteps_2)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.lbMinWeight = QLabel(self.frmMinSteps_2)
        self.lbMinWeight.setObjectName(u"lbMinWeight")
        self.lbMinWeight.setFont(font)

        self.horizontalLayout_51.addWidget(self.lbMinWeight)

        self.lbMinWeightValue = QLabel(self.frmMinSteps_2)
        self.lbMinWeightValue.setObjectName(u"lbMinWeightValue")
        self.lbMinWeightValue.setFont(font)
        self.lbMinWeightValue.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.lbMinWeightValue)


        self.verticalLayout_45.addWidget(self.frmMinSteps_2)


        self.verticalLayout_44.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frmLeftContentSteps_2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_51)


        self.horizontalLayout_47.addWidget(self.frmLeftContentSteps_2)

        self.frmRightContentSteps_2 = QFrame(self.frmContentSteps_2)
        self.frmRightContentSteps_2.setObjectName(u"frmRightContentSteps_2")
        self.frmRightContentSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmRightContentSteps_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frmRightContentSteps_2)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.weightChart = QFrame(self.frmRightContentSteps_2)
        self.weightChart.setObjectName(u"weightChart")
        self.weightChart.setFrameShape(QFrame.StyledPanel)
        self.weightChart.setFrameShadow(QFrame.Raised)

        self.verticalLayout_46.addWidget(self.weightChart)

        self.frmChartSelectionSteps_2 = QFrame(self.frmRightContentSteps_2)
        self.frmChartSelectionSteps_2.setObjectName(u"frmChartSelectionSteps_2")
        self.frmChartSelectionSteps_2.setMaximumSize(QSize(16777215, 100))
        self.frmChartSelectionSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmChartSelectionSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frmChartSelectionSteps_2)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 9, 0)
        self.frame_52 = QFrame(self.frmChartSelectionSteps_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(100, 16777215))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_52)

        self.frmSelectionBtnSteps_2 = QFrame(self.frmChartSelectionSteps_2)
        self.frmSelectionBtnSteps_2.setObjectName(u"frmSelectionBtnSteps_2")
        self.frmSelectionBtnSteps_2.setMaximumSize(QSize(16777215, 50))
        self.frmSelectionBtnSteps_2.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frmSelectionBtnSteps_2.setFrameShape(QFrame.StyledPanel)
        self.frmSelectionBtnSteps_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frmSelectionBtnSteps_2)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.lbSelectionSteps_2 = QLabel(self.frmSelectionBtnSteps_2)
        self.lbSelectionSteps_2.setObjectName(u"lbSelectionSteps_2")
        self.lbSelectionSteps_2.setFont(font)

        self.horizontalLayout_53.addWidget(self.lbSelectionSteps_2)

        self.cbWeight = QComboBox(self.frmSelectionBtnSteps_2)
        self.cbWeight.addItem("")
        self.cbWeight.addItem("")
        self.cbWeight.addItem("")
        self.cbWeight.setObjectName(u"cbWeight")
        self.cbWeight.setMinimumSize(QSize(120, 0))
        self.cbWeight.setMaximumSize(QSize(120, 16777215))
        self.cbWeight.setFont(font)
        self.cbWeight.setStyleSheet(u"")
        self.cbWeight.setEditable(False)
        self.cbWeight.setMaxCount(2147483645)

        self.horizontalLayout_53.addWidget(self.cbWeight)


        self.horizontalLayout_52.addWidget(self.frmSelectionBtnSteps_2)

        self.frame_53 = QFrame(self.frmChartSelectionSteps_2)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(100, 16777215))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_53)


        self.verticalLayout_46.addWidget(self.frmChartSelectionSteps_2)


        self.horizontalLayout_47.addWidget(self.frmRightContentSteps_2)


        self.verticalLayout_17.addWidget(self.frmContentSteps_2)


        self.horizontalLayout_24.addWidget(self.frame_7)

        self.pages.addWidget(self.pageStatWeight)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.horizontalLayout_41 = QHBoxLayout(self.pageSettings)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.pageSettings)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(470, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_12)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setStyleSheet(u"background-color: rgb(211, 201, 242);\n"
"border-radius: 15px")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label = QLabel(self.frame_14)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_42.addWidget(self.label)


        self.verticalLayout_26.addWidget(self.frame_14)

        self.frame_18 = QFrame(self.frame_12)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_18)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_24)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 20)
        self.lbSetFirstName = QLabel(self.frame_24)
        self.lbSetFirstName.setObjectName(u"lbSetFirstName")
        self.lbSetFirstName.setFont(font)

        self.verticalLayout_28.addWidget(self.lbSetFirstName)

        self.lbSetFirstNameValue = QLabel(self.frame_24)
        self.lbSetFirstNameValue.setObjectName(u"lbSetFirstNameValue")
        self.lbSetFirstNameValue.setFont(font)

        self.verticalLayout_28.addWidget(self.lbSetFirstNameValue)


        self.verticalLayout_27.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_25)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 20)
        self.lbSetLastName = QLabel(self.frame_25)
        self.lbSetLastName.setObjectName(u"lbSetLastName")
        self.lbSetLastName.setFont(font)

        self.verticalLayout_29.addWidget(self.lbSetLastName)

        self.lbSetLastNameValue = QLabel(self.frame_25)
        self.lbSetLastNameValue.setObjectName(u"lbSetLastNameValue")
        self.lbSetLastNameValue.setFont(font)

        self.verticalLayout_29.addWidget(self.lbSetLastNameValue)


        self.verticalLayout_27.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_18)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_26)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 20)
        self.lbSetBirthday = QLabel(self.frame_26)
        self.lbSetBirthday.setObjectName(u"lbSetBirthday")
        self.lbSetBirthday.setFont(font)

        self.verticalLayout_30.addWidget(self.lbSetBirthday)

        self.lbSetBirthdayValue = QLabel(self.frame_26)
        self.lbSetBirthdayValue.setObjectName(u"lbSetBirthdayValue")
        self.lbSetBirthdayValue.setFont(font)

        self.verticalLayout_30.addWidget(self.lbSetBirthdayValue)


        self.verticalLayout_27.addWidget(self.frame_26)

        self.frame_31 = QFrame(self.frame_18)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_31)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 20)
        self.lbSetSex = QLabel(self.frame_31)
        self.lbSetSex.setObjectName(u"lbSetSex")
        self.lbSetSex.setFont(font)

        self.verticalLayout_31.addWidget(self.lbSetSex)

        self.lbSetSexValue = QLabel(self.frame_31)
        self.lbSetSexValue.setObjectName(u"lbSetSexValue")
        self.lbSetSexValue.setFont(font)

        self.verticalLayout_31.addWidget(self.lbSetSexValue)


        self.verticalLayout_27.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_18)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_32)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 20)
        self.lbSetHeight = QLabel(self.frame_32)
        self.lbSetHeight.setObjectName(u"lbSetHeight")
        self.lbSetHeight.setFont(font)

        self.verticalLayout_32.addWidget(self.lbSetHeight)

        self.lbSetHeightValue = QLabel(self.frame_32)
        self.lbSetHeightValue.setObjectName(u"lbSetHeightValue")
        self.lbSetHeightValue.setFont(font)

        self.verticalLayout_32.addWidget(self.lbSetHeightValue)


        self.verticalLayout_27.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_18)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_33)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 20)
        self.lbSetEmail = QLabel(self.frame_33)
        self.lbSetEmail.setObjectName(u"lbSetEmail")
        self.lbSetEmail.setFont(font)

        self.verticalLayout_33.addWidget(self.lbSetEmail)

        self.lbSetEmailValue = QLabel(self.frame_33)
        self.lbSetEmailValue.setObjectName(u"lbSetEmailValue")
        self.lbSetEmailValue.setFont(font)

        self.verticalLayout_33.addWidget(self.lbSetEmailValue)


        self.verticalLayout_27.addWidget(self.frame_33)


        self.verticalLayout_26.addWidget(self.frame_18)


        self.horizontalLayout_41.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.pageSettings)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_13)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_34 = QFrame(self.frame_13)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 40))
        self.frame_34.setStyleSheet(u"background-color: rgb(211, 201, 242);\n"
"border-radius: 15px")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_15 = QLabel(self.frame_34)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_43.addWidget(self.label_15)


        self.verticalLayout_34.addWidget(self.frame_34)

        self.frame_19 = QFrame(self.frame_13)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_19)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_40 = QFrame(self.frame_19)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_40)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 0, -1, 25)
        self.lbSetHeightChange = QLabel(self.frame_40)
        self.lbSetHeightChange.setObjectName(u"lbSetHeightChange")
        self.lbSetHeightChange.setFont(font)

        self.verticalLayout_36.addWidget(self.lbSetHeightChange)

        self.leSetHeight = QLineEdit(self.frame_40)
        self.leSetHeight.setObjectName(u"leSetHeight")
        self.leSetHeight.setFont(font)
        self.leSetHeight.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.verticalLayout_36.addWidget(self.leSetHeight)


        self.verticalLayout_35.addWidget(self.frame_40)

        self.frame_37 = QFrame(self.frame_19)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_37)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, 25)
        self.lbSetEmailChange = QLabel(self.frame_37)
        self.lbSetEmailChange.setObjectName(u"lbSetEmailChange")
        self.lbSetEmailChange.setFont(font)

        self.verticalLayout_37.addWidget(self.lbSetEmailChange)

        self.leSetEmail = QLineEdit(self.frame_37)
        self.leSetEmail.setObjectName(u"leSetEmail")
        self.leSetEmail.setFont(font)
        self.leSetEmail.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.verticalLayout_37.addWidget(self.leSetEmail)


        self.verticalLayout_35.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_19)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_38)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 25)
        self.lbSetConfirmEmail = QLabel(self.frame_38)
        self.lbSetConfirmEmail.setObjectName(u"lbSetConfirmEmail")
        self.lbSetConfirmEmail.setFont(font)

        self.verticalLayout_38.addWidget(self.lbSetConfirmEmail)

        self.leSetConfirmEmail = QLineEdit(self.frame_38)
        self.leSetConfirmEmail.setObjectName(u"leSetConfirmEmail")
        self.leSetConfirmEmail.setFont(font)
        self.leSetConfirmEmail.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")

        self.verticalLayout_38.addWidget(self.leSetConfirmEmail)


        self.verticalLayout_35.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_19)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_39)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 0, -1, 25)
        self.lbSetPassword = QLabel(self.frame_39)
        self.lbSetPassword.setObjectName(u"lbSetPassword")
        self.lbSetPassword.setFont(font)

        self.verticalLayout_39.addWidget(self.lbSetPassword)

        self.leSetPassword = QLineEdit(self.frame_39)
        self.leSetPassword.setObjectName(u"leSetPassword")
        self.leSetPassword.setFont(font)
        self.leSetPassword.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leSetPassword.setEchoMode(QLineEdit.Password)
        self.leSetPassword.setReadOnly(False)

        self.verticalLayout_39.addWidget(self.leSetPassword)


        self.verticalLayout_35.addWidget(self.frame_39)

        self.frame_35 = QFrame(self.frame_19)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_35)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 0, -1, 25)
        self.lbSetConfirmPassword = QLabel(self.frame_35)
        self.lbSetConfirmPassword.setObjectName(u"lbSetConfirmPassword")
        self.lbSetConfirmPassword.setFont(font)

        self.verticalLayout_40.addWidget(self.lbSetConfirmPassword)

        self.leSetConfirmPassword = QLineEdit(self.frame_35)
        self.leSetConfirmPassword.setObjectName(u"leSetConfirmPassword")
        self.leSetConfirmPassword.setFont(font)
        self.leSetConfirmPassword.setStyleSheet(u"border-bottom: 2px solid rgb(211, 201, 242);\n"
"")
        self.leSetConfirmPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_40.addWidget(self.leSetConfirmPassword)


        self.verticalLayout_35.addWidget(self.frame_35)


        self.verticalLayout_34.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 0))
        self.frame_20.setMaximumSize(QSize(16777215, 40))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.frame_20)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(0, 0))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.btnChangeInfo = QPushButton(self.frame_36)
        self.btnChangeInfo.setObjectName(u"btnChangeInfo")
        self.btnChangeInfo.setMinimumSize(QSize(160, 40))
        self.btnChangeInfo.setMaximumSize(QSize(160, 40))
        self.btnChangeInfo.setFont(font)
        self.btnChangeInfo.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(155, 127, 240);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(122, 100, 189);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(211, 201, 242);\n"
"	border-radius: 15px;\n"
"}")

        self.horizontalLayout_45.addWidget(self.btnChangeInfo)

        self.lbSetError = QLabel(self.frame_36)
        self.lbSetError.setObjectName(u"lbSetError")

        self.horizontalLayout_45.addWidget(self.lbSetError)


        self.horizontalLayout_44.addWidget(self.frame_36)


        self.verticalLayout_34.addWidget(self.frame_20)


        self.horizontalLayout_41.addWidget(self.frame_13)

        self.pages.addWidget(self.pageSettings)
        self.pageCalendar = QWidget()
        self.pageCalendar.setObjectName(u"pageCalendar")
        self.horizontalLayout_46 = QHBoxLayout(self.pageCalendar)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QFrame(self.pageCalendar)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(470, 16777215))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_41)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_10 = QFrame(self.frame_41)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_41)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 300))
        self.frame_9.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_55.setSpacing(6)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(9, 9, 9, 9)
        self.calendarWidget = QCalendarWidget(self.frame_9)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setFont(font)

        self.horizontalLayout_55.addWidget(self.calendarWidget)


        self.verticalLayout_41.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_41)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.frame_8)


        self.horizontalLayout_46.addWidget(self.frame_41)

        self.frame_42 = QFrame(self.pageCalendar)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setMaximumSize(QSize(500, 16777215))
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_42)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_58 = QFrame(self.frame_42)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(16777215, 124))
        self.frame_58.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_58)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_59)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_61.addWidget(self.label_12)

        self.lbCalendarKcal = QLabel(self.frame_59)
        self.lbCalendarKcal.setObjectName(u"lbCalendarKcal")
        self.lbCalendarKcal.setFont(font)
        self.lbCalendarKcal.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_61.addWidget(self.lbCalendarKcal)


        self.verticalLayout_48.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(-1, 0, -1, 0)
        self.label_14 = QLabel(self.frame_60)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_62.addWidget(self.label_14)

        self.lbCalendarSteps = QLabel(self.frame_60)
        self.lbCalendarSteps.setObjectName(u"lbCalendarSteps")
        self.lbCalendarSteps.setFont(font)
        self.lbCalendarSteps.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.lbCalendarSteps)


        self.verticalLayout_48.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_58)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(9, 0, 9, 0)
        self.label_17 = QLabel(self.frame_61)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.horizontalLayout_63.addWidget(self.label_17)

        self.lbCalendarWeight = QLabel(self.frame_61)
        self.lbCalendarWeight.setObjectName(u"lbCalendarWeight")
        self.lbCalendarWeight.setFont(font)
        self.lbCalendarWeight.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_63.addWidget(self.lbCalendarWeight)


        self.verticalLayout_48.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_58)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(-1, 0, -1, 0)
        self.label_19 = QLabel(self.frame_62)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_64.addWidget(self.label_19)

        self.lbCalendarBP = QLabel(self.frame_62)
        self.lbCalendarBP.setObjectName(u"lbCalendarBP")
        self.lbCalendarBP.setFont(font)
        self.lbCalendarBP.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.lbCalendarBP)


        self.verticalLayout_48.addWidget(self.frame_62)


        self.verticalLayout_47.addWidget(self.frame_58)

        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"background-color: rgb(155, 127, 240);\n"
"border-radius: 15px;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_43)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.tableFoodCalendar = QTableWidget(self.frame_43)
        if (self.tableFoodCalendar.columnCount() < 3):
            self.tableFoodCalendar.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableFoodCalendar.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableFoodCalendar.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableFoodCalendar.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tableFoodCalendar.setObjectName(u"tableFoodCalendar")

        self.verticalLayout_49.addWidget(self.tableFoodCalendar)


        self.verticalLayout_47.addWidget(self.frame_43)


        self.horizontalLayout_46.addWidget(self.frame_42)

        self.pages.addWidget(self.pageCalendar)

        self.verticalLayout_4.addWidget(self.pages)


        self.horizontalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.mainWidget)

        WndMain.setCentralWidget(self.centralwidget)

        self.retranslateUi(WndMain)

        self.pages.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"MainWindow", None))
        self.btnToggle.setText("")
        self.lbName.setText(QCoreApplication.translate("WndMain", u" Max Mustermann", None))
        self.lbDate.setText(QCoreApplication.translate("WndMain", u"09.06.2022", None))
        self.lbPageDescription.setText(QCoreApplication.translate("WndMain", u"Home", None))
        self.btnHome.setText(QCoreApplication.translate("WndMain", u"Home", None))
        self.btnFood.setText(QCoreApplication.translate("WndMain", u"Food", None))
        self.btnStatistic.setText(QCoreApplication.translate("WndMain", u"Statistics", None))
        self.btnSettings.setText(QCoreApplication.translate("WndMain", u"Settings", None))
        self.btnCalendar.setText(QCoreApplication.translate("WndMain", u"Calendar", None))
        self.btnLogout.setText(QCoreApplication.translate("WndMain", u"Logout", None))
        self.lbWeight.setText(QCoreApplication.translate("WndMain", u"Weight:", None))
        self.lbSteps.setText(QCoreApplication.translate("WndMain", u"Steps:", None))
        self.lbBP.setText(QCoreApplication.translate("WndMain", u"Blood Pressure:", None))
        self.leBPLow.setText("")
        self.leBPLow.setPlaceholderText(QCoreApplication.translate("WndMain", u"Diastolic", None))
        self.leBPHigh.setPlaceholderText(QCoreApplication.translate("WndMain", u"Systolic", None))
        self.btnSubmit.setText(QCoreApplication.translate("WndMain", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"Successfully added", None))
        self.lbSearchFood.setText(QCoreApplication.translate("WndMain", u"Search:", None))
        self.btnSearchFood.setText(QCoreApplication.translate("WndMain", u"Find", None))
        ___qtablewidgetitem = self.tbFood.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndMain", u"Name", None));
        ___qtablewidgetitem1 = self.tbFood.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndMain", u"Calories per 100g", None));
        self.lbAmount.setText(QCoreApplication.translate("WndMain", u"Calories per 100g:", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"Amount (g):", None))
        self.btnAddFood.setText(QCoreApplication.translate("WndMain", u"Add", None))
        self.lbFoodAdded.setText(QCoreApplication.translate("WndMain", u"Successfully added!", None))
        self.btnKcal1.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps1.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP1.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.btnWeight1.setText(QCoreApplication.translate("WndMain", u"Weight", None))
        self.lbAvgKcal.setText(QCoreApplication.translate("WndMain", u"Avarage Kcal eaten:", None))
        self.lbAvgKcalValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMaxKcal.setText(QCoreApplication.translate("WndMain", u"Maximum Kcal eaten:", None))
        self.lbMaxKcalValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMinKcal.setText(QCoreApplication.translate("WndMain", u"Minimum Kcal eaten:", None))
        self.lbMinKcalValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbSelectionKcal.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbKcal.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbKcal.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbKcal.setItemText(2, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbKcal.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.btnKcal2.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps2.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP2.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.btnWeight2.setText(QCoreApplication.translate("WndMain", u"Weight", None))
        self.lbAvgSteps.setText(QCoreApplication.translate("WndMain", u"Avarage Steps walked:", None))
        self.lbAvgStepsValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMaxSteps.setText(QCoreApplication.translate("WndMain", u"Maximum Steps walked:", None))
        self.lbMaxStepsValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMinSteps.setText(QCoreApplication.translate("WndMain", u"Minimum Steps Walked:", None))
        self.lbMinStepsValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbSelectionSteps.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbSteps.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbSteps.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbSteps.setItemText(2, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbSteps.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.btnKcal3.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps3.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP3.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.btnWeight3.setText(QCoreApplication.translate("WndMain", u"Weight", None))
        self.lbAvgBP.setText(QCoreApplication.translate("WndMain", u"Avarage Blood Pressure:", None))
        self.lbAvgBpValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMaxBP.setText(QCoreApplication.translate("WndMain", u"Maximum Blood Pressure:", None))
        self.lbMaxBpValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMinBP.setText(QCoreApplication.translate("WndMain", u"Minimum Blood Pressure:", None))
        self.lbMinBpValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbSelectionBP.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbBP.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbBP.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbBP.setItemText(2, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbBP.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.btnKcal4.setText(QCoreApplication.translate("WndMain", u"Kcal", None))
        self.btnSteps4.setText(QCoreApplication.translate("WndMain", u"Steps", None))
        self.btnBP4.setText(QCoreApplication.translate("WndMain", u"Blood Pressure", None))
        self.btnWeight4.setText(QCoreApplication.translate("WndMain", u"Weight", None))
        self.lbAvgWeight.setText(QCoreApplication.translate("WndMain", u"Avarage Weight:", None))
        self.lbAvgWeightValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMaxWeight.setText(QCoreApplication.translate("WndMain", u"Maximum Weight:", None))
        self.lbMaxWeightValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbMinWeight.setText(QCoreApplication.translate("WndMain", u"Minimum Weight:", None))
        self.lbMinWeightValue.setText(QCoreApplication.translate("WndMain", u"TextLabel", None))
        self.lbSelectionSteps_2.setText(QCoreApplication.translate("WndMain", u"Time Priod:", None))
        self.cbWeight.setItemText(0, QCoreApplication.translate("WndMain", u"1 week", None))
        self.cbWeight.setItemText(1, QCoreApplication.translate("WndMain", u"1 month", None))
        self.cbWeight.setItemText(2, QCoreApplication.translate("WndMain", u"complete", None))

        self.cbWeight.setCurrentText(QCoreApplication.translate("WndMain", u"1 week", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"Personal Information:", None))
        self.lbSetFirstName.setText(QCoreApplication.translate("WndMain", u"First Name:", None))
        self.lbSetFirstNameValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">Max</span></p></body></html>", None))
        self.lbSetLastName.setText(QCoreApplication.translate("WndMain", u"Last Name:", None))
        self.lbSetLastNameValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">Mustermann</span></p></body></html>", None))
        self.lbSetBirthday.setText(QCoreApplication.translate("WndMain", u"Birthday:", None))
        self.lbSetBirthdayValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">27.01.2001</span></p></body></html>", None))
        self.lbSetSex.setText(QCoreApplication.translate("WndMain", u"Sex:", None))
        self.lbSetSexValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">male</span></p></body></html>", None))
        self.lbSetHeight.setText(QCoreApplication.translate("WndMain", u"Height:", None))
        self.lbSetHeightValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">196 cm</span></p></body></html>", None))
        self.lbSetEmail.setText(QCoreApplication.translate("WndMain", u"Email:", None))
        self.lbSetEmailValue.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><span style=\" color:#d3c9f2;\">max.mustermann@gmail.com</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("WndMain", u"Change Information:", None))
        self.lbSetHeightChange.setText(QCoreApplication.translate("WndMain", u"Height:", None))
        self.leSetHeight.setText("")
        self.lbSetEmailChange.setText(QCoreApplication.translate("WndMain", u"Email:", None))
        self.lbSetConfirmEmail.setText(QCoreApplication.translate("WndMain", u"Confirm Email:", None))
        self.lbSetPassword.setText(QCoreApplication.translate("WndMain", u"Password:", None))
        self.leSetPassword.setText("")
        self.lbSetConfirmPassword.setText(QCoreApplication.translate("WndMain", u"Confirm Password:", None))
        self.btnChangeInfo.setText(QCoreApplication.translate("WndMain", u"Submit", None))
        self.lbSetError.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("WndMain", u"Calories eaten:", None))
        self.lbCalendarKcal.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("WndMain", u"Steps walked:", None))
        self.lbCalendarSteps.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("WndMain", u"Weight:", None))
        self.lbCalendarWeight.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("WndMain", u"Blood Pressure:", None))
        self.lbCalendarBP.setText(QCoreApplication.translate("WndMain", u"<html><head/><body><p><br/></p></body></html>", None))
        ___qtablewidgetitem2 = self.tableFoodCalendar.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndMain", u"Food", None));
        ___qtablewidgetitem3 = self.tableFoodCalendar.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndMain", u"Calories per 100 g", None));
        ___qtablewidgetitem4 = self.tableFoodCalendar.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndMain", u"Amount (g)", None));
    # retranslateUi

