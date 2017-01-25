import requests
import nose

class Get_By_Query_String_TestCase:

    def Test_when_endDueDate_lessThan_startDueDate(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2018-12-30;endDueDate=2018-12-29"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_invalid_date(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2017-02-30;endDueDate=2018-12-20"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_invalid_date_format(self):

        response = requests.get("http://localhost:5000/property/35/task",
                                params={"q":"startDueDate=01-01-2015;endDueDate=29-12-2018"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_missing_startDueDate(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"endDueDate=2018-12-29"},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")
