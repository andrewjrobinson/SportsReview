# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Mar 27 21:33:49 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(690, 541)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.videoFrame = QtGui.QLabel(self.splitter)
        self.videoFrame.setText(_fromUtf8(""))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.buttonArea = QtGui.QWidget(self.splitter)
        self.buttonArea.setStyleSheet(_fromUtf8("background-color: rgb(106, 106, 106);"))
        self.buttonArea.setObjectName(_fromUtf8("buttonArea"))
        self.gridLayout_2 = QtGui.QGridLayout(self.buttonArea)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.delay = QtGui.QLabel(self.buttonArea)
        self.delay.setObjectName(_fromUtf8("delay"))
        self.gridLayout_2.addWidget(self.delay, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.buttonArea)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.frameRate = QtGui.QLabel(self.buttonArea)
        self.frameRate.setObjectName(_fromUtf8("frameRate"))
        self.gridLayout_2.addWidget(self.frameRate, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.buttonArea)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.frameNum = QtGui.QLabel(self.buttonArea)
        self.frameNum.setObjectName(_fromUtf8("frameNum"))
        self.gridLayout_2.addWidget(self.frameNum, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.buttonArea)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.buttonArea)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 3)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.delay.setText(_translate("MainWindow", "2", None))
        self.label.setText(_translate("MainWindow", "Delay:", None))
        self.frameRate.setText(_translate("MainWindow", "30", None))
        self.label_2.setText(_translate("MainWindow", "Frame rate:", None))
        self.frameNum.setText(_translate("MainWindow", "~", None))
        self.label_3.setText(_translate("MainWindow", "Frame:", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>F7 &lt;space&gt;     = toggle play/pause mode<br/>F12     = write buffer to /tmp/video_* (only when paused)<br/>\'+.=&gt;\'     = increase delay, next frame<br/>\'-,&lt;\'     = decrease delay, previous frame<br/>Esc    = quit</p></body></html>", None))

