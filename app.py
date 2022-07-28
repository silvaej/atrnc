
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
import sys

class App(QMainWindow):
    def __init__ (self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('69 -> LXIX')
        self.setFixedSize(500, 300)
        
        self.statusBar().showMessage('Hindu Arabic to Roman Numerals Conversion version 1.0')

        oImage = QImage(r'356843.jpg')
        sImage = oImage.scaled(QSize(500, 300))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        
        convertButton = QPushButton('Convert', self)
        convertButton.move(200, 180)
        convertButton.clicked.connect(self.showDialog)

        label = QLabel('Click the \'Convert\' button.', self)
        label.resize(200, 30)
        label.move(175, 150)
        label.setStyleSheet('color: white')

        self.le = QLineEdit(self)
        self.le.setAlignment(QtCore.Qt.AlignCenter)
        self.le.setEnabled(False)
        self.le.move(100, 100)
        self.le.resize(300, 50)
        self.le.setStyleSheet('color: black')

        self.show()

    def showDialog(self):
        num, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter a 4-digit number:')
        
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM', 'M(V)', '(V)', '(V)M', '(V)MM', '(V)MMM', 'M(X)']

        try:
            arabic = list(map(int, [x for x in str(num).zfill(4)]))
            if len(arabic) > 4:
                text = 'Max limit reached!'
            else:
                roman = [thousands[arabic[0]], hundreds[arabic[1]], tens[arabic[2]], ones[arabic[3]]]
                translated = ''
                for l in roman:
                    if l:
                        translated += l
                text = f'{num} -> {translated}'
        except Exception as e:
            text = 'Syntax Error!'
            
        if ok:
            self.le.setText(str(text))

            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Oxygen')
    ex = App()

    sys.exit(app.exec_())
        
