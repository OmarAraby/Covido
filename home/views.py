from django.shortcuts import render, redirect
from .models import FAQ , Prevention
from contact.models import ImageSlide
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    images = ImageSlide.objects.all()
    faqs = FAQ.objects.all().order_by('-id')[:5]
    preventions_should_do = Prevention.objects.filter(tag="Things You Should Do")
    preventions_should_not_do = Prevention.objects.filter(tag="Things You Shouldn't Do")
    
    context = {'images':images,'faqs':faqs,'preventions_should_do': preventions_should_do, 'preventions_should_not_do': preventions_should_not_do}


    return render(request,'home.html',context)











def prevention(request):
    preventions_should_do = Prevention.objects.filter(tag="Things You Should Do")
    preventions_should_not_do = Prevention.objects.filter(tag="Things You Shouldn't Do")


    context = {'preventions_should_do': preventions_should_do, 'preventions_should_not_do': preventions_should_not_do}

    return render(request, 'prevention.html', context)









def faqs(request):

    faqs = FAQ.objects.all()
    
    # Determine if the length is even or odd
    is_odd_length = len(faqs) % 2 != 0

    # Calculate the index to split the FAQs into two halves
    split_index = len(faqs) // 2 + (1 if is_odd_length else 0)

    # Slice the FAQs into two halves
    faqs_first_half = faqs[:split_index]
    faqs_second_half = faqs[split_index:]



    ## FAQs Form

    if request.method=='POST':
            
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            


    

            email_subject = 'New Covido Contact Submission Form FAQs '
            message = 'Subject : {}\nEmail :  {}\nPhone_Number : {}\n\nMessage :\n{}'.format(subject, email, phone, message)
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]

            
            
            send_mail(
                subject=email_subject,
                message=message,
                from_email=from_email,
                recipient_list=recipient_list,
                fail_silently=False,
                
            )

            return redirect('home:faqs')





    # Pass the data to the template
    context = {
        'faqs_first_half': faqs_first_half,
        'faqs_second_half': faqs_second_half,
    }


    return render(request,'faqs.html',context)