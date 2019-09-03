# -*- coding: utf-8 -*
from django.urls import reverse 
from django.http import JsonResponse
from django.template import RequestContext
from product.models import ProductList
from utils.tools import response_err


def check_user(view_func): 

    def _wrapped_view_func(request, *args, **kwargs):
        try:
            pid = request.POST['product_id']
            prod = ProductList.objects.get(product_id=pid)

            if int(prod.vip) != int(request.POST['vip']):
                return JsonResponse(response_err(code=1002))

        except ProductList.DoesNotExist:
            return JsonResponse(response_err(code=1))

        # return func
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
