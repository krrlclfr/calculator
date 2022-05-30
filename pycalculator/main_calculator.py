import sys
from PyQt5.QtWidgets import QApplication

from Standard_calculator import StandardCalculatorWindow




app = QApplication(sys.argv)

calculator = StandardCalculatorWindow()


sys.exit(app.exec())
