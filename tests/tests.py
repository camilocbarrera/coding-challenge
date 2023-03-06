import unittest
from controller.payroll import PayrollController


class TestPayrollController(unittest.TestCase):
    def setUp(self):
        self.input_data = "tests/input_tests_cases.txt"

        self.controller = PayrollController(self.input_data)

    def test_generate_report(self):
        expected_report = {
            'RENE': 645,
            'ASTRID': 255,
            'PEDRO': 600,
            'CRIS': 1620,
            'MELI': 4860
        }

        self.assertEqual(self.controller.generate_report(), expected_report)


if __name__ == '__main__':
    unittest.main()
