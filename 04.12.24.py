# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.ders_button.clicked.connect(self.func1)
        self.ui.sum.clicked.connect(self.sum)
        self.ui.ext.clicked.connect(self.ext)
        self.ui.multi.clicked.connect(self.multi)
        self.ui.divide.clicked.connect(self.divide)

        self.count=0



    def func1(self):
        self.count=self.count+1
        self.ui.label.setText(str(self.count))


    def sum(self):
        self.num1=float(self.ui.number1.text())
        self.num2=float(self.ui.number2.text())
        self.sum=self.num1+self.num2
        self.ui.result.setText(str(self.sum))

    def ext(self):
         self.num1=float(self.ui.number1.text())
         self.num2=float(self.ui.number2.text())
         self.ext=self.num1-self.num2
         self.ui.result.setText(str(self.ext))

    def multi(self):
         self.num1=float(self.ui.number1.text())
         self.num2=float(self.ui.number2.text())
         self.multi=self.num1*self.num2
         self.ui.result.setText(str(self.multi))

    def divide(self):
         self.num1=float(self.ui.number1.text())
         self.num2=float(self.ui.number2.text())
         self.divide=self.num1/self.num2
         self.ui.result.setText(str(self.divide))






if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
