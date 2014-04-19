# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delayvideo/ui/mainwindow.ui'
#
# Created: Sat Apr 19 19:40:33 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 541)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/common/resources/icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.videoFrame = QtGui.QLabel(self.splitter)
        self.videoFrame.setText("")
        self.videoFrame.setAlignment(QtCore.Qt.AlignCenter)
        self.videoFrame.setObjectName("videoFrame")
        self.buttonArea = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonArea.sizePolicy().hasHeightForWidth())
        self.buttonArea.setSizePolicy(sizePolicy)
        self.buttonArea.setMaximumSize(QtCore.QSize(16777215, 108))
        self.buttonArea.setStyleSheet("background-color: rgb(106, 106, 106);")
        self.buttonArea.setObjectName("buttonArea")
        self.gridLayout_2 = QtGui.QGridLayout(self.buttonArea)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtGui.QLabel(self.buttonArea)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.buttonArea)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 4, 1, 3)
        self.frameRate = QtGui.QLabel(self.buttonArea)
        self.frameRate.setObjectName("frameRate")
        self.gridLayout_2.addWidget(self.frameRate, 0, 4, 1, 1)
        self.frameNum = QtGui.QLabel(self.buttonArea)
        self.frameNum.setObjectName("frameNum")
        self.gridLayout_2.addWidget(self.frameNum, 0, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.buttonArea)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 4)
        self.delay = QtGui.QLabel(self.buttonArea)
        self.delay.setObjectName("delay")
        self.gridLayout_2.addWidget(self.delay, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.buttonArea)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.buttonArea)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Delay Analysis - SportsReview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Frame rate:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>\'+.=&gt;\' = increase delay, next frame<br/>\'-,&lt;\' = decrease delay, previous frame<br/>Esc = quit</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.frameRate.setText(QtGui.QApplication.translate("MainWindow", "30", None, QtGui.QApplication.UnicodeUTF8))
        self.frameNum.setText(QtGui.QApplication.translate("MainWindow", "~", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>F7 &lt;space&gt; = toggle play/pause mode<br/>F11 = toggle fullscreen mode<br/>F12 = write buffer to /tmp/video_* (only when paused)</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.delay.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Delay:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Frame:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
