import requests
import nose

class Check_Content_Type_TestCase:

    def Test_check_content_type_header(self):
        response = requests.get("http://localhost:5000/property/34/task",
                                params={'q': 'startDueDate=2015-01-01;endDueDate=2018-12-29'},
                                headers={"Accept": "application/json", "Authorization": "text.text.t"})

        nose.tools.assert_equals("application/json",response.headers["Content-Type"],"Test Failed. Content-Type should be application/json")






