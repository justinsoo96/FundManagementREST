from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import InvestmentFund
import datetime

# Create your tests here.
class FundAPITestCase(APITestCase):
    def setUp(self):
        self.fund = InvestmentFund.objects.create(
            fund_id='AHAM0001',
            fund_name='Test Fund',
            fund_manager_name='Justin Soo',
            fund_description='For AHAM assessment',
            fund_nav='10000.00',
            fund_performance='5.0'
        )

    def test_list_funds(self):
        response = self.client.get('/gateway/funds/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_fund(self):
        data = {
            'fund_id': 'AHAM0002',
            'fund_name': 'New Fund', 
            'fund_manager_name': 'Fund Manager 1',
            'fund_description': 'Test Fund Creation',
            'fund_nav': '5999.99',
            'fund_performance': '3.33'
        }
        response = self.client.post('/gateway/funds/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class FundModelTestCase(TestCase):
    def setUp(self):
        self.fund = InvestmentFund.objects.create(
            fund_id='AHAM0001',
            fund_name='Test Fund',
            fund_manager_name='Justin Soo',
            fund_description='For AHAM assessment',
            fund_nav='10000.00',
            fund_performance='5.0'
        )

    def test_create_fund(self):
        fund_count = InvestmentFund.objects.count()
        self.assertEqual(fund_count, 1)

    def test_update_fund_performance(self):
        self.fund.fund_performance = 15.0
        self.fund.save()
        updated_fund = InvestmentFund.objects.get(pk=self.fund.pk)
        self.assertEqual(updated_fund.fund_performance, 15.0)

class FundIntegrationTestCase(APITestCase):
    def test_create_fund(self):
        data = {
            'fund_id': 'AHAM0002',
            'fund_name': 'New Fund', 
            'fund_manager_name': 'Fund Manager 1',
            'fund_description': 'Test Fund Creation',
            'fund_nav': '5999.99',
            'fund_performance': '3.33'
        }
        
        response = self.client.post('/gateway/funds/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify the data is stored in the database
        new_fund = InvestmentFund.objects.last()
        self.assertEqual(new_fund.fund_name, 'New Fund')