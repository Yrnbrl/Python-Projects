# This Python file uses the following encoding: utf-8
import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

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

        self.original_image = None

        self.ui.verticalSlider.setMinimum(0)
        self.ui.verticalSlider.setMaximum(255)
        self.ui.verticalSlider.setValue(127)

        self.ui.pushButton.clicked.connect(self.open_image)
        self.ui.verticalSlider.valueChanged.connect(self.apply_thereshold)



    def open_image(self):
        file_name,_ = QFileDialog.getOpenFileName(
        self,
        "Resim seç",
        "",
        "Resim Dosyaları(*.png)"
        )
        if file_name:
         self.original_image=cv2.imread(file_name)
         cv2.imwrite('sonuc.png',self.original_image)
         self.ui.widget.setStyleSheet("border-image:url(sonuc.png);")



    def apply_thereshold(self, value):
        if self.original_image is None:
            return

        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        gereksiz_deger, thresh = cv2.threshold(gray, value,  255, cv2.THRESH_BINARY)
        #THRESH_TRUNC
        #THRESH_TOZERO
        cv2.imwrite('sonuc.png', thresh)
        self.ui.widget.setStyleSheet("border-image: url(sonuc.png)")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
