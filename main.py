#!/usr/bin/python3

import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import images_rc


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleinput(self.text))
        self.results.returnPressed.connect(self.do_math)

    def handleinput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "C":
            self.results.setText("")
        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)

    def do_math(self):
        res = eval(self.results.text())
        self.results.setText(str(res))


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qalculator")
        self.setWindowIcon(QIcon(':/img/qalc.png'))
        self.blabel = QLabel("Qalculator 1.0 by Ivaylo Vasilev")
        self.createapp()

    def createapp(self):

        # Create the grid
        grid = QGridLayout()
        results = QLineEdit()

        buttons = ["C", "DEL", "√", "/",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "="]

        grid.addWidget(results, 0, 0, 1, 4)

        row = 1
        col = 0

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            buttonobject = Button(button, results)

            if button == 0:
                grid.addWidget(buttonobject.b, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(buttonobject.b, row, col, 1, 1)

            col += 1

        grid.addWidget(self.blabel, 6, 0, 1, 4)

        self.setLayout(grid)

        self.show()


app = QApplication(sys.argv)
window = Application()
with open("style.css", "r") as style:
    app.setStyleSheet(style.read())

sys.exit(app.exec_())
