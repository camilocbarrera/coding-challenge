import unittest
from controller.payroll import PayrollController


class TestPayrollController(unittest.TestCase):
    def setUp(self):
        self.input_data = "input.txt"

        self.controller = PayrollController(self.input_data)

    def test_generate_report(self):
        expected_report = {'RENE': 215, 'ASTRID': 85, 'PEDRO': 170, 'CRIS': 540, 'MELI': 1620}

        self.assertEqual(self.controller.generate_report(), expected_report)


if __name__ == '__main__':
    unittest.main()
