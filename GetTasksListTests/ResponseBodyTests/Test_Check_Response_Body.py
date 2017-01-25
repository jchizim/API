import requests
from datetime import datetime
import json
import nose

class Check_Response_Body_TestCase:

    def Test_check_due_on_values(self):
        response = requests.get("http://localhost:5000/property/34/task",
                                params={'q': 'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        tasks = response.json()

        for task in tasks:
            start = datetime(2015, 1, 1)
            end = datetime(2018, 12, 29)
            nose.tools.assert_false(datetime.strptime(task["dueOn"], '%Y-%m-%d') < start,"Test Failed. DueOn is not in query range.")
            nose.tools.assert_false(datetime.strptime(task["dueOn"], '%Y-%m-%d') > end,"Test Failed. DueOn is not in query range.")

    def Test_check_if_json(self):

        response = requests.get("http://localhost:5000/property/34/task",
                                params={'q': 'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        try:
            json.loads(response.text)
            nose.tools.assert_true(True)
        except ValueError as e:
            nose.tools.assert_true(False,'Test Failed. Invalid json')

    def Test_check_if_list(self):

        response = requests.get("http://localhost:5000/property/34/task",
                                params={'q': 'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})
        tasks = response.json()

        nose.tools.assert_true(isinstance(tasks, list),"Test Failed. Response should be a list")

    def Test_check_length_of_list(self):

        response = requests.get("http://localhost:5000/property/34/task",
                                params={'q': 'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})
        tasks = response.json()

        nose.tools.assert_equals(10,len(tasks),"Test Failed. Length should be 10")

