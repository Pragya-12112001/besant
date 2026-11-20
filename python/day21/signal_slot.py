from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

app = QApplication([])
window = QWidget()

window.setWindowTitle('push button example')
window.resize(550, 150)

def show_mess():
  QMessageBox.information(window, 'message', 'button was clicked')

btn = QPushButton('click me', window)
btn.clicked.connect(show_mess)

window.show()
app.exec_()

# signal - event that is generated when a user interacts with a widget
# slot - function that is called when a signal is generated