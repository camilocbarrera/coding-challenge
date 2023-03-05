from data.data_handler import InputData, GenerateDatasets, JoinDatasets, _aggregate_result
from typing import Dict


class PayrollController:
    def __init__(self, input_data: str):
        self.input_data = input_data

    def generate_report(self):
        """

        :return:
        """
        input_data = InputData(self.input_data)
        GenerateDatasets(input_data.read_file_to_list())
        datasets = GenerateDatasets(input_data.read_file_to_list())

        input_ds = datasets.generate_dataset
        rules_ds = datasets.generate_rules_dataset()
        joined_ds = JoinDatasets(rules_ds, input_ds, 'id').join()
        aggregated_report = _aggregate_result(joined_ds)

        return aggregated_report
