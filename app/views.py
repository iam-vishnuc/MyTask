
from django.shortcuts import redirect, render
from .forms import UserForms,LoginForm, UpdateForm
from . models import Register, Gallery

from django.contrib.auth import logout 



# Create your views here.
def index(request):
    return render(request,'index.html')


#login
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = Register.objects.get( username=username, password=password)
            
            if user is not None:
                # login(request,user)
                return redirect('/profile/%s' % user.id )
            else:
                return redirect('/login/')
    else:
        login_form = LoginForm()
    return render(request,'login.html',{'form':login_form})



#gallery
def gallery(request):
    image = Gallery.objects.all()
    return render(request,'gallery.html',{'images':image})

def details(request, id):
    images = Gallery.objects.get(id=id)
    return render(request, 'details.html', {'images':images})

#register
def register(request):
    if request.method == 'POST':
        register_form = UserForms(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']  
            name = register_form.cleaned_data['name']  
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            savedata = Register(username=username,name=name,email=email, password=password)
            savedata.save()
            return redirect('/login/')
    else:
        register_form = UserForms()

    
    return render(request, 'register.html', {'form': register_form})

#profile
def profile(request, id):
    user = Register.objects.get(id=id)
    return render(request, 'profile.html', {'user':user})


#update
def update(request, id):
    user = Register.objects.get(id=id)
    if request.method == 'POST':
        update_form = UpdateForm(request.POST or None, instance=user)
        if update_form.is_valid():
            update_form.save()
            return redirect('/profile/%s' % user.id)
    else:
        update_form = UpdateForm(instance=user)
    return render(request, 'update.html', {'user':user, 'form':update_form})


def delete(request):
    pass


def logouts(request):
    logout(request)
    return redirect('/')