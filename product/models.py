from django.db import models


# Create your models here.
class ProductList(models.Model):
	product_id = models.AutoField(primary_key=True)
	stock_pcs = models.IntegerField()
	price = models.IntegerField()
	shop_id = models.CharField(max_length=20)
	vip = models.IntegerField()


class Order(models.Model):
	id = models.AutoField(primary_key=True)
	product_id = models.IntegerField()
	qty = models.IntegerField()
	price = models.IntegerField()
	shop_id = models.CharField(max_length=20, blank=True, null=True)
