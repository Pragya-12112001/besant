from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

app = QApplication([])

window = QWidget()
window.setWindowTitle('Q Buttons Examples')
window.resize(550, 250)

# Create buttons
info_btn = QPushButton('Information', window)
warning_btn = QPushButton('Warning', window)
critical_btn = QPushButton('Critical', window)

# Position buttons
info_btn.move(50, 50)
warning_btn.move(200, 50)
critical_btn.move(350, 50)

# Button functions
def info():
  QMessageBox.information(
    window,
    'Information',
    'Students marks were saved successfully'
  )

def warn():
  QMessageBox.warning(
    window,
    'Warning',
    'Please enter students name'
  )

def crit():
  QMessageBox.critical(
    window,
    'Error',
    'The database operation failed'
  )

# Connect buttons
info_btn.clicked.connect(info)
warning_btn.clicked.connect(warn)
critical_btn.clicked.connect(crit)

window.show()
app.exec_()