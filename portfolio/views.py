
from django.shortcuts import render

def home_page_view(request):
    context = {}
    print("This works!")
    return render(request, "home.html", context)