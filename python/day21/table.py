
import sys
import mysql.connector

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QLabel, QMessageBox
)


class StudentViewer(QWidget):

  def __init__(self):
    super().__init__()

    self.setWindowTitle('Student Records')
    self.resize(600, 400)

    # Create layout
    layout = QVBoxLayout()

    # Create table
    self.table = QTableWidget()
    layout.addWidget(self.table)

    self.setLayout(layout)
    # Load student records
    self.load_data()


  def load_data(self):
    cur = None
    con = None
    try:
      # Connect to MySQL
      con = mysql.connector.connect(
          host='localhost',
          user='root',
          password='12345',
          database='college'
      )

      cur = con.cursor()

      # Fetch records
      cur.execute('SELECT * FROM students order by id')

      records = cur.fetchall()

      # Get column names
      columns = [i[0] for i in cur.description]

      # Set table dimensions
      self.table.setRowCount(len(records))
      self.table.setColumnCount(len(columns))

      # Set headers
      self.table.setHorizontalHeaderLabels(columns)

      # Insert records
      for i, row_data in enumerate(records):
        for j, value in enumerate(row_data):
          item = QTableWidgetItem(str(value))

          self.table.setItem(i, j, item)

    
    except mysql.connector.Error as e:
      QMessageBox.critical(self, 'database error', str(e))
    finally:
      if cur:
        cur.close()
      if con and con.is_connected:
        con.close()


# Main application
app = QApplication(sys.argv)

window = StudentViewer()
window.show()

sys.exit(app.exec_())
