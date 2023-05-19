from django.shortcuts import render, redirect
from email import message
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from phone import settings
from django.views.generic import ListView, DetailView
from .models import Contact
from .forms import ContactForm


# Create your views here.
#def home(request):
#    return render(request, 'home.html')
    
    
    
def signup(request):
    
    
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')
         
        if password != password2:
            messages.error(request, "Passwords do not match!")  
            return redirect('home')
         
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('home')      
    
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        myuser.save()    
        
        messages.success(request, "Your Account has been created successfully.")
        return redirect('signin')  
        
       
    
    return render(request, 'signup.html')
    
    
    
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('home')
            
        else:
            messages.error(request, "Login Error")
            return redirect('home')    
    
    return render(request, 'signin.html')



def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out ")
    return redirect('home')


def add(request):
    contacts = Contact.objects.all()
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.author = request.user
            #author = Contact.objects.create(author=contact.author)
            contact.save()        
            messages.success(request, ('Your contact was successfully added!'))
        else:
            messages.error(request, 'Error saving form')
		
        #return redirect("home")

    #context = {'contacts':contacts, 'contact_form': contact_form}
    return render(request=request, template_name="home.html", context={'contact_form':contact_form, 'contacts':contacts})	
     

   