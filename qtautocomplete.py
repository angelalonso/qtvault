#!/bin/usr/env python
"""
example taken from http://stackoverflow.com/questions/29062322/how-can-i-create-a-searchbar-in-pyqt
"""

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

model = QtGui.QStringListModel()
model.setStringList(['lucas', 'luquitas', 'angel', 'angelote', 'angelito'])

completer = QtGui.QCompleter()
completer.setModel(model)

lineedit = QtGui.QLineEdit()
lineedit.setCompleter(completer)
lineedit.show()

sys.exit(app.exec_())
