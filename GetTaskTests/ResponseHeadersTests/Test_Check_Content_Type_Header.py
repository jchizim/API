import requests
import nose

class Check_Content_Type_TestCase:

    def Test_Check_Content_Type_Header(self):
        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        nose.tools.assert_equals("application/json",response.headers["Content-Type"],"Test Failed. Content-Type should be application/json")

