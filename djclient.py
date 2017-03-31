# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'djclient.ui'
#
# Created: Thu Mar 30 15:08:44 2017
#      by: PyQt4 UI code generator 4.11.2
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
        MainWindow.resize(1029, 749)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.klistwidget = KListWidget(self.centralwidget)
        self.klistwidget.setGeometry(QtCore.QRect(20, 530, 256, 192))
        self.klistwidget.setObjectName(_fromUtf8("klistwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 530, 111, 81))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 640, 111, 81))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 490, 971, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.qwtPlot = QwtPlot(self.centralwidget)
        self.qwtPlot.setGeometry(QtCore.QRect(30, 80, 951, 331))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.qwtPlot_2 = QwtPlot(self.centralwidget)
        self.qwtPlot_2.setGeometry(QtCore.QRect(429, 540, 551, 181))
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LastNight DJ", None))
        self.pushButton.setText(_translate("MainWindow", "START", None))
        self.pushButton_2.setText(_translate("MainWindow", "STOP", None))

from PyKDE4.kdeui import KListWidget
from PyQt4.Qwt5.Qwt import QwtPlot


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

