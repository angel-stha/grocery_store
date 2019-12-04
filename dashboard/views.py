from django.shortcuts import render

# Create your views here.
def items(request):
    return render(request,'base.html')
def purchase(request):
    return render(request,'purchase.html')   
