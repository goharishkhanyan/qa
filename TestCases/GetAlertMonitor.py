from Tools.LoginAuthentication import Login
import requests
import unittest
import random
import string


class GetAlertMonitor(unittest.TestCase):
    url = "http://crm01-ye.betconstruct.int:8085/api/AlertMonitor/Get"


    def test_GetAlertMonitorValidData(self):
        auth = Login.LoginValidCases(self)
        response = requests.get(self.url,headers ={'Content-Type': 'application/json','Authentication':auth})
        data = response.json()

        self.assertIn("Data",data)
        for i in range(0,len(data["Data"])):
            self.assertIn("AntiFraud",data["Data"][i])
            for j in range(0,len(data["Data"][i]["AntiFraud"])):
                self.assertIn("Id",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Type",data["Data"][i]["AntiFraud"][j])
                self.assertIn("CategoryType",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Partner",data["Data"][i]["AntiFraud"][j])
                self.assertIn("PartnerId",data["Data"][i]["AntiFraud"][j])
                self.assertIn("PlayerId",data["Data"][i]["AntiFraud"][j])
                self.assertIn("OperatorID",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Reviewer",data["Data"][i]["AntiFraud"][j])
                self.assertIn("PlayerName",data["Data"][i]["AntiFraud"][j])
                self.assertIn("PlayerMail",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Status",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Comment",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Locked",data["Data"][i]["AntiFraud"][j])
                self.assertIn("AlertGroupId",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Category",data["Data"][i]["AntiFraud"][j])
                self.assertIn("Id",data["Data"][i]["AntiFraud"][j]["Category"])
                self.assertIn("Name",data["Data"][i]["AntiFraud"][j]["Category"])
                self.assertIn("SubId",data["Data"][i]["AntiFraud"][j]["Category"])
            self.assertIn("Monitoring",data["Data"][i])
            for m in range(0,len(data["Data"][i]["Monitoring"])):
                print(data["Data"][i]["Monitoring"][m]["Id"])
                self.assertIn("Id", data["Data"][i]["Monitoring"][m])
                self.assertIn("Type", data["Data"][i]["Monitoring"][m])
                self.assertIn("CategoryType", data["Data"][i]["Monitoring"][m])
                self.assertIn("Partner", data["Data"][i]["Monitoring"][m])
                self.assertIn("PartnerId", data["Data"][i]["Monitoring"][m])
                self.assertIn("PlayerId", data["Data"][i]["Monitoring"][m])
                self.assertIn("OperatorID", data["Data"][i]["Monitoring"][m])
                self.assertIn("Reviewer", data["Data"][i]["Monitoring"][m])
                self.assertIn("PlayerName", data["Data"][i]["Monitoring"][m])
                self.assertIn("PlayerMail", data["Data"][i]["Monitoring"][m])
                self.assertIn("Status", data["Data"][i]["Monitoring"][m])
                self.assertIn("Comment", data["Data"][i]["Monitoring"][m])
                self.assertIn("Locked", data["Data"][i]["Monitoring"][m])
                self.assertIn("AlertGroupId", data["Data"][i]["Monitoring"][m])
                self.assertIn("Category", data["Data"][i]["Monitoring"][m])
                if data["Data"][i]["Monitoring"][m]["Category"] != None:
                    self.assertIn("Id", data["Data"][i]["Monitoring"][m]["Category"])
                    self.assertIn("Name", data["Data"][i]["Monitoring"][m]["Category"])
                    self.assertIn("SubId", data["Data"][i]["Monitoring"][m]["Category"])



if __name__ == '__main__':
    unittest.main()