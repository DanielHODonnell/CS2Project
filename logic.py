from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    Main logic for the sales tax calculator application.
    """
    def __init__(self) -> None:
        """
        Initializes the application and connects button clicks to functions
        """
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.calculate_tax)
        self.exit_button.clicked.connect(self.close)
        self.reset_button.clicked.connect(self.clear_input)
        self.help_button.clicked.connect(self.help)

    def calculate_tax(self) -> None:
        """
        Calculates sales tax based on the user's input and city selected.
        :return: None
        """
        input_text = self.input_num.text()
        if input_text:
            try:
                num = float(input_text)
                if num < 0:
                    raise TypeError('Please enter a positive number.')
                elif num == 0:
                    raise TypeError('Please enter a non-zero number.')

            except ValueError as e:
                QtWidgets.QMessageBox.warning(
                    None,
                    "Warning",
                    "Please enter a valid number."
                )
                return
            except TypeError as e:
                QtWidgets.QMessageBox.warning(
                    None,
                    "Warning",
                    str(e)
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

    def clear_input(self) -> None:
        """
        Clears user's input in text box.
        :return: None
        """
        self.input_num.clear()

    def help(self) -> None:
        """
        Displays help message.
        :return: None
        """
        QtWidgets.QMessageBox.information(
            None,
            "Help Box",
            "(All calculations are done in dollars)\nsales tax = initial price * tax\ntotal = initial price + sales tax"
        )
