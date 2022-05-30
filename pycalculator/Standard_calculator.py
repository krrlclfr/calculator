from PyQt5 import QtWidgets
from standard_ui import Ui_Standard
import math
from Scientific_calculator import ScientificCalculator



class StandardCalculatorWindow(QtWidgets.QMainWindow, Ui_Standard):
    first_number = None
    user_secondNumber = False
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #clicked For all buttons
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
        self.modulus.clicked.connect(self.operations)

        self.addition.clicked.connect(self.operator)
        self.subtract.clicked.connect(self.operator)
        self.multiply.clicked.connect(self.operator)
        self.divide.clicked.connect(self.operator)

        #buttons for operator if the click is true
        self.addition.setCheckable(True)
        self.subtract.setCheckable(True)
        self.multiply.setCheckable(True)
        self.divide.setCheckable(True)

        self.Equal.clicked.connect(self.equals)
        
        self.exponent.clicked.connect(self.squard)
        self.exponent_one.clicked.connect(self.ex)
        self.square_root.clicked.connect(self.square)

        self.clear.clicked.connect(self.Clear)
        self.clear_Erase.clicked.connect(self.Clear_E)

        self.Scientific.clicked.connect(self.ScientificCal)


    #Operation for all buttons
    def numbers(self):
        number_button = self.sender()

        if ((self.addition.isChecked() or self.subtract.isChecked() or self.multiply.isChecked() or self.divide.isChecked())) and (not self.user_secondNumber):
            result_text = format(float(number_button.text()), '.15g')
            self.user_secondNumber = True

        else:
            if('.' in self.result.text()) and (number_button.text() == "0"):
                result_text = format(self.result.text() + number_button.text(), '.15')
            else:
                result_text = format(float(self.result.text() + number_button.text()), '.15g')
        self.result.setText(result_text)
        

    def decimal_point(self):
        self.result.setText(self.result.text() +  '.')

    def operations(self):
        number_button = self.sender()

        operation_number = float(self.result.text())

        if number_button.text() == '+/-':
            operation_number = operation_number * -1
        else:
            self.addition.setChecked(False)
            self.subtract.setChecked(False)
            self.multiply.setChecked(False)
            self.divide.setChecked(False)

            self.user_secondNumber = False
            operation_number = operation_number * 0.01

        result_text = format(operation_number, '.15g')
        self.result.setText(result_text)

    def operator(self):
        operator_button = self.sender()

        self.first_number = float(self.result.text())
        operator_button.setChecked(True)
        


    def equals(self):

        second_number = float(self.result.text())

        if self.addition.isChecked():
            if('.' in self.result.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' + ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)

                
                operation_number = self.first_number + second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' + ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)

                
                operation_number = self.first_number + second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)

            
            
            self.addition.setChecked(False)
            

            
            

        elif self.subtract.isChecked():
            if('.' in self.result.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' - ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)

                
                operation_number = self.first_number - second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            else:
            
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' - ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)
                
                operation_number = self.first_number - second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                

            self.subtract.setChecked(False)

        elif self.multiply.isChecked():

            if('.' in self.result.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' * ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)

                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            else:
            
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' * ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)
                
                operation_number = self.first_number * second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            self.multiply.setChecked(False)

        elif self.divide.isChecked():
            if('.' in self.result.text()):
                first_num = float(self.first_number)
                second_num = float(second_number)
                add_result = (str(first_num)) + ' / ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)

                
                operation_number = self.first_number / second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            else:
                first_num = int(self.first_number)
                second_num = int(second_number)
                add_result = (str(first_num)) + ' / ' + (str(second_num))
                print(add_result)
                result_add = format(add_result)
                self.top_result.setText(result_add)
                
                operation_number = self.first_number / second_number
                result_text = format(operation_number, '.15g')
                self.result.setText(result_text)
                
            self.divide.setChecked(False)       
            

        self.user_secondNumber = False
        
        
    def squard(self):
        squared = (int(self.result.text()) * int(self.result.text()))
        squared_result = format(round(squared, 13), '.15g')
        self.result.setText(squared_result)

    def ex(self):
        ex = (1 / int(self.result.text()))
        exs = format(round(ex, 13), '.15g')
        self.result.setText(exs)

    def square(self):
        square_root = float(self.result.text())
        square_result = format(round(math.sqrt(square_root), 13), '.15g')
        self.result.setText(square_result)
        

    def Clear(self):
        self.addition.setChecked(False)
        self.subtract.setChecked(False)
        self.multiply.setChecked(False)
        self.divide.setChecked(False)

        self.user_secondNumber = False
        self.top_result.setText("")

    def Clear_E(self):
        self.addition.setChecked(False)
        self.subtract.setChecked(False)
        self.multiply.setChecked(False)
        self.divide.setChecked(False)

        self.user_secondNumber = False
        self.result.setText('0')
        self.top_result.setText("")


    #Function for Scientific Calculator
    def ScientificCal(self):
        
        self.cal = ScientificCalculator()
        self.cal.show()
        self.hide()
        

        
              
        

        
        
        
        
        
        
        
