from Tools.LoginAuthentication import Login
import requests
import unittest
import random
import string

class GetUserSettings(unittest.TestCase):
    url = "http://crm01-ye.betconstruct.int:8085/api/User/GetUserSettings"

    def test_GetUserSettingsValidData(self):
        authentication = Login.LoginValidCases(self)
        response = requests.get(self.url,headers = {'Content-Type': 'application/json','Authentication':authentication})
        data = response.json()


        self.assertIn('Data',data)
        self.assertIn('HasError',data)
        self.assertIn('AlertType',data)
        self.assertIn('AlertMessage',data)
        self.assertIn('ModelErrors',data)
        self.assertEqual(None,data['Data'])
        self.assertEqual(False, data['HasError'])
        self.assertEqual("success",data['AlertType'])
        self.assertEqual(None,data['AlertMessage'])
        self.assertEqual(None,data['ModelErrors'])



    def test_GetUserSettingsInvalidData(self):
        char_set = string.ascii_uppercase + string.digits
        invalidAuthentication = ''.join(random.sample(char_set * 24, 24))
        response = requests.get(self.url,headers={'Content-Type': 'application/json','Authentication':invalidAuthentication})
        data = response.json()

        self.assertIn('Data', data)
        self.assertIn('HasError', data)
        self.assertIn('AlertType', data)
        self.assertIn('AlertMessage', data)
        self.assertIn('ModelErrors', data)
        self.assertIn('Message',data['Data'])
        self.assertEqual("Authorization has been denied for this request.",data['Data']['Message'])
        self.assertEqual(True, data['HasError'])
        self.assertEqual("alert", data['AlertType'])
        self.assertEqual("Authorization has been denied for this request.", data['AlertMessage'])
        self.assertEqual(None, data['ModelErrors'])



    def test_GetUserSettingsInvalidTypeOfRequest(self):

        authentication = Login.LoginValidCases(self)
        body = {"invalidKey": "invalidValue"}
        response = requests.post(self.url, data=body,headers={'Content-Type': 'application/json', 'Authentication': authentication})
        data = response.json()

        self.assertIn("HasError", data)
        self.assertIn("AlertType", data)
        self.assertIn("AlertMessage", data)
        self.assertIn("ModelErrors", data)
        self.assertEqual(True, data["HasError"])
        self.assertEqual("alert", data["AlertType"])
        self.assertEqual("The requested resource is not found", data["AlertMessage"])
        self.assertEqual(None, data["ModelErrors"])


if __name__ == '__main__':
    unittest.main()