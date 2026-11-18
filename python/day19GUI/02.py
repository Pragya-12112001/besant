from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()

label = QLabel('wlecom to python GUI', window)
label.move(30, 30)

window.setWindowTitle('label example')
window.resize(350, 150)

window.show()

app.exec_()