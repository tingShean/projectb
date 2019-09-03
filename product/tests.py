from django.test import TestCase, Client
from django.urls import reverse
from .models import ProductList

import json


class ProductViewTest(TestCase):
    """
    This class contains tests that convert measurements from one
    unit of measurement to another.
    """
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")


    def setUp(self):
        ProductList.objects.create(stock_pcs=6, price=150, shop_id='um', vip=0)
        ProductList.objects.create(stock_pcs=10, price=110, shop_id='ms', vip=0)
        ProductList.objects.create(stock_pcs=20, price=900, shop_id='ps', vip=0)
        ProductList.objects.create(stock_pcs=2, price=1899, shop_id='ps', vip=1)
        ProductList.objects.create(stock_pcs=8, price=35, shop_id='ms', vip=0)
        ProductList.objects.create(stock_pcs=5, price=60, shop_id='um', vip=0)
        ProductList.objects.create(stock_pcs=5, price=800, shop_id='ps', vip=1)

        # Every response test need client
        self.client = Client()


    def test_db_view(self):
        p_list = ProductList.objects.all()

        self.assertEqual(len(p_list), 7)


    def test_select_product_id(self):
        resp = self.client.get('/product/list/1/1')
        # response is 200 ok
        self.assertEqual(resp.status_code, 200)

        resp = self.client.get('/product/list/1/7')
        resp_json = json.loads(resp.content)
        # response is 200 ok
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp_json['status'], 1)
        self.assertEqual(resp_json['code'], 1001)

        resp = self.client.get('/product/list/8/100')

        self.assertEqual(resp.status_code, 200)


    def test_add_del_order(self):
        print('test_add_order')
        data = {'product_id': 1, 'stock_pcs': 1, 'customer_id': 1, 'vip': 0}
        resp = self.client.post('/product/add_order', data)
        # response is 200 ok
        print(resp.content)
        self.assertEqual(resp.status_code, 200)

        data = {'order_id': 1}
        resp = self.client.post('/product/del_order', data)
        print(resp.content)
        self.assertEqual(resp.status_code, 200)
