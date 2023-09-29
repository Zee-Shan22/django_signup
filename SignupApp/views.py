from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request,"home.html")
    else:
        # Do something for anonymous users.
        return redirect("/login")

def loginUser(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return redirect("/login")
    else:
            return render(request,"login.html")
            # return redirect(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")


def signupUser(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        password=request.POST['password']
        # password2=request.POST['password2']

        # Credentials checking here:
        # if password != password2:
        #      messages.error(request, "Password did not match")
        #      return redirect("/signup")   

        user = User.objects.create_user(username,email, password,)

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        user.first_name = fname
        user.last_name = lname
        # user.email=email
        # user.password = password
        user.save()
        messages.success(request, "User has been created successfully")
        # return HttpResponse(request,"User has been created successfully")
        return redirect("/login")
    else:
         return render (request,"signup.html")



