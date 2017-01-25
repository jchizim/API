import requests
import nose

class Request_Headers_TestCase:

    def Test_when_invalid_header_value(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/xml", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(406,response.status_code,"Test Failed. Status Code should be 406")

    def Test_when_missing_header_value(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": ""})

        nose.tools.assert_equals(401,response.status_code,"Test Failed. Status Code should be 401")

    def Test_when_missing_authorization_header(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/json"})

        nose.tools.assert_equals(401,response.status_code,"Test Failed. Status Code should be 401")

    def Test_when_missing_accept_header(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(406,response.status_code,"Test Failed. Status Code should be 406")