from django.shortcuts import render

# Create your views here.


def home(request):



    return render(request,'home.html')







def detect(request):


    return render(request,'detect.html')







def prevention(request):


    return render(request,'prevention.html')










def faqs(request):


    return render(request,'faqs.html')