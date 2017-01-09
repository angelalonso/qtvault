#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
First draft taken from:
 http://stackoverflow.com/questions/15561608/detecting-enter-on-a-qlineedit-or-qpushbutton#15567835
TODO:
    - show password after <Enter> or better yet:  thaat it exists
    - clean defs
    - add colors to "Password Exists" and "Password copied", and a text message
"""

from PyQt4 import QtGui, QtCore
import subprocess
import sys


def get_passnames():
    List = []
    cmd = "/home/aaf/Software/Dev/qtvault/test.sh pass"
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # wait for the process to terminate
    out, err = process.communicate()
    # TODO: check this errcode
    errcode = process.returncode
    for word in out.split(' '):
        List.append(word)
    return List


def get_pass(passname):
    password = passname + 'blah'
    return password


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.setGeometry(412, 250, 600, 150)

        self.PassList = get_passnames()

        self.label = QtGui.QLabel()
        self.label.move(20, 20)
        self.label.setText("What are you looking for?")

        self.model = QtGui.QStringListModel()
        self.model.setStringList(self.PassList)

        self.completer = QtGui.QCompleter()
        self.completer.setModel(self.model)

        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.move(20, 40)
        self.lineEdit.setCompleter(self.completer)

        self.pushButtonSearch = QtGui.QPushButton(self)
        self.pushButtonSearch.setText("Search Pass")
        self.pushButtonSearch.clicked.connect(self.Search)
        self.pushButtonSearch.setAutoDefault(True)

        self.lineEdit.returnPressed.connect(self.pushButtonSearch.click)

        self.pushButtonCopy = QtGui.QPushButton(self)
        self.pushButtonCopy.setText("Copy Pass")
        self.pushButtonCopy.clicked.connect(self.on_pushButtonCopy_clicked)
        self.pushButtonCopy.setAutoDefault(True)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.addWidget(self.label, 0, 1)
        self.gridLayout.addWidget(self.lineEdit, 0, 2)
        self.gridLayout.addWidget(self.pushButtonSearch, 1, 1)
        self.gridLayout.addWidget(self.pushButtonCopy, 1, 2)
        self.setLayout(self.gridLayout)

        self.lineEdit.setFocus()

    @QtCore.pyqtSlot()
    def Search(self):
        passwdname_written = self.lineEdit.text()
        if passwdname_written in self.PassList:
            self.label.setText("Ready to Copy")
            # TODO: grey button if not ready, test after each stroke or click
        else:
            self.label.setText("Nothing found, try again")

    def on_pushButtonCopy_clicked(self):
        passwd_received = get_pass(self.lineEdit.text())
        clipboard = QtGui.QApplication.clipboard()
        clipboard.setText(passwd_received)
        self.label.setText("Password copied to Clipboard")


if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('QtVault')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())
