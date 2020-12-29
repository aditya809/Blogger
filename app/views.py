from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *

class home(TemplateView):
    template_name = "app/home.html"
    
    def get_context_data(self,**kwargs):
        context = super(home,self).get_context_data(**kwargs)
        context['social'] = SocialLink.objects.all()
        context['blog'] = Blogs.objects.all()
        return context



def login_user(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'You have Logged In!!')
            return redirect('create_post')

        else:
            messages.success(request,'Sorry Invalid Input!!')
            #return redirect('index')
            return render(request,'Login/index.html')

    else:
        return render(request,'Login/index.html')

def logout_user(request):
    logout(request)
    return home.as_view()(request)


def register(request):
   
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request,'registeration/index.html', {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, 'registeration/index.html', {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, 'registeration/index.html', {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return render(request,'./app/temp2.html')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, 'registeration/index.html', {'form': form})



def create_post(request):

    if request.method=='POST':

        form1=Blogform(request.POST,request.FILES)
        if form1.is_valid():

            form1.save()
            return render(request,'./app/temp.html')
    else:
        form1 = Blogform()

    return render(request, 'create.html', {'form1': form1})
    
    
