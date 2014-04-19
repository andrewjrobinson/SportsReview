# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aftertouches/aftertouches.ui'
#
# Created: Sat Apr 19 15:37:12 2014
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
        MainWindow.resize(481, 444)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/common/resources/icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setMargin(2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frameLabel = QtGui.QLabel(self.widget)
        self.frameLabel.setStyleSheet(_fromUtf8("border: 1px solid rgb(0, 85, 255);"))
        self.frameLabel.setText(_fromUtf8(""))
        self.frameLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/common/resources/icon.svg")))
        self.frameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.frameLabel.setObjectName(_fromUtf8("frameLabel"))
        self.verticalLayout.addWidget(self.frameLabel)
        self.verticalLayout_2.addWidget(self.widget)
        self.frameSelectionFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameSelectionFrame.sizePolicy().hasHeightForWidth())
        self.frameSelectionFrame.setSizePolicy(sizePolicy)
        self.frameSelectionFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameSelectionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.frameSelectionFrame.setObjectName(_fromUtf8("frameSelectionFrame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frameSelectionFrame)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widgetControlWidget = QtGui.QWidget(self.frameSelectionFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetControlWidget.sizePolicy().hasHeightForWidth())
        self.widgetControlWidget.setSizePolicy(sizePolicy)
        self.widgetControlWidget.setObjectName(_fromUtf8("widgetControlWidget"))
        self.gridLayout = QtGui.QGridLayout(self.widgetControlWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.prevFrameButton = QtGui.QPushButton(self.widgetControlWidget)
        self.prevFrameButton.setObjectName(_fromUtf8("prevFrameButton"))
        self.gridLayout.addWidget(self.prevFrameButton, 0, 1, 1, 1)
        self.nextFrameButton = QtGui.QPushButton(self.widgetControlWidget)
        self.nextFrameButton.setObjectName(_fromUtf8("nextFrameButton"))
        self.gridLayout.addWidget(self.nextFrameButton, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.widgetControlWidget)
        self.previewLabel = QtGui.QLabel(self.frameSelectionFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previewLabel.sizePolicy().hasHeightForWidth())
        self.previewLabel.setSizePolicy(sizePolicy)
        self.previewLabel.setMinimumSize(QtCore.QSize(0, 80))
        self.previewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewLabel.setObjectName(_fromUtf8("previewLabel"))
        self.verticalLayout_3.addWidget(self.previewLabel)
        self.frameSlider = QtGui.QSlider(self.frameSelectionFrame)
        self.frameSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frameSlider.setObjectName(_fromUtf8("frameSlider"))
        self.verticalLayout_3.addWidget(self.frameSlider)
        self.verticalLayout_2.addWidget(self.frameSelectionFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_SportsReview = QtGui.QAction(MainWindow)
        self.actionAbout_SportsReview.setObjectName(_fromUtf8("actionAbout_SportsReview"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "After Touches - SportsReview", None))
        self.prevFrameButton.setToolTip(_translate("MainWindow", "Select previous frame", None))
        self.prevFrameButton.setText(_translate("MainWindow", "< &Prev", None))
        self.prevFrameButton.setShortcut(_translate("MainWindow", "Alt+P", None))
        self.nextFrameButton.setToolTip(_translate("MainWindow", "Select next frame", None))
        self.nextFrameButton.setText(_translate("MainWindow", "&Next >", None))
        self.nextFrameButton.setShortcut(_translate("MainWindow", "Alt+N", None))
        self.previewLabel.setText(_translate("MainWindow", "No file open", None))
        self.frameSlider.setToolTip(_translate("MainWindow", "Select Frame", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "E&xit", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionAbout_SportsReview.setText(_translate("MainWindow", "About SportsReview", None))

import resources_rc
