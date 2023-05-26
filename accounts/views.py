from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import re
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from .optGenerator import GenerateOpt, StoreUser


storeUser = StoreUser()
#user_profile = UserProfile(user=request.user, email_verify=False,username=user_name)
def register(request):
    storeUser.email = ''
    if request.method == 'POST':
        if 'first_name' in request.POST:
            first_name = request.POST['first_name']
        # Handle the case where 'first_name' is missing
        if 'last_name' in request.POST:
                last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        if 'email' in request.POST:
                email= request.POST['email']
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if not password:
                messages.info(request, 'Please enter a password :')
                return redirect('register')
            else:
                if User.objects.filter(username=user_name).exists():
                    messages.info(request, 'user already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
                    user_profile = UserProfile(user=user, email_verify=False, username=user_name)
                    user_profile.save()
                    user.save()
                    return  redirect('/')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')
 

def login(request):
    if request.method == 'POST':
        storeUser.EmailValid = ''
        StoreUser().user = ''
        StoreUser().email = ''
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(username=user_name, password=password)
        if user is not None:
            try:
                # Create your views here.
                user_profile = UserProfile.objects.get(username=user_name)
                user_profile = UserProfile.objects.get(username=user_name)
                userValidate = user_profile.email_verify  # Set the desired value
                storeUser.user = user_name
                storeUser.email = user.email
                if userValidate:
                    auth.login(request, user)
                    return redirect('chatbot/')
                else:
                    return redirect('registereder') 
            except:
                messages.error(request, 'verrificvation error')
                return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html',{'sucess' : storeUser.EmailValid})
        
def logout(request):
    auth.logout(request)
    return redirect('/')

#user_profile = UserProfile.objects.get(username='gymbro')
#user_profile.email_verify = False  # Set the desired value
#user_profile.save()  # Save the changes to the database
generator = GenerateOpt()
def registered(request):
    if request.method == 'POST':
        storeUser.Error = ''
        storeUser.EmailValid = ''
        user_otp = request.POST['otp']
        if generator.generateOtp == user_otp:
            user_profile = UserProfile.objects.get(username=storeUser.user)
            user_profile.email_verify = True  # Set the desired value
            user_profile.save()  # Save the changes to the database
            storeUser.EmailValid = 'User Validated sucessfully' 
            otp = generator.validate(storeUser.user,storeUser.email )
            storeUser.user == ''
            storeUser.email = ''
            return redirect('/')
        else:
            storeUser.Error = 'Invalid OTP'
            return redirect('registereder')
    else:
        return render(request, 'registered.html')

def registereder(request):
    if request.method == 'POST':
        # Generate the OTP and send the email

        otp = generator.generate(storeUser.user,storeUser.email )
        print(otp) 
        return  redirect('registered')
    else:
        messages.error(request, storeUser.Error)
        return render(request, 'registereder.html')


