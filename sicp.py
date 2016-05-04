# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sicp.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(961, 388)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 961, 411))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("sicp.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(539, 50, 301, 281))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(530, 10, 321, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(lambda: self.save(True))
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.clicked.connect(self.open)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.new)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.filename = None

    def save(self, saveAs=False):
        if saveAs == True:
            self.filename = QtGui.QFileDialog.getSaveFileName()
        else:
            if not self.filename:
                self.filename = QtGui.QFileDialog.getSaveFileName()

        if self.filename == "":
            print("Error!")
            return

        if not self.filename.endswith(".txt"):
            self.filename += ".txt"


        with open(self.filename, "wt") as file:
            file.write(self.plainTextEdit.toPlainText())


    def open(self):
        self.filename = QtGui.QFileDialog.getOpenFileName()
        try:
            text = open(self.filename)
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(text.read())
        except FileNotFoundError:
            print("File not found!")

    def new(self):
        self.filename = None
        self.plainTextEdit.clear()

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "SICP note taking.", None))
        self.pushButton.setText(_translate("Form", "Save", None))
        self.pushButton_2.setText(_translate("Form", "SaveAs", None))
        self.pushButton_3.setText(_translate("Form", "Open", None))
        self.pushButton_4.setText(_translate("Form", "New", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

