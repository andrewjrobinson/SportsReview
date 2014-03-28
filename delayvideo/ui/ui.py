# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delayvideo/ui/mainwindow.ui'
#
# Created: Fri Mar 28 20:49:42 2014
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
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.videoFrame = QtGui.QLabel(self.splitter)
        self.videoFrame.setText(_fromUtf8(""))
        self.videoFrame.setObjectName(_fromUtf8("videoFrame"))
        self.buttonArea = QtGui.QWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonArea.sizePolicy().hasHeightForWidth())
        self.buttonArea.setSizePolicy(sizePolicy)
        self.buttonArea.setMaximumSize(QtCore.QSize(16777215, 108))
        self.buttonArea.setStyleSheet(_fromUtf8("background-color: rgb(106, 106, 106);"))
        self.buttonArea.setObjectName(_fromUtf8("buttonArea"))
        self.gridLayout_2 = QtGui.QGridLayout(self.buttonArea)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.buttonArea)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.buttonArea)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 3, 4, 1, 3)
        self.frameRate = QtGui.QLabel(self.buttonArea)
        self.frameRate.setObjectName(_fromUtf8("frameRate"))
        self.gridLayout_2.addWidget(self.frameRate, 0, 4, 1, 1)
        self.frameNum = QtGui.QLabel(self.buttonArea)
        self.frameNum.setObjectName(_fromUtf8("frameNum"))
        self.gridLayout_2.addWidget(self.frameNum, 0, 6, 1, 1)
        self.label_4 = QtGui.QLabel(self.buttonArea)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 4)
        self.delay = QtGui.QLabel(self.buttonArea)
        self.delay.setObjectName(_fromUtf8("delay"))
        self.gridLayout_2.addWidget(self.delay, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.buttonArea)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.buttonArea)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 5, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Frame rate:", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>\'+.=&gt;\' = increase delay, next frame<br/>\'-,&lt;\' = decrease delay, previous frame<br/>Esc = quit</p></body></html>", None))
        self.frameRate.setText(_translate("MainWindow", "30", None))
        self.frameNum.setText(_translate("MainWindow", "~", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>F7 &lt;space&gt; = toggle play/pause mode<br/>F11 = toggle fullscreen mode<br/>F12 = write buffer to /tmp/video_* (only when paused)</p></body></html>", None))
        self.delay.setText(_translate("MainWindow", "2", None))
        self.label.setText(_translate("MainWindow", "Delay:", None))
        self.label_3.setText(_translate("MainWindow", "Frame:", None))

