from django.shortcuts import render
from .models import Info ,Feedback,ImageSlide
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contact(request):
    myinfo = Info.objects.last()


    if request.method=='POST':
            
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']
            


    

            email_subject = 'New Covido Contact Submission '
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


    context = {'myinfo':myinfo}


    return render(request,'contact.html',context)







def about(request):
    feedbacks = Feedback.objects.all()
    images = ImageSlide.objects.all()
    
    context = {'feedbacks':feedbacks,'images':images}

    return render(request,'about.html',context)

