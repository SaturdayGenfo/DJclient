# embedding_in_qt5.py --- Simple Qt5 application embedding matplotlib canvases
#
# Copyright (C) 2005 Florent Rougon
#               2006 Darren Dale
#               2015 Jens H Nielsen
#
# This file is an example program for matplotlib. It may be used and
# modified with no restriction; raw copies as well as modified versions
# may be distributed without limitation.

from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi, random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from RankingReader import RankingReader
from AverageScoreReader import ScoreReader

progname = os.path.basename(sys.argv[0])
progversion = "0.1"


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass




class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        self.scorereader = ScoreReader('D.txt')
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(5000)
        

    def compute_initial_figure(self):
        T, S = self.scorereader.read(20)
        self.axes.plot(S, 'r')
        

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        T, S = self.scorereader.read(20)
        self.axes.cla()
        self.axes.plot(S, 'r')
        self.draw()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Last Night DJ")

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)



        self.main_widget = QtWidgets.QWidget(self)

        l = QtWidgets.QVBoxLayout(self.main_widget)
        
        
        self.ranking = QtWidgets.QTextEdit(self.main_widget)
        self.ranking.setReadOnly(True)
        
        self.ranking.setGeometry(QtCore.QRect(20, 50, 361, 161))
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_ranking)
        timer.start(5000)
        
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        
        
        l.addWidget(self.ranking)
        l.addWidget(dc)
        
        self.rreader = RankingReader("ranking.txt")
        self.update_ranking()

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        
    
    def update_ranking(self):
        rn = self.rreader.read()
        self.ranking.clear()
        html = "<br>".join(rn)
        self.ranking.setHtml(html)
        

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()



qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle("LAST NIGHT")
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()