from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .views import home, register,user_login,user_logout,filenames_inv,filenames_testcases,filenames_appliance,get_workspace,get_options
urlpatterns = [
    url(r'^inv/',filenames_inv),
    url(r'^root/',get_workspace),
    url(r'^getoptions/',get_options),
    # url(r'/', welcome),
    url(r'^testcases/',filenames_testcases),
    url(r'^appliances/',filenames_appliance),
    # url(r'^trial/',hello_world),
    url(r'^actifio/',user_login),
    url(r'^register/',register),
    url(r'^logout/',user_logout),

]