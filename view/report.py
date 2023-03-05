from controller.payroll import PayrollController
from data.constants import FILE_NAME


def show_report():
    """

    :return:
    """
    input_data = FILE_NAME
    payroll_controller = PayrollController(input_data)

    result = payroll_controller.generate_report()
    for employee, value_usd in result.items():
        print(f" The amount to pay {employee} is: {value_usd}")
