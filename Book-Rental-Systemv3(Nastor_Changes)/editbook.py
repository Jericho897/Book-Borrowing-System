# Form implementation generated from reading ui file 'editbook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class editbookDialog(object):
    def setupUi(self, editbook):
        editbook.setObjectName("editbook")
        editbook.resize(583, 560)
        editbook.setStyleSheet("background:rgb(72, 72, 72)")
        self.label_6 = QtWidgets.QLabel(parent=editbook)
        self.label_6.setGeometry(QtCore.QRect(70, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(parent=editbook)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.bookbasefee = QtWidgets.QLineEdit(parent=editbook)
        self.bookbasefee.setGeometry(QtCore.QRect(150, 379, 411, 22))
        self.bookbasefee.setStyleSheet(" background: white")
        self.bookbasefee.setObjectName("bookbasefee")
        self.titlelineedit = QtWidgets.QLineEdit(parent=editbook)
        self.titlelineedit.setGeometry(QtCore.QRect(150, 126, 411, 22))
        self.titlelineedit.setStyleSheet(" background: white")
        self.titlelineedit.setObjectName("titlelineedit")
        self.label_9 = QtWidgets.QLabel(parent=editbook)
        self.label_9.setGeometry(QtCore.QRect(30, 430, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.bookdesc = QtWidgets.QTextEdit(parent=editbook)
        self.bookdesc.setGeometry(QtCore.QRect(150, 260, 411, 101))
        self.bookdesc.setAutoFillBackground(False)
        self.bookdesc.setStyleSheet(" background: white")
        self.bookdesc.setObjectName("bookdesc")
        self.Confirm = QtWidgets.QPushButton(parent=editbook)
        self.Confirm.setGeometry(QtCore.QRect(90, 500, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Confirm.setFont(font)
        self.Confirm.setStyleSheet("QPushButton {\n"
"                background-color: rgb(6, 217, 66);\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(50, 255, 100);\n"
"            }")
        self.Confirm.setFlat(False)
        self.Confirm.setObjectName("Confirm")
        self.label_10 = QtWidgets.QLabel(parent=editbook)
        self.label_10.setGeometry(QtCore.QRect(60, 210, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color:white;")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.isbnlineedit = QtWidgets.QLineEdit(parent=editbook)
        self.isbnlineedit.setGeometry(QtCore.QRect(150, 84, 411, 22))
        self.isbnlineedit.setStyleSheet(" background: white")
        self.isbnlineedit.setFrame(False)
        self.isbnlineedit.setObjectName("isbnlineedit")
        self.authorlineedit = QtWidgets.QLineEdit(parent=editbook)
        self.authorlineedit.setGeometry(QtCore.QRect(150, 170, 411, 22))
        self.authorlineedit.setStyleSheet(" background: white")
        self.authorlineedit.setObjectName("authorlineedit")
        self.openpicbutton = QtWidgets.QToolButton(parent=editbook)
        self.openpicbutton.setGeometry(QtCore.QRect(150, 440, 411, 31))
        self.openpicbutton.setStyleSheet("QToolButton {\n"
"                background-color: rgb(72, 72, 72);\n"
"                color:rgb(255, 255, 255);\n"
"                border: none;\n"
"                padding: 10px;\n"
"            }\n"
"            QToolButton:hover {\n"
"                background-color: rgb(100, 100, 100);\n"
"            }")
        self.openpicbutton.setObjectName("openpicbutton")
        self.frame = QtWidgets.QFrame(parent=editbook)
        self.frame.setGeometry(QtCore.QRect(0, 0, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(230, 0, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.bookcbox = QtWidgets.QComboBox(parent=editbook)
        self.bookcbox.setGeometry(QtCore.QRect(150, 210, 231, 31))
        self.bookcbox.setStyleSheet(" background: white")
        self.bookcbox.setObjectName("bookcbox")
        self.label_8 = QtWidgets.QLabel(parent=editbook)
        self.label_8.setGeometry(QtCore.QRect(28, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.Cancel = QtWidgets.QPushButton(parent=editbook)
        self.Cancel.setGeometry(QtCore.QRect(330, 500, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("QPushButton {\n"
"                background-color: rgb(200, 46, 18);\n"
"                color: white;\n"
"                border: none;\n"
"                border-radius: 5px;\n"
"                padding: 10px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: rgb(255, 100, 100);\n"
"            }")
        self.Cancel.setObjectName("Cancel")
        self.label_7 = QtWidgets.QLabel(parent=editbook)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=editbook)
        self.label_5.setGeometry(QtCore.QRect(90, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.bookbasefee.raise_()
        self.titlelineedit.raise_()
        self.label_9.raise_()
        self.bookdesc.raise_()
        self.Confirm.raise_()
        self.label_10.raise_()
        self.isbnlineedit.raise_()
        self.authorlineedit.raise_()
        self.openpicbutton.raise_()
        self.frame.raise_()
        self.bookcbox.raise_()
        self.label_8.raise_()
        self.Cancel.raise_()
        self.label_5.raise_()

        self.retranslateUi(editbook)
        QtCore.QMetaObject.connectSlotsByName(editbook)

    def retranslateUi(self, editbook):
        _translate = QtCore.QCoreApplication.translate
        editbook.setWindowTitle(_translate("editbook", "Edit Book"))
        self.label_6.setText(_translate("editbook", "Author:"))
        self.label_4.setText(_translate("editbook", "ISBN:"))
        self.label_9.setText(_translate("editbook", "Book Cover:"))
        self.bookdesc.setHtml(_translate("editbook", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.13913pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.13913pt;\"><br /></p></body></html>"))
        self.Confirm.setText(_translate("editbook", "Confirm"))
        self.label_10.setText(_translate("editbook", "Category:"))
        self.openpicbutton.setText(_translate("editbook", "Select Picture"))
        self.label.setText(_translate("editbook", "Edit Book"))
        self.label_8.setText(_translate("editbook", "Base Rent Fee:"))
        self.Cancel.setText(_translate("editbook", "Cancel"))
        self.label_7.setText(_translate("editbook", "Description:"))
        self.label_5.setText(_translate("editbook", "Title:"))
