import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Manikalkulator')

        self.btn = QPushButton('Вычислить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 330)
        self.btn.clicked.connect(self.summa)

        self.label1 = QLabel(self)
        self.label1.setText("Понедельник")
        self.label1.move(20, 20)

        self.label2 = QLabel(self)
        self.label2.setText("1 урок                           ")
        self.label2.move(0, 50)

        self.label3 = QLabel(self)
        self.label3.setText("2 урок")
        self.label3.move(0, 70)

        self.label4 = QLabel(self)
        self.label4.setText("3 урок")
        self.label4.move(0, 90)

        self.label5 = QLabel(self)
        self.label5.setText("4 урок")
        self.label5.move(0, 110)

        self.label6 = QLabel(self)
        self.label6.setText("5 урок")
        self.label6.move(0, 130)

        self.label7 = QLabel(self)
        self.label7.setText("6 урок")
        self.label7.move(0, 150)

        self.label8 = QLabel(self)
        self.label8.setText("7 урок")
        self.label8.move(0, 170)

        self.label9 = QLabel(self)
        self.label9.setText("8 урок")
        self.label9.move(0, 190)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Введите 1 число:")
        self.name_label1.move(0, 250)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(90, 250)

    def summa(self):
        number1 = self.name_input1.text()
        self.label2.setText("1 урок - {}".format(number1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
