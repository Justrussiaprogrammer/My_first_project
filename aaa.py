import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(150, 300, 1200, 600)
        self.setWindowTitle('Дневник')

        self.btn = QPushButton('Создать расписание дня', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(0, 330)
        self.btn.clicked.connect(self.create_schedule)

        self.name_label1 = QLabel(self)
        self.name_label1.setText("Введите расписание дня вида урок1/урок2/урок3/.../урок10")
        self.name_label1.move(0, 300)

        self.name_label2 = QLabel(self)
        self.name_label2.setText("Введите номер дня недели - от 1 до 7")
        self.name_label2.move(0, 270)

        self.error = QLabel(self)
        self.error.setText("Вид ошибки: Ошибок нет                                           ")
        self.error.move(0, 370)

        self.name_input1 = QLineEdit(self)
        self.name_input1.move(315, 300)

        self.name_input2 = QLineEdit(self)
        self.name_input2.move(200, 270)

        self.names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

        self.arr = []

        for j in range(7):
            self.label1 = QLabel(self)
            self.label1.setText(self.names[j])
            self.label1.move(20 + 180 * j, 20)

            self.labels = []

            for i in range(10):
                label = QLabel(self)
                label.setText(str(i + 1) + " урок -                                               ")
                label.move(0 + 180 * j, 50 + 20 * i)
                self.labels.append(label)

            self.arr.append(self.labels)

        self.name_answer = QLabel(self)
        self.name_answer.setText("В данном окне вы можете вводить свои комментарии к неделе, максимум - 48 символов")
        self.name_answer.move(500, 270)

        self.btn2 = QPushButton('Создайте комментарий', self)
        self.btn2.resize(self.btn.sizeHint())
        self.btn2.move(500, 330)
        self.btn2.clicked.connect(self.create_window_of_text)

        self.name_input_text = QLineEdit(self)
        self.name_input_text.move(500, 300)

        self.window_of_text = QLabel(self)
        self.window_of_text.setText("Тут пока ничего нет                                                              ")
        self.window_of_text.move(500, 370)

    def create_schedule(self):
        lessons = self.name_input1.text()
        number = self.name_input2.text()
        if not number.isdigit():
            self.error.setText("Вид ошибки: Вы ввели некорректный номер дня")
            return 0
        elif int(number) > 7 or int(number) < 1:
            self.error.setText("Вид ошибки: Дня под таким номером в неделе нет")
            return 0
        number = int(number) - 1
        mass = lessons.split('/')
        if len(mass) > 10:
            self.error.setText("Вид ошибки: Слишком много уроков")
        else:
            for i in range(len(mass)):
                self.arr[number][i].setText(str(i + 1) + " урок - {}".format(mass[i]))
            for j in range(i + 1, 10):
                self.arr[number][j].setText(str(j + 1) + " урок - ")
        self.error.setText("Вид ошибки: Ошибок нет")

    def create_window_of_text(self):
        text = self.name_input_text.text()
        self.window_of_text.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
