from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Submission

# Create your views here.
def hello(res):
    hai="hello world"
    return render(res,"one.html")

def register_page(request):
    if request.method=='GET':
        return render(request,'login.html')  

    if request.method == 'POST':
        name=request.POST.get('name','')
        crop_type=request.POST.get('crop_type','')
        quantity=request.POST.get('quantity',0)
        submissions = Submission.objects.create(name=name,crop_type=crop_type,quantity=quantity)
        submissions= Submission.objects.all()
        return render(request,'farmer.html',{'submissions':submissions})
def delete_submission(request, id):
    submission = get_object_or_404(Submission, id=id)
    submission.delete()
    return render(request,'login.html')  # Replace 'farmer_page' with the name of your page view    
      



        
    
    
    

def farmer_page(request):
    submissions= Submission.objects.all()
    
    return render(request, 'farmer.html',{'submissions':submissions})
    

def customer_page(request):
    return render(request, 'customer.html')

def vendor_page(request):
    return render(request, 'vendor.html')
