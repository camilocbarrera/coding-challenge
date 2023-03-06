import unittest
from controller.payroll import PayrollController


class TestPayrollController(unittest.TestCase):
    """
    Responsible to taste different uses cases of payroll and assert output.
    """

    def setUp(self):
        """
        Initializes objects for testing
        """
        self.input_data = "tests/input_tests_cases.txt"

        self.controller = PayrollController(self.input_data)

    def test_generate_report(self):
        """
        Test to generate datasets output and validate with input_test_cases.txt
        :return:  assert expected output
        """
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
