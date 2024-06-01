from django.shortcuts import render

# Create your views here.
def PrivacyNoticeView(request):
    return render(request, 'privacynotice/privacy.html')