from django.shortcuts import render,redirect, get_object_or_404
from django.http import request, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import models
from . import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.db.models import F
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def homePage(request):
    return render(request,'homePage.html')

def signupPage(request):
    if request.method == 'POST':
        form = forms.Signupform(request.POST)
        if form.is_valid():
           # form.save()
            user = form.save(commit=False)
            category = request.POST.get('category')
            if category == 'teacher':
                group = Group.objects.get(name='Teachers')
            elif category == 'student':
                group = Group.objects.get(name='Students')
            user.save()
            user.groups.add(group)
            return render(request,'homePage.html')
        else:
            return HttpResponse('Please enter proper values.')
    else:
        form = forms.Signupform()
    return render(request,'signupPage.html',{'form':form})

def loginPage(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=email, password=password)
            if user:
                login(request,user)
                
                if user.groups.filter(name='Teachers').exists():
                    return redirect('teacherPage')
                elif user.groups.filter(name='Students').exists():
                    return redirect('studentPage')
                else:
                    return render(request,'homePage.html')

        else:
            return HttpResponse('Please enter proper values.')
    else:
        form = forms.LoginForm()
    return render(request,'loginPage.html',{'form':form})
        
def viewdata(request):
    if request.method == 'POST':
        #print(request.POST)
        email = request.POST.get('Email')
        english = request.POST.get('English')
        benagli = request.POST.get('Bengali')
        mathematics = request.POST.get('Mathematics')
        science = request.POST.get('Science')
        programming = request.POST.get('Programming')
        environment = request.POST.get('Environment')
        student = models.Account.objects.filter(email=email).first()
        if student:
            if models.ResultDb.objects.filter(email=student).first():
                return HttpResponse("This email is already exist with scores!")
            else:
                models.ResultDb.objects.create(email=student,english=english,bengali=benagli,mathematics=mathematics,science=science,programming=programming,environment=environment)
                #return HttpResponseRedirect(reverse('viewdata'))
                return redirect('viewdata')
        else:
            return HttpResponse("This email does not exist")
    
    # Display data in decreasing order.
    display_data = models.ResultDb.objects.annotate(
        total=F('english') + F('bengali') + F('mathematics') + F('science') + F('programming') + F('environment')
    ).order_by('-total')

    #Display the Rank
    rank = 1
    for data in display_data:
        data.rank = rank
        rank += 1

    #Add Page number
    paginator = Paginator(display_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)    
    return render(request,'viewResult.html',{'display_data':display_data,'page_obj': page_obj})

def get_result_for_student(request):
    student_email = models.Account.objects.get(email=request.user.email)
    result = models.ResultDb.objects.filter(email=student_email)
    return render(request,'resultPage.html',{'result':result})

def studentPage(request):
    student_name = request.user.username
    return render(request,'studentPage.html',{'student_name':student_name})

def teacherPage(request):
    teacher_name = request.user.username
    return render(request,'teacherPage.html',{'teacher_name':teacher_name})

def addResultPage(request):
    return render(request,'addResultPage.html')

def logoutPage(request):
    logout(request)
    return redirect('homePage')

def contactusPage(request):
    return render(request,'contactus.html')

def deletepage(request,id):
    models.ResultDb.objects.filter(id=id).delete()
    return redirect('viewdata')

def updatepage(request,id):
    edit_data = get_object_or_404(models.ResultDb,pk=id)
    if request.method == 'POST':
        form = forms.UpdateResultForm(request.POST, instance=edit_data)
        if form.is_valid():
            form.save()
            return redirect('viewdata')
    else:
        form = forms.UpdateResultForm(instance=edit_data)
        email = edit_data.email
    return render(request,'updatepage.html',{'form':form, 'email':email})
 

def resetPage(request):
    if request.method == 'POST':
        # Get the email from the form
        email = request.POST.get('Email')

        # Get the user based on the email
        user = models.Account.objects.filter(email=email).first()

        if user:
            # Update the specific fields for the user
            models.ResultDb.objects.filter(email=user).update(
                english=0,
                bengali=0,
                mathematics=0,
                science=0,
                programming=0,
                environment=0
            )

            return HttpResponse('Data reset successfully.')
        else:
            return HttpResponse('User with this email does not exist.')
    else:
        return HttpResponse('Invalid request method. Use POST to reset data.')
    

def sendmail(request):
    student_email = models.Account.objects.get(email=request.user.email)
    print(student_email)
    result = models.ResultDb.objects.filter(email=student_email).first()
    mail_body = f"""Dear {student_email},

            Please find your marks:

            English: {result.english},
            Bengali: {result.bengali},
            Mathematics: {result.mathematics},
            Science: {result.science},
            Programming: {result.programming},
            Environment: {result.environment}
            
            Regards,
            S.O School Management."""
    print(mail_body)
    send_mail(
        "Result 2024", #title
        mail_body, #body
        'settings.EMAIL_HOST_USER',  #form mail
        [student_email],  # to-mail
        fail_silently=False,
    )
    return render(request,'studentPAge.html')