import requests
import nose

class Get_By_PropertyId_And_TaskId_TestCase:

    def Test_when_missing_propertyId(self):

        response = requests.get("http://localhost:5000/property//task",
                                params={"q":'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(404,response.status_code,"Test Failed. Status Code should be 404")

    def Test_when_negative_propertyId(self):

        response = requests.get("http://localhost:5000/property/-35/task",
                                params={"q":"startDueDate=2015-01-01;endDueDate=2018-12-29"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_propertyId_contains_character(self):

        response = requests.get("http://localhost:5000/property/df35/task",
                                params={"q":"startDueDate=2015-01-01;endDueDate=2018-12-29"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_propertyId_contains_space(self):

        response = requests.get("http://localhost:5000/property/3 5/task",
                                params={"q":"startDueDate=2015-01-01;endDueDate=2018-12-29"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

