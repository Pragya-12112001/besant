import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle('text input example')
window.setGeometry(200, 200, 450, 250)

name_field = QLineEdit(window)
name_field.move(30, 30)
name_field.resize(300, 30)
name_field.setPlaceholderText('enter student name: ')

comment_field = QTextEdit(window)
comment_field.move(30, 80)
comment_field.resize(300, 120)
comment_field.setPlaceholderText('enter comments: ')


window.show()
sys.exit(app.exec_())