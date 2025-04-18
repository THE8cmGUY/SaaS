  
  
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit


def home(request):
    return about_page(request)
def about_page(request):
    query_set_all = PageVisit.objects.all()
    queryset_count_path = PageVisit.objects.filter(path = request.path)
    try:
        percent = (queryset_count_path.count()*100)/query_set_all.count()
    except Exception:
        percent = 0
    my_page = {
        "page_title":"This is a resturant website",
        "queryset_count_path":queryset_count_path.count(),
        "query_set_all":query_set_all.count(),
        "percent":percent
        
    }
   
    #print(path)
    # whenever the page is visited a object is created of PageVisit table
    
    PageVisit.objects.create(path = request.path)
    return render(request , "home.html" , my_page)
    