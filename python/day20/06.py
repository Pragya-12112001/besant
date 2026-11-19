import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('form layout example')
window.resize(400, 180)

name_input = QLineEdit()
email_input = QLineEdit()
phone_input = QLineEdit()

layout = QFormLayout()
layout.addRow('name', name_input)
layout.addRow('age', email_input)
layout.addRow('course', phone_input)

window.setLayout(layout)

window.show()
sys.exit(app.exec_())