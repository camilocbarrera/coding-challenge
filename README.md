# Coding Challenge

<!-- TOC -->
* [Coding Challenge](#coding-challenge)
* [Context](#context)
    * [Exercise](#exercise)
      * [Goal](#goal)
      * [Input/Ouput](#inputouput)
* [Solution](#solution)
  * [Architecture](#architecture)
    * [UML Diagram](#uml-diagram)
  * [Methodology](#methodology)
  * [Handle Data](#handle-data)
    * [Rules Data](#rules-data)
    * [Input Data](#input-data)
    * [Join Data](#join-data)
    * [Print results](#print-results)
  * [How to run this?](#how-to-run-this)
<!-- TOC -->

# Context

Exercise

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

Monday - Friday
00:01 - 09:00 25 USD
09:01 - 18:00 15 USD
18:01 - 00:00 20 USD

Saturday and Sunday
00:01 - 09:00 30 USD
09:01 - 18:00 20 USD
18:01 - 00:00 25 USD

### Exercise
#### Goal 
The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

MO: Monday
WE: Wednesday
TH: Thursday
FR: Friday
SA: Saturday
SU: Sunday

#### Input/Ouput

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.
Output: indicate how much the employee has to be paid

For example:
Case 1:

INPUT
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
The amount to pay ASTRID is: 85 USD

# Solution
The proposal to solve this exercise consists of abstracting through a simple MVC pattern. Different classes and methods to get a match between the given rules and the input data.

## Architecture
Slim (Model–view–controller) for abstract methods and class. This will allow changes to be made easily, because each module takes responsibility for its functions, creating low coupling and high cohesion.   
### UML Diagram
The following diagram shows the classes created that control each of the interacting elements.
<img width="819" alt="image" src="https://user-images.githubusercontent.com/85809276/223017865-faebc6db-e182-4e24-b278-1774fb50fe36.png">

## Methodology
To solve this challenge, try to imagine two data sets that could be joined. To do this, he first had to organize the data structures.

## Handle Data
### Rules Data
Heuristically I generate the data that contained the rules for the payroll.

This is loaded from the `generate_rules_dataset()` method of the model layer.

```python
 def generate_rules_dataset() -> Dict:
        """
        Generates a Dictionary DataFrame containing the rules for matching with input file.
        :return: A Dictionary DataFrame containing the data generated from heuristic rules.
        """
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
```
### Input Data
Then the method `generate_dataset()` Converts the data structure to a tabular format, note that the data comes in the form start_at, end_at. So what this method does is create one for the number of hours that exist between each range, for each day.

Eg. Notice how the record is increased by rows depending on the interval of start_at, end_at.
<img width="536" alt="image" src="https://user-images.githubusercontent.com/85809276/223019987-bc7df04e-b143-452e-b659-dc97ca734e40.png">
### Join Data
Finally, the two data sets are joined via the unique key (day_type ,hour). These are the two columns that are required to obtain the value of the USD rate in each time slot. 

Note how it is possible with this unique key to retrieve the values for each hour. After this it is only required to add by the name of the employee to add the payroll.

<img width="1052" alt="image" src="https://user-images.githubusercontent.com/85809276/223021169-69a1b9c5-8c25-4521-bfe9-773c05a756a0.png">


### Print results
The result of the joined data is a dictionary, which it is possible to iterate to group, this is done with the function `_aggregate_result(joined_dataset: Dict) -> Dict`. Which groups for each employee name. Adding the total hours worked.

<img width="643" alt="image" src="https://user-images.githubusercontent.com/85809276/223021847-a203d3b3-800f-4c02-9f92-10103a75da0c.png">

## How to run this?
To run this solution. Follow the steps below:

1. clone the repository with the command
```bash
git clone git@github.com:camilocbarrera/coding-challenge.git
```
2. Create and activate a virtual environment (Optional) the code uses the standard libraries of Python 3.9.xx It does not require other dependencies.
```bash
python3 -m venv venv
```
```bash
source ven/bin/activate
```
3. In case you want to use another test file data/constants.py update the FILE_NAME constant.
```python
FILE_NAME = './your_file_name.txt'
```
4. Run the code with the following command
```bash
python main.py
```