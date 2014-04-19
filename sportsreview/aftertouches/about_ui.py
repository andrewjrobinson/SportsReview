# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aftertouches/about.ui'
#
# Created: Sat Apr 19 16:35:35 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(500, 315)
        Dialog.setMinimumSize(QtCore.QSize(500, 315))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 0, 1, 2)
        self.title = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title.setWordWrap(True)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 0, 1, 2, 1)
        self.version = QtGui.QLabel(Dialog)
        self.version.setObjectName(_fromUtf8("version"))
        self.gridLayout.addWidget(self.version, 4, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/common/resources/icon.svg")))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 9, 1)
        self.copyright = QtGui.QLabel(Dialog)
        self.copyright.setWordWrap(True)
        self.copyright.setObjectName(_fromUtf8("copyright"))
        self.gridLayout.addWidget(self.copyright, 3, 1, 1, 1)
        self.contributorsTitle = QtGui.QLabel(Dialog)
        self.contributorsTitle.setObjectName(_fromUtf8("contributorsTitle"))
        self.gridLayout.addWidget(self.contributorsTitle, 6, 1, 1, 1)
        self.licence = QtGui.QLabel(Dialog)
        self.licence.setObjectName(_fromUtf8("licence"))
        self.gridLayout.addWidget(self.licence, 5, 1, 1, 1)
        self.intro = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intro.sizePolicy().hasHeightForWidth())
        self.intro.setSizePolicy(sizePolicy)
        self.intro.setWordWrap(True)
        self.intro.setObjectName(_fromUtf8("intro"))
        self.gridLayout.addWidget(self.intro, 2, 1, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 342, 57))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.contributors = QtGui.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contributors.sizePolicy().hasHeightForWidth())
        self.contributors.setSizePolicy(sizePolicy)
        self.contributors.setStyleSheet(_fromUtf8(""))
        self.contributors.setTextFormat(QtCore.Qt.RichText)
        self.contributors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.contributors.setWordWrap(True)
        self.contributors.setObjectName(_fromUtf8("contributors"))
        self.verticalLayout.addWidget(self.contributors)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "About ...", None))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">After Touches</span></p></body></html>", None))
        self.version.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Version</span>: 0.1</p></body></html>", None))
        self.copyright.setText(_translate("Dialog", "<html><head/><body><p>Copyright 2014 Andrew Robinson (<a href=\"mailto:andrewjrobinson+sr@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">andrewjrobinson@gmail.com</span></a>)</p></body></html>", None))
        self.contributorsTitle.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Contributors</span>:</p></body></html>", None))
        self.licence.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Licence</span>: LGPL 2+</p></body></html>", None))
        self.intro.setText(_translate("Dialog", "After Touches is a video analysis tool aimed coaches and sports people of all skill levels. After Touches is part of the SportsReview software suite.", None))
        self.contributors.setText(_translate("Dialog", "<html><head/><body><ul type=\"square\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 0;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Andrew Robinson (<a href=\"mailto:andrewjrobinson+sr@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">andrewjrobinson@gmail.com</span></a>)</li></ul></body></html>", None))

import resources_rc
