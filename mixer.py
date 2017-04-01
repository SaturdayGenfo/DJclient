# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mixerchoice.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from untitled1 import mixerlist


        
class Ui_Dialog(object):
    
        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 279)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 83, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonclicked)
        
        self.listView = QtWidgets.QListWidget(Dialog)
        self.listView.setGeometry(QtCore.QRect(20, 50, 361, 161))
        self.listView.setObjectName("listView")
        mixers = mixerlist()
        for m in mixers:
            item = QtWidgets.QListWidgetItem(m)
            self.listView.addItem(item)
            
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 231, 20))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def buttonclicked(self):
        print("selected item : ", self.listView.currentRow())
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Choix de mixer"))
        self.pushButton.setText(_translate("Dialog", "Select"))
        self.label.setText(_translate("Dialog", "Available Mixers (Choose a stereo mixer ): "))
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    print("Testing")
    sys.exit(app.exec_())

