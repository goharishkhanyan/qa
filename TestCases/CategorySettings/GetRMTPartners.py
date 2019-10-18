from Tools.LoginAuthentication import Login
import requests
import unittest
import json

class GetRMTPartners(unittest.TestCase):



    def test_GetRMTPartners(self):

        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GetPartners"
        response = requests.get(url,headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        id = []
        for i in range(0,len(data["Data"])):
            id.append(data["Data"][i]["PartnerId"])

        return id

