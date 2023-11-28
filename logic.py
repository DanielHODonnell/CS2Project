from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.calculate_tax)
        self.exit_button.clicked.connect(self.close)
        self.reset_button.clicked.connect(self.clear_input)
        self.help_button.clicked.connect(self.help)

    def calculate_tax(self):
        global num
        input_text = self.input_num.text()
        if input_text:
            try:
                num = float(input_text)
            except ValueError:
                QtWidgets.QMessageBox.warning(
                    None,
                    "Warning",
                    "Please enter a valid number"
                )
                return
        else:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning",
                "Please enter a number"
            )
            return

        selected_city = self.comboBox_city.currentText()
        tax_rates = {
            "No city": 0.055,
            "Omaha": 0.07,
            "Lincoln": 0.0725,
            "Bellevue": 0.07,
            "Grand Island": 0.075,
            "Kearney": 0.07,
            "Fremont": 0.07,
            "Norfolk": 0.07,
            "Hastings": 0.07,
            "Columbus": 0.07,
            "Papillion": 0.075
        }
        if selected_city in tax_rates:
            tax_rate = tax_rates[selected_city]
            sales_tax = num * tax_rate
            total = num + sales_tax
            QtWidgets.QMessageBox.information(
                None,
                "Sales Tax",
                f"Sales Tax in {selected_city}: ${total:.2f}"
            )
        else:
            QtWidgets.QMessageBox.warning(
                None,
                "Warning",
                "Please select a valid city"
            )

    def clear_input(self):
        self.input_num.clear()

    def help(self):
        QtWidgets.QMessageBox.information(
            None,
            "Help Box",
            "(All calculations are done in dollars)\nsales tax = initial price * tax\ntotal = initial price + sales tax",
        )
