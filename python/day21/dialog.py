from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QMessageBox, QLineEdit, QVBoxLayout,
    QLabel, QDialog
)

app = QApplication([])


class NameDialog(QDialog):
  def __init__(self):
    super().__init__()

    self.setWindowTitle('Enter Name')

    layout = QVBoxLayout()

    # Create an input field
    self.name_field = QLineEdit()
    self.name_field.setPlaceholderText("Enter your name")

    layout.addWidget(self.name_field)

    # Create OK button
    btn = QPushButton('OK')
    btn.clicked.connect(self.accept)

    layout.addWidget(btn)

    self.setLayout(layout)


dialog = NameDialog()

if dialog.exec_() == QDialog.Accepted:
    print('Entered name:', dialog.name_field.text())

app.exec_()

# model - we have to click on the ok button to close the dialog and do other things
# modeless - we can deo otherthings too