import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('My 1st GUI')
window.setGeometry(200, 200, 400, 250)

window.show()

sys.exit(app.exec_())