import requests
import json
import nose

class Check_Response_Body_TestCase:

    def Test_Check_If_Json(self):
        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})


        try:
            json.loads(response.text)
            nose.tools.assert_true(True, "ResponseBody is json")
        except ValueError as e:
            nose.tools.assert_true(False,'Test Failed. Invalid json')


    def Test_Check_TaskId_Value(self):

        response = requests.get("http://localhost:5000/property/23/task/369-tak-20172",
                                headers={"Accept": "application/json", "Authorization": "Bearer test.json.test"})

        task = response.json()

        nose.tools.assert_equals('369-tak-20172',task["id"],"Test Failed.TaskId is incorrect")

