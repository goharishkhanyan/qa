import requests
import json
import unittest

class Login(unittest.TestCase):

    def LoginValidCases(self):

        url = "http://agptest02-ye.betconstruct.int:8080/api/en/Account/login"
        data = {"Username": "svetarmt", "Password": "svetarmt"}
        response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        dataJson = response.json()
        responseHeaders = response.headers['Authentication']
        # print(responseHeaders)

        # self.assertIn("HasError",dataJson)
        # self.assertIn("AlertType",dataJson)
        # self.assertIn("AlertMessage",dataJson)
        # self.assertIn("ModelErrors",dataJson)
        # self.assertIn("Data",dataJson)
        # self.assertIn("UserName",dataJson["Data"])
        # self.assertIn("LangId",dataJson["Data"])
        # self.assertIn("AuthenticationStatus",dataJson["Data"])
        # self.assertIn("UserId",dataJson["Data"])
        # self.assertIn("Settings",dataJson["Data"])
        # self.assertIn("Language",dataJson["Data"]["Settings"])
        # self.assertIn("TimeZone", dataJson["Data"]["Settings"])
        # self.assertIn("OddsType", dataJson["Data"]["Settings"])
        # self.assertIn("ReportCurrency", dataJson["Data"]["Settings"])
        # self.assertIn("ReportPartner", dataJson["Data"]["Settings"])
        # self.assertIn("IsSubscribedToNotification", dataJson["Data"]["Settings"])
        # self.assertIn("ReportsColumns", dataJson["Data"]["Settings"])
        # self.assertIn("PartnerId", dataJson["Data"])
        # self.assertIn("PartnerName", dataJson["Data"])
        # self.assertIn("CurrencyId", dataJson["Data"])
        # self.assertIn("ServerTime", dataJson["Data"])
        # self.assertIn("FirstName", dataJson["Data"])
        # self.assertIn("PermissionList", dataJson["Data"])
        # self.assertIn("AgentId", dataJson["Data"])
        # self.assertIn("PartnerBalanceChangeTime", dataJson["Data"])
        # self.assertIn("IsQRCodeSent", dataJson["Data"])
        # self.assertIn("QRCode", dataJson["Data"])
        # self.assertIn("OriginalQRCode", dataJson["Data"])
        # self.assertIn("PartnerLimitType", dataJson["Data"])
        # self.assertIn("PartnerLimit", dataJson["Data"])
        # self.assertIn("PartnerTimeZone", dataJson["Data"])
        # self.assertIn("LicenseType", dataJson["Data"])
        #

        return responseHeaders


if __name__ == '__main__':
    unittest.main()