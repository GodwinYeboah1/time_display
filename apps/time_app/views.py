from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
# this is how you rener a page
def index(request):
    context = {
                "time": strftime("%I:%M %p", gmtime()),
                "date": strftime("%b %m, %y", gmtime())
             }   
    return render(request,'time_app/index.html',context)

