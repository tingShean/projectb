from django.urls import path
from product import views


urlpatterns = [
	path('index', views.index),
	path('list/<int:pid>/<int:stock_pcs>', views.plist),
	path('add_order', views.add_order),
	path('del_order', views.del_order),
]