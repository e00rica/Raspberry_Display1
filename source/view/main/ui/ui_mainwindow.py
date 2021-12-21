# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(480, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(480, 800))
        MainWindow.setMaximumSize(QSize(480, 800))
        MainWindow.setAcceptDrops(False)
        self.dial = QDial(MainWindow)
        self.dial.setObjectName(u"dial")
        self.dial.setEnabled(False)
        self.dial.setGeometry(QRect(70, 240, 341, 341))
        self.dial.setMouseTracking(False)
        self.dial.setTabletTracking(True)
        self.dial.setFocusPolicy(Qt.StrongFocus)
        self.dial.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.dial.setAcceptDrops(False)
        self.dial.setAutoFillBackground(False)
        self.dial.setMinimum(500)
        self.dial.setMaximum(1000)
        self.dial.setTracking(True)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchesVisible(True)
        self.lcdNumber = QLCDNumber(MainWindow)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(300, 700, 131, 51))
        self.lcdNumber.setAutoFillBackground(False)
        self.lcdNumber.setInputMethodHints(Qt.ImhNone)
        self.lcdNumber.setFrameShape(QFrame.Box)
        self.lcdNumber.setFrameShadow(QFrame.Raised)
        self.lcdNumber.setSegmentStyle(QLCDNumber.Filled)
        self.PRF = QLabel(MainWindow)
        self.PRF.setObjectName(u"PRF")
        self.PRF.setGeometry(QRect(300, 670, 51, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(True)
        self.PRF.setFont(font)
        self.LED = QLabel(MainWindow)
        self.LED.setObjectName(u"LED")
        self.LED.setEnabled(True)
        self.LED.setGeometry(QRect(40, 700, 131, 48))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.LED.setFont(font1)
        self.LED.setAutoFillBackground(False)
        self.LED.setFrameShape(QFrame.Panel)
        self.LED.setFrameShadow(QFrame.Sunken)
        self.LED.setLineWidth(1)
        self.LED.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 50, 441, 141))
        self.groupBox.setFont(font)
        self.PS871_Button = QPushButton(self.groupBox)
        self.PS871_Button.setObjectName(u"PS871_Button")
        self.PS871_Button.setGeometry(QRect(20, 40, 84, 75))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.PS871_Button.setFont(font2)
        self.PS871_Button.setMouseTracking(False)
        self.PS871_Button.setTabletTracking(True)
        self.PS871_Button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:Checked {\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 127, 206), stop:0.35 rgba(255, 255, 127, 80), stop:0.4 rgba(255, 255, 127, 80), stop:0.425 rgba(255, 255, 127, 156), stop:0.44 rgba(255, 255, 127, 80), stop:1 rgba(255, 255, 127, 0))\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color:red;/*navy; /* make the default button prominent */\n"
"}")
        self.PS871_Button.setCheckable(True)
        self.PS871_Button.setChecked(False)
        self.PS871_Button.setAutoDefault(False)
        self.Stallbar_Button = QPushButton(self.groupBox)
        self.Stallbar_Button.setObjectName(u"Stallbar_Button")
        self.Stallbar_Button.setGeometry(QRect(180, 40, 84, 75))
        self.Stallbar_Button.setFont(font2)
        self.Stallbar_Button.setMouseTracking(False)
        self.Stallbar_Button.setTabletTracking(True)
        self.Stallbar_Button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:Checked {\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 127, 206), stop:0.35 rgba(255, 255, 127, 80), stop:0.4 rgba(255, 255, 127, 80), stop:0.425 rgba(255, 255, 127, 156), stop:0.44 rgba(255, 255, 127, 80), stop:1 rgba(255, 255, 127, 0))\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color:red;/*navy; /* make the default button prominent */\n"
"}")
        self.Stallbar_Button.setCheckable(True)
        self.Stallbar_Button.setChecked(False)
        self.Stallbar_Button.setAutoDefault(False)
        self.Slump_Button = QPushButton(self.groupBox)
        self.Slump_Button.setObjectName(u"Slump_Button")
        self.Slump_Button.setGeometry(QRect(340, 40, 84, 75))
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(246, 247, 250, 255))
        gradient.setColorAt(1, QColor(218, 219, 222, 255))
        brush = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(246, 247, 250, 255))
        gradient1.setColorAt(1, QColor(218, 219, 222, 255))
        brush1 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(246, 247, 250, 255))
        gradient2.setColorAt(1, QColor(218, 219, 222, 255))
        brush2 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(246, 247, 250, 255))
        gradient3.setColorAt(1, QColor(218, 219, 222, 255))
        brush3 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(246, 247, 250, 255))
        gradient4.setColorAt(1, QColor(218, 219, 222, 255))
        brush4 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(246, 247, 250, 255))
        gradient5.setColorAt(1, QColor(218, 219, 222, 255))
        brush5 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(246, 247, 250, 255))
        gradient6.setColorAt(1, QColor(218, 219, 222, 255))
        brush6 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(246, 247, 250, 255))
        gradient7.setColorAt(1, QColor(218, 219, 222, 255))
        brush7 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(246, 247, 250, 255))
        gradient8.setColorAt(1, QColor(218, 219, 222, 255))
        brush8 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush8)
        self.Slump_Button.setPalette(palette)
        self.Slump_Button.setFont(font2)
        self.Slump_Button.setMouseTracking(False)
        self.Slump_Button.setTabletTracking(True)
        self.Slump_Button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:Checked {\n"
"    background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 127, 206), stop:0.35 rgba(255, 255, 127, 80), stop:0.4 rgba(255, 255, 127, 80), stop:0.425 rgba(255, 255, 127, 156), stop:0.44 rgba(255, 255, 127, 80), stop:1 rgba(255, 255, 127, 0))\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color:red;/*navy; /* make the default button prominent */\n"
"}")
        self.Slump_Button.setCheckable(True)
        self.Slump_Button.setChecked(False)
        self.Slump_Button.setAutoDefault(False)
        self.Stallbar_Button.raise_()
        self.Slump_Button.raise_()
        self.PS871_Button.raise_()
        self.Status = QLabel(MainWindow)
        self.Status.setObjectName(u"Status")
        self.Status.setGeometry(QRect(40, 670, 81, 31))
        self.Status.setFont(font)

        self.retranslateUi(MainWindow)

        self.PS871_Button.setDefault(False)
        self.Stallbar_Button.setDefault(False)
        self.Slump_Button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Modulator", None))
        self.PRF.setText(QCoreApplication.translate("MainWindow", u" PRF:", None))
        self.LED.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Val av PRF", None))
        self.PS871_Button.setText(QCoreApplication.translate("MainWindow", u"PS871", None))
        self.Stallbar_Button.setText(QCoreApplication.translate("MainWindow", u"ST\u00c4LLBAR", None))
        self.Slump_Button.setText(QCoreApplication.translate("MainWindow", u"SLUMPGEN", None))
        self.Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
    # retranslateUi

