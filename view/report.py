from controller.payroll import PayrollController
from data.constants import FILE_NAME


class Report:
    """
    Report class
    """

    def __init__(self):
        """
        Initializes objects for testing
        """
        self.input_data = FILE_NAME
        self.controller = PayrollController(self.input_data)

    def show_report(self):
        """
        Organize dictionary and show report.
        :return: Print result from a dictionary
        """
        try:

            result = self.controller.generate_report()
            for employee, value_usd in result.items():
                print(f" The amount to pay {employee} is: {value_usd}")

        except ValueError:
            print("Debes verificar la estructura del archivo")
