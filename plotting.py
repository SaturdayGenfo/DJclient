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
from PyQt5 import QtCore, QtWidgets, QtGui

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
        timer.start(4000)
        self.axes.get_yaxis().set_visible(False)

    def compute_initial_figure(self):
        T, S = self.scorereader.read(100)
        S = [0] + S + [0]
        self.axes.set_xlim(1, len(S) - 2)
        self.axes.plot([i for i in range(len(S))], S, color=(237.0/255, 28.0/255, 36.0/255))
        self.axes.fill(S, facecolor=(237.0/255, 28.0/255, 62.0/255), alpha=0.5)
        
        

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        T, S = self.scorereader.read(100)
        self.axes.cla()
        S = [0] + S + [0]
        self.axes.plot([i for i in range(len(S))], S, color=(237.0/255, 28.0/255, 36.0/255))
        self.axes.set_xlim(1, len(S) - 2)
        self.axes.fill([i for i in range(len(S))], S, facecolor=(237.0/255, 28.0/255, 62.0/255), alpha=0.5)
        self.draw()


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Last Night DJ")
        
        '''

        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        '''

        self.main_widget = QtWidgets.QWidget(self)
        
        h = QtWidgets.QVBoxLayout(self.main_widget)

        l = QtWidgets.QHBoxLayout(self.main_widget)
        
        self.logo = QtWidgets.QLabel(self.main_widget)
        self.logo.setPixmap(QtGui.QPixmap("logo2.png"))
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        
        self.ranking = QtWidgets.QTextEdit(self.main_widget)
        self.ranking.setReadOnly(True)
        self.ranking.setStyleSheet("QTextEdit { border : none;} ")
        
        
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_ranking)
        timer.start(4000)
        
        dc = MyDynamicMplCanvas(self.main_widget, width=7, height=5, dpi=100)
        
        
        l.addWidget(self.ranking)
        l.addWidget(dc)
        h.addWidget(self.logo)
        h.addLayout(l)
        self.setLayout(h)
        
        self.setStyleSheet("QMainWindow { background-color : white; }")
        self.rreader = RankingReader("ranking.txt")
        self.update_ranking()

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        
    
    def update_ranking(self):
        rn = self.rreader.read()
        self.ranking.clear()
        html = "".join(rn)
        self.ranking.setHtml(html)
        

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()



qApp = QtWidgets.QApplication(sys.argv)

aw = ApplicationWindow()
aw.setWindowTitle(" ")
aw.setWindowIcon(QtGui.QIcon("icon.png"))
aw.show()
sys.exit(qApp.exec_())
#qApp.exec_()