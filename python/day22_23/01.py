
import sys
import mysql.connector

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QMessageBox,
    QPushButton, QLineEdit, QFormLayout,
    QAbstractItemView, QHeaderView
)


class StudentApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Student Management System")
        self.resize(800, 600)

        # Database connection
        self.connect_db()

        # Create UI
        self.create_interface()

        # Load existing records
        self.load_students()

    # ---------------- DATABASE CONNECTION ----------------
    def connect_db(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="college"
            )

            self.cur = self.con.cursor()

        except mysql.connector.Error as err:
            QMessageBox.critical(
                self, "Database Error", str(err)
            )
            raise SystemExit(1)

    # ---------------- CREATE INTERFACE ----------------
    def create_interface(self):
        # Input fields
        self.name_input = QLineEdit()
        self.marks_input = QLineEdit()

        # Form layout
        form = QFormLayout()

        form.addRow("Student Name:", self.name_input)
        form.addRow("Student Marks:", self.marks_input)

        # Buttons
        self.add_button = QPushButton("Add")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")
        self.clear_button = QPushButton("Clear Fields")

        # Connect buttons to methods
        self.add_button.clicked.connect(self.add_student)
        self.update_button.clicked.connect(self.update_student)
        self.delete_button.clicked.connect(self.delete_student)
        self.clear_button.clicked.connect(self.clear_fields)

        # Button layout
        btns = QHBoxLayout()
        btns.addWidget(self.add_button)
        btns.addWidget(self.update_button)
        btns.addWidget(self.delete_button)
        btns.addWidget(self.clear_button)

        # Table widget
        self.table = QTableWidget()

        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Student Name", "Marks"]
        )

        # this is new for selection of the current row and perform events 
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.cellClicked.connect(self.select_student)

        # Main layout
        main_layout = QVBoxLayout()

        main_layout.addLayout(form)
        main_layout.addLayout(btns)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    # ---------------- LOAD STUDENTS ----------------
    def load_students(self):
        try:
            self.cur.execute(
                "SELECT * FROM students ORDER BY id"
            )

            records = self.cur.fetchall() # this returns tuples of records

            self.table.setRowCount(len(records))

            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):

                    self.table.setItem(
                        row_idx,
                        col_idx,
                        QTableWidgetItem(str(col_data))
                    )

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", str(err))

    # ---------------- SELECT STUDENT ----------------
    def select_student(self, row):
        self.name_input.setText(
            self.table.item(row, 1).text()
        )

        self.marks_input.setText(
            self.table.item(row, 2).text()
        )

    # ---------------- VALIDATE INPUT ----------------
    def validate_input(self):
        name = self.name_input.text().strip()
        marks_text = self.marks_input.text().strip()

        if not name:
            QMessageBox.warning(
                self, "Warning", "Enter student name!"
            )
            return None

        try:
            marks = int(marks_text)

        except ValueError:
            QMessageBox.warning(
                self, "Warning", "Marks must be an integer!"
            )
            return None

        if marks < 0 or marks > 100:
            QMessageBox.warning(
                self, "Warning",
                "Marks must be between 0 and 100!"
            )
            return None

        return name, marks

    # ---------------- ADD STUDENT ----------------
    def add_student(self):
        data = self.validate_input()

        if data is None:
            return

        name, marks = data

        try:
            sql = """
                INSERT INTO students (name, marks)
                VALUES (%s, %s)
            """

            self.cur.execute(sql, (name, marks))
            self.con.commit()

            QMessageBox.information(
                self, "Success",
                "Student added successfully!"
            )

            self.load_students()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()
            QMessageBox.critical(self, "Error", str(err))

    # ---------------- UPDATE STUDENT ----------------
    def update_student(self):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self, "Warning",
                "Please select a student first!"
            )
            return

        data = self.validate_input()

        if data is None:
            return

        name, marks = data

        student_id = self.table.item(
            selected_row, 0
        ).text()

        try:
            sql = """
                UPDATE students
                SET name = %s, marks = %s
                WHERE id = %s
            """

            self.cur.execute(
                sql, (name, marks, student_id)
            )

            self.con.commit()

            QMessageBox.information(
                self, "Success",
                "Student updated successfully!"
            )

            self.load_students()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()
            QMessageBox.critical(self, "Error", str(err))

    # ---------------- DELETE STUDENT ----------------
    def delete_student(self):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self, 
                "Warning",
                "Please select a student first!"
            )
            return

        student_id = self.table.item(
            selected_row, 0
        ).text()

        student_name = self.table.item(
            selected_row, 1
        ).text()

        # Ask for confirmation
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete {student_name}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        try:
            sql = "DELETE FROM students WHERE id = %s"

            self.cur.execute(sql, (student_id,))
            self.con.commit()

            QMessageBox.information(
                self, "Success",
                "Student deleted successfully!"
            )

            self.load_students()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()
            QMessageBox.critical(self, "Error", str(err))

    # ---------------- CLEAR FIELDS ----------------
    def clear_fields(self):
        self.name_input.clear()
        self.marks_input.clear()

        self.table.clearSelection()

    # ---------------- CLOSE DATABASE ----------------
    def closeEvent(self, event):
        if self.cur:
            self.cur.close()

        if self.con and self.con.is_connected():
            self.con.close()

        event.accept()


# ---------------- MAIN APPLICATION ----------------
if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = StudentApp()
    window.show()

    sys.exit(app.exec_())