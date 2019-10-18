from Tools.LoginAuthentication import Login
from TestCases.FIndPlayer import FindPlayer
import requests
import unittest
import random
import string
import json


class UpdateComment(unittest.TestCase):

    def test_UpdateCommentValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        clientId = str(random.choice(clientIdList))
        auth = Login.LoginValidCases(self)
        body = {"Comment":"testRMT","PlayerId":clientId}
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/UpdateComment"
        response = requests.post(url,data=json.dumps(body),headers = {'Content-Type': 'application/json','Authentication':auth})
        data = response.json()
        print(data)

        self.assertIn("Data",data)
        self.assertIn("HasError",data)
        self.assertIn("AlertType",data)
        self.assertIn("AlertMessage",data)
        self.assertIn("ModelErrors",data)
        self.assertIn("MessageId",data["Data"])
        self.assertIn("PlayerId",data["Data"])
        self.assertIn("Comment",data["Data"])
        self.assertIn("Date",data["Data"])
        self.assertIn("UserId",data["Data"])
        self.assertIn("UserName",data["Data"])









