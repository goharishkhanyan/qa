from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.CategorySettings.GetCategorySettings import GetCategorySettings
import json
import string
from random import choice
from random import sample
from random import *


class UpdateAdditionalSettings(unittest.TestCase):

    def test_UpdateAdditionalSettingsWomenValidData(self):
        auth = Login.LoginValidCases(self)
        Ids, CurrencyId,Currencies, Countries = GetCategorySettings.test_GetAdditionalCategoryValidData(self)
        boolean = [True,False]
        char_set = string.ascii_uppercase + string.digits
        description = ''.join(sample(char_set*6, 6))
        url = "http://crm01-ye.betconstruct.int:8085/api/AdditionalSettings/EditWomen"
        for j in range(0,len(Ids)):
            body = {"Enabled":choice(boolean),"Limit":randint(0,100),"Delay":randint(0,50),"PartnerId":Ids[j]["PartnerId"],"Id":Ids[j]["Id"]}

            response = requests.post(url,data=json.dumps(body), headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()


            self.assertIn("Data",data)
            self.assertIn("HasError",data)
            self.assertIn("AlertType",data)
            self.assertIn("AlertMessage",data)
            self.assertIn("ModelErrors",data)
            self.assertIn("Id",data["Data"])
            self.assertIn("Limit",data["Data"])
            self.assertIn("AdditionalId",data["Data"])
            self.assertIn("Delay",data["Data"])
            self.assertIn("Enabled",data["Data"])


    def test_UpdateAdditionalSettingsAgeValidData(self):
        auth = Login.LoginValidCases(self)
        Ids, CurrencyId,Currencies, Countries = GetCategorySettings.test_GetAdditionalCategoryValidData(self)
        boolean = [True,False]
        char_set = string.ascii_uppercase + string.digits
        description = ''.join(sample(char_set*6, 6))
        url = "http://crm01-ye.betconstruct.int:8085/api/AdditionalSettings/EditAge"
        for j in range(0,len(Ids)):
            body = {"Age":randint(10,100),"Enabled":choice(boolean),"Limit":randint(0,100),"Delay":randint(0,50),"PartnerId":Ids[j]["PartnerId"],"Id":Ids[j]["Id"]}

            response = requests.post(url,data=json.dumps(body), headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()
            print(data)


            self.assertIn("Data",data)
            self.assertIn("HasError",data)
            self.assertIn("AlertType",data)
            self.assertIn("AlertMessage",data)
            self.assertIn("ModelErrors",data)
            self.assertIn("Id",data["Data"])
            self.assertIn("Limit",data["Data"])
            self.assertIn("AdditionalId",data["Data"])
            self.assertIn("Delay",data["Data"])
            self.assertIn("Enabled",data["Data"])


    def test_UpdateAdditionalSettingsCountryValidData(self):
        auth = Login.LoginValidCases(self)
        Ids = GetCategorySettings.test_AddAdditionalCountry(self)
        boolean = [True, False]
        char_set = string.ascii_uppercase + string.digits
        description = ''.join(sample(char_set * 6, 6))
        url = "http://crm01-ye.betconstruct.int:8085/api/AdditionalSettings/EditCountry"
        for j in range(0, len(Ids)):
            body = {"Enabled":choice(boolean),"Limit":randint(10,30),"RegionId":Ids[j]["RegionId"],"Name":Ids[j]["Name"],"Delay":randint(10,30),"PartnerId":Ids[j]["PartnerId"],"Id":Ids[j]["Id"]}
            response = requests.post(url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()

            self.assertIn("Data", data)
            self.assertIn("HasError", data)
            self.assertIn("AlertType", data)
            self.assertIn("AlertMessage", data)
            self.assertIn("ModelErrors", data)
            self.assertIn("AdditionalCategorySettingId", data["Data"])
            self.assertIn("Name", data["Data"])
            self.assertIn("Code", data["Data"])
            self.assertIn("RegionId", data["Data"])
            self.assertIn("AdditionalId", data["Data"])
            self.assertIn("Id", data["Data"])
            self.assertIn("Limit", data["Data"])
            self.assertIn("Delay", data["Data"])
            self.assertIn("Enabled", data["Data"])


