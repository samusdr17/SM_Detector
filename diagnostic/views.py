from django.shortcuts import render

# Create your views here.


def Diagnostic(request):
    return render(request,"diagnostic/diagnostic.html")