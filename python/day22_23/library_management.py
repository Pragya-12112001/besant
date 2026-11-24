import sys
import mysql.connector

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTableWidget, QTableWidgetItem, QMessageBox,
    QPushButton, QLineEdit, QFormLayout,
    QAbstractItemView, QHeaderView
)


class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("Library Management System")
        self.resize(800, 600)

        # Database connection
        self.connect_db()

        # Create UI
        self.create_interface()

        # Load existing records
        self.load_books()

    # ---------------- DATABASE CONNECTION ----------------
    def connect_db(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345",
                database="library"
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
        self.book_name_input = QLineEdit()
        self.author_input = QLineEdit()

        # Form layout
        form = QFormLayout()

        form.addRow("Book Name:", self.book_name_input)
        form.addRow("Author:", self.author_input)

        # Buttons
        self.add_button = QPushButton("Add")
        self.update_button = QPushButton("Update")
        self.delete_button = QPushButton("Delete")
        self.clear_button = QPushButton("Clear Fields")

        # Connect buttons to methods
        self.add_button.clicked.connect(self.add_book)
        self.update_button.clicked.connect(self.update_book)
        self.delete_button.clicked.connect(self.delete_book)
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
            ["ID", "Book Name", "Author"]
        )

        # Select complete row
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )
        self.table.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        # Stretch columns
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # When a row is clicked
        self.table.cellClicked.connect(self.select_book)

        # Main layout
        main_layout = QVBoxLayout()

        main_layout.addLayout(form)
        main_layout.addLayout(btns)
        main_layout.addWidget(self.table)

        self.setLayout(main_layout)

    # ---------------- LOAD BOOKS ----------------
    def load_books(self):
        try:
            self.cur.execute(
                "SELECT * FROM books ORDER BY id"
            )

            records = self.cur.fetchall()

            self.table.setRowCount(len(records))

            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):

                    self.table.setItem(
                        row_idx,
                        col_idx,
                        QTableWidgetItem(str(col_data))
                    )

        except mysql.connector.Error as err:
            QMessageBox.critical(
                self, "Error", str(err)
            )

    # ---------------- SELECT BOOK ----------------
    def select_book(self, row):
        self.book_name_input.setText(
            self.table.item(row, 1).text()
        )

        self.author_input.setText(
            self.table.item(row, 2).text()
        )

    # ---------------- VALIDATE INPUT ----------------
    def validate_input(self):
        book_name = self.book_name_input.text().strip()
        author = self.author_input.text().strip()

        if not book_name:
            QMessageBox.warning(
                self,
                "Warning",
                "Enter book name!"
            )
            return None

        if not author:
            QMessageBox.warning(
                self,
                "Warning",
                "Enter author name!"
            )
            return None

        return book_name, author

    # ---------------- ADD BOOK ----------------
    def add_book(self):
        data = self.validate_input()

        if data is None:
            return

        book_name, author = data

        try:
            sql = """
                INSERT INTO books (book_name, author)
                VALUES (%s, %s)
            """

            self.cur.execute(
                sql,
                (book_name, author)
            )

            self.con.commit()

            QMessageBox.information(
                self,
                "Success",
                "Book added successfully!"
            )

            self.load_books()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()

            QMessageBox.critical(
                self,
                "Error",
                str(err)
            )

    # ---------------- UPDATE BOOK ----------------
    def update_book(self):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a book first!"
            )
            return

        data = self.validate_input()

        if data is None:
            return

        book_name, author = data

        book_id = self.table.item(
            selected_row, 0
        ).text()

        try:
            sql = """
                UPDATE books
                SET book_name = %s, author = %s
                WHERE id = %s
            """

            self.cur.execute(
                sql,
                (book_name, author, book_id)
            )

            self.con.commit()

            QMessageBox.information(
                self,
                "Success",
                "Book updated successfully!"
            )

            self.load_books()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()

            QMessageBox.critical(
                self,
                "Error",
                str(err)
            )

    # ---------------- DELETE BOOK ----------------
    def delete_book(self):
        selected_row = self.table.currentRow()

        if selected_row < 0:
            QMessageBox.warning(
                self,
                "Warning",
                "Please select a book first!"
            )
            return

        book_id = self.table.item(
            selected_row, 0
        ).text()

        book_name = self.table.item(
            selected_row, 1
        ).text()

        # Ask for confirmation
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete {book_name}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        try:
            sql = "DELETE FROM books WHERE id = %s"

            self.cur.execute(
                sql,
                (book_id,)
            )

            self.con.commit()

            QMessageBox.information(
                self,
                "Success",
                "Book deleted successfully!"
            )

            self.load_books()
            self.clear_fields()

        except mysql.connector.Error as err:
            self.con.rollback()

            QMessageBox.critical(
                self,
                "Error",
                str(err)
            )

    # ---------------- CLEAR FIELDS ----------------
    def clear_fields(self):
        self.book_name_input.clear()
        self.author_input.clear()

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

    window = LibraryApp()
    window.show()

    sys.exit(app.exec_())