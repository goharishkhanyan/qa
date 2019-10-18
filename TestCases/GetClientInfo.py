from Tools.LoginAuthentication import Login
from TestCases.FIndPlayer import FindPlayer
from TestCases.GetPartners import GetPartners
import requests
import unittest
import random
import string
import json



class GetClientInfo(unittest.TestCase):

    def test_GetClientValidData(self):
        clientIdList = FindPlayer.test_FindPlayerValidData(self)
        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/GetPlayer?PlayerId="+str(random.choice(clientIdList))
        response = requests.get(url,headers ={'Content-Type': 'application/json','Authentication':auth} )
        data = response.json()
        print(data)

        self.assertIn("Data",data)
        self.assertIn("HasError",data)
        self.assertIn("AlertType",data)
        self.assertIn("AlertMessage",data)
        self.assertIn("ModelErrors",data)
        self.assertIn("Id",data["Data"])
        self.assertIn("PartnerId",data["Data"])
        self.assertIn("Name",data["Data"])
        self.assertIn("Email",data["Data"])
        self.assertIn("Gender",data["Data"])
        self.assertIn("Country",data["Data"])
        self.assertIn("BirthDate",data["Data"])
        self.assertIn("Created",data["Data"])
        self.assertIn("TimeInUse",data["Data"])
        self.assertIn("IsVerified",data["Data"])
        self.assertIn("LastBetDate",data["Data"])
        self.assertIn("LastStake",data["Data"])
        self.assertIn("LastLoginIp",data["Data"])
        self.assertIn("LastComment",data["Data"])
        self.assertIn("IsRMTBlocked",data["Data"])
        self.assertIn("IsInCalculationProcess",data["Data"])
        self.assertIn("BetKPIs",data["Data"])
        for i in range(0,len(data["Data"]["BetKPIs"])):
            self.assertIn("ClientId",data["Data"]["BetKPIs"][i])
            self.assertIn("Type",data["Data"]["BetKPIs"][i])
            self.assertIn("nameId",data["Data"]["BetKPIs"][i])
            self.assertIn("SportId", data["Data"]["BetKPIs"][i])
            self.assertIn("RegionId", data["Data"]["BetKPIs"][i])
            self.assertIn("TournamentId", data["Data"]["BetKPIs"][i])
            self.assertIn("Date", data["Data"]["BetKPIs"][i])
            self.assertIn("CurrencyId", data["Data"]["BetKPIs"][i])
            self.assertIn("TurnOver", data["Data"]["BetKPIs"][i])
            self.assertIn("Profit", data["Data"]["BetKPIs"][i])
            self.assertIn("PercentofProfite", data["Data"]["BetKPIs"][i])
            self.assertIn("CalcBets", data["Data"]["BetKPIs"][i])
            self.assertIn("AvgBets", data["Data"]["BetKPIs"][i])
            self.assertIn("AvgPrice", data["Data"]["BetKPIs"][i])
        self.assertIn("KpiChartModel",data["Data"])
        self.assertIn("Profit",data["Data"]["KpiChartModel"])
        for j in range(0,len(data["Data"]["KpiChartModel"]["Profit"])):
            self.assertIn("Date",data["Data"]["KpiChartModel"]["Profit"][j])
            self.assertIn("Value",data["Data"]["KpiChartModel"]["Profit"][j])
        self.assertIn("CategoryChart",data["Data"])
        self.assertIn("Labels",data["Data"]["CategoryChart"])
        self.assertIn("Count", data["Data"]["CategoryChart"])
        self.assertIn("Colors", data["Data"]["CategoryChart"])
        self.assertIn("Partner",data["Data"])
        self.assertIn("Name",data["Data"]["Partner"])
        self.assertIn("CashOutKPI",data["Data"])
        for k in range(0,len(data["Data"]["CashOutKPI"])):
            self.assertIn("Quantity",data["Data"]["CashOutKPI"][k])
            self.assertIn("COBets", data["Data"]["CashOutKPI"][k])
            self.assertIn("WinCOPercent", data["Data"]["CashOutKPI"][k])
            self.assertIn("PercentСО",data["Data"]["CashOutKPI"][k])
            self.assertIn("Profit", data["Data"]["CashOutKPI"][k])
            self.assertIn("AvgTimeCO",data["Data"]["CashOutKPI"][k])
        self.assertIn("TransactionsHeaders",data["Data"])
        self.assertIn("CashOutKPIHeaders",data["Data"])
        self.assertIn("Transactions",data["Data"])
        for t in range(0,len(data["Data"]["Transactions"])):
            self.assertIn("Date",data["Data"]["Transactions"][t])
            self.assertIn("OperationType", data["Data"]["Transactions"][t])
            self.assertIn("VirtualWallet", data["Data"]["Transactions"][t])
            self.assertIn("Amount", data["Data"]["Transactions"][t])
            self.assertIn("State", data["Data"]["Transactions"][t])
        self.assertIn("PlayerBetKPIGlobal",data["Data"])
        self.assertIn("Name",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("TurnOver",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("Profit",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("PercentofProfite",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("CalcBets",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("AvgBets",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("AvgPrice",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("Type",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("SportId",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("RegionId",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("Count",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("ParentKey",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("ChildLevelId",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("CompetitionId",data["Data"]["PlayerBetKPIGlobal"])
        self.assertIn("NameId",data["Data"]["PlayerBetKPIGlobal"])


    #
    # def test_GetClientInfoInvalidId(self):
    #     ClientId = random.randint(1,2000)
    #     auth = Login.LoginValidCases(self)
    #     url = "http://crm01-ye.betconstruct.int:8085/api/Player/GetPlayer?PlayerId=" + str(ClientId)
    #     response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
    #     data = response.json()
    #     # print(data)
    #
    #
    #     self.assertIn("Data",data)
    #     self.assertIn("HasError",data)
    #     self.assertIn("AlertType",data)
    #     self.assertIn("AlertMessage",data)
    #     self.assertIn("ModelErrors",data)
    #     self.assertEqual(None,data["Data"])
    #     self.assertEqual(False,data["HasError"])
    #     self.assertEqual("alert",data["AlertType"])
    #     self.assertEqual("Object"+" "+ str(ClientId)+" "+"not found",data["AlertMessage"])
    #     self.assertEqual(None,data["ModelErrors"])
















