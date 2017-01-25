import requests
import nose

class Get_By_Header_TestCase:

    def Test_when_invalid_header_value(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2016-12-20;endDueDate=2017-12-20"},
                                headers={"Accept": "application/xml", "Authorization": "text.text.t"})

        nose.tools.assert_equals(406,response.status_code,"Test Failed. Status Code should be 406")

    def Test_when_missing_header_value(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2016-12-20;endDueDate=2017-12-20"},
                                headers={"Accept": "application/json", "Authorization": ""})

        nose.tools.assert_equals(401,response.status_code,"Test Failed. Status Code should be 401")

    def Test_when_missing_authorization_header(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2016-12-20;endDueDate=2017-12-20"},
                                headers={"Accept": "application/json"})

        nose.tools.assert_equals(401,response.status_code,"Test Failed. Status Code should be 401")

    def Test_when_missing_accept_header(self):
        response = requests.get("http://localhost:5000/property/32/task",
                                params={"q":"startDueDate=2016-12-20;endDueDate=2017-12-20"},
                                headers={"Authorization": "text.text.t"})

        nose.tools.assert_equals(406,response.status_code,"Test Failed. Status Code should be 406")

