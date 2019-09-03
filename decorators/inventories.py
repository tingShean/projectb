# -*- coding: utf-8 -*
from django.urls import reverse 
from django.http import JsonResponse
from django.template import RequestContext
from product.models import ProductList
from utils.tools import response_err


def inventories(view_func):

	# check inventories fo the follow product
	def _wrapped_view_func(request, *args, **kwargs):
		# get inventories from request
		try:
			#pid = request.product_id
			pid = kwargs.get('pid') if kwargs.get('pid', -1) > -1 else request.POST['product_id']

			prod = ProductList.objects.get(product_id=pid)

			amount = kwargs.get('stock_pcs') if kwargs.get('stock_pcs', -1) > -1 else request.POST['stock_pcs']

			if int(prod.stock_pcs) < int(amount):
				return JsonResponse(response_err(code=1001))

		except ProductList.DoesNotExist:
			return JsonResponse(response_err(code=1000))

		except Exception as e:
			print(e)
			return JsonResponse(response_err())

		return view_func(request, *args, **kwargs)

	return _wrapped_view_func
