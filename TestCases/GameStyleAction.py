from Tools.LoginAuthentication import Login
from  Tools.RMTPartners import RMTPartners
import requests
import unittest
import json

class GameStyleAction(unittest.TestCase):

    def test_GameStyleActionValidDataGlobal(self):
        auth = Login.LoginValidCases(self)
        partnerIdList,PartnerId = RMTPartners.test_FindPlayerRMTPartner(self)
        urlforSettings = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GameStyleSettings?PartnerId="+str(PartnerId["PartnerId"])
        responseSettings = requests.get(urlforSettings,headers={'Content-Type': 'application/json', 'Authentication': auth})
        dataSettings = responseSettings.json()
        # print(dataSettings)
        url = "http://crm01-ye.betconstruct.int:8085/api/GameStyle/GameStyleAction"
        id = [11,12,25,26,27,34,35]
        for i in id:
            # data1 = {"BetKPI":{},"GameStyles":[{"Id":i,"IsSelected":True}],"PlayerId":27528273,"LevelId":0}

            data1 = {"BetKPI":{},"GameStyles":[{"Id":i,"IsSelected":True}],"PlayerId":str(PartnerId["ClientId"]),"LevelId":0}
            response = requests.post(url,data=json.dumps(data1),headers = {'Content-Type': 'application/json','Authentication':auth})
            data = response.json()
            # print(data)
            for j in  range(0,len(data1["GameStyles"])):
                for k in range(0,len(dataSettings["Data"])):

                    if data1["GameStyles"][j]["Id"]==dataSettings["Data"][k]["CategoryId"]:
                        self.assertEqual(data["Data"]["Limit"],dataSettings["Data"][k]["Limit"])
                        self.assertEqual(data["Data"]["Delay"],dataSettings["Data"][k]["Delay"])
                        self.assertIn("Data",data)
                        self.assertIn("Limit",data["Data"])
                        self.assertIn("Delay",data["Data"])
                        self.assertIn("IsForAllNodes",data["Data"])
                        self.assertIn("HasError",data)
                        self.assertIn("AlertType",data)
                        self.assertIn("AlertMessage",data)
                        self.assertIn("ModelErrors",data)



    def test_GameStyleActionSportID(self):
        auth = Login.LoginValidCases(self)
        clientId,sportId = RMTPartners.test_GetSportId(self)
        urlforSettings = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GameStyleSettings?PartnerId=" + str(clientId["PartnerId"])
        responseSettings = requests.get(urlforSettings,headers={'Content-Type': 'application/json', 'Authentication': auth})
        dataSettings = responseSettings.json()
        id = [11,12,25,26,27,34,35]
        url = "http://crm01-ye.betconstruct.int:8085/api/GameStyle/GameStyleAction"
        for i in sportId:
            for j in id:
                body = {"HasChildren":True,"ChildLevelId":3,"BetKPI":{"SportId":i},"GameStyles":[{"Id":j,"IsSelected":True}],"PlayerId":str(clientId["Id"]),"LevelId":2}
                response = requests.post(url,data=json.dumps(body),headers = {'Content-Type': 'application/json','Authentication':auth})
                data = response.json()

                for j in range(0, len(body["GameStyles"])):
                    for k in range(0, len(dataSettings["Data"])):

                        if body["GameStyles"][j]["Id"] == dataSettings["Data"][k]["CategoryId"]:
                            self.assertEqual(data["Data"]["Limit"], dataSettings["Data"][k]["Limit"])
                            self.assertEqual(data["Data"]["Delay"], dataSettings["Data"][k]["Delay"])
                            self.assertIn("Data", data)
                            self.assertIn("Limit", data["Data"])
                            self.assertIn("Delay", data["Data"])
                            self.assertIn("IsForAllNodes", data["Data"])
                            self.assertIn("HasError", data)
                            self.assertIn("AlertType", data)
                            self.assertIn("AlertMessage", data)
                            self.assertIn("ModelErrors", data)


    def test_GameStyleCompetitionId(self):
        auth = Login.LoginValidCases(self)
        clientId,competitionId = RMTPartners.test_CompetiotionId(self)
        urlforSettings = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GameStyleSettings?PartnerId=" + str(clientId["PartnerId"])
        responseSettings = requests.get(urlforSettings,headers={'Content-Type': 'application/json', 'Authentication': auth})
        dataSettings = responseSettings.json()
        id = [11, 12, 25, 26, 27, 34, 35]
        url = "http://crm01-ye.betconstruct.int:8085/api/GameStyle/GameStyleAction"
        for i in range(0,len(competitionId)):
            for j in id:
                body = {"HasChildren":False,"ChildLevelId":5,"BetKPI":{"SportId":competitionId[i]["SportId"],"RegionId":competitionId[i]["RegionId"],"CompetitionId":competitionId[i]["CompetitionId"]},"GameStyles":[{"Id":j,"IsSelected":True},],"PlayerId":str(clientId["Id"]),"LevelId":4}
                response = requests.post(url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': auth})
                data = response.json()

                for j in range(0, len(body["GameStyles"])):
                    for k in range(0, len(dataSettings["Data"])):

                        if body["GameStyles"][j]["Id"] == dataSettings["Data"][k]["CategoryId"]:
                            self.assertEqual(data["Data"]["Limit"], dataSettings["Data"][k]["Limit"])
                            self.assertEqual(data["Data"]["Delay"], dataSettings["Data"][k]["Delay"])
                            self.assertIn("Data", data)
                            self.assertIn("Limit", data["Data"])
                            self.assertIn("Delay", data["Data"])
                            self.assertIn("IsForAllNodes", data["Data"])
                            self.assertIn("HasError", data)
                            self.assertIn("AlertType", data)
                            self.assertIn("AlertMessage", data)
                            self.assertIn("ModelErrors", data)








