from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])
window = QWidget()

btn = QPushButton('click me', window)
btn.move(30, 30)

window.setWindowTitle('push button example')
window.resize(250, 150)

window.show()

app.exec_()