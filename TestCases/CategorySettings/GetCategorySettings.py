from Tools.LoginAuthentication import Login
import requests
import unittest
from TestCases.CategorySettings.GetRMTPartners import GetRMTPartners
from random import choice
from random import sample
from random import *
import json



class GetCategorySettings(unittest.TestCase):

    def test_GetFinancialCategoryValidData(self):
        auth = Login.LoginValidCases(self)
        Id=GetRMTPartners.test_GetRMTPartners(self)
        for i in Id:
            url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/FinanceSettings?PartnerId="+str(i)
            response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()
            if i == 57:
                self.assertEqual([],data["Data"])

            else:
                self.assertIn("Data",data)
                self.assertIn("HasError",data)
                self.assertIn("AlertType",data)
                self.assertIn("ModelErrors",data)
                for i in range(0,len(data["Data"])):
                    self.assertIn("CategoryId",data["Data"][i])
                    self.assertIn("SportbookProfileId",data["Data"][i])
                    self.assertIn("Name",data["Data"][i])
                    self.assertIn("Description",data["Data"][i])
                    self.assertIn("Type",data["Data"][i])
                    self.assertIn("Balance", data["Data"][i])
                    self.assertIn("Share", data["Data"][i])
                    self.assertIn("AvgBet", data["Data"][i])
                    self.assertIn("BetCount", data["Data"][i])
                    self.assertIn("Limit", data["Data"][i])
                    self.assertIn("Delay", data["Data"][i])
                    self.assertIn("PlayerCategoryGroupId", data["Data"][i])
                    self.assertIn("Delay", data["Data"][i])
                    self.assertIn("ReportPartnerId", data["Data"][i])
                    self.assertIn("Priority", data["Data"][i])
                    self.assertIn("Editing", data["Data"][i])
                    self.assertIn("PlayerSubCategories", data["Data"][i])
                    self.assertIsInstance(data["Data"][i]["CategoryId"],int)
                    self.assertIsInstance(data["Data"][i]["SportbookProfileId"], int)
                    self.assertIsInstance(data["Data"][i]["ReportPartnerId"],int)
                    self.assertIsInstance(data["Data"][i]["Name"], str)
                    self.assertIsInstance(data["Data"][i]["PlayerCategoryGroupId"], int)



    def test_GetGameStyleCategoryValidData(self):
        auth = Login.LoginValidCases(self)
        Id = GetRMTPartners.test_GetRMTPartners(self)
        for i in Id:
            url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GameStyleSettings?PartnerId=" + str(i)
            response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()
            print(data)

            if i == 57:
                self.assertEqual([],data["Data"])

            else:
                self.assertIn("Data",data)
                self.assertIn("HasError",data)
                self.assertIn("AlertType",data)
                self.assertIn("ModelErrors",data)
                for i in range(0,len(data["Data"])):
                    self.assertIn("CategoryId",data["Data"][i])
                    self.assertIn("SportbookProfileId",data["Data"][i])
                    self.assertIn("Name",data["Data"][i])
                    self.assertIn("Description",data["Data"][i])
                    self.assertIn("Type",data["Data"][i])
                    self.assertIn("Balance", data["Data"][i])
                    self.assertIn("Share", data["Data"][i])
                    self.assertIn("AvgBet", data["Data"][i])
                    self.assertIn("BetCount", data["Data"][i])
                    self.assertIn("Limit", data["Data"][i])
                    self.assertIn("Delay", data["Data"][i])
                    self.assertIn("PlayerCategoryGroupId", data["Data"][i])
                    self.assertIn("Delay", data["Data"][i])
                    self.assertIn("ReportPartnerId", data["Data"][i])
                    self.assertIn("Priority", data["Data"][i])
                    self.assertIn("Editing", data["Data"][i])
                    self.assertIn("PlayerSubCategories", data["Data"][i])
                    self.assertIsInstance(data["Data"][i]["CategoryId"],int)
                    self.assertIsInstance(data["Data"][i]["SportbookProfileId"], int)
                    self.assertIsInstance(data["Data"][i]["ReportPartnerId"],int)
                    self.assertIsInstance(data["Data"][i]["Name"], str)
                    self.assertIsInstance(data["Data"][i]["PlayerCategoryGroupId"], int)


    def test_GetAdditionalCategoryValidData(self):
        auth = Login.LoginValidCases(self)
        Id = GetRMTPartners.test_GetRMTPartners(self)
        IDs = []
        CountryId = []
        CurrencyId = []
        Countries = []
        Currencies = []
        for i in Id:
            url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/AdditionalSettings?PartnerId=" + str(i)
            response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()

            self.assertIn("Data",data)
            self.assertIn("Id",data["Data"])
            self.assertIn("Countries",data["Data"])
            for j in range(0,len(data["Data"]["Countries"])):
                self.assertIn("AdditionalCategorySettingId",data["Data"]["Countries"][j])
                self.assertIn("Name", data["Data"]["Countries"][j])
                self.assertIn("Code", data["Data"]["Countries"][j])
                self.assertIn("RegionId", data["Data"]["Countries"][j])
                self.assertIn("AdditionalId", data["Data"]["Countries"][j])
                self.assertIn("Id", data["Data"]["Countries"][j])
                self.assertIn("Limit", data["Data"]["Countries"][j])
                self.assertIn("Delay", data["Data"]["Countries"][j])
                self.assertIn("Enabled", data["Data"]["Countries"][j])
            for k in range(0,len(data["Data"]["Currencies"])):
                self.assertIn("AdditionalCategorySettingId",data["Data"]["Currencies"][k])
                self.assertIn("CurrencyId",data["Data"]["Currencies"][k])
                self.assertIn("NumId",data["Data"]["Currencies"][k])
                self.assertIn("AdditionalId",data["Data"]["Currencies"][k])
                self.assertIn("Id",data["Data"]["Currencies"][k])
                self.assertIn("Limit",data["Data"]["Currencies"][k])
                self.assertIn("Delay",data["Data"]["Currencies"][k])
                self.assertIn("Enabled",data["Data"]["Currencies"][k])
            CurrencyId.append(data["Data"]["Currencies"])
            for n in range(0,len(data["Data"]["DangerousIPList"])):
                self.assertIn("AdditionalCategorySettingId", data["Data"]["DangerousIPList"][n])
                self.assertIn("Ip", data["Data"]["DangerousIPList"][n])
                self.assertIn("Date", data["Data"]["DangerousIPList"][n])
                self.assertIn("Reason", data["Data"]["DangerousIPList"][n])
                self.assertIn("IsPreDefined",data["Data"]["DangerousIPList"][n])
                self.assertIn("AdditionalId", data["Data"]["DangerousIPList"][n])
                self.assertIn("Id", data["Data"]["DangerousIPList"][n])
                self.assertIn("Limit", data["Data"]["DangerousIPList"][n])
                self.assertIn("Delay", data["Data"]["DangerousIPList"][n])
                self.assertIn("Enabled", data["Data"]["DangerousIPList"][n])
            self.assertIn("Women",data["Data"])
            self.assertIn("AdditionalId",data["Data"]["Women"])
            self.assertIn("Id", data["Data"]["Women"])
            self.assertIn("Limit", data["Data"]["Women"])
            self.assertIn("Delay", data["Data"]["Women"])
            self.assertIn("Enabled", data["Data"]["Women"])
            self.assertIn("Age",data["Data"])
            self.assertIn("Age",data["Data"]["Age"])
            self.assertIn("AdditionalId", data["Data"]["Age"])
            self.assertIn("Id", data["Data"]["Age"])
            self.assertIn("Limit", data["Data"]["Age"])
            self.assertIn("Delay", data["Data"]["Age"])
            self.assertIn("Enabled", data["Data"]["Age"])
            self.assertIn("PartnerId",data["Data"])
            IDs.append({"PartnerId":data["Data"]["PartnerId"],"Id":data["Data"]["Id"]})
            for m in range(0,len(data["Data"]["PredefinedDangerousIPsList"])):
                self.assertIn("AdditionalCategorySettingId", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Ip", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Date", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Reason", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("IsPreDefined",data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("AdditionalId", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Id", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Limit", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Delay", data["Data"]["PredefinedDangerousIPsList"][m])
                self.assertIn("Enabled",data["Data"]["PredefinedDangerousIPsList"][m])
            self.assertIn("SupportedCurrencies",data["Data"])
            Currencies.append(data["Data"]["SupportedCurrencies"])
            for p in range(0,len(data["Data"]["CountryList"])):
                self.assertIn("Name",data["Data"]["CountryList"][p])
                self.assertIn("Code", data["Data"]["CountryList"][p])
                self.assertIn("RegionId", data["Data"]["CountryList"][p])
            Countries.append(data["Data"]["CountryList"])

        print(CountryId)
        return IDs,CurrencyId,Currencies,Countries




    def test_AddAdditionalCountry(self):
        auth = Login.LoginValidCases(self)
        Ids, CurrencyId,Currencies, Countries = GetCategorySettings.test_GetAdditionalCategoryValidData(self)
        countryId = []
        CountriesId = []
        for i in range(0,len(Countries)):
            for k in range(0,len(Countries[i])):
                countryId.append(Countries[i][k]["RegionId"])
        boolean = [True, False]
        for j in range(0, len(Ids)):
            url = "http://crm01-ye.betconstruct.int:8085/api/AdditionalSettings/AddCountry"
            body = {"Enabled": choice(boolean), "Limit": randint(0, 30),
                    "Delay": randint(0, 50), "PartnerId": Ids[j]["PartnerId"], "Id": Ids[j]["Id"],"Name":None,"RegionId":choice(countryId)}
            response = requests.post(url,data=json.dumps(body), headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()
            print(body,">>>",data)

            CountriesId.append({"PartnerId": Ids[j]["PartnerId"], "RegionId": choice(countryId),"Id":data["Data"]["Id"],"Name" : data["Data"]["Name"]})





            self.assertIn("Data",data)
            self.assertIn("HasError",data)
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








