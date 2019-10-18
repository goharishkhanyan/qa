from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.FIndPlayer import FindPlayer
import random
import string

class GetKPIChart(unittest.TestCase):

    def test_GetKPIChartValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/GetKpiChart?playerId="+str(random.choice(clientIdList))
        response = requests.get(url,headers ={'Content-Type': 'application/json','Authentication':auth} )
        data = response.json()
        print(data)



        self.assertIn("Data",data)
        self.assertIn("Profit",data["Data"])
        self.assertIn('HasError', data)
        self.assertIn('AlertType', data)
        self.assertIn('AlertMessage', data)
        self.assertIn('ModelErrors', data)
        if data["Data"]["Profit"]!=[]:
            for i in range(0,len(data["Data"]["Profit"])):
                self.assertIn("Date",data["Data"]["Profit"][i])
                self.assertIn("Value", data["Data"]["Profit"][i])



