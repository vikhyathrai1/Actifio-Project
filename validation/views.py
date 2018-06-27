from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from .serializers import UserSerializer, SimpleDataSerializer
# from django.contrib.auth.models import Inventory
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages, auth
from rest_framework.decorators import api_view
from .models import SimpleData
import os
from django.urls import reverse


class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')

    serializer_class = UserSerializer


def home(request):
    if not request.session.session_key:
        return render(request, 'login.html')
    else:
        return render(request,'actifio.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            request.session["username"]=username;
            #request.session.set_expiry(60)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
            #return render(request, "actifio.html")
        else:
            messages.info(request, message="username or password is not correct")
    else:
        return render(request, 'login.html')


def user_logout(request):
    del request.session["username"]
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']


            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.info(request, message="Username or password already exists")
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

# def hello_world(request):
#     os.chdir('validation')
#     stream = os.popen('test.sh')
#     stream.read()
#     return render(request, stream.read())


def get_workspace(request):
    global root
    if request.method=='POST':
        root=request.POST['views']
        #return HttpResponseRedirect(reverse('appliance'))
        return redirect('/')
    else:

        return HttpResponseRedirect(reverse('home'))

@api_view(['GET'])
def filenames_inv(request):
    global root
    demo=list()
    smp = SimpleData()
    root_inv = os.path.join(root,'inv')
    root_host= os.path.join(root_inv,'host')
    for path, dirs, files in os.walk(root_host):
            for f in files:
                if f.endswith('.py'):
                    smp.add(f)

            # data = {"data": demo}
    # inventory_files_obj = Inventory.objects.all().values(*demo)
    # serializer = Inventoryserializer(inventory_files_obj, many=True)
    # serializer = SimpleDataSerializer(SimpleData(demo))
    return Response(smp.__dict__)
# return render(request, )



@api_view(['GET'])
def filenames_appliance(request):
    global root
    demo=list()
    smp_app= SimpleData()
    #root="C:/Users/Vikhyath Rai/PycharmProjects/internship/robot/robot/inv/appliance"
    root_inv = os.path.join(root, 'inv')
    root_appliance = os.path.join(root_inv, 'appliance')
    for path, dirs, files in os.walk(root_appliance):
            for f in files:
                if f.endswith('.py'):
                    smp_app.add(f)
    return Response(smp_app.__dict__)


@api_view(['GET'])
def filenames_testcases(request):
    global root
    # demo=list()
    smp_test= SimpleData()
    #root="C:/Users/Vikhyath Rai/PycharmProjects/internship/robot/robot/suites"
    root_testcases = os.path.join(root, 'suites')
    for path, dirs, files in os.walk(root_testcases):
             for f in files:
                 if f.endswith('.robot'):
                     smp_test.add(f)
    return Response(smp_test.__dict__)

def get_options(request):
    print(request.read())
    return HttpResponse('')

# Create your views here.
# printing details from db