#!/usr/bin/env python
"""
First draft taken from http://www.learningpython.com/2008/09/20/an-introduction-to-pyqt/#FirstApplication
TODO:
    - show password after <Enter> or better yet:  thaat it exists
    - copy into clipboard after button click
"""


from PyQt4 import QtGui
import subprocess
import sys

def get_passnames():
    List = []
    cmd = "/home/aaf/Software/qtvault/test.sh pass"
    process = subprocess.Popen(cmd, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    # wait for the process to terminate
    out, err = process.communicate()
    errcode = process.returncode
    for word in out.split(' '):
        List.append(word)
    return List

def

def get_pass(passname):
    password = passname + 'blah'
    return password

def textchanged(text):
    print "contents of text box: "+text


def window():
    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()

    label = QtGui.QLabel(widget)
    label.move(20,20)
    label.setText("What are you looking for?")

    model = QtGui.QStringListModel()
    model.setStringList(get_passnames())

    completer = QtGui.QCompleter()
    completer.setModel(model)

    lineedit = QtGui.QLineEdit(widget)
    lineedit.textChanged.connect(textchanged)
    lineedit.move(20,40)
    lineedit.setCompleter(completer)
    lineedit.show()

    btn_cncl = QtGui.QPushButton("Cancel")

    widget.setGeometry(412,250,400,150)
    widget.setWindowTitle("QtVault")
    widget.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
