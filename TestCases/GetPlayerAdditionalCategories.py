from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.FIndPlayer import FindPlayer
import random
import string

class GetPlayerAdditionalCategories(unittest.TestCase):

    def test_GetPlayerAdditionalCategoriesValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/GetPlayerAdditionalCategories?PlayerId=" + str(random.choice(clientIdList))
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        print(data)


        self.assertIn("Data",data)
        self.assertIn('HasError', data)
        self.assertIn('AlertType', data)
        self.assertIn('AlertMessage', data)
        self.assertIn('ModelErrors', data)
        if data["Data"] != []:
            for i in range(0,len(data["Data"])):
                self.assertIn("Id",data["Data"][i])
                self.assertIn("AdditionaId", data["Data"][i])
                self.assertIn("CategoryId", data["Data"][i])
                self.assertIn("PartnerId", data["Data"][i])
                self.assertIn("PlayerId", data["Data"][i])
                self.assertIn("Created", data["Data"][i])
                self.assertIn("CategoryName",data["Data"][i])
                self.assertIn("LiveLimit", data["Data"][i])
                self.assertIn("Delay", data["Data"][i])




