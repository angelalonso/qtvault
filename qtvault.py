#!/usr/bin/env python
"""
First draft taken from http://www.learningpython.com/2008/09/20/an-introduction-to-pyqt/#FirstApplication
"""

import PyQt4
import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):

	def __init__(self, win_parent = None):
		#Init the base class
		QtGui.QMainWindow.__init__(self, win_parent)

if __name__ == "__main__":
	# Someone is launching this directly
	# Create the QApplication
	app = QtGui.QApplication(sys.argv)
	#The Main window
	main_window = MainWindow()
	main_window.show()
	# Enter the main loop
	app.exec_()
