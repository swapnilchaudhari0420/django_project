from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
#from django.contrib.auth.models import User
#from django.core.mail import send_mail
from django.contrib.auth import  logout
#from .models import register_table, appointment_table
from .models import register_table, appointment_table
from   django.conf  import settings


def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request,'register.html')

def registerhandle(request):
    if request.method == 'POST':
        try:

            # get the post parameters
            username = request.POST['username']
            age = request.POST['age']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            password = request.POST['password']
            confirm_password = request.POST['confirm_password']

            # check of input errors
            if password == confirm_password:
                if register_table.objects.filter(username=username).exists():
                    messages.error(request, "Username is already taken")
                    return redirect('register')

                elif register_table.objects.filter(email=email).exists():
                    messages.error(request, "email is already taken")
                    return redirect('register')

                else:
                    myuser = register_table(username=username, age=age, email=email, phone_number=phone_number,password=password,confirm_password=confirm_password)
                    myuser.save()

                    messages.success(request, " Your account has been successfully created")
                    # Welcome Email
                    subject = "Welcome to stylo !!"
                    message = f"Welcome  {username}!! \nRegistration Successfull! "
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [email]
                    send_mail(subject, message, from_email, to_list, fail_silently=True)
                    return redirect('home')
            else:
                messages.error(request, "Password is Mismatched")
                return redirect('register')

        except Exception as e:
            print(e)
            return redirect('register')


def userpage(request):
    return render(request,'UserPage.html')

def handleLogin(request):
    if request.method == "POST":
        try:
            login_username = request.POST['login_username']
            login_password = request.POST['login_password']

            us = register_table.objects.get(username=login_username, password=login_password)
            if us:
                messages.success(request,"Login Successfully")
                return redirect('userpage')
            else:
                messages.error(request, "Invalid credentials! Please try again")
                return redirect("home")
        except Exception as e:
            print(e)
            return redirect("home")

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def hairstyle(request):
    return render(request, 'hairstyle.html', )


def haircut(request):
    return render(request, 'haircut.html')


def beard(request):
    return render(request, 'beard.html')

def appointment(request):
    return render(request,'appointment.html')



def appointmenthandle(request):
    if request.method == 'POST':
        try:
            # get the post parameters
            destination = request.POST['destination']
            date = request.POST['date']
            time = request.POST['time']
            beard = request.POST['beard']
            hairstyle = request.POST['hairstyle']
            haircut = request.POST['haircut']
            email = request.POST['email']
            phone = request.POST['phone']

            if appointment_table.objects.filter(date=date).exists()  and appointment_table.objects.filter(time=time).exists():
                messages.error(request," this appointment was booked by another client, please try another Date or Time !")
                return redirect('appointmenthandle')

            # create user
            user_appo = appointment_table(destination=destination, date=date, time=time, beard=beard,hairstyle=hairstyle, haircut=haircut,email=email, phone=phone)

            user_appo.save()
            messages.success(request, " Your appointment has been Booked")
            # Welcome Email
            subject = "Welcome to stylo !!"
            message = f"Welcome to stylo!! \nThank you for visiting our website. \n Your appointment was booked ! \n\n Your Appointment DATE = {date} \n TIME = {time}  \n\nThanking You\n -Stylo"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return redirect('userpage')


        except Exception as e:
            print(e)
            return redirect('appointmenthandle')


    return render(request, 'appointment.html')



