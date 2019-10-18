from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.FIndPlayer import FindPlayer
import random
import string

class GetManualSettings(unittest.TestCase):

    def test_GetManualSettings(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/PlayerManualCategory/GetPlayerManualSettings?playerID="+str(random.choice(clientIdList))
        response = requests.get(url,headers ={'Content-Type': 'application/json','Authentication':auth} )
        data = response.json()
        print(data)



        self.assertIn("Data",data)
        self.assertIn('HasError', data)
        self.assertIn('AlertType', data)
        self.assertIn('AlertMessage', data)
        self.assertIn('ModelErrors', data)
        self.assertIn("PlayerId",data["Data"])
        self.assertIn("CurrentCategoryName",data["Data"])
        self.assertIn("Modified",data["Data"])
        self.assertIn("IsSelected",data["Data"])
        self.assertIn("Level",data["Data"])
