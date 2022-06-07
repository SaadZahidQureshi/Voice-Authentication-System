from unicodedata import name
from django.urls import path

from Banker import views as bv



urlpatterns = [
    path("", bv.voicesignin, name= "voicesignin"),
    path ('aboutus', bv.aboutus, name = 'aboutus'),
    path ('contactus', bv.contactus, name = 'contactus'),
    path ('signup', bv.signup, name = 'signup'),
    path ('index', bv.index, name = 'index'),
    path ('logout', bv.logout, name = 'logout'),
    path ('signin', bv.signin, name = 'signin'),
    path('test', bv.test , name='test'),
    path('result', bv.result, name='result'),
]