from Tools.LoginAuthentication import Login
import requests
import unittest
import random
import json

class RMTPartners(unittest.TestCase):



    def test_GetPartnersforRMT(self):

        auth = Login.LoginValidCases(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/CategorySettings/GetPartners"
        response = requests.get(url,headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        id = []
        for i in range(0,len(data["Data"])):
            id.append(data["Data"][i]["PartnerId"])
        return id

    def test_FindPlayerRMTPartner(self):

        auth = Login.LoginValidCases(self)
        Id = RMTPartners.test_GetPartnersforRMT(self)
        url = "http://crm01-ye.betconstruct.int:8085/api/Player/FindPlayer"
        body = {"Count": 50, "CreatedFrom": "", "CreatedTo": "", "Email": "", "FirstName": "", "GameStyles": [],
                    "IsEmailPartial": True, "IsFirstNamePartial": True, "IsLastNamePartial": True, "IsMobilePhonePartial": True,
                    "IsVerified": None, "LastName": "","LastSessionFrom": "", "LastSessionTo": "", "MobilePhone": None, "PartnerName": "", "Partners": Id,"PaymentTypeId": None, "PlayerId": None, "Start": 1, "WalletId": ""}
        response = requests.post(url, data=json.dumps(body),headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        partnerid = []
        partnerIdList = []
        for i in range(0,len(data["Data"]["Players"])):
            partnerid.append(data["Data"]["Players"][i]["PartnerId"])
            partnerIdList.append({"PartnerId":data["Data"]["Players"][i]["PartnerId"],
                                  "ClientId":data["Data"]["Players"][i]["Id"]})
        # print(len(partnerIdList))
        return partnerIdList,random.choice(partnerIdList)


    def test_rmtPartnersClients(self):

        auth = Login.LoginValidCases(self)
        urlfordata = "http://crm01-ye.betconstruct.int:8085/api/Player/GetSvetikdata"
        responsefordata = requests.get(urlfordata,headers={'Content-Type': 'application/json', 'Authentication': auth})
        datafordata = responsefordata.json()
        # for i in range(0,len(datafordata["Data"])):
        clientId = random.choice(datafordata["Data"])

        return clientId


    def test_GetSportId(self):

        auth = Login.LoginValidCases(self)
        clientId = RMTPartners.test_rmtPartnersClients(self)
        # print(clientId)
        url = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=2&PlayerId="+str(clientId["Id"])+"&SportId=0&RegionId=0"
        response = requests.get(url,headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        sportId = []
        for i in range(0,len(data["Data"])):
            sportId.append(data["Data"][i]["BetKPI"]["SportId"])
        return clientId,sportId

    def test_RegionId(self):

        auth = Login.LoginValidCases(self)
        clientId,sportId = RMTPartners.test_GetSportId(self)
        Id = []
        for i in sportId:
            urlRegionId = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=3&PlayerId="+str(clientId["Id"])+"&SportId="+str(i)+"&RegionId=0"
            response = requests.get(urlRegionId,headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()
            # print(urlRegionId,">>>>",data)
            if data["Data"] != []:
                for j in range(0,len(data["Data"])):
                    Id.append({"RegionId":data["Data"][j]["BetKPI"]["RegionId"],
                            "SportId":data["Data"][j]["BetKPI"]["SportId"]})
                return clientId,Id


    def test_CompetiotionId(self):

        auth = Login.LoginValidCases(self)
        competitionId = []
        clientId,Id = RMTPartners.test_RegionId(self)
        for i in range(0,len(Id)):
            urlCompetitionId = "http://crm01-ye.betconstruct.int:8085/api/PlayerKPI/GetPlayerKPITree?Level=4&PlayerId="+str(clientId["Id"])+"&SportId="+str(Id[i]["SportId"])+"&RegionId="+str(Id[i]["RegionId"])
            response = requests.get(urlCompetitionId,headers={'Content-Type': 'application/json', 'Authentication': auth})
            data = response.json()

            for j in range(0,len(data["Data"])):
                competitionId.append({"SportId":data["Data"][j]["BetKPI"]["SportId"],
                                      "RegionId":data["Data"][j]["BetKPI"]["RegionId"],
                                      "CompetitionId":data["Data"][j]["BetKPI"]["CompetitionId"]})
        print(clientId,competitionId)
        return clientId,competitionId

















