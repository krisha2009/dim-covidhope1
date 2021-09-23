from django.urls import path
from .import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('info/',views.info,name='info'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup')
    

    

]