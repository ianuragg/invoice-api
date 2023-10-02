from django.shortcuts import render

def endpoints(request):
    context={}
    return render(request, "api/home.html", context=context)
