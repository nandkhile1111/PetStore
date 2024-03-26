from django.shortcuts import render,redirect
from Petstoreapp.models import Product,Category
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q     # you can use the Q object in combination with the | (OR) operator.



# Create your views here.
@login_required(login_url="/handlelogin")
def about(request):
    cdata =Category.objects.all()
    return render(request,'about.html',{'cdata':cdata})

@login_required(login_url="/handlelogin")
def services(request):
    cdata =Category.objects.all()
    return render(request,'services.html',{'cdata':cdata})

def index(request):
    m=Product.objects.all()
    cdata =Category.objects.all()
    return render(request,'index.html',{'m':m,'cdata':cdata})

@login_required(login_url="/handlelogin")
def listproduct(request):
    data = Product.objects.all()
    cdata = Category.objects.all()
    return render(request,'listproduct.html',{'data':data,'cdata':cdata})

@login_required(login_url="/handlelogin")
def petcategory(request,id):
    cdata = Category.objects.all()
    pdata = Product.objects.filter(category_id = id)
    return render(request,'petcategory.html',{'cdata':cdata,'pdata':pdata})

def searchform(request):
    cdata =Category.objects.all()
    data = Product.objects.all()
    if request.method =="POST":
        search=request.POST['search']
        try:
            search_as_int = int(search)
            # If the conversion to int is successful, filter based on price__gt
            items = Product.objects.filter(
                Q(name__icontains=search) |
                Q(price__gt=search_as_int)
            )
        except ValueError:
            # If the conversion to int fails, only filter based on name__icontains
            items = Product.objects.filter(name__icontains=search)
        return render(request,'searchitem.html',{'sdata':items,'cdata':cdata,'data':data})

    
    return render(request,'searchform.html')


@login_required(login_url="/handlelogin")
def petdetail(request,id):
    cdata = Category.objects.all()
    pdata = Product.objects.filter(id = id)
   
    
    return render(request,'petdetail.html',{'cdata':cdata,'pdata':pdata})





def register(request):
    if request.method=="POST":
        email=request.POST['email']
        username = request.POST['username']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']

        if email == "" or username == "" or password =="" or confirm_password == "":
            messages.warning(request,"Field is not be Empty")
            return render(request,'register.html')

        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'register.html')
        try:
            if User.objects.get(email=email):
                
                messages.error(request,"Email is Taken")
                return render(request,'register.html')
        except Exception as identifier:
            pass

        try:
            if User.objects.get(username=username):
               
                messages.error(request,"Username is Taken")
                return render(request,'register.html')
        except Exception as identifier:
            pass



        user = User.objects.create(
            email = email,
            username = username,
        
        )
        user.set_password(password)
        
        user.save()
    return render(request,'register.html')


def handlelogin(request):
    if request.method == 'POST':

        username = request.POST['username']
        password= request.POST['password']
        myuser = authenticate(username = username , password = password)
        
        if myuser is not None:
            login(request,myuser)
            #messages.success(request,"Login Successfully")
            return redirect("/index")
        else:
            messages.success(request,"Invalid Details")
            return redirect("/handlelogin")

    return render(request,'handlelogin.html')

def forgotpassword(request):
    if request.method=="POST":
        username = request.POST['username']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']

        if username == "" or password =="" or confirm_password == "":
            messages.warning(request,"Field is not be Empty")
            return render(request,'forgotpassword.html')
        
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Please enter a correct username")
            return render(request, 'forgotpassword.html')
        
        
        
        if password != confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'forgotpassword.html')
        



        
        user.set_password(password)
        messages.warning(request,"Password Change Successfully")
        user.save()

    return render(request,'forgotpassword.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect("/handlelogin")
