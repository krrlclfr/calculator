from PyQt5 import QtWidgets
from scientific_ui import Ui_Form
import sys
from PyQt5.QtWidgets import QApplication
import math

    
class ScientificCalculator(QtWidgets.QMainWindow, Ui_Form):

    first_number = None
    user_secondNumber = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #clicked for all buttons
        self.zero.clicked.connect(self.numbers)
        self.number_1.clicked.connect(self.numbers)
        self.number_2.clicked.connect(self.numbers)
        self.number_3.clicked.connect(self.numbers)
        self.number_4.clicked.connect(self.numbers)
        self.number_5.clicked.connect(self.numbers)
        self.number_6.clicked.connect(self.numbers)
        self.number_7.clicked.connect(self.numbers)
        self.number_8.clicked.connect(self.numbers)
        self.number_9.clicked.connect(self.numbers)

        self.point.clicked.connect(self.decimal_point)

        self.plus_minus.clicked.connect(self.operations)

        self.inf.clicked.connect(self.inf_func)

        self.addition.clicked.connect(self.operator)
        self.subtract.clicked.connect(self.operator)
        self.multiply.clicked.connect(self.operator)
        self.divide.clicked.connect(self.operator)
        self.xy.clicked.connect(self.operator)
        self.mod.clicked.connect(self.operator)

        self.clear.clicked.connect(self.Clear)

        #buttons for operator if the click is true
        self.addition.setCheckable(True)
        self.subtract.setCheckable(True)
        self.multiply.setCheckable(True)
        self.divide.setCheckable(True)
        self.xy.setCheckable(True)
        self.mod.setCheckable(True)


        self.Equal.clicked.connect(self.equals)

        self.clear_Erase.clicked.connect(self.Clear_E)

        self.nfactorial.clicked.connect(self.factorial)
        self.floor_brackets.clicked.connect(self.floors)
        self.ceiling_brackets.clicked.connect(self.ceiling)
        self.exp.clicked.connect(self.exponential)
        self.sin.clicked.connect(self.sin_func)
        self.pi.clicked.connect(self.pi_func)
        self.cos.clicked.connect(self.cos_func)
        self.tan.clicked.connect(self.tan_func)
        self.squared.clicked.connect(self.squared_func)
        self.pow_three.clicked.connect(self.pow_func)
        self.ln.clicked.connect(self.ln_func)
        self.pow_ten.clicked.connect(self.pow_ten_func)
        self.one_x.clicked.connect(self.one_func)
        self.deg.clicked.connect(self.deg_func)
        self.rad.clicked.connect(self.rad_func)
        self.sinh.clicked.connect(self.sinh_func)
        self.tanh.clicked.connect(self.tanh_func)
        self.square_root.clicked.connect(self.square_root_func)
        self.cube_root.clicked.connect(self.cube_root_func)
        self.e.clicked.connect(self.e_func)
        self.erf.clicked.connect(self.erf_func)
        self.abs.clicked.connect(self.abs_func)
        self.open_parenthisis.clicked.connect(self.open_func)
        self.close_parenthisis.clicked.connect(self.close_func)
        self.Standard.clicked.connect(self.standard_cal)
        self.log.clicked.connect(self.log_func)


    #operation for all buttons
    def open_func(self):
        print("Hello")
        
    def close_func(self):
        print("Hello")
        
    def numbers(self):
        number_button = self.sender()
        if ((self.addition.isChecked() or self.subtract.isChecked() or self.mod.isChecked() or self.multiply.isChecked() or self.divide.isChecked() or self.xy.isChecked())) and (not self.user_secondNumber):
              result_text = format(float(number_button.text()), '.15g')
              self.user_secondNumber = True

        else:

            result_text = format(float(self.result_2.text() + number_button.text()), '.15g')
            
        self.result_2.setText(result_text)
       
    def decimal_point(self):
        self.result_2.setText(self.result_2.text() +  '.')
       
    def operations(self):
        number_button = self.sender()

        operation_number = float(self.result_2.text())

        if number_button.text() == '+/-':
             operation_number = operation_number * -1
        else:
            self.addition.setChecked(False)
            self.subtract.setChecked(False)
            self.multiply.setChecked(False)
            self.divide.setChecked(False)
            self.xy.setChecked(False)
            
            operation_number = operation_number * 0.01

        result_text = format(operation_number, '.15g')
        self.result_2.setText(result_text)    
        
    def operator(self):
        operator_button = self.sender()

        self.first_number = float(self.result_2.text())
        operator_button.setChecked(True)


    def equals(self):

        second_number = float(self.result_2.text())

        if self.addition.isChecked():
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' + ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number + second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' + ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number + second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            
            
            self.addition.setChecked(False)

        elif self.subtract.isChecked():
            
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' - ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number - second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' - ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number - second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            
            
            self.subtract.setChecked(False)

        elif self.multiply.isChecked():
            
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' * ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' * ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            
            
            self.multiply.setChecked(False)

        elif self.divide.isChecked():
            
            
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' / ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number / second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' / ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number / second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            
            
            self.addition.setChecked(False)

        elif self.xy.isChecked():
            
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' ^ ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' ^ ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number ** second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            self.xy.setChecked(False)

        elif self.mod.isChecked():
            
            if('.' in self.result_2.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' mod ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' mod ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result_2.setText(result_add)

                
                operation_number = math.fmod(self.first_number, second_number)
                result_text = format(operation_number, '.15g')
                self.result_2.setText(result_text)

            self.mod.setChecked(False)

            

        else:
            self.result_2.setText("Invalid")
            

        self.user_secondNumber = False



    def factorial(self):
        self.top_result_2.setText(str("fact(" + self.result_2.text() + ')'))
        n_factorial = float(self.result_2.text())
        factorial_result = format(round(math.factorial(n_factorial), 13), '.15g')
        self.result_2.setText(factorial_result)
    

    def floors(self):
        self.top_result_2.setText(str("floor(" + self.result_2.text() + ')'))
        floor_bracks = float(self.result_2.text())
        floor_result = format(round(math.floor(floor_bracks), 13), '.15g')
        self.result_2.setText(floor_result)

    def ceiling(self):
        self.top_result_2.setText(str("ceiling(" + self.result_2.text() + ')'))
        ceiling_bracks = float(self.result_2.text())
        ceiling_result = format(round(math.ceil(ceiling_bracks), 13), '.15g')
        self.result_2.setText(ceiling_result)

    def exponential(self):
        self.top_result_2.setText(str("exp(" + self.result_2.text() + ')'))
        exponential_val = float(self.result_2.text())
        exp_result = format(round(math.exp(exponential_val), 10), '.15g')
        self.result_2.setText(exp_result)

    def sin_func(self):
        self.top_result_2.setText(str("sin(" + self.result_2.text() + ')'))
        sin_val = float(self.result_2.text())
        sin_result = format(round(math.sin(sin_val), 13), '.15g')
        self.result_2.setText(sin_result)

    def log_func(self):
        self.top_result_2.setText(str("log10(" + self.result_2.text() + ')'))
        log_val = float(self.result_2.text())
        log_result = format(round(math.log10(log_val), 13), '.15g')
        self.result_2.setText(log_result)
        

    def pi_func(self):
        pi_result = format(round(math.pi, 13), '.15g')
        self.result_2.setText(pi_result)

    def cos_func(self):
        self.top_result_2.setText(str("cos(" + self.result_2.text() + ')'))
        cos_val = float(self.result_2.text())
        cos_result = format(round(math.cos(cos_val), 13), '.15g')
        self.result_2.setText(cos_result)

    def tan_func(self):
        self.top_result_2.setText(str("tan(" + self.result_2.text() + ')'))
        tan_val = float(self.result_2.text())
        tan_result = format(round(math.tan(tan_val), 13), '.15g')
        self.result_2.setText(tan_result)

    def squared_func(self):
        self.top_result_2.setText(str("sqrt(" + self.result_2.text() + ')'))
        squared_val = int(self.result_2.text()) * int(self.result_2.text())
        squared_result = format(round(squared_val, 13), '.15g')
        self.result_2.setText(squared_result)

    def pow_func(self):
        self.top_result_2.setText(str("pow(" + self.result_2.text() + ')'))
        cube_val = int(self.result_2.text()) * int(self.result_2.text()) * int(self.result_2.text())
        cube_result = format(round(cube_val, 13), '.15g')
        self.result_2.setText(cube_result)

    def ln_func(self):
        self.top_result_2.setText(str("ln(" + self.result_2.text() + ')'))
        ln_val = float(self.result_2.text())
        ln_result = format(round(math.log(ln_val), 13), '.15g')
        self.result_2.setText(ln_result)


    def pow_ten_func(self):
        self.top_result_2.setText(str("10^" + self.result_2.text()))
        pow_ten_val = int(self.result_2.text())
        pow_result = format(round(math.pow(10, pow_ten_val), 13), '.15g')
        self.result_2.setText(pow_result)

    def one_func(self):
        self.top_result_2.setText(str("1/(" + self.result_2.text() + ')'))
        one_val = 1 / int(self.result_2.text())
        one_result = format(round(one_val, 13), '.15g')
        self.result_2.setText(one_result)


    def deg_func(self):
        self.top_result_2.setText(str("degrees(" + self.result_2.text() + ')'))
        deg_val = int(self.result_2.text())
        deg_result = format(round(math.degrees(deg_val), 13), '.15g')
        self.result_2.setText(deg_result)

    def rad_func(self):
        self.top_result_2.setText(str("radians(" + self.result_2.text() + ')'))
        rad_val = int(self.result_2.text())
        rad_result = format(round(round(math.radians(rad_val), 9), 13), '.15g')
        self.result_2.setText(rad_result)

    def sinh_func(self):
        self.top_result_2.setText(str("sinh(" + self.result_2.text() + ')'))
        sinh_val = float(self.result_2.text())
        sinh_result = format(round(math.sinh(sinh_val), 13), '.15g')
        self.result_2.setText(sinh_result)

    def cosh_func(self):
        self.top_result_2.setText(str("cosh(" + self.result_2.text() + ')'))
        cosh_val = float(self.result_2.text())
        cosh_result = format(round(math.cosh(cosh_val), 13), '.15g')
        self.result_2.setText(cosh_result)

    def tanh_func(self):
        self.top_result_2.setText(str("tanh(" + self.result_2.text() + ')'))
        tanh_val = float(self.result_2.text())
        tanh_result = format(round(math.tanh(tanh_val), 9), '.15g')
        self.result_2.setText(tanh_result)

    def square_root_func(self):
        self.top_result_2.setText(str("√(" + self.result_2.text() + ')'))
        square_val = float(self.result_2.text())
        square_result = format(round(math.sqrt(square_val), 13), '.15g')
        self.result_2.setText(square_result)

    def cube_root_func(self):
        cube_val = float(self.result_2.text())
        cube_result = format(round(math.sqrt(cube_val ** 3), 13) , '.15g')
        self.result_2.setText(cube_result)

    def e_func(self):
        self.top_result_2.setText(str("e(" + self.result_2.text() + ')'))
        e_result = format(round(math.e, 13), '.15g')
        self.result_2.setText(e_result)
        

    def inf_func(self):
        self.top_result_2.setText(str("inf(" + self.result_2.text() + ')'))
        inf_result = format(round(math.inf, 13), '.15g')
        self.result_2.setText(inf_result)
        
        
    def erf_func(self):
        self.top_result_2.setText(str("erf(" + self.result_2.text() + ')'))
        erf_val = float(self.result_2.text())
        erf_result = format(round(math.erf(erf_val), 13), '.15g')
        self.result_2.setText(erf_result)

    def abs_func(self):
        self.top_result_2.setText(str("abs(" + self.result_2.text() + ')'))
        abs_val = float(self.result_2.text())
        abs_result = format(round(math.fabs(abs_val), 13), '.15g')
        self.result_2.setText(abs_result)

    

    def Clear(self):
        self.addition.setChecked(False)
        self.subtract.setChecked(False)
        self.multiply.setChecked(False)
        self.divide.setChecked(False)

        self.user_secondNumber = False
        self.top_result_2.setText("")

    def Clear_E(self):
        self.addition.setChecked(False)
        self.subtract.setChecked(False)
        self.multiply.setChecked(False)
        self.divide.setChecked(False)

        self.user_secondNumber = False
        self.result_2.setText('0')
        self.top_result_2.setText("")



    #function for standard calculator
    def standard_cal(self):
        from Standard_calculator import StandardCalculatorWindow
        self.cal = StandardCalculatorWindow()
        self.cal.show()
        self.hide()
        
        




