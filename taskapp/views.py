from django.shortcuts import render
from .models import place
from .models import people

# Create your views here.
from django.http import HttpResponse
def fun(request):
   obj=place.objects.all()
   obj1=people.objects.all()
   return render(request,'index.html',{'result':obj,'result1':obj1})


#def home(request):
   #return render(request,'home.html')
#def about(request):
   ##def contact(request):
  # return render(request,'contact.html')
#def details(request):
  # return render(request,'details.html')
