# Form implementation generated from reading ui file '2.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(633, 248)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 131, 20))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 100, 131, 20))
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 160, 56, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(310, 70, 256, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(40, 20, 561, 181))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("QFrame {\n"
"    background-color:rgb(234, 246, 255)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=self.frame)
        self.commandLinkButton.setGeometry(QtCore.QRect(90, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setShortcut("")
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 140, 56, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.frame_2.setStyleSheet("QFrame {\n"
"    background-color:rgb(255, 255, 255)\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(230, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/Interaction 1/图片1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.frame_2.raise_()
        self.commandLinkButton.raise_()
        self.pushButton_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log in"))
        self.commandLinkButton.setText(_translate("Form", "Forget Password?"))
        self.pushButton_2.setText(_translate("Form", "Log out"))
        self.label_3.setText(_translate("Form", "THP Login System"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())