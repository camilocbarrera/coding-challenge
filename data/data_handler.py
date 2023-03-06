from typing import Dict, List
from datetime import datetime, timedelta
from .constants import WEEK_DAYS


class InputData:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file_to_list(self):
        with open(self.file_path, "r") as f:
            content = f.read().strip()
            rows_ = content.split('\n')
        return rows_


class GenerateDatasets:
    def __init__(self, content_input_list):
        self.content_input_list = content_input_list

    @property
    def generate_dataset(self) -> Dict:
        DataSet = Dict[str, List]
        input_dataset: DataSet = {
            'id': [],
            'employee': [],
            'day_type': [],
            'day_of_week': [],
            'start_at': [],
            'end_at': [],
            'hour': []
        }
        content_input_list: List = self.content_input_list

        for row in content_input_list:

            employee_name, data = row.split('=')

            for day in data.split(','):
                day_of_week = day[:2]
                start_at = day[2:7]
                end_at = day[8:]
                start_time = datetime.strptime(f"{start_at}:00", "%H:%M:%S")
                end_time = datetime.strptime(f"{end_at}:00", "%H:%M:%S")

                hour_list = []
                current_time = start_time

                # Augment with start_at, to end_at, for tabular denormalized shape
                while current_time < end_time:
                    hour_list.append(current_time)
                    current_time += timedelta(hours=1)

                for hh in hour_list:
                    hour = int(hh.strftime('%H'))
                    day_type = 'week_days' if day_of_week in WEEK_DAYS else 'weekend_days'

                    # add the data to the dataset dictionary
                    input_dataset['employee'].append(employee_name)
                    input_dataset['day_of_week'].append(day_of_week)
                    input_dataset['day_type'].append(day_type)
                    input_dataset['start_at'].append(start_at)
                    input_dataset['end_at'].append(end_at)
                    input_dataset['hour'].append(hour)
                    input_dataset['id'].append(day_type + '-' + str(hour))

        return input_dataset

    @staticmethod
    def generate_rules_dataset() -> Dict:
        range_day = ['week_days'] * 24 + ['weekend_days'] * 24
        hour = list(range(24)) * 2
        id = [range_day[i] + '-' + str(hour[i]) for i in range(len(range_day))]
        value_usd = [25] * 9 + [15] * 9 + [20] * 6 + [30] * 9 + [20] * 10 + [25] * 5

        DataSet = Dict[str, List]
        rules_dataset: DataSet = {
            'id': id,
            'range_day': range_day,
            'hour': hour,
            'value_usd': value_usd
        }
        return rules_dataset


class JoinDatasets:
    def __init__(self, dataset_a, dataset_b, key_join):
        self.dataset_a: Dict = dataset_a
        self.dataset_b: Dict = dataset_b
        self.key_join: str = key_join

    def join(self) -> Dict:
        """
        rules_dataset:dataset_a
        input_dataset:dataset_b
        :return:
        """

        rules_dataset = self.dataset_a
        input_dataset = self.dataset_b
        id = self.key_join

        # todo: abstract for any column
        data_resp = {'employee': [], 'value_usd': []}

        for i in range(len(rules_dataset[id])):
            for j in range(len(input_dataset[id])):
                if rules_dataset[id][i] == input_dataset[id][j]:
                    employee = input_dataset['employee'][j]
                    value_usd = rules_dataset['value_usd'][i]

                    data_resp['employee'].append(employee)
                    data_resp['value_usd'].append(value_usd)
        return data_resp


def _aggregate_result(joined_dataset: Dict) -> Dict:
    """

    :param joined_dataset:
    :return:
    """

    # todo: abstract for any column
    result: Dict = {}
    response: List = []
    employees: List = joined_dataset['employee']

    for i in range(len(employees)):
        employee = joined_dataset['employee'][i]
        value_usd = joined_dataset['value_usd'][i]

        if employee in result:
            result[employee] += value_usd
        else:
            result[employee] = value_usd

    return result
