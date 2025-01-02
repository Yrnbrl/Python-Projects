# This Python file uses the following encoding: utf-8
import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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
        self.fig = Figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self.ui.widget1)
        self.canvas.resize(self.ui.widget1.size())
        self.ui.spinBox1.valueChanged.connect(self.update_plot)
        self.plot_example(self.ui.spinBox1.value())


    def plot_example(self,frequency):
        self.fig.clear()
        x = np.linspace(0, 1, 100)
        y= np.sin(2*np.pi * x*frequency)
        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(f'Frekans: {frequency}')
        ax.grid(True)
        ax.set_ylim(-1,1)
        self.canvas.draw()



    def update_plot(self,value):
        self.plot_example(value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
