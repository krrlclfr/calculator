# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'standard_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Standard(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(441, 653)
        MainWindow.setStyleSheet("QFrame{\n"
"background-color: #4B4453;\n"
"font-family: times-new-roman;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"#label{\n"
"background-color: rgba(0,0,0,0.2);\n"
"color: grey;\n"
"font-size: 25px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#label_2{\n"
"padding: 15px;\n"
"font-size: 30px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: #B0A8B9;\n"
"border-radius: 5px;\n"
"margin: 2px;\n"
"font-size: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #9B89B3;\n"
"}\n"
"#Equal, #addition, #subtract, #multiply, #divide, #Exit, #clear, #clear_Erase, #modulus, #Scientific{\n"
"background-color: #00C2A8;\n"
"}\n"
"\n"
"#Equal:hover, #addition:hover, #subtract:hover, #multiply:hover, #divide:hover, #Exit:hover, #clear:hover, #clear_Erase:hover, #modulus:hover, #Scientific:hover{\n"
"background-color: #FFC75F;\n"
"}\n"
"#result{\n"
"font-size: 45px;\n"
"padding: 20px;\n"
"color: white;\n"
"background-color: rgba(0,0,0,0.1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#top_result{\n"
"color: white;\n"
"font-size: 20px;\n"
"background-color: rgba(0,0,0,0.0);\n"
"padding: 5px;\n"
"}\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 441, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 201, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 441, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.result = QtWidgets.QLabel(self.frame_2)
        self.result.setGeometry(QtCore.QRect(0, 10, 441, 101))
        self.result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result.setObjectName("result")
        self.top_result = QtWidgets.QLabel(self.frame_2)
        self.top_result.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.top_result.setText("")
        self.top_result.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.top_result.setObjectName("top_result")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 160, 441, 501))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Equal = QtWidgets.QPushButton(self.frame_3)
        self.Equal.setGeometry(QtCore.QRect(330, 410, 111, 71))
        self.Equal.setObjectName("Equal")
        self.point = QtWidgets.QPushButton(self.frame_3)
        self.point.setGeometry(QtCore.QRect(220, 410, 111, 71))
        self.point.setObjectName("point")
        self.zero = QtWidgets.QPushButton(self.frame_3)
        self.zero.setGeometry(QtCore.QRect(110, 410, 111, 71))
        self.zero.setObjectName("zero")
        self.plus_minus = QtWidgets.QPushButton(self.frame_3)
        self.plus_minus.setGeometry(QtCore.QRect(0, 410, 111, 71))
        self.plus_minus.setObjectName("plus_minus")
        self.addition = QtWidgets.QPushButton(self.frame_3)
        self.addition.setGeometry(QtCore.QRect(330, 340, 111, 71))
        self.addition.setObjectName("addition")
        self.subtract = QtWidgets.QPushButton(self.frame_3)
        self.subtract.setGeometry(QtCore.QRect(330, 270, 111, 71))
        self.subtract.setObjectName("subtract")
        self.multiply = QtWidgets.QPushButton(self.frame_3)
        self.multiply.setGeometry(QtCore.QRect(330, 200, 111, 71))
        self.multiply.setObjectName("multiply")
        self.divide = QtWidgets.QPushButton(self.frame_3)
        self.divide.setGeometry(QtCore.QRect(330, 130, 111, 71))
        self.divide.setObjectName("divide")
        self.Scientific = QtWidgets.QPushButton(self.frame_3)
        self.Scientific.setGeometry(QtCore.QRect(330, 60, 111, 71))
        self.Scientific.setObjectName("Scientific")
        self.number_3 = QtWidgets.QPushButton(self.frame_3)
        self.number_3.setGeometry(QtCore.QRect(220, 340, 111, 71))
        self.number_3.setObjectName("number_3")
        self.number_2 = QtWidgets.QPushButton(self.frame_3)
        self.number_2.setGeometry(QtCore.QRect(110, 340, 111, 71))
        self.number_2.setObjectName("number_2")
        self.number_1 = QtWidgets.QPushButton(self.frame_3)
        self.number_1.setGeometry(QtCore.QRect(0, 340, 111, 71))
        self.number_1.setObjectName("number_1")
        self.number_6 = QtWidgets.QPushButton(self.frame_3)
        self.number_6.setGeometry(QtCore.QRect(220, 270, 111, 71))
        self.number_6.setObjectName("number_6")
        self.number_5 = QtWidgets.QPushButton(self.frame_3)
        self.number_5.setGeometry(QtCore.QRect(110, 270, 111, 71))
        self.number_5.setObjectName("number_5")
        self.number_4 = QtWidgets.QPushButton(self.frame_3)
        self.number_4.setGeometry(QtCore.QRect(0, 270, 111, 71))
        self.number_4.setObjectName("number_4")
        self.number_9 = QtWidgets.QPushButton(self.frame_3)
        self.number_9.setGeometry(QtCore.QRect(220, 200, 111, 71))
        self.number_9.setObjectName("number_9")
        self.number_8 = QtWidgets.QPushButton(self.frame_3)
        self.number_8.setGeometry(QtCore.QRect(110, 200, 111, 71))
        self.number_8.setObjectName("number_8")
        self.number_7 = QtWidgets.QPushButton(self.frame_3)
        self.number_7.setGeometry(QtCore.QRect(0, 200, 111, 71))
        self.number_7.setObjectName("number_7")
        self.square_root = QtWidgets.QPushButton(self.frame_3)
        self.square_root.setGeometry(QtCore.QRect(220, 130, 111, 71))
        self.square_root.setObjectName("square_root")
        self.exponent = QtWidgets.QPushButton(self.frame_3)
        self.exponent.setGeometry(QtCore.QRect(110, 130, 111, 71))
        self.exponent.setObjectName("exponent")
        self.exponent_one = QtWidgets.QPushButton(self.frame_3)
        self.exponent_one.setGeometry(QtCore.QRect(0, 130, 111, 71))
        self.exponent_one.setObjectName("exponent_one")
        self.clear = QtWidgets.QPushButton(self.frame_3)
        self.clear.setGeometry(QtCore.QRect(220, 60, 111, 71))
        self.clear.setObjectName("clear")
        self.clear_Erase = QtWidgets.QPushButton(self.frame_3)
        self.clear_Erase.setGeometry(QtCore.QRect(110, 60, 111, 71))
        self.clear_Erase.setObjectName("clear_Erase")
        self.modulus = QtWidgets.QPushButton(self.frame_3)
        self.modulus.setGeometry(QtCore.QRect(0, 60, 111, 71))
        self.modulus.setObjectName("modulus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "Standard"))
        self.result.setText(_translate("MainWindow", "0"))
        self.Equal.setText(_translate("MainWindow", "="))
        self.point.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.plus_minus.setText(_translate("MainWindow", "+/-"))
        self.addition.setText(_translate("MainWindow", "+"))
        self.subtract.setText(_translate("MainWindow", "-"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.divide.setText(_translate("MainWindow", "÷"))
        self.Scientific.setText(_translate("MainWindow", "Scientific\n"
"Calculator"))
        self.number_3.setText(_translate("MainWindow", "3"))
        self.number_2.setText(_translate("MainWindow", "2"))
        self.number_1.setText(_translate("MainWindow", "1"))
        self.number_6.setText(_translate("MainWindow", "6"))
        self.number_5.setText(_translate("MainWindow", "5"))
        self.number_4.setText(_translate("MainWindow", "4"))
        self.number_9.setText(_translate("MainWindow", "9"))
        self.number_8.setText(_translate("MainWindow", "8"))
        self.number_7.setText(_translate("MainWindow", "7"))
        self.square_root.setText(_translate("MainWindow", "2√x"))
        self.exponent.setText(_translate("MainWindow", "x²"))
        self.exponent_one.setText(_translate("MainWindow", "1/x"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.clear_Erase.setText(_translate("MainWindow", "CE"))
        self.modulus.setText(_translate("MainWindow", "%"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
