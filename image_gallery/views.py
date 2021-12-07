from django.http import HttpResponse
from django.shortcuts import render ,redirect
from myapp.models import *
from django.contrib import messages


def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html' )

def show_home_page(request):

    cats=Category.objects.all()

    images = Image.objects.all()
    data = {'images': images, 'cats': cats}


    return render(request,"home.html", data)



def show_category_page(request, cid):
    print(cid)

    cats = Category.objects.all()


    category = Category.objects.get(pk=cid)

    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}


    return render(request,"home.html", data)

def home(request):
    return redirect('/home')


def login(request):
    print("login cALL")
    username = request.POST["username"]
    password = request.POST["password"]

    # username and password is carect
    user = LoginDetails.objects.get(name=username)
    if username == user.name and password == user.password:
        request.session['username'] = username
        return redirect("/home")
    else:
        messages.error(request, "Invalid password!")
        return redirect("/home")

def singup(request):
    name = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]
    confirmPassword = request.POST["confirmpassword"]
    if password != confirmPassword:
        messages.error(request,"password and confirmpassword are not same please try again")
    else:
         data = LoginDetails(name=name, emailid=email, password=password)
         data.save()
         messages.success(request,"successfully singup please login")

    return redirect("/home")

def logout(request):
    request.session.flush()
    return redirect('/home')

