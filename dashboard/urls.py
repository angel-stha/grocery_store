from django.urls import path
from . import views

urlpatterns =[
    path('items',views.items, name='items'),
    path('purchase',views.purchase, name='purchase'),
    path('buyer',views.buyer,name='buyer'),
 

]