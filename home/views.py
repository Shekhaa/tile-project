from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from home.models import tile
from django.http import HttpResponse
from home.models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember=request.POST.get('remember',False)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if not remember:
                request.session.set_expiry(0)
            return redirect('/home/index')  # Redirect to the home page after successful sign-in
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('/home/index')  # Redirect to the home page after successful sign-out


def index(request):
    if request.method=="POST":
        lists=[1,2,3,4,5,6,7,8,9,10]
        
        lists[0]=eval(request.POST.get('ob1'))
        lists[1]=eval(request.POST.get("ob2"))
        lists[2]=eval(request.POST.get("ob3"))
        lists[3]=eval( request.POST.get("ob4"))
        lists[4]=eval(request.POST.get("ob5"))
        lists[5]=eval( request.POST.get("ob6"))
        lists[6]=eval(request.POST.get('ob7'))
        lists[7]=eval(request.POST.get("ob8"))
        lists[8]=eval(request.POST.get("ob9"))
        lists[9]=eval( request.POST.get("ob10"))

        print(lists)
        dicts=dict(enumerate(lists))
        print(dicts)
        context={'dicts':dicts}
        return render(request,'show.html',context)

    return render(request, 'index.html')

def shop(request):
    
    return render(request,'lists.html')

def Carts(request):
    var=tile.objects.all()
    #chalo ek site ka sara maal nikalte hain
    kar={'la':var}
    return render(request,'Carts.html',kar)

def contact(request):
    if request.method=="POST":
        a=request.POST['obj1']
        b=request.POST['obj2']
        c=request.POST['obj3']
        d=request.POST['obj4']

        con=Contact(name=a,email=c,phone=d,issue=b)
        con.save()
    return render(request,'ok.html')

def about(request):
    
    return render(request,'about.html')