# iport for uploads
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from myapp.algo import Algo
# import for authenticate authorise

from django.views import generic
from django.views.generic import View


from myapp.forms import UserForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'myapp/index.html')

def user(request):
    return render(request,"myapp/user.html")

def mapuser(request):
    return render(request,'myapp/usermap.html')

@login_required
def viewdata(request):
    return render(request,'myapp/test.html')


@login_required
def dashboard(request):
    if request.method == 'POST':
        state = request.POST['state']
        district = request.POST['district']
        city = request.POST['city']
        algo = Algo()
        op = algo.myalgo(state,district,city)
        return render(request, 'myapp/adm2.html',{'algo':op})

    return render(request,'myapp/adm2.html')

@login_required
def special(request):
    if request.method == 'POST':
        return render(request, 'myapp/jsdd.html')

    return render(request,'myapp/jsdd.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            #user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm

            # Check if they provided a profile picture

            # Now save model

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'myapp/registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect('special')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'myapp/login.html', {})
