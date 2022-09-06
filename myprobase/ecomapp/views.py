
from unittest import result
from django import http
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import account, product, cart
from .form import accountform, proform, cartform
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.

def home(request):
    
    global result
    
    result = ""
   
    obj = product.objects.all()

   # cartcount = cart.objects.all().filter().count()
 #print(cartcount)

    form = cartform(request.POST)
    
    
    if 'usrnm' in request.session.keys():

        cartcount = cart.objects.all().filter().count()
        userlog = request.session['usrnm']
        
       
        if request.method == "POST":
            
            nm = request.POST['pro_name']
            desc = request.POST['pro_desc']
            qty = request.POST['pro_qty']
            price = request.POST['pro_price']
            imgpro = request.POST['pro_image']
            usercart = request.session['userobj']
            objget = account.objects.get(id=usercart)
            cart.objects.create(
                useofcart = objget,
                pro_name = nm,
                pro_desc = desc,
                pro_qty = qty,
                pro_price = price,
                pro_image = imgpro
            )
            
            return redirect('home')
        
        # if form.is_valid():
        
        #     form.save()
        
        #     return redirect('/home')
    
        elif request.POST:
            qry = request.POST['mysearch']
            result = product.objects.all().filter(Q(productname__icontains=qry | Q(productdesc__icontains=qry)))

        
           
        else:
            result = False
            obj = product.objects.all()

    else:
        userlog = ""
        
        result = False
        
        obj = product.objects.all()                   
    
    return render(request,'home.html',{"obj":obj,"result":result,'userlog':userlog,"cartcount":cartcount})


def about(request):

    return render(request,'about.html')

def signup(request):

    form = accountform(request.POST)

    if form.is_valid():

        ps1 = form.cleaned_data['pass1']
        ps2 = form.cleaned_data['pass2']

        if ps1 == ps2:

            form.save()
        else:
            return HttpResponse("password mismatch")

        return redirect('login')

    return render(request,'signup.html')

def login(request):

    if request.method == "POST":
        try:
            a = account.objects.get(username = request.POST['username'])
            request.session['ssnforfrgtps'] = a.username
            if a.pass1 == request.POST['password']:
                request.session['usrnm'] = a.username
                request.session['userobj'] = a.id
                return redirect('home')

            else:

                return redirect(forgotpassword)
        except:
             return HttpResponse("Incorrect Password or Username<br><lable>Click below to forgot password</lable><br><a href="""" forgotpassword """">Forgot Password</a>")

    
    return render(request,'login.html')

def logout(request):

    if 'usrnm' in request.session.keys():

        del request.session['usrnm']

        return redirect('home')

def forgotpassword(request):

    if request.method == "POST":

        try:
            m = account.objects.get(username=request.POST['username'])

            if m.answer == request.POST['answer']:
                return redirect(f'updatepassword/{m.username}')

            else:
                return render('forgotpassword.html')

        except:
            return HttpResponse("Incorrect Password or Username<br><lable>Click below to forgot password</lable><br><a href="""" Forgotpassword """">Forgot Password</a>")
    
    return render(request,'forgotpassword.html')

def updatepassword(request,username):

    getdata = account.objects.get(username=username)
    form = accountform(request.POST or None,instance=getdata)

    if form.is_valid():
        form.save()
        return redirect('login')

    return render(request,'passwordreset.html',{"form":form})


def crudtable(request):

    obj = product.objects.all()

    return render(request, 'crudtable.html', {"obj":obj})

def crudtabledelete(request, pk):

    obj = product.objects.get(id=pk)

    obj.delete()

    return redirect('crudtable')


def crudtableupdate(request, pk):

    getproduct = product.objects.get(id=pk)
    request.session['updateimage'] = getproduct.id
    form = proform(request.POST or None and request.FILES,  instance=getproduct)

    if form.is_valid():
        form.save()
        return redirect('crudtable')

    return render(request, 'updateproduct.html', {"form":form})

def updateproimg(request):

    qry = request.session['updateimage']
    updt = product.objects.get(pk=qry)

    if request.method == "POST":
        updt.productimage = request.FILES['productimage']
        updt.save()
        return redirect('crudtable')

    return render(request,'updateprodimage.html')

def addnewproduct(request):

    newproduct = product.objects.all()

    formnew = proform(request.POST ,request.FILES)

    if formnew.is_valid():

        formnew.save()

        return redirect('crudtable')

    return render(request,'crudtable.html', {"formnew":formnew})

def view(request,pk):

    obj = product.objects.get(id=pk)

    return render(request, 'procard.html',{"obj":obj})

def cartview(request):

     if 'usrnm' in request.session.keys():
         usercart = request.session['userobj']
         objget = account.objects.get(id=usercart)
         data = cart.objects.filter(useofcart=objget)
         countcart =  data.count()
         print(countcart)
         global total
         total = 0
         for i in data:
            total += i.pro_price
         request.session['total'] = total

     else:
         return HttpResponse("please login to view cart")
     showtotal = request.session['total']
     return render(request, 'cartview.html',{"data":data,"total":total,"countcart":countcart})

def removefromcart(request,pk):

    obj = cart.objects.get(id=pk)
    obj.delete()
    return redirect('cartview')



    

    
    