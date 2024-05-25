# Form implementation generated from reading ui file 'rentbook.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QFileDialog, QCalendarWidget, QMessageBox, QDialog
from datetime import date

class RentBookDialog(object):
    def setupUi(self, RentBook):
        self.dialog = RentBook
        RentBook.setObjectName("RentBook")
        RentBook.resize(580, 367)
        RentBook.setStyleSheet("background:rgb(72, 72, 72)")
        self.label_4 = QtWidgets.QLabel(parent=RentBook)
        self.label_4.setGeometry(QtCore.QRect(29, 85, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.Confirm = QtWidgets.QPushButton(parent=RentBook)
        self.Confirm.setGeometry(QtCore.QRect(60, 310, 221, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Confirm.setFont(font)
        self.Confirm.setStyleSheet("QPushButton {\n"
                                   "                background-color: rgb(6, 217, 66);\n"
                                   "                color: white;\n"
                                   "                border: none;\n"
                                   "                border-radius: 5px;\n"
                                   "                padding: 10px;\n"
                                   "            }\n"
                                   "            QPushButton:hover {\n"
                                   "                background-color: rgb(50, 255, 100);\n"
                                   "            }")
        self.Confirm.setFlat(False)
        self.Confirm.setObjectName("Confirm")
        self.label_5 = QtWidgets.QLabel(parent=RentBook)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.bookscbox = QtWidgets.QComboBox(parent=RentBook)
        self.bookscbox.setGeometry(QtCore.QRect(170, 90, 371, 22))
        self.bookscbox.setStyleSheet(" background: white; color:black;")
        self.bookscbox.setObjectName("bookscbox")
        self.Cancel = QtWidgets.QPushButton(parent=RentBook)
        self.Cancel.setGeometry(QtCore.QRect(310, 310, 231, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("QPushButton {\n"
                                  "                background-color: rgb(200, 46, 18);\n"
                                  "                color: white;\n"
                                  "                border: none;\n"
                                  "                border-radius: 5px;\n"
                                  "                padding: 10px;\n"
                                  "            }\n"
                                  "            QPushButton:hover {\n"
                                  "                background-color: rgb(255, 100, 100);\n"
                                  "            }")
        self.Cancel.setObjectName("Cancel")
        self.customersbox = QtWidgets.QComboBox(parent=RentBook)
        self.customersbox.setGeometry(QtCore.QRect(170, 126, 371, 22))
        self.customersbox.setStyleSheet(" background: white; color:black;")
        self.customersbox.setObjectName("customersbox")
        self.label_6 = QtWidgets.QLabel(parent=RentBook)
        self.label_6.setGeometry(QtCore.QRect(80, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.frame = QtWidgets.QFrame(parent=RentBook)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 591, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(50, 50, 50);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(230, 0, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.rentfeefield = QtWidgets.QLineEdit(parent=RentBook)
        self.rentfeefield.setGeometry(QtCore.QRect(170, 165, 371, 22))
        self.rentfeefield.setStyleSheet(" background: white; color: black;")
        self.rentfeefield.setFrame(False)
        self.rentfeefield.setObjectName("rentfeefield")
        self.label_7 = QtWidgets.QLabel(parent=RentBook)
        self.label_7.setGeometry(QtCore.QRect(80, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=RentBook)
        self.label_8.setGeometry(QtCore.QRect(341, 208, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:white;")
        self.label_8.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.startdate = QtWidgets.QPushButton(parent=RentBook)
        self.startdate.setGeometry(QtCore.QRect(180, 206, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.startdate.setFont(font)
        self.startdate.setStyleSheet("QPushButton {\n"
                                     "                background-color: rgb(255, 170, 0);\n"
                                     "                color: white;\n"
                                     "                border: none;\n"
                                     "                border-radius: 5px;\n"
                                     "                padding: 10px;\n"
                                     "            }\n"
                                     "            QPushButton:hover {\n"
                                     "                background-color: rgb(255, 196, 78);\n"
                                     "            }")
        self.startdate.setFlat(False)
        self.startdate.setObjectName("startdate")
        self.duedate = QtWidgets.QPushButton(parent=RentBook)
        self.duedate.setGeometry(QtCore.QRect(370, 206, 151, 40))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.duedate.setFont(font)
        self.duedate.setStyleSheet("QPushButton {\n"
                                   "                background-color: rgb(76, 94, 255);\n"
                                   "                color: white;\n"
                                   "                border: none;\n"
                                   "                border-radius: 5px;\n"
                                   "                padding: 10px;\n"
                                   "            }\n"
                                   "            QPushButton:hover {\n"
                                   "                background-color:rgb(106, 153, 255);\n"
                                   "            }")
        self.duedate.setFlat(False)
        self.duedate.setObjectName("duedate")

        self.retranslateUi(RentBook)
        QtCore.QMetaObject.connectSlotsByName(RentBook)

        
        self.bookscbox.currentIndexChanged.connect(self.update_rent_fee)
        

        # Set the current date as the text of the start date button
        self.startdate.setText(QDate.currentDate().toString(QtCore.Qt.DateFormat.ISODate))

        # Disable the start date button
        self.startdate.setEnabled(False)

        self.duedate.clicked.connect(self.select_due_date)
        self.Confirm.clicked.connect(self.confirm_rent)
        self.Cancel.clicked.connect(self.dialog.close)

        self.populate_books_combo_box()
        self.populate_customers_combo_box()

    def retranslateUi(self, RentBook):
        _translate = QtCore.QCoreApplication.translate
        RentBook.setWindowTitle(_translate("RentBook", "Rent Book"))
        self.label_4.setText(_translate("RentBook", "Available Books:"))
        self.Confirm.setText(_translate("RentBook", "Confirm"))
        self.label_5.setText(_translate("RentBook", "Customer:"))
        self.Cancel.setText(_translate("RentBook", "Cancel"))
        self.label_6.setText(_translate("RentBook", "Rent Fee:"))
        self.label.setText(_translate("RentBook", "Rent Book"))
        self.label_7.setText(_translate("RentBook", "Rent Date:"))
        self.label_8.setText(_translate("RentBook", "to"))
        self.startdate.setText(_translate("RentBook", "Start Date"))
        self.duedate.setText(_translate("RentBook", "Due Date"))

    

    

    def select_due_date(self):
        try:
            # Create a calendar dialog
            calendar_dialog = QDialog()
            calendar_dialog.setWindowTitle("Select Return Date")
            calendar = QCalendarWidget(calendar_dialog)
            calendar.setGeometry(10, 10, 400, 250)

            # Create a button to confirm the date selection
            select_button = QtWidgets.QPushButton("Select Date", calendar_dialog)
            select_button.setGeometry(150, 270, 100, 30)
            select_button.clicked.connect(lambda: self.on_duedate_selected(calendar, calendar_dialog))

            # Show the calendar dialog
            calendar_dialog.exec()
        except Exception as e:
            print(e)

    def on_duedate_selected(self, calendar, dialog):
        # Get the selected date from the calendar widget
        selected_date = calendar.selectedDate()

        # If no date is selected, return without setting the button text
        if not selected_date.isValid():
            return

        # Format the selected date as a string
        formatted_date = selected_date.toString(QtCore.Qt.DateFormat.ISODate)

        # Set the selected date as the text of the due date button
        self.duedate.setText(formatted_date)

        # Store the selected return date in a class variable for later use
        self.selected_due_date = formatted_date

        # Close the dialog
        dialog.accept()

    def confirm_rent(self):
        try:
            # Convert QDate objects to strings in ISO format
            rent_date_str = self.startdate.text()
            due_date_str = self.selected_due_date
            

            # Check if due_date is None
            if self.selected_due_date is None:
                QMessageBox.warning(self.dialog, "Error", "Please select a due date.")
                return
                
            book_title = self.bookscbox.currentText()
            customer_name = self.customersbox.currentText()
            rent_fee = self.rentfeefield.text()

            print("Book Title:", book_title)
            print("Customer Name:", customer_name)
            print("Rent Fee:", rent_fee)
            print("Rent Date:", rent_date_str)
            print("Due Date:", due_date_str)

            # Calculate the number of days between rentalDate and rentalDueDate
            rent_date = date.fromisoformat(rent_date_str)
            due_date = date.fromisoformat(self.selected_due_date)
            days_between = (due_date - rent_date).days
            
            print("Days between:", days_between)

            # Connect to the database
            conn = sqlite3.connect("library.db")
            c = conn.cursor()

            try:
                # Fetch the CustomerID based on the selected customer's name
                c.execute("SELECT CustomerID FROM customers WHERE Name = ?", (customer_name,))
                customer_id_result = c.fetchone()
                if customer_id_result is None:
                    QMessageBox.warning(self.dialog, "Error", "Customer not found")
                    return

                customer_id = customer_id_result[0]

                # Fetch the BookID based on the selected book's title
                c.execute("SELECT BookID, RentalFee, Status FROM books WHERE Title = ?", (book_title,))
                book_info_result = c.fetchone()
                if book_info_result is None:
                    QMessageBox.warning(self.dialog, "Error", "Book not found")
                    return

                book_id, rental_fee, book_status = book_info_result

                print("Book ID:", book_id)
                print("Rental Fee from Database:", rental_fee)
                print("Book Status:", book_status)
                
                # Check if the book is available for rent
                if book_status != 'Available':
                    QMessageBox.warning(self.dialog, "Error", "Book is not available for rent.")
                    return

                # Check if the book is reserved for the selected date
                c.execute("SELECT CustomerID FROM reserve WHERE BookID = ? AND ReservationDate = ?", (book_id, rent_date))
                reserved_customer_id = c.fetchone()
                if reserved_customer_id is not None:
                    QMessageBox.warning(self.dialog, "Error", "Book is reserved for another customer on the selected date.")
                    return

                # Calculate the final fee in terms of rent days
                final_rent_fee = days_between * rental_fee
                print("Final Rent Fee:", final_rent_fee)

                # Proceed to insert the rental record
                c.execute(
                    "INSERT INTO rentals (CustomerID, BookID, RentalDate, RentalDueDate, RentalFee) VALUES (?, ?, ?, ?, ?)",
                    (customer_id, book_id, rent_date_str, due_date_str, final_rent_fee)
                )

                # Update the status of the book to 'Rented'
                c.execute("UPDATE books SET Status = 'Rented' WHERE BookID = ?", (book_id,))
                print("Success!")
                conn.commit()
                conn.close()
                self.dialog.accept()

            except sqlite3.Error as e:
                QMessageBox.critical(self.dialog, "Error", f"Error renting book: {e}")

            except Exception as e:
                QMessageBox.critical(self.dialog, "Error", f"An unexpected error occurred: {e}")

        except Exception as e:
            print("Error here pi: ", e)

    def populate_customers_combo_box(self):
        # Clear existing items in the combo box
        self.customersbox.clear()

        conn = sqlite3.connect("library.db")
        c = conn.cursor()

        # Execute a query to fetch customers who are in good standing from the database
        c.execute("SELECT Name FROM customers")

        # Fetch all customer names from the executed query
        customer_names = c.fetchall()

        # Iterate through the fetched customer names and add them to the combo box
        for customer_name in customer_names:
            self.customersbox.addItem(customer_name[0])

    def populate_books_combo_box(self):
        # Clear existing items in the combo box
        self.bookscbox.clear()

        conn = sqlite3.connect("library.db")
        c = conn.cursor()

        # Execute a query to fetch book titles with status "Available" from the database
        c.execute("SELECT Title FROM books WHERE Status = 'Available'")

        # Fetch all titles from the executed query
        titles = c.fetchall()

        # Iterate through the fetched titles and add them to the combo box
        for title in titles:
            self.bookscbox.addItem(title[0])

    def get_rental_fee(self, book_name):
        try:
            # Create connection to database
            conn = sqlite3.connect("library.db")
            c = conn.cursor()
            
            # Fetch the rental fee from the database based on the book ID
            c.execute("SELECT RentalFee FROM books WHERE Title = ?", (book_name,))
            rental_fee = c.fetchone()[0]

            conn.close()
            return rental_fee

        except sqlite3.Error as e:
            print("Error fetching rental fee:", e)
            return None
        
    def update_rent_fee(self):
        # Get the selected book title
        try:
            selected_book_title = self.bookscbox.currentText()

            # Fetch the rental fee of the selected book from the database
            rental_fee = self.get_rental_fee(selected_book_title)

            # If rental fee is found, set it as the text of the rent fee entry field
            if rental_fee is not None:
                self.rentfeefield.setText(str(rental_fee))
            else:
                self.rentfeefield.setText("")  # Clear the field if no rental fee is found
        except Exception as e:
            print("Error occured sa pag cbox chuchu:",e)


    def select_due_date(self):
        try:
            # Create a calendar dialog
            calendar_dialog = QDialog()
            calendar_dialog.setWindowTitle("Select Return Date")
            calendar = QCalendarWidget(calendar_dialog)
            calendar.setGeometry(10, 10, 400, 250)

            # Set minimum date to current date
            calendar.setMinimumDate(QDate.currentDate())

            # Create a button to confirm the date selection
            select_button = QtWidgets.QPushButton("Select Date", calendar_dialog)
            select_button.setGeometry(150, 270, 100, 30)
            select_button.clicked.connect(lambda: self.on_duedate_selected(calendar, calendar_dialog))

            # Show the calendar dialog
            calendar_dialog.exec()
        except Exception as e:
            print(e)