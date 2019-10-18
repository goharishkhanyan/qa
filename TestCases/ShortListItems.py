from Tools.LoginAuthentication import Login
import requests
import random
import unittest
import string
from TestCases.GetPartners import GetPartners


class ShortListItems(unittest.TestCase):

    def test_ShortListItemsValidData(self):
        auth = Login.LoginValidCases(self)
        PartnerId = GetPartners.test_GetPartnersValidData(self)
        Id = random.choice(PartnerId)
        url  = "http://crm01-ye.betconstruct.int:8085/api/PlayerCategory/ShortListItems?partnerId="+str(Id)
        response = requests.get(url,headers ={'Content-Type': 'application/json','Authentication':auth} )
        data = response.json()
        print(data)

        self.assertIn("Data",data)
        self.assertIn('HasError', data)
        self.assertIn('AlertType', data)
        self.assertIn('AlertMessage', data)
        self.assertIn('ModelErrors', data)
        for i in range(0,len(data["Data"])):
            self.assertIn("CategoryId",data["Data"][i])
            self.assertIn("Name",data["Data"][i])

    def test_ShortListItemsInvalidData(self):
        auth = Login.LoginValidCases(self)
        char_set = string.ascii_uppercase + string.digits
        invalidPartnerId = ''.join(random.sample(char_set * 24, 24))
        url = "http://crm01-ye.betconstruct.int:8085/api/PlayerCategory/ShortListItems?partnerId=" + str(invalidPartnerId)
        response = requests.get(url, headers={'Content-Type': 'application/json', 'Authentication': auth})
        data = response.json()
        print(data)

        self.assertIn("Data",data)
        self.assertIn("Message",data["Data"])
        self.assertIn("MessageDetail", data["Data"])
        self.assertEqual("The request is invalid.",data["Data"]["Message"])
        self.assertEqual("The parameters dictionary contains a null entry for parameter 'partnerId' of non-nullable type 'System.Int32' for method 'System.Collections.Generic.List`1[BetConstruct.RMT.Models.ViewModels.PlayerCategoriesShortViewModel] ShortListItems(Int32)' in 'BetConstruct.RMT.Backend.Controllers.PlayerCategoryController'. An optional parameter must be a reference type, a nullable type, or be declared as an optional parameter.",data["Data"]["MessageDetail"])
        self.assertIn("HasError", data)
        self.assertEqual(True,data["HasError"])
        self.assertIn("AlertType", data)
        self.assertIn("AlertMessage", data)
        self.assertEqual("The request is invalid.",data["AlertMessage"])
        self.assertIn("ModelErrors", data)