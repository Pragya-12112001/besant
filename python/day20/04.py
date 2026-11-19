import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout

app = QApplication(sys.argv)
window = QWidget()

layout = QHBoxLayout()
layout.addWidget(QLabel('student registration'))
layout.addWidget(QPushButton('save'))
layout.addWidget(QPushButton('cancle'))

window.setLayout(layout)

window.show()
sys.exit(app.exec_())