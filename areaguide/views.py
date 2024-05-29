from django.shortcuts import render

# Create your views here.
def AreaGuide(request):
    """A view that displays the Area Guide page"""
    return render(request, 'areaguide/areaguide.html')