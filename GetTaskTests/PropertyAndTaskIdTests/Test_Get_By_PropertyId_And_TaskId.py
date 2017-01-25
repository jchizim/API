import requests
import nose

class Get_By_PropertyId_And_TaskId_TestCase:

    def Test_when_missing_propertyId(self):

        response = requests.get("http://localhost:5000/property//task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(404, response.status_code, "Test Failed. Status Code should be 404")

    def Test_when_negative_propertyId(self):

        response = requests.get("http://localhost:5000/property/-23/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(400, response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_propertyId_contains_character(self):

        response = requests.get("http://localhost:5000/property/2h%3/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(400, response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_propertyId_contains_space(self):

        response = requests.get("http://localhost:5000/property/2 3/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(400,response.status_code,"Test Failed. Status Code should be 400")

    def Test_when_taskId_invalid(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-2017233",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals(404,response.status_code,"Test Failed. Status Code should be 404")




