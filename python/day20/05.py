import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('grid layout example')
window.resize(400, 600)

name_input = QLineEdit()
age_input = QLineEdit()
course_input = QLineEdit()

layout = QGridLayout()
layout.addWidget(QLabel('name'), 0,0)
layout.addWidget(name_input, 0,1)

layout.addWidget(QLabel('age'), 1,0)
layout.addWidget(age_input, 1,1)

layout.addWidget(QLabel('course'), 2,0)
layout.addWidget(course_input, 2,1)

submit_btn = QPushButton('submit')
layout.addWidget(submit_btn, 3, 1)


window.setLayout(layout)

window.show()
sys.exit(app.exec_())