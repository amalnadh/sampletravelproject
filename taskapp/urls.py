


from django.urls import path

from  . import views

urlpatterns = [

    path('',views.fun,name='fun'),
    #path('home/',views.home,name='home'),
    #path('about/',views.about,name='about'),
    #path('contact/',views.contact,name='contact'),
   # path('details/',views.details,name='det')

]
