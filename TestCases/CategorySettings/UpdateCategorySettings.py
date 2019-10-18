from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.CategorySettings.GetRMTPartners import GetRMTPartners
import json
import string
from random import choice
from random import sample
from random import *


class UpdateCategorySettings(unittest.TestCase):

    def test_UpdateFinanceCategorySettingsValidData(self):
        auth = Login.LoginValidCases(self)
        Id=GetRMTPartners.test_GetRMTPartners(self)
        char_set = string.ascii_uppercase + string.digits
        description = ''.join(sample(char_set*6, 6))
        url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/Update"
        Category = [{"CategoryId":1,"Name":"Neutral","SportbookProfileId":1},{"CategoryId":2,"Name":"Positive","SportbookProfileId":2},{"CategoryId":3,"Name":"Negative","SportbookProfileId":3},{"CategoryId":4,"Name":"Very negative","SportbookProfileId":37},{"CategoryId":5,"Name":"VIP Bronze","SportbookProfileId":5},{"CategoryId":6,"Name":"VIP Silver","SportbookProfileId":5},{"CategoryId":7,"Name":"VIP Gold","SportbookProfileId":5},{"CategoryId":8,"Name":"VIP Platinum","SportbookProfileId":5}]
        for j in Id:
            for i in range(0,len(Category)):
                body = {"CategoryId":Category[i]["CategoryId"],"SportbookProfileId":Category[i]["SportbookProfileId"],"Name":Category[i]["Name"],"Description":description,"Type":1,"Balance":randint(10,100),"Share":randint(10,100),"AvgBet":randint(10,100),"BetCount":randint(10,50),"Limit":randint(10,100),"Delay":randint(10,100),"PlayerCategoryGroupId":8,"ReportPartnerId":j,"Priority":1,"Editing":False,"PlayerSubCategories":[]}
                response = requests.post(url,data=json.dumps(body), headers={'Content-Type': 'application/json', 'Authentication': auth})
                data = response.json()


                if j == 57:

                    continue

                else:
                    self.assertIn("Data",data)
                    self.assertIn("CategoryId",data["Data"])
                    self.assertIn("SportbookProfileId",data["Data"])
                    self.assertIn("Name", data["Data"])
                    self.assertIn("Description", data["Data"])
                    self.assertIn("Type", data["Data"])
                    self.assertIn("Balance", data["Data"])
                    self.assertIn("Share", data["Data"])
                    self.assertIn("AvgBet", data["Data"])
                    self.assertIn("BetCount", data["Data"])
                    self.assertIn("Limit", data["Data"])
                    self.assertIn("Delay", data["Data"])
                    self.assertIn("PlayerCategoryGroupId", data["Data"])
                    self.assertIn("Priority", data["Data"])
                    self.assertIn("PlayerSubCategories", data["Data"])



    def test_UpdateGameStyleLevel0CategorySettingsValidData(self):
        auth = Login.LoginValidCases(self)
        Id = GetRMTPartners.test_GetRMTPartners(self)
        char_set = string.ascii_uppercase + string.digits
        description = ''.join(sample(char_set * 6, 6))
        url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/Update"
        Category = [{"CategoryId": 11, "Name": "Arbitrage Betting", "SportbookProfileId": 11},{"CategoryId": 12, "Name": "SFM", "SportbookProfileId": 12},{"CategoryId": 25, "Name": "Corridor", "SportbookProfileId": 25},{"CategoryId": 26, "Name": "Late Betting", "SportbookProfileId": 26},{"CategoryId": 27, "Name": "Strong Opinion", "SportbookProfileId": 27},{"CategoryId": 34, "Name": "Bot Arbitrage", "SportbookProfileId": 34},{"CategoryId": 35, "Name": "Bonus Hunter", "SportbookProfileId": 35}]
        for j in Id:
            for i in range(0, len(Category)):
                body = {"CategoryId": Category[i]["CategoryId"],"SportbookProfileId": Category[i]["SportbookProfileId"], "Name": Category[i]["Name"],"Description": description, "Type": 1, "Balance": randint(10, 100), "Share": randint(10, 100),"AvgBet": randint(10, 100), "BetCount": randint(10, 50), "Limit": randint(10, 100),"Delay": randint(10, 100), "PlayerCategoryGroupId": 8, "ReportPartnerId": j, "Priority": 1,"Editing": False, "PlayerSubCategories": []}
                response = requests.post(url, data=json.dumps(body), headers={'Content-Type': 'application/json', 'Authentication': auth})
                data = response.json()


                if j == 57:
                    continue

                else:
                    self.assertIn("Data",data)
                    self.assertIn("CategoryId",data["Data"])
                    self.assertIn("SportbookProfileId",data["Data"])
                    self.assertIn("Name", data["Data"])
                    self.assertIn("Description", data["Data"])
                    self.assertIn("Type", data["Data"])
                    self.assertIn("Balance", data["Data"])
                    self.assertIn("Share", data["Data"])
                    self.assertIn("AvgBet", data["Data"])
                    self.assertIn("BetCount", data["Data"])
                    self.assertIn("Limit", data["Data"])
                    self.assertIn("Delay", data["Data"])
                    self.assertIn("PlayerCategoryGroupId", data["Data"])
                    self.assertIn("Priority", data["Data"])
                    self.assertIn("PlayerSubCategories", data["Data"])



























