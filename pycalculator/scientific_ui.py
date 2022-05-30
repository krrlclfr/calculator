# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scientific.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon('icon.png'))
        Form.setFixedSize(441, 653)
        Form.setStyleSheet("QFrame{\n"
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
"#Equal, #addition, #subtract, #multiply, #divide, #Exit, #clear, #clear_Erase, #modulus, #mod, #Standard, #nd, #pi, #inf{\n"
"background-color: #00C2A8;\n"
"}\n"
"\n"
"#Equal:hover, #addition:hover, #subtract:hover, #multiply:hover, #divide:hover, #Exit:hover, #clear:hover, #clear_Erase:hover, #modulus:hover, #mod:hover, #Standard:hover, #nd:hover, #pi:hover, #inf:hover{\n"
"background-color: #FFC75F;\n"
"}\n"
"#result_2{\n"
"font-size: 45px;\n"
"padding: 20px;\n"
"color: white;\n"
"background-color: rgba(0,0,0,0.1);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"#top_result_2{\n"
"color: white;\n"
"font-size: 20px;\n"
"background-color: rgba(0,0,0,0.0);\n"
"padding: 5px;\n"
"}\n"
"\n"
"#nd_2, #sin, #cos, #tan, #hyp, #sec, #csc, #cot, #vertical_bars_2, #floor_brackets, #ceiling_brackets, #rand, #dms, #deg, #rad, #sinh, #cosh, #tanh, #square_root, #cube_root, #e, #erf{\n"
"background-color: #FF6F91;\n"
"}\n"
"\n"
"#deg:hover, #sin:hover, #cos:hover, #tan:hover, #rad:hover, #sinh:hover, #cosh:hover, #tanh:hover, #vertical_bars:hover, #floor_brackets:hover, #ceiling_brackets:hover, #square_root:hover, #cube_root:hover, #e:hover, #erf:hover{\n"
"background-color: #FF9671;\n"
"}\n"
"")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(0, 160, 441, 501))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Equal = QtWidgets.QPushButton(self.frame_3)
        self.Equal.setGeometry(QtCore.QRect(350, 420, 91, 61))
        self.Equal.setObjectName("Equal")
        self.point = QtWidgets.QPushButton(self.frame_3)
        self.point.setGeometry(QtCore.QRect(260, 420, 91, 61))
        self.point.setObjectName("point")
        self.zero = QtWidgets.QPushButton(self.frame_3)
        self.zero.setGeometry(QtCore.QRect(180, 420, 81, 61))
        self.zero.setObjectName("zero")
        self.plus_minus = QtWidgets.QPushButton(self.frame_3)
        self.plus_minus.setGeometry(QtCore.QRect(90, 420, 91, 61))
        self.plus_minus.setObjectName("plus_minus")
        self.addition = QtWidgets.QPushButton(self.frame_3)
        self.addition.setGeometry(QtCore.QRect(350, 360, 91, 61))
        self.addition.setObjectName("addition")
        self.subtract = QtWidgets.QPushButton(self.frame_3)
        self.subtract.setGeometry(QtCore.QRect(350, 300, 91, 61))
        self.subtract.setObjectName("subtract")
        self.multiply = QtWidgets.QPushButton(self.frame_3)
        self.multiply.setGeometry(QtCore.QRect(350, 240, 91, 61))
        self.multiply.setObjectName("multiply")
        self.divide = QtWidgets.QPushButton(self.frame_3)
        self.divide.setGeometry(QtCore.QRect(350, 180, 91, 61))
        self.divide.setObjectName("divide")
        self.Standard = QtWidgets.QPushButton(self.frame_3)
        self.Standard.setGeometry(QtCore.QRect(350, 60, 91, 61))
        self.Standard.setObjectName("Standard")
        self.number_3 = QtWidgets.QPushButton(self.frame_3)
        self.number_3.setGeometry(QtCore.QRect(260, 360, 91, 61))
        self.number_3.setObjectName("number_3")
        self.number_2 = QtWidgets.QPushButton(self.frame_3)
        self.number_2.setGeometry(QtCore.QRect(180, 360, 81, 61))
        self.number_2.setObjectName("number_2")
        self.number_1 = QtWidgets.QPushButton(self.frame_3)
        self.number_1.setGeometry(QtCore.QRect(90, 360, 91, 61))
        self.number_1.setObjectName("number_1")
        self.number_6 = QtWidgets.QPushButton(self.frame_3)
        self.number_6.setGeometry(QtCore.QRect(260, 300, 91, 61))
        self.number_6.setObjectName("number_6")
        self.number_5 = QtWidgets.QPushButton(self.frame_3)
        self.number_5.setGeometry(QtCore.QRect(180, 300, 81, 61))
        self.number_5.setObjectName("number_5")
        self.number_4 = QtWidgets.QPushButton(self.frame_3)
        self.number_4.setGeometry(QtCore.QRect(90, 300, 91, 61))
        self.number_4.setObjectName("number_4")
        self.number_9 = QtWidgets.QPushButton(self.frame_3)
        self.number_9.setGeometry(QtCore.QRect(260, 240, 91, 61))
        self.number_9.setObjectName("number_9")
        self.number_8 = QtWidgets.QPushButton(self.frame_3)
        self.number_8.setGeometry(QtCore.QRect(180, 240, 81, 61))
        self.number_8.setObjectName("number_8")
        self.number_7 = QtWidgets.QPushButton(self.frame_3)
        self.number_7.setGeometry(QtCore.QRect(90, 240, 91, 61))
        self.number_7.setObjectName("number_7")
        self.nfactorial = QtWidgets.QPushButton(self.frame_3)
        self.nfactorial.setGeometry(QtCore.QRect(260, 180, 91, 61))
        self.nfactorial.setObjectName("nfactorial")
        self.close_parenthisis = QtWidgets.QPushButton(self.frame_3)
        self.close_parenthisis.setGeometry(QtCore.QRect(180, 180, 81, 61))
        self.close_parenthisis.setObjectName("close_parenthisis")
        self.open_parenthisis = QtWidgets.QPushButton(self.frame_3)
        self.open_parenthisis.setGeometry(QtCore.QRect(90, 180, 91, 61))
        self.open_parenthisis.setObjectName("open_parenthisis")
        self.clear = QtWidgets.QPushButton(self.frame_3)
        self.clear.setGeometry(QtCore.QRect(260, 60, 91, 61))
        self.clear.setObjectName("clear")
        self.clear_Erase = QtWidgets.QPushButton(self.frame_3)
        self.clear_Erase.setGeometry(QtCore.QRect(180, 60, 81, 61))
        self.clear_Erase.setObjectName("clear_Erase")
        self.pi = QtWidgets.QPushButton(self.frame_3)
        self.pi.setGeometry(QtCore.QRect(90, 60, 91, 61))
        self.pi.setObjectName("pi")
        self.ln = QtWidgets.QPushButton(self.frame_3)
        self.ln.setGeometry(QtCore.QRect(0, 420, 91, 61))
        self.ln.setObjectName("ln")
        self.log = QtWidgets.QPushButton(self.frame_3)
        self.log.setGeometry(QtCore.QRect(0, 360, 91, 61))
        self.log.setObjectName("log")
        self.pow_ten = QtWidgets.QPushButton(self.frame_3)
        self.pow_ten.setGeometry(QtCore.QRect(0, 300, 91, 61))
        self.pow_ten.setObjectName("pow_ten")
        self.xy = QtWidgets.QPushButton(self.frame_3)
        self.xy.setGeometry(QtCore.QRect(0, 240, 91, 61))
        self.xy.setObjectName("xy")
        self.pow_three = QtWidgets.QPushButton(self.frame_3)
        self.pow_three.setGeometry(QtCore.QRect(0, 180, 91, 61))
        self.pow_three.setObjectName("pow_three")
        self.squared = QtWidgets.QPushButton(self.frame_3)
        self.squared.setGeometry(QtCore.QRect(0, 120, 91, 61))
        self.squared.setObjectName("squared")
        self.one_x = QtWidgets.QPushButton(self.frame_3)
        self.one_x.setGeometry(QtCore.QRect(90, 120, 91, 61))
        self.one_x.setObjectName("one_x")
        self.abs = QtWidgets.QPushButton(self.frame_3)
        self.abs.setGeometry(QtCore.QRect(180, 120, 81, 61))
        self.abs.setObjectName("abs")
        self.exp = QtWidgets.QPushButton(self.frame_3)
        self.exp.setGeometry(QtCore.QRect(260, 120, 91, 61))
        self.exp.setObjectName("exp")
        self.mod = QtWidgets.QPushButton(self.frame_3)
        self.mod.setGeometry(QtCore.QRect(350, 120, 91, 61))
        self.mod.setObjectName("mod")
        self.inf = QtWidgets.QPushButton(self.frame_3)
        self.inf.setGeometry(QtCore.QRect(0, 60, 91, 61))
        self.inf.setObjectName("inf")
        self.floor_brackets = QtWidgets.QPushButton(self.frame_3)
        self.floor_brackets.setGeometry(QtCore.QRect(320, 0, 61, 31))
        self.floor_brackets.setObjectName("floor_brackets")
        self.cos = QtWidgets.QPushButton(self.frame_3)
        self.cos.setGeometry(QtCore.QRect(120, 0, 61, 31))
        self.cos.setObjectName("cos")
        self.e = QtWidgets.QPushButton(self.frame_3)
        self.e.setGeometry(QtCore.QRect(260, 0, 61, 31))
        self.e.setObjectName("e")
        self.tanh = QtWidgets.QPushButton(self.frame_3)
        self.tanh.setGeometry(QtCore.QRect(180, 30, 81, 31))
        self.tanh.setObjectName("tanh")
        self.erf = QtWidgets.QPushButton(self.frame_3)
        self.erf.setGeometry(QtCore.QRect(380, 30, 61, 31))
        self.erf.setObjectName("erf")
        self.sin = QtWidgets.QPushButton(self.frame_3)
        self.sin.setGeometry(QtCore.QRect(60, 0, 61, 31))
        self.sin.setObjectName("sin")
        self.ceiling_brackets = QtWidgets.QPushButton(self.frame_3)
        self.ceiling_brackets.setGeometry(QtCore.QRect(380, 0, 61, 31))
        self.ceiling_brackets.setObjectName("ceiling_brackets")
        self.square_root = QtWidgets.QPushButton(self.frame_3)
        self.square_root.setGeometry(QtCore.QRect(260, 30, 61, 31))
        self.square_root.setObjectName("square_root")
        self.tan = QtWidgets.QPushButton(self.frame_3)
        self.tan.setGeometry(QtCore.QRect(180, 0, 81, 31))
        self.tan.setObjectName("tan")
        self.deg = QtWidgets.QPushButton(self.frame_3)
        self.deg.setGeometry(QtCore.QRect(0, 0, 61, 31))
        self.deg.setObjectName("deg")
        self.cube_root = QtWidgets.QPushButton(self.frame_3)
        self.cube_root.setGeometry(QtCore.QRect(320, 30, 61, 31))
        self.cube_root.setObjectName("cube_root")
        self.sinh = QtWidgets.QPushButton(self.frame_3)
        self.sinh.setGeometry(QtCore.QRect(60, 30, 61, 31))
        self.sinh.setObjectName("sinh")
        self.cosh = QtWidgets.QPushButton(self.frame_3)
        self.cosh.setGeometry(QtCore.QRect(120, 30, 61, 31))
        self.cosh.setObjectName("cosh")
        self.rad = QtWidgets.QPushButton(self.frame_3)
        self.rad.setGeometry(QtCore.QRect(0, 30, 61, 31))
        self.rad.setObjectName("rad")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 50, 441, 111))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.result_2 = QtWidgets.QLabel(self.frame_2)
        self.result_2.setGeometry(QtCore.QRect(0, 10, 441, 101))
        self.result_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.result_2.setObjectName("result_2")
        self.top_result_2 = QtWidgets.QLabel(self.frame_2)
        self.top_result_2.setGeometry(QtCore.QRect(10, 10, 421, 31))
        self.top_result_2.setText("")
        self.top_result_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.top_result_2.setObjectName("top_result_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 441, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 201, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculator"))
        self.Equal.setText(_translate("Form", "="))
        self.point.setText(_translate("Form", "."))
        self.zero.setText(_translate("Form", "0"))
        self.plus_minus.setText(_translate("Form", "+/-"))
        self.addition.setText(_translate("Form", "+"))
        self.subtract.setText(_translate("Form", "-"))
        self.multiply.setText(_translate("Form", "x"))
        self.divide.setText(_translate("Form", "÷"))
        self.Standard.setText(_translate("Form", "Standard\n"
"Calculator"))
        self.number_3.setText(_translate("Form", "3"))
        self.number_2.setText(_translate("Form", "2"))
        self.number_1.setText(_translate("Form", "1"))
        self.number_6.setText(_translate("Form", "6"))
        self.number_5.setText(_translate("Form", "5"))
        self.number_4.setText(_translate("Form", "4"))
        self.number_9.setText(_translate("Form", "9"))
        self.number_8.setText(_translate("Form", "8"))
        self.number_7.setText(_translate("Form", "7"))
        self.nfactorial.setText(_translate("Form", "n!"))
        self.close_parenthisis.setText(_translate("Form", ")"))
        self.open_parenthisis.setText(_translate("Form", "("))
        self.clear.setText(_translate("Form", "C"))
        self.clear_Erase.setText(_translate("Form", "CE"))
        self.pi.setText(_translate("Form", "π"))
        self.ln.setText(_translate("Form", "ln"))
        self.log.setText(_translate("Form", "Log"))
        self.pow_ten.setText(_translate("Form", "10x"))
        self.xy.setText(_translate("Form", "x/y"))
        self.pow_three.setText(_translate("Form", "x3"))
        self.squared.setText(_translate("Form", "x²"))
        self.one_x.setText(_translate("Form", "1/x"))
        self.abs.setText(_translate("Form", "abs"))
        self.exp.setText(_translate("Form", "exp"))
        self.mod.setText(_translate("Form", "mod"))
        self.inf.setText(_translate("Form", "Inf"))
        self.floor_brackets.setText(_translate("Form", "⌊x⌋"))
        self.cos.setText(_translate("Form", "cos"))
        self.e.setText(_translate("Form", "e"))
        self.tanh.setText(_translate("Form", "tanh"))
        self.erf.setText(_translate("Form", "erf"))
        self.sin.setText(_translate("Form", "sin"))
        self.ceiling_brackets.setText(_translate("Form", "⌈x⌉"))
        self.square_root.setText(_translate("Form", "2√x"))
        self.tan.setText(_translate("Form", "tan"))
        self.deg.setText(_translate("Form", "deg"))
        self.cube_root.setText(_translate("Form", "3√x"))
        self.sinh.setText(_translate("Form", "sinh"))
        self.cosh.setText(_translate("Form", "cosh"))
        self.rad.setText(_translate("Form", "rad"))
        self.result_2.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "Scientific"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
