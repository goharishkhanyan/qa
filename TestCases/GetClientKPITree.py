from Tools.LoginAuthentication import Login
from TestCases.FIndPlayer import FindPlayer
from TestCases.GetPartners import GetPartners
import requests
import unittest
import random
import string
import json


class GetClientKPITree(unittest.TestCase):
    def test_GetClientKPITreeValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        clientId = str(random.choice(clientIdList))
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=0&PlayerId="+clientId+"&SportId=0&RegionId=0"
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()

        self.assertIn("Data",data)
        self.assertIn("HasError",data)
        self.assertIn("AlertType",data)
        self.assertIn("AlertMessage",data)
        self.assertIn("ModelErrors",data)
        for k in range(0,len(data["Data"])):
            self.assertIn("Key",data["Data"][k])
            self.assertIn("Limit", data["Data"][k])
            self.assertIn("Delay", data["Data"][k])
            self.assertIn("Name", data["Data"][k])
            self.assertEqual("Global",data["Data"][k]["Name"])
            self.assertIn("HasChildren", data["Data"][k])
            self.assertIn("ChildLevelId", data["Data"][k])
            self.assertEqual(1,data["Data"][k]["ChildLevelId"])
            self.assertIn("Expanded", data["Data"][k])
            self.assertIn("ParentKey", data["Data"][k])
            self.assertIn("Children", data["Data"][k])
            self.assertIn("BetKPI", data["Data"][k])
            self.assertIn("Name",data["Data"][k]["BetKPI"])
            self.assertIn("TurnOver", data["Data"][k]["BetKPI"])
            self.assertIn("Profit", data["Data"][k]["BetKPI"])
            self.assertIn("PercentofProfite", data["Data"][k]["BetKPI"])
            self.assertIn("CalcBets", data["Data"][k]["BetKPI"])
            self.assertIn("AvgBets", data["Data"][k]["BetKPI"])
            self.assertIn("AvgPrice", data["Data"][k]["BetKPI"])
            self.assertIn("Type", data["Data"][k]["BetKPI"])
            self.assertIn("SportId", data["Data"][k]["BetKPI"])
            self.assertIn("RegionId", data["Data"][k]["BetKPI"])
            self.assertIn("Count", data["Data"][k]["BetKPI"])
            self.assertIn("ParentKey", data["Data"][k]["BetKPI"])
            self.assertIn("ChildLevelId", data["Data"][k]["BetKPI"])
            self.assertIn("CompetitionId", data["Data"][k]["BetKPI"])
            self.assertIn("NameId", data["Data"][k]["BetKPI"])
            self.assertIn("GameStyles",data["Data"][k])
            for i in range(0,len(data["Data"][k]["GameStyles"])):
                self.assertIn("Id",data["Data"][k]["GameStyles"][i])
                self.assertIn("Name",data["Data"][k]["GameStyles"][i])
                self.assertIn("IsSelected",data["Data"][k]["GameStyles"][i])
                self.assertIn("IsNested",data["Data"][k]["GameStyles"][i])
                self.assertIn("IsSubSelected",data["Data"][k]["GameStyles"][i])
                self.assertIn("Priority",data["Data"][k]["GameStyles"][i])
                self.assertIn("SubId",data["Data"][k]["GameStyles"][i])
                self.assertIn("PlayerSubCategories",data["Data"][k]["GameStyles"][i])
                if data["Data"][k]["GameStyles"][i]["PlayerSubCategories"] != None:
                    for j in range(0,len(data["Data"][k]["GameStyles"][i]["PlayerSubCategories"])):
                        self.assertIn("Id",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("Name",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("IsSelected",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("IsNested",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("IsSubSelected",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("Priority",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("SubId",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                        self.assertIn("PlayerSubCategories",data["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
            if data["Data"][k]["HasChildren"]==True:
                # url1 = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=1&PlayerId=10702&SportId=0&RegionId=0"

                url1 = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=1&PlayerId=" + clientId + "&SportId=0&RegionId=0"
                response1 = requests.get(url1, headers={'Content-Type': 'application/json', 'Authentication': auth})
                data1 = response1.json()

                self.assertIn("Data", data1)
                for k in range(0, len(data1["Data"])):
                    self.assertIn("Key", data1["Data"][k])
                    self.assertIn("Limit", data1["Data"][k])
                    self.assertIn("Delay", data1["Data"][k])
                    self.assertIn("Name", data1["Data"][k])
                    self.assertIn("HasChildren", data1["Data"][k])
                    self.assertIn("ChildLevelId", data1["Data"][k])
                    # self.assertEqual(2, data1["Data"][k]["ChildLevelId"])
                    self.assertIn("Expanded", data1["Data"][k])
                    self.assertIn("ParentKey", data1["Data"][k])
                    self.assertIn("Children", data1["Data"][k])
                    self.assertIn("BetKPI", data1["Data"][k])
                    self.assertIn("Name", data1["Data"][k]["BetKPI"])
                    self.assertIn("TurnOver", data1["Data"][k]["BetKPI"])
                    self.assertIn("Profit", data1["Data"][k]["BetKPI"])
                    self.assertIn("PercentofProfite", data1["Data"][k]["BetKPI"])
                    self.assertIn("CalcBets", data1["Data"][k]["BetKPI"])
                    self.assertIn("AvgBets", data1["Data"][k]["BetKPI"])
                    self.assertIn("AvgPrice", data1["Data"][k]["BetKPI"])
                    self.assertIn("Type", data1["Data"][k]["BetKPI"])
                    self.assertIn("SportId", data1["Data"][k]["BetKPI"])
                    self.assertIn("RegionId", data1["Data"][k]["BetKPI"])
                    self.assertIn("Count", data1["Data"][k]["BetKPI"])
                    self.assertIn("ParentKey", data1["Data"][k]["BetKPI"])
                    self.assertIn("ChildLevelId", data1["Data"][k]["BetKPI"])
                    self.assertIn("CompetitionId", data1["Data"][k]["BetKPI"])
                    self.assertIn("NameId", data1["Data"][k]["BetKPI"])
                    self.assertIn("GameStyles", data1["Data"][k])
                    for i in range(0, len(data1["Data"][k]["GameStyles"])):
                        self.assertIn("Id", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("Name", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("IsSelected", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("IsNested", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("IsSubSelected", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("Priority", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("SubId", data1["Data"][k]["GameStyles"][i])
                        self.assertIn("PlayerSubCategories", data1["Data"][k]["GameStyles"][i])
                        if data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"] != None:
                            for j in range(0, len(data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"])):
                                self.assertIn("Id", data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("Name", data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("IsSelected",data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("IsNested", data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("IsSubSelected",data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("Priority", data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("SubId", data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                self.assertIn("PlayerSubCategories",data1["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])

                    if data1["Data"][k]["Name"] == "Ordinar":
                        url2 = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=2&PlayerId=" + clientId + "&SportId=0&RegionId=0"
                        response2 = requests.get(url2, headers={'Content-Type': 'application/json','Authentication': auth})
                        data2 = response2.json()
                        sportId = []

                        self.assertIn("Data", data2)
                        for k in range(0, len(data2["Data"])):
                            self.assertIn("Key", data2["Data"][k])
                            self.assertIn("Limit", data2["Data"][k])
                            self.assertIn("Delay", data2["Data"][k])
                            self.assertIn("Name", data2["Data"][k])
                            self.assertIn("HasChildren", data2["Data"][k])
                            self.assertIn("ChildLevelId", data2["Data"][k])
                            # self.assertEqual(3, data2["Data"][k]["ChildLevelId"])
                            self.assertIn("Expanded", data2["Data"][k])
                            self.assertIn("ParentKey", data2["Data"][k])
                            self.assertIn("Children", data2["Data"][k])
                            self.assertIn("BetKPI", data2["Data"][k])
                            self.assertIn("Name", data2["Data"][k]["BetKPI"])
                            self.assertIn("TurnOver", data2["Data"][k]["BetKPI"])
                            self.assertIn("Profit", data2["Data"][k]["BetKPI"])
                            self.assertIn("PercentofProfite", data2["Data"][k]["BetKPI"])
                            self.assertIn("CalcBets", data2["Data"][k]["BetKPI"])
                            self.assertIn("AvgBets", data2["Data"][k]["BetKPI"])
                            self.assertIn("AvgPrice", data2["Data"][k]["BetKPI"])
                            self.assertIn("Type", data2["Data"][k]["BetKPI"])
                            self.assertIn("SportId", data2["Data"][k]["BetKPI"])
                            sportId.append(data2["Data"][k]["BetKPI"]["SportId"])
                            self.assertIn("RegionId", data2["Data"][k]["BetKPI"])
                            self.assertIn("Count", data2["Data"][k]["BetKPI"])
                            self.assertIn("ParentKey", data2["Data"][k]["BetKPI"])
                            self.assertIn("ChildLevelId", data2["Data"][k]["BetKPI"])
                            self.assertIn("CompetitionId", data2["Data"][k]["BetKPI"])
                            self.assertIn("NameId", data2["Data"][k]["BetKPI"])
                            self.assertIn("GameStyles", data2["Data"][k])
                            for i in range(0, len(data2["Data"][k]["GameStyles"])):
                                self.assertIn("Id", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("Name", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("IsSelected", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("IsNested", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("IsSubSelected", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("Priority", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("SubId", data2["Data"][k]["GameStyles"][i])
                                self.assertIn("PlayerSubCategories", data2["Data"][k]["GameStyles"][i])
                                if data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"] != None:
                                    for j in range(0, len(data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"])):
                                        self.assertIn("Id", data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("Name", data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("IsSelected",data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("IsNested",data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("IsSubSelected",data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("Priority",data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("SubId", data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                        self.assertIn("PlayerSubCategories",data2["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])

                        for s in sportId:
                            url3 ="http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=2&PlayerId=" + clientId + "&SportId="+str(s)+"&RegionId=0"
                            response3 = requests.get(url3, headers={'Content-Type': 'application/json','Authentication': auth})
                            data3 = response3.json()
                            regionId = []

                            self.assertIn("Data", data3)
                            for k in range(0, len(data3["Data"])):
                                self.assertIn("Key", data3["Data"][k])
                                self.assertIn("Limit", data3["Data"][k])
                                self.assertIn("Delay", data3["Data"][k])
                                self.assertIn("Name", data3["Data"][k])
                                self.assertIn("HasChildren", data3["Data"][k])
                                self.assertIn("ChildLevelId", data3["Data"][k])
                                self.assertEqual(4, data3["Data"][k]["ChildLevelId"])
                                self.assertIn("Expanded", data3["Data"][k])
                                self.assertIn("ParentKey", data3["Data"][k])
                                self.assertIn("Children", data3["Data"][k])
                                self.assertIn("BetKPI", data3["Data"][k])
                                self.assertIn("Name", data3["Data"][k]["BetKPI"])
                                self.assertIn("TurnOver", data3["Data"][k]["BetKPI"])
                                self.assertIn("Profit", data3["Data"][k]["BetKPI"])
                                self.assertIn("PercentofProfite", data3["Data"][k]["BetKPI"])
                                self.assertIn("CalcBets", data3["Data"][k]["BetKPI"])
                                self.assertIn("AvgBets", data3["Data"][k]["BetKPI"])
                                self.assertIn("AvgPrice", data3["Data"][k]["BetKPI"])
                                self.assertIn("Type", data3["Data"][k]["BetKPI"])
                                self.assertIn("SportId", data3["Data"][k]["BetKPI"])
                                self.assertIn("RegionId", data3["Data"][k]["BetKPI"])
                                regionId.append(data3["Data"][k]["BetKPI"]["RegionId"])
                                self.assertIn("Count", data3["Data"][k]["BetKPI"])
                                self.assertIn("ParentKey", data3["Data"][k]["BetKPI"])
                                self.assertIn("ChildLevelId", data3["Data"][k]["BetKPI"])
                                self.assertIn("CompetitionId", data3["Data"][k]["BetKPI"])
                                self.assertIn("NameId", data3["Data"][k]["BetKPI"])
                                self.assertIn("GameStyles", data3["Data"][k])
                                for i in range(0, len(data3["Data"][k]["GameStyles"])):
                                    self.assertIn("Id", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("Name", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("IsSelected", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("IsNested", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("IsSubSelected", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("Priority", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("SubId", data3["Data"][k]["GameStyles"][i])
                                    self.assertIn("PlayerSubCategories", data3["Data"][k]["GameStyles"][i])
                                    if data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"] != None:
                                        for j in range(0, len(data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"])):
                                            self.assertIn("Id", data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("Name",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("IsSelected",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("IsNested",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("IsSubSelected",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("Priority",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("SubId",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])
                                            self.assertIn("PlayerSubCategories",data3["Data"][k]["GameStyles"][i]["PlayerSubCategories"][j])






    #
    #
    # def test_GetClientKPITreeInvalidClientId(self):
    #     InvalidID = string.ascii_uppercase + string.digits
    #     clientID = ''.join(random.sample(InvalidID * 24, 24))
    #     auth = Login.LoginValidCases(self)
    #     url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=0&PlayerId="+str(clientID)+"&SportId=0&RegionId=0"
    #     # url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=0&PlayerId="+clientId+"&SportId=0&RegionId=0"
    #     response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
    #     data = response.json()
    #
    #     self.assertIn("Data",data)
    #     self.assertIn("Message",data["Data"])
    #     self.assertIn("MessageDetail",data["Data"])
    #     self.assertIn("HasError",data)
    #     self.assertIn("AlertType",data)
    #     self.assertIn("AlertMessage",data)
    #     self.assertIn("ModelErrors",data)
    #     self.assertEqual("The request is invalid.",data["Data"]["Message"])
    #     self.assertEqual("The parameters dictionary contains a null entry for parameter 'PlayerId' of non-nullable type 'System.Int32' for method 'System.Collections.Generic.List`1[BetConstruct.RMT.Models.ViewModels.PlayerKPITreeViewModel] GetPlayerKPITree(Int32, Int32, Int32, Int32)' in 'BetConstruct.RMT.Backend.Controllers.PlayerKPIController'. An optional parameter must be a reference type, a nullable type, or be declared as an optional parameter.",data["Data"]["MessageDetail"])
    #     self.assertEqual(True,data["HasError"])
    #     self.assertEqual("alert",data["AlertType"])
    #     self.assertEqual("The request is invalid.",data["AlertMessage"])
    #     self.assertEqual(None,data["ModelErrors"])
    #
    #
    #
    #
    # def test_GetClientKPITreeInvalidSportId(self):
    #     InvalidID = string.ascii_uppercase + string.digits
    #     Id = ''.join(random.sample(InvalidID * 24, 24))
    #     auth = Login.LoginValidCases(self)
    #     url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=0&PlayerId=10702&SportId="+str(Id)+"&RegionId=0"
    #     # url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=0&PlayerId="+clientId+"&SportId=0&RegionId=0"
    #     response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
    #     data = response.json()
    #
    #     self.assertIn("Data", data)
    #     self.assertIn("Message", data["Data"])
    #     self.assertIn("MessageDetail", data["Data"])
    #     self.assertIn("HasError", data)
    #     self.assertIn("AlertType", data)
    #     self.assertIn("AlertMessage", data)
    #     self.assertIn("ModelErrors", data)
    #     self.assertEqual("The request is invalid.", data["Data"]["Message"])
    #     self.assertEqual("The parameters dictionary contains a null entry for parameter 'SportId' of non-nullable type 'System.Int32' for method 'System.Collections.Generic.List`1[BetConstruct.RMT.Models.ViewModels.PlayerKPITreeViewModel] GetPlayerKPITree(Int32, Int32, Int32, Int32)' in 'BetConstruct.RMT.Backend.Controllers.PlayerKPIController'. An optional parameter must be a reference type, a nullable type, or be declared as an optional parameter.",data["Data"]["MessageDetail"])
    #     self.assertEqual(True, data["HasError"])
    #     self.assertEqual("alert", data["AlertType"])
    #     self.assertEqual("The request is invalid.", data["AlertMessage"])
    #     self.assertEqual(None, data["ModelErrors"])
    #
    #
    #
    #
