from Tools.LoginAuthentication import Login
from TestCases.FIndPlayer import FindPlayer
import requests
import unittest
import random
import string
import json


class GetCommentHistory(unittest.TestCase):

    def test_GetCommentHistoryValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        clientId = str(random.choice(clientIdList))
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/CommentHistory/GetCommentHistory?playerId="+str(clientId)
        response = requests.get(url,headers = {'Content-Type': 'application/json','Authentication':auth})
        data = response.json()

        self.assertIn("Data",data)
        self.assertIn("HasError",data)
        self.assertIn("AlertType",data)
        self.assertIn("AlertMessage",data)
        self.assertIn("ModelErrors",data)
        self.assertEqual(False,data["HasError"])
        if data["Data"] != []:
            for i in data["Data"]:
                self.assertIn("PlayerId",data["Data"][i])
                self.assertIn("Date",data["Data"][i])
                self.assertIn("Comment",data["Data"][i])
                self.assertIn("UserName",data["Data"][i])

        else:
            self.assertEqual([],data["Data"])



    def test_GetCommentHistoryInvalidData(self):
        InvalidID = string.ascii_uppercase + string.digits
        clientID = ''.join(random.sample(InvalidID * 24, 24))
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/CommentHistory/GetCommentHistory?playerId="+str(clientID)
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()

        self.assertIn("Data",data)
        self.assertIn("HasError", data)
        self.assertIn("AlertType", data)
        self.assertIn("AlertMessage", data)
        self.assertIn("ModelErrors", data)
        self.assertEqual(True, data["HasError"])
        self.assertIn("Message",data["Data"])
        self.assertIn("MessageDetail",data["Data"])
        self.assertEqual("The request is invalid.",data["Data"]["Message"])
        self.assertEqual("The parameters dictionary contains a null entry for parameter 'playerId' of non-nullable type 'System.Int32' for method 'System.Collections.Generic.List`1[BetConstruct.RMT.Models.ViewModels.CommentHistoryViewModel] GetCommentHistory(Int32)' in 'BetConstruct.RMT.Backend.Controllers.CommentHistoryController'. An optional parameter must be a reference type, a nullable type, or be declared as an optional parameter.",data["Data"]["MessageDetail"])



    def test_GetCommentHistoryInvalidLogin(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        clientId = str(random.choice(clientIdList))
        char_set = string.ascii_uppercase + string.digits
        invalidAuthentication = ''.join(random.sample(char_set * 24, 24))
        url = "http://crm01-ye.betconstruct.int:8085/api/CommentHistory/GetCommentHistory?playerId="+str(clientId)
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': invalidAuthentication})
        data = response.json()

        self.assertIn("Data", data)
        self.assertIn("HasError", data)
        self.assertIn("AlertType", data)
        self.assertIn("AlertMessage", data)
        self.assertIn("ModelErrors", data)
        self.assertIn("Message",data["Data"])
        self.assertEqual("Authorization has been denied for this request.",data["Data"]["Message"])


    def test_InvalidTypeOfRequest(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        clientId = str(random.choice(clientIdList))
        authentication = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/CommentHistory/GetCommentHistory?playerId=" + str(clientId)
        body = {"invalidKey": "invalidValue"}
        response = requests.post(url, data=body,headers={'Content-Type': 'application/json', 'Authentication': authentication})
        data = response.json()

        self.assertIn("HasError", data)
        self.assertIn("AlertType", data)
        self.assertIn("AlertMessage", data)
        self.assertIn("ModelErrors", data)
        self.assertEqual(True, data["HasError"])
        self.assertEqual("alert", data["AlertType"])
        self.assertEqual("The requested resource is not found", data["AlertMessage"])
        self.assertEqual(None, data["ModelErrors"])