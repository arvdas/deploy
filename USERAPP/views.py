from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from ADMINAPP.models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from USERAPP.models import *
from django.db.models.aggregates import Sum
import stripe
from django.conf import settings
def home(request):
         data=Product.objects.all()
         dataa=Category.objects.all()
         return render(request,'user.html',{'data':data,'dataa':dataa}) 
def about_us(request):
      dataa=Category.objects.all()
      return render(request,'about.html',{'dataa':dataa}) 
def single(request,id):
          dataa=Category.objects.all()
          data=Product.objects.filter(id=id)
          
          return render(request,'single.html',{'data':data,'dataa':dataa})       
def contact(request):
      dataa=Category.objects.all()
      return render(request,'contact.html',{'dataa':dataa})
def register(request):
      dataa=Category.objects.all()
      return render(request,'register.html',{'dataa':dataa})
def login(request):
      dataa=Category.objects.all()
      return render(request,'login.html',{'dataa':dataa})
def publicdata(request):
    if request.method == "POST":
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        if Register.objects.filter(Email=Email,Password=Password).exists():
           data = Register.objects.filter(Email=Email,Password=Password).values('Username','id','Phone_no').first()
           request.session['username'] = data['Username']
          
           request.session['u_id'] = data['id']
           request.session['phonenumber_u'] = data['Phone_no'] 
           
           request.session['email'] = Email
           request.session['password_u'] = Password
           return redirect('home') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')
def userlogout(request):
    del request.session['username']
    
    del request.session['u_id']
    del request.session['phonenumber_u']

    del request.session['email']
    del request.session['password_u']
    return redirect('home')   
def customerdata(request):
      if request.method=='POST':
           FName=request.POST['FName']
           LName=request.POST['LName']
           Email=request.POST['Email']
           Message=request.POST['Message']
           data=Customer(FName=FName,LName=LName,Email=Email,Message=Message)
           data.save()
           return redirect('contact')
def registerdata(request):
      if request.method=='POST':
           Username=request.POST['Username']
           Phone_no=request.POST['Phone_no']
           Email=request.POST['Email']
           Password=request.POST['Password']
           data=Register(Username=Username,Phone_no=Phone_no,Email=Email,Password=Password)
           data.save()
           return redirect('login')         
      
def product_list(request,category):
      if(category=="all"):
            data=Product.objects.all()
      else:
            data=Product.objects.filter(category=category)
      dataa=Category.objects.all()
      return render(request,'products.html',{'data':data,'dataa':dataa})
         
def category_list(request):
      data=Category.objects.all()
      return render(request,'categories.html',{'data':data}) 
def booking(request):
      
      u = request.session.get('u_id')
      data = Cart.objects.filter(userid=u, status=0)
      s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
      return render(request, 'booking.html', {'data': data,'s':s})
stripe.api_key=settings.STRIPE_SECRET_KEY
def bookingdata(request):
      if request.method=='POST':
            user_id=request.session.get('u_id')
            Address=request.POST['Address']
            City=request.POST['City']
            State=request.POST['State']
            request.session['address']= Address
            request.session['city']= City
            request.session['state']= State
           
            order = Cart.objects.filter(userid=user_id, status=0)
            for i in order:
                 
             data=Booking(userid=Register.objects.get(id=user_id),cartid=Cart.objects.get(id=i.id),Address=Address,City=City,State=State)
             data.save()
             Cart.objects.filter(id=i.id).update(status=1)
            #return redirect('ordered')
            total_amount=0
            cartid=[]
            for i in order:
                 total_amount+=i.total
                 #cartid.append(i.id)

            #request.session['cart_id_no'] = cartid 
            # product = Product.objects.get(id=product_id)
            session = stripe.checkout.Session.create(
            payment_method_types = ['card'],
           line_items=[{
    'price_data': {
        'currency': 'inr',
        'product_data': {
            'name': 'Total:',  
        },
        'unit_amount': int(total_amount) * 100,
    },
    'quantity': 1,
}],

            mode='payment',
            success_url = "http://127.0.0.1:8000/payment_success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = "http://127.0.0.1:8000/pay_cancel",
            #client_reference_id=product_id,
            )
            return redirect(session.url, code=303)
      

def payment_success(request):
      #cart_id_num = request.session.get('cart_id_no')
      session = stripe.checkout.Session.retrieve(request.GET['session_id'])
      plan_id = session.client_reference_id
     
     
    

      return redirect('ordered')
def ordered(request):
      dataa=Category.objects.all()
      return render(request,'Ordered.html',{'dataa':dataa}) 

def cart(request):
   
    u = request.session.get('u_id')
    if u:
        data = Cart.objects.filter(userid=u, status=0)
        s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
        return render(request, 'cart.html', {'data': data,'s':s})
    else:
        return render(request, 'login.html', {'msg': 'Please log in to access your cart'})

def cartdata(request,id):
    
    try:
        if request.method=="POST":
            user_id=request.session.get('u_id')
            quantity=request.POST['quantity']
            total=request.POST['total']
            data=Cart(userid=Register.objects.get(id=user_id),productid=Product.objects.get(id=id),quantity=quantity,total=total)
            data.save()
            data1 = get_object_or_404(Product, id=id)
            current_stock = data1.stock

            if data1:  # Assuming purchased is a boolean indicating whether the product is added to the cart
              if current_stock > 0:
               current_stock -= 1
               data1.stock = current_stock
               data1.save()
              else:
        # Handle out-of-stock scenario here (e.g., display a message or redirect to a different page)
               pass
        return redirect('cart')
    except Register.DoesNotExist:
        
         return render(request, 'login.html', {'msg': 'Please log in to access your cart'})

       
        
def cartdelete(request,id):
       Cart.objects.filter(id=id).delete()
       return redirect('cart')
def history(request):
      
      u = request.session.get('u_id')
      data = Booking.objects.filter(userid=u)
      
      return render(request, 'userhistory.html', {'data': data})

def complaint(request,id):
       u = request.session.get('u_id')
       data = Cart.objects.filter(userid=u,id=id)
       return render(request, 'complaints.html', {'data': data}) 
def complaintdata(request, id):
    if request.method == "POST":
        user_id = request.session.get('u_id')
        complaint = request.POST['complaint']
        
        userid = Register.objects.get(id=user_id)
        productid = Product.objects.get(id=id)
        data = Complaint(userid=userid, productid=productid, complaint=complaint)
        data.save()
        return redirect('complaint', id=id)


     

     

      