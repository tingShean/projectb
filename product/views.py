from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.db.models import F
from .models import ProductList, Order
from .object import ProductObject
from order.object import OrderObject
from decorators.inventories import inventories
from decorators.check_user import check_user
from utils.tools import response_err

import json


# Create your views here.
def index(request):
    tmpl = loader.get_template('product_list.html')
    pro_list = ProductList.objects.all()

    context = {
        'pro_list': pro_list if pro_list else {},
    }
    return render(request, 'product_list.html', context)


@inventories
def plist(request, pid, stock_pcs):
    """取得Product list by pid"""

    try:
        prod = ProductList.objects.filter(product_id=pid)

        if not prod.exists():
            return JsonResponse({})

        data = json.dumps(list(prod.values()))
        # print(data)
        # print(prod)
        # print(json.dumps(list(prod)))

    except Exception as e:
        print(e)
        return JsonResponse({})

    # return HttpResponse(status=200)
    return JsonResponse(data, safe=False)


@inventories
@check_user
def add_order(request):
    """add order in db"""
    try:
        pid = request.POST['product_id']
        prod = ProductList.objects.filter(product_id=pid).values()
        print(prod[0])

        if not prod.exists():
            return JsonResponse(response_err(code=1000))

        # Order.objects.create(**orderObj.get_all_data())
        qty = int(request.POST['stock_pcs'])
        Order.objects.create(
            product_id=prod[0]['product_id'],
            qty=qty,
            price=(qty * prod[0]['price']),
            shop_id=prod[0]['shop_id']
        )

        amount = prod[0]['stock_pcs'] - qty

        prod_data = ProductList.objects.filter(product_id=pid).update(stock_pcs=amount)
        # prod.update(stock_pcs=amount)
        if prod_data != 1:
            return JsonResponse(response_err(code=2))

        orders = Order.objects.all().values()
        olist = json.dumps(list(orders))

    except Exception as e:
        print('error:', e)
        return JsonResponse(response_err())

    return JsonResponse(olist, safe=False)


def del_order(request):
    """del order"""
    try:
        oid = request.POST['order_id']
        order = Order.objects.filter(id=oid)

        if not order.exists():
            return JsonResponse(response_err(code=2000))

        order_data = order.values()

        # 把刪除的數量補回去
        ProductList.objects.filter(product_id=order_data[0]['product_id']).update(
            stock_pcs=F('stock_pcs') + order_data[0]['qty'])

        # 刪除訂單
        order.delete()

    except Exception as e:
        print(e)
        return JsonResponse(response_err())

    return JsonResponse({})



