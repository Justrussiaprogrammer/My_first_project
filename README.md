import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle('Дневник')

        self.btn = QPushButton('Создать расписание дня', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 330)
        self.btn.clicked.connect(self.create_schedule)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Введите расписание дня вида урок1/урок2/урок3/.../урок8")
        self.name_label1.move(0, 300)

        self.name_label2 = QLabel(self)
        self.name_label2.setText("Введите номер дня")
        self.name_label2.move(0, 270)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(310, 300)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(105, 270)

        self.label1 = QLabel(self)
        self.label1.setText("Понедельник")
        self.label1.move(20, 20)

        self.labels = []

        for i in range(10):
            label = QLabel(self)
            label.setText(str(i + 1) + " урок                                                ")
            label.move(0, 50 + 20 * i)
            self.labels.append(label)

        self.label1 = QLabel(self)
        self.label1.setText("Вторник")
        self.label1.move(220, 20)

        self.labels2 = []

        for i in range(10):
            label = QLabel(self)
            label.setText(str(i + 1) + " урок                                                ")
            label.move(200, 50 + 20 * i)
            self.labels2.append(label)

    def create_schedule(self):
        lessons = self.name_input1.text()
        mass = lessons.split('/')
        if len(mass) > 10:
            for i in range(10):
                self.labels[i].setText("Слишком много уроков")
        else:
            for i in range(len(mass)):
                self.labels[i].setText(str(i + 1) + " урок - {}".format(mass[i]))
            for j in range(i + 1, 10):
                self.labels[j].setText(str(j + 1) + " урок")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
