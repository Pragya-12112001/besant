import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QRadioButton

app = QApplication(sys.argv)
window = QWidget()

window.setWindowTitle('checkbox and radio btn')
window.setGeometry(200, 200, 450, 250)

hostel = QCheckBox('hostel required', window)
hostel.move(30, 30)

transport = QCheckBox('transport required', window)
transport.move(30, 50)


full_time = QRadioButton('full time', window)
full_time.move(30, 100)
transport = QRadioButton('part time', window)
transport.move(30, 120)


window.show()
sys.exit(app.exec_())