from Tools.LoginAuthentication import Login
from TestCases.GetPartners import GetPartners
import requests
import unittest
import random
import string
import json


class FindPlayer(unittest.TestCase):
    url = "http://crm01-ye.betconstruct.int:8085/api/Player/FindPlayer"

    def test_FindPlayerValidData(self):
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/FindPlayer"
        authentication = Login.LoginValidCases(self)
        body = {"Count": 50,"CreatedFrom": "","CreatedTo": "","Email": "","FirstName": "","GameStyles": [],"IsEmailPartial": True,"IsFirstNamePartial": True,"IsLastNamePartial": True,"IsMobilePhonePartial": True,"IsVerified": None,"LastName": "",
                    "LastSessionFrom": "","LastSessionTo": "","MobilePhone": None,"PartnerName": "","Partners": None,"PaymentTypeId": None,"PlayerId": None,"Start": 1,"WalletId": ""}
        response = requests.post(url,data=json.dumps(body),headers = {'Content-Type': 'application/json','Authentication':authentication})
        data = response.json()
        ID = []

        self.assertIn("Data",data)
        self.assertIn("TotalCount",data["Data"])
        self.assertIn("Players",data["Data"])
        for i in range(0,len(data["Data"]["Players"])):
            ID.append(data["Data"]["Players"][i]["Id"])
            self.assertIn("Id",data["Data"]["Players"][i])
            self.assertIsInstance(data["Data"]["Players"][i]["Id"],int)
            self.assertIn("FirstName",data["Data"]["Players"][i])
            self.assertIn("LastName",data["Data"]["Players"][i])
            self.assertIn("Email",data["Data"]["Players"][i])
            self.assertIn("MobilePhone",data["Data"]["Players"][i])
            self.assertIn("Created",data["Data"]["Players"][i])
            self.assertIn("IsVerified",data["Data"]["Players"][i])
            self.assertIn("LastSessionDate",data["Data"]["Players"][i])
            self.assertIn("Partner",data["Data"]["Players"][i])
            self.assertIn("Name",data["Data"]["Players"][i]["Partner"])
            self.assertIn("PartnerId",data["Data"]["Players"][i])
            self.assertIn("CurrentGameStyle",data["Data"]["Players"][i])
            self.assertIn("Documents",data["Data"]["Players"][i])
            if data["Data"]["Players"][i]["CurrentGameStyle"]!=None:
                self.assertIn("Id",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Name",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSelected",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsNested",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSubSelected",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Priority",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("SubId",data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("PlayerSubCategories",data["Data"]["Players"][i]["CurrentGameStyle"])

        return ID

    def test_FindPlayerValidDatawithValidID(self):
        Id = self.test_FindPlayerValidData()
        authentication = Login.LoginValidCases(self)
        body = {"Count": 50,"CreatedFrom": "","CreatedTo": "","Email": "","FirstName": "","GameStyles": [],"IsEmailPartial": True,"IsFirstNamePartial": True,"IsLastNamePartial": True,"IsMobilePhonePartial": True,"IsVerified": None,"LastName": "","LastSessionFrom": "","LastSessionTo": "","MobilePhone": None,"PartnerName": "","Partners": None,"PaymentTypeId": None,"PlayerId": random.choice(Id),"Start": 1,"WalletId": ""}
        response = requests.post(self.url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': authentication})
        data = response.json()

        self.assertIn("Data", data)
        self.assertIn("TotalCount", data["Data"])
        self.assertEqual(1,data["Data"]["TotalCount"])
        self.assertIn("Players", data["Data"])
        for i in range(0, len(data["Data"]["Players"])):
            self.assertIn("Id", data["Data"]["Players"][i])
            self.assertIsInstance(data["Data"]["Players"][i]["Id"], int)
            self.assertIn("FirstName", data["Data"]["Players"][i])
            self.assertIn("LastName", data["Data"]["Players"][i])
            self.assertIn("Email", data["Data"]["Players"][i])
            self.assertIn("MobilePhone", data["Data"]["Players"][i])
            self.assertIn("Created", data["Data"]["Players"][i])
            self.assertIn("IsVerified", data["Data"]["Players"][i])
            self.assertIn("LastSessionDate", data["Data"]["Players"][i])
            self.assertIn("Partner", data["Data"]["Players"][i])
            self.assertIn("Name", data["Data"]["Players"][i]["Partner"])
            self.assertIn("PartnerId", data["Data"]["Players"][i])
            self.assertIn("CurrentGameStyle", data["Data"]["Players"][i])
            self.assertIn("Documents", data["Data"]["Players"][i])
            if data["Data"]["Players"][i]["CurrentGameStyle"] != None:
                self.assertIn("Id", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Name", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsNested", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSubSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Priority", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("SubId", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("PlayerSubCategories", data["Data"]["Players"][i]["CurrentGameStyle"])



    def test_FindPlayerValidGameStyle(self):
        gameStyle = [11, 12, 25, 26, 27, 34, 35]
        authentication = Login.LoginValidCases(self)
        body = {"Count": 50, "CreatedFrom": "", "CreatedTo": "", "Email": "", "FirstName": "", "GameStyles": [random.choice(gameStyle)],"IsEmailPartial": True, "IsFirstNamePartial": True, "IsLastNamePartial": True,"IsMobilePhonePartial": True, "IsVerified": None, "LastName": "", "LastSessionFrom": "","LastSessionTo": "", "MobilePhone": None, "PartnerName": "", "Partners": None, "PaymentTypeId": None,"PlayerId": None, "Start": 1, "WalletId": ""}
        response = requests.post(self.url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': authentication})
        data = response.json()


        self.assertIn("Data", data)
        self.assertIn("TotalCount", data["Data"])
        self.assertIn("Players", data["Data"])
        for i in range(0, len(data["Data"]["Players"])):
            self.assertIn("Id", data["Data"]["Players"][i])
            self.assertIsInstance(data["Data"]["Players"][i]["Id"], int)
            self.assertIn("FirstName", data["Data"]["Players"][i])
            self.assertIn("LastName", data["Data"]["Players"][i])
            self.assertIn("Email", data["Data"]["Players"][i])
            self.assertIn("MobilePhone", data["Data"]["Players"][i])
            self.assertIn("Created", data["Data"]["Players"][i])
            self.assertIn("IsVerified", data["Data"]["Players"][i])
            self.assertIn("LastSessionDate", data["Data"]["Players"][i])
            self.assertIn("Partner", data["Data"]["Players"][i])
            self.assertIn("Name", data["Data"]["Players"][i]["Partner"])
            self.assertIn("PartnerId", data["Data"]["Players"][i])
            self.assertIn("CurrentGameStyle", data["Data"]["Players"][i])
            self.assertIn("Documents", data["Data"]["Players"][i])
            self.assertIn("Id", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("Name", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("IsSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("IsNested", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("IsSubSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("Priority", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("SubId", data["Data"]["Players"][i]["CurrentGameStyle"])
            self.assertIn("PlayerSubCategories", data["Data"]["Players"][i]["CurrentGameStyle"])


    def test_FindPlayerVslidPartnerId(self):
        # PartnerId = GetPartners.test_GetPartnersValidData(self)
        PartnerId = [1,4,128,333]
        authentication = Login.LoginValidCases(self)
        for i in PartnerId:
            body = {"Count": 5, "CreatedFrom": "", "CreatedTo": "", "Email": "", "FirstName": "",
                    "GameStyles": [], "IsEmailPartial": True, "IsFirstNamePartial": True,
                    "IsLastNamePartial": True, "IsMobilePhonePartial": True, "IsVerified": None, "LastName": "",
                    "LastSessionFrom": "", "LastSessionTo": "", "MobilePhone": None, "PartnerName": "",
                    "Partners": [i], "PaymentTypeId": None, "PlayerId": None, "Start": 1, "WalletId": ""}
            response = requests.post(self.url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': authentication})
            data = response.json()
            print(data)

        self.assertIn("Data", data)
        self.assertIn("TotalCount", data["Data"])
        self.assertIn("Players", data["Data"])
        for i in range(0, len(data["Data"]["Players"])):
            self.assertIn("Id", data["Data"]["Players"][i])
            self.assertIsInstance(data["Data"]["Players"][i]["Id"], int)
            self.assertIn("FirstName", data["Data"]["Players"][i])
            self.assertIn("LastName", data["Data"]["Players"][i])
            self.assertIn("Email", data["Data"]["Players"][i])
            self.assertIn("MobilePhone", data["Data"]["Players"][i])
            self.assertIn("Created", data["Data"]["Players"][i])
            self.assertIn("IsVerified", data["Data"]["Players"][i])
            self.assertIn("LastSessionDate", data["Data"]["Players"][i])
            self.assertIn("Partner", data["Data"]["Players"][i])
            self.assertIn("Name", data["Data"]["Players"][i]["Partner"])
            self.assertIn("PartnerId", data["Data"]["Players"][i])
            if data["Data"]["Players"][i]["CurrentGameStyle"] != None:
                self.assertIn("Id", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Name", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsNested", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("IsSubSelected", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("Priority", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("SubId", data["Data"]["Players"][i]["CurrentGameStyle"])
                self.assertIn("PlayerSubCategories", data["Data"]["Players"][i]["CurrentGameStyle"])






if __name__ == '__main__':
    unittest.main()