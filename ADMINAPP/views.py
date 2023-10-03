from django.shortcuts import render,redirect
from django.http import HttpResponse
from ADMINAPP.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from USERAPP.models import*
def add_category(request):
      return render(request,'addcategories.html') 
def view_category(request):
      data=Category.objects.all()
      return render(request,'viewcategories.html',{'data':data}) 
def add_product(request):
      data=Category.objects.all()
      return render(request,'addproduct.html',{'data':data})
def view_product(request):
      data=Product.objects.all()
      return render(request,'viewproduct.html',{'data':data}) 


def customerlist(request):
       data=Customer.objects.all()
       return render(request,'viewfeedback.html',{'data':data})
def complaintlist(request):
       data=Complaint.objects.all()
       
       return render(request,'viewcomplaint.html',{'data':data})
                 

def registerlist(request):
       data=Register.objects.all()
       return render(request,'viewusers.html',{'data':data})
def admin(request):
      category=Category.objects.all().count()
      product=Product.objects.all().count()
      orders=Booking.objects.all().count()
      complaints=Complaint.objects.all().count()
      return render(request,'index.html',{'category':category,'product':product,'orders':orders,'complaints':complaints}) 
def productform(request):
      return render(request,'addproducts.html') 

      
def productdata(request):
      if request.method=='POST':
           productName=request.POST['productName']
           productDescription=request.POST['productDescription']
           productPrice=request.POST['productPrice']
           category=request.POST['category']
           stock=request.POST['stock']
           productImage=request.FILES['productImage']
          
           data=Product(productName=productName,productDescription=productDescription,productPrice=productPrice,category=category,productImage=productImage,stock=stock)
           data.save()
           return redirect('view_product')

      
def categorydata(request):
      if request.method=='POST':
          
           description=request.POST['description']
          
           category=request.POST['category']
           data=Category(description=description,category=category)
           data.save()
           return redirect('view_category')      
def view_booking(request):
       data=Booking.objects.all()
       return render(request,'viewbookings.html',{'data':data})   
def deleteproduct(request,id):
                  Product.objects.filter(id=id).delete()
                  return redirect('view_product')
def editproduct(request,id):
      data=Product.objects.filter(id=id)
      dataa=Category.objects.all()
      return render(request,'editproduct.html',{'data':data,'dataa':dataa}) 
     
      
def updateproduct(request,id):
       if request.method=='POST':
           productName=request.POST['productName']
           productDescription=request.POST['productDescription']
           productPrice=request.POST['productPrice']
           stock= request.POST['stock']
           category=request.POST['category']
           try:
             img_c = request.FILES['productImage']
             fs = FileSystemStorage()
             file = fs.save(img_c.name, img_c)
           except MultiValueDictKeyError:
             file = Product.objects.get(id=id).productImage
           Product.objects.filter(id=id).update(productName=productName,productDescription=productDescription,stock=stock,productPrice=productPrice,category=category,productImage=file)
           return redirect('view_product')
      
def deletecategory(request,id):
                  Category.objects.filter(id=id).delete()
                  return redirect('view_category')
def editcategory(request,id):
      data=Category.objects.filter(id=id)
      return render(request,'editcategory.html',{'data':data}) 
def updatecategory(request,id):
       if request.method=='POST':
          
           description=request.POST['description']
           
           category=request.POST['category']
          
           Category.objects.filter(id=id).update(description=description,category=category)
           return redirect('view_category')
       
def notdelivered(request):
       data=Booking.objects.filter(status=0)
       return render(request,'notdelivered.html',{'data':data})  
def delivereddata(request,id):
       data=Booking.objects.filter(id=id).update(status=1)
       return redirect('delivered')   
def delivered(request):
        data=Booking.objects.filter(status=1)
        return render(request,'delivered.html',{'data':data})  