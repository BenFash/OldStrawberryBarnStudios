from django.shortcuts import render

# Create your views here.
def AboutUs(request):
    return render(request, 'aboutus/about_us.html')