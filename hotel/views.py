from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import UpdateForm
from django.contrib.auth import authenticate,login,logout 
import simplejson as json
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views import View
lis =[]
# Create your views here.
def Admin(request):
    return render(request,'admin.html')
"""
class Home(View):
    global lis
    f = Types.objects.filter(name=1)
    #f=Types.object.raw('selct * from ')
    f2 = Types.objects.filter(name=2)
    f3 = Types.objects.filter(name=3)
    def get(self,request):
        return render(request,'index.html' ,{"f":self.f,"f2":self.f2,'f3':self.f3})
    def post(self,request):
        self.lis = request.POST.getlist('key')
        price=0
        lis =map(int,self.lis)
        order =Types.objects.filter(id__in=list(self.lis))
        for i in order:
            price=price+i.price
        adv = price*25/100
        return render(request ,'order.html',{'order':order ,'price':price,'lis':self.lis,'adv':round(adv,1)})




"""        
def Home(request): 
    f = Types.objects.filter(name=1)
    f2 = Types.objects.filter(name=2)
    f3 = Types.objects.filter(name=3)
    return render(request,'index.html' ,{"f":f,"f2":f2,'f3':f3})

def About(request):
    form = Jobs.objects.all()
    return render(request,'about.html',{'form':form})
def Contact(request):
    form =Address.objects.get(id=1)
    
    return render(request,'contact.html',{'form':form})

def Order(request):
    global lis
    if request.method == 'POST':
        lis = request.POST.getlist('key')
        price=0
        order =Types.objects.filter(id__in=list(lis))
        for i in order:
            price=price+i.price
        adv = price*25/100
        return render(request ,'order.html',{'order':order ,'price':price,'lis':lis,'adv':round(adv,1)})
@login_required
def Dashboard(request):
    ords = ConForm_Orders.objects.order_by('-id')
    total= ConForm_Orders.objects.all().count()
    pending = ConForm_Orders.objects.filter(status__in=['Order not packed','Ready to Dlivery']).count()
    forms ={'form':ords,'total':total,'pending':pending,'d':total-pending}
    
    return render(request ,'dashboard.html',forms)
@login_required
def DashboardStaff(request):
    ords = ConForm_Orders.objects.filter(delivery_boy_id=request.user).order_by('-id')
    total= ConForm_Orders.objects.filter(delivery_boy_id=request.user).count()
    pending = ConForm_Orders.objects.filter(delivery_boy_id=request.user,status__in=['Order not packed','Ready to Dlivery']).count()
    forms ={'form':ords,'total':total,'pending':pending,'d':total-pending}
    return render(request,'staff.html',forms)

def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        select   = request.POST.get('select')

        try:
            user = authenticate(username=username,password=password)
            if select=='Admin':
                if user.is_superuser:
                    if user is not None:
                        login(request,user)
                        return redirect('dashboard')
            else:
                if user.is_superuser ==False:
                    if user is not None:
                        login(request,user)
                        return redirect('staff')
        except:
            
            return render(request,'login.html',{'message':True})


    return render(request,'login.html',{'message':False})
@login_required
def Logout(request):
    logout(request)
    return redirect('login')


def Mail(email,Id):
    
    subject = 'welcome to Brown Multi Cuisine Restaurant'
    message = "We've reciver Your Order. Your id is "+ str(Id)
   
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail( subject, message, email_from, recipient_list )
def Receive_mail(request):
    pass


def Conform_orders(request):
    global lis
    if request.method=='POST':
        Price = request.POST.get('price')
        print(Price)
        advance = request.POST.get('advance')
        Payment_mode =request.POST.get('fullpayment')
        Name = request.POST.get('contact_name')
        No   = request.POST.get('contact_no')
        Email = request.POST.get('contact_email')
        Addr = request.POST.get('contact')
        Phone_pay = request.POST.get('phone_pay')
        Paytm   =  request.POST.get('paytm')
        Upi   =  request.POST.get('upi')
        lis = map(int,lis)
        list_1 = list(lis)
        lis = Types.objects.filter(id__in=list_1)
        list_1 = [
               {
               "id":i.id,
               "name":i.types,
               "price":i.price             
               } for i in lis
                 ] 
        list_1 = json.dumps(list_1)
        print(lis)
        if advance:    
            if Phone_pay:
                conform_order = ConForm_Orders(price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Phone_pay,json=list_1,payment_mode='advance',advance=advance,balance=float(Price)-float(advance))
                
                conform_order.save()
                print(Email)
                Id = ConForm_Orders.objects.all().last()
                #Mail(Email,Id.id)
                return redirect('home')
            if Paytm:
                conform_order = ConForm_Orders( price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Paytm,json=list_1,payment_mode='advance',advance=advance,balance=float(Price)-float(advance))
                conform_order.save()
                Id = ConForm_Orders.objects.all().last()
               # Mail(Email,Id.id)
                return redirect('home')
            elif Upi:
                conform_order = ConForm_Orders( price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Upi,json=list_1,payment_mode='advance',advance=advance,balance=float(Price)-float(advance))
                conform_order.save()
                Id = ConForm_Orders.objects.all().last()
                #Mail(Email,Id.id)
                return redirect('home')
        else:
            if Phone_pay:
                conform_order = ConForm_Orders(price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Phone_pay,json=list_1,advance=Price,balance=0)
                
                conform_order.save()
                Id = ConForm_Orders.objects.all().last()
                #Mail(Email,Id.id)
            
                return redirect('home')
            elif Paytm:
                conform_order = ConForm_Orders( price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Paytm,json=list_1,balance=0,advance=Price)
                conform_order.save()
                Id = ConForm_Orders.objects.all().last()
              #  Mail(Email,Id.id)
                return redirect('home')
            elif Upi:
                conform_order = ConForm_Orders( price=Price,name=Name, email=Email, ph_no=No, addr=Addr, payment=Upi,json=list_1,balance=0,advance=Price)
                conform_order.save()
                Id = ConForm_Orders.objects.all().last()
              #  Mail(Email,Id.id)
                return redirect('home')
        



        


        
def Update(request,pk):
    up = ConForm_Orders.objects.get(id=pk)
    order = UpdateForm(instance=up)
    if request.method == 'POST':
        order = UpdateForm(request.POST,instance=up)
        if order.is_valid():
            order.save()
            return redirect('../../')
    
    return render(request,'update_form.html',{"ord":order,'user':request.user.is_superuser})
def Delete_order(request,pk):
    del_order = ConForm_Orders.objects.get(id=pk)
    
    del_order.delete()
    return redirect('dashboard')

def Items(request,list):
    no = ConForm_Orders.objects.get(id=list)
    list1 =json.loads(no.json)
    p=[]
    for i in list1:
        p.append(i['id'])
    order = Types.objects.filter(id__in=p)
    return render(request,'items.html',{'order':order})

def Print(request,pk):
    addres =Address.objects.get(id=1)
    order = ConForm_Orders.objects.get(id=pk)
    items = json.loads(order.json)
    subtotal =0
    for i in items:
        subtotal+=i["price"]
    
    total = subtotal
    x = datetime.now()
    time = x.strftime("%X")
    text = {'addr':order,'addr1':addres.address,'items':items,'subtotal':subtotal,'total':total,'date':order.date,'time':time}
    return render(request,'print.html',text)

