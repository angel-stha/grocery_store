from django.shortcuts import render
from django import forms
from login.models import Buyer
# Create your views here.
def items(request):
    return render(request,'base.html')
def purchase(request):
    # if request.method == 'POST':
    #     return render(request,'form.html')

   
   
             
    return render(request,'purchase.html')   
def buyer(request):
    Buyer_list = Buyer.objects.all()
    buyer_list = {
    "Buyer_list": Buyer_list
      }
    print(buyer_list)
    return render(request,'purchase.html', {'buyer_list': Buyer_list})


     
             
             
        