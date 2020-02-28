from django.shortcuts import render, redirect
from .forms import SignUp, SignIn, AdminReg, Edit
from .models import UserDetails, Session
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


def registerView(request):
    html = "Registration Form"
    check = ""
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            name = form.cleaned_data['Aname']
            email = form.cleaned_data['Aemail']
            phone = form.cleaned_data['Aphone']
            user = form.cleaned_data['Auser']
            password = form.cleaned_data['Apass']
            role = "primary"
            status = 1
            perms = 7
            ref = "Master"
            userCheck = UserDetails.objects.filter(adminUser=user).exists()
            emailCheck = UserDetails.objects.filter(adminEmail=email).exists()
            ph = str(phone)
            if userCheck == True:
                check = "The username exists already. Use a different one"
            elif emailCheck == True:
                check = "The phone number is not valid. Enter a 10 digit phone number"
            elif len(ph) != 10:
                check = "The phone number is not valid. Enter a 10 digit phone number"
            else:
                html = "Thank you for registering! You can login now"
                passwordSave = make_password(password)
                check = ""
                userDetails = UserDetails(
                    adminName=name.strip(),
                    adminEmail=email.strip(),
                    adminPhone=ph,
                    adminUser=user.strip(),
                    adminPass=passwordSave.strip(),
                    adminRole=role,
                    adminStatus=status,
                    adminPerms=perms,
                    adminRef=ref)
                userDetails.save()
    else:
        form = SignUp()
    return render(request, 'user/register.html', {'html': html, 'form': form, 'check': check})


def loginView(request):
    sessionCheck = Session.objects.filter(sessionStat=1).exists()
    text = ""
    if sessionCheck == True:
        return HttpResponseRedirect('dashboard/')
    else:
        if request.method == 'POST':
            form = SignIn(request.POST)
            if form.is_valid():
                email = form.cleaned_data['Lemail']
                password = form.cleaned_data['Lpass']

                emailCheck = UserDetails.objects.filter(adminEmail=email).exists()
                if emailCheck != True:
                    text = "The email does not exist in the database"
                else:
                    b = UserDetails.objects.get(adminEmail=email)
                    passCheck = check_password(password, b.adminPass)
                    if passCheck == False:
                        text = "The email and password does not match"
                    else:
                        import datetime
                        b = UserDetails.objects.get(adminEmail=email)
                        now = datetime.datetime.now()
                        ses = Session.objects.create(sessionID=b, sessionStat=1, sessionIn=now)
                        return HttpResponseRedirect('/dashboard/')
        else:
            form = SignIn()
    return render(request, 'user/login.html', {'html': text, 'form': form})


def dashboardView(request):
    sessionCheck = authenticate()
    text = ''
    if sessionCheck == False:
        return HttpResponseRedirect('/error404')
    return render(request, 'user/dashboard.html', {'html': text})


def errorView(request):
    text = "You are not authorized to access this page. Please login."
    return render(request, 'user/404.html', {'html': text})


def logout(request):
    from datetime import datetime
    check = Session.objects.get(sessionStat=1)
    check.sessionStat = 0
    check.sessionOut = datetime.now()
    check.save()
    text = "You have been logged out. Please login again"
    #return redirect('Login')
    return render(request, 'user/logout.html', {'html': text})


def authenticate():
    sessionCheck = Session.objects.filter(sessionStat=1).exists()
    return sessionCheck


def adminRegister(request):
    sessionCheck = authenticate()
    if sessionCheck == False:
        return HttpResponseRedirect('/error404')
    else:
        html = "Make an Admin Account"
        check = ""
        if request.method == 'POST':
            form = AdminReg(request.POST)
            if form.is_valid():
                name = form.cleaned_data['Aname']
                email = form.cleaned_data['Aemail']
                phone = form.cleaned_data['Aphone']
                user = form.cleaned_data['Auser']
                password = form.cleaned_data['Apass']
                choice = form.cleaned_data['Aperms']
                role = form.cleaned_data['Arole']
                status = 1
                perms = 0
                temp = Session.objects.get(sessionStat=1)
                ref = temp.sessionID.adminUser
                userCheck = UserDetails.objects.filter(adminUser=user).exists()
                emailCheck = UserDetails.objects.filter(adminEmail=email).exists()
                for i in choice:
                    perms = perms + int(i)
                ph = str(phone)
                if userCheck == True or emailCheck == True or len(ph) != 10:
                    if userCheck == True:
                        check = "The username exists already. Use a different one"
                    elif emailCheck == True:
                        check = "The email exists already. Use a different one"
                    elif len(ph) != 10:
                        check = "The phone number is not valid. Enter a 10 digit phone number"
                else:
                    html = "Thank you for registering! You can login now"
                    passwordSave = make_password(password)
                    check = ""
                    userDetails = UserDetails(
                        adminName=name.strip(),
                        adminEmail=email.strip(),
                        adminPhone=ph,
                        adminUser=user.strip(),
                        adminPass=passwordSave.strip(),
                        adminRole=role,
                        adminStatus=status,
                        adminPerms=perms,
                        adminRef=ref)
                    userDetails.save()
        else:
            form = AdminReg()
    return render(request, 'user/account.html', {'html': html, 'form': form, 'check': check})


def deleteView(request, id):
    sessionCheck = authenticate()
    check2 = ''
    if sessionCheck == False:
        return HttpResponseRedirect('/error404')
    else:
        if request.method == 'POST':
            edit = Edit(request.POST)
            if edit.is_valid():
                check2 = editForm(edit)
        details = UserDetails.objects.filter()
        check = UserDetails.objects.get(adminID=id)
        auth = Session.objects.get(sessionStat=1)
        if check.adminRole == "secondary" and auth.sessionID.adminPerms > 4:
            check.adminStatus = 0
            check.save()
            value = 1
        else:
            value = 0
    return render(request, 'user/details.html', {'forms': details, 'value': value, 'check': check2})

def editView(request, id):
    details = UserDetails.objects.filter()
    check = UserDetails.objects.get(adminID=id)
    auth = Session.objects.get(sessionStat=1)
    if check.adminRole == "secondary" and auth.sessionID.adminPerms > 4:
        check.delete()
        value = 1
        return redirect ('Details')
    else:
        value = 0
    return render(request, 'user/details.html', {'forms': details, 'value': value})

def editForm(edit):
    id = edit.cleaned_data['Eid']
    name = edit.cleaned_data['Ename']
    email = edit.cleaned_data['Eemail']
    phone = edit.cleaned_data['Ephone']
    user = edit.cleaned_data['Euser']
    password = edit.cleaned_data['Epass']
    choice = edit.cleaned_data['Eperms']
    row = UserDetails.objects.get(adminID=id)
    enPass = make_password(password)
    perms = 0
    for i in choice:
        perms = perms + int(i)
    userCheck = UserDetails.objects.filter(adminUser=user).exists()
    emailCheck = UserDetails.objects.filter(adminEmail=email).exists()
    auth = Session.objects.get(sessionStat=1)
    ph = str(phone)
    if row.adminRole == "secondary" and auth.sessionID.adminPerms > 4:
        check = "You are not authorized to edit this user"
    elif auth.sessionID.adminRole == "secondary":
        check = "You are not allowed to edit as a secondary user"
    elif userCheck == True:
        check = "The username exists already. Use a different one"
    elif emailCheck == True:
        check = "The phone number is not valid. Enter a 10 digit phone number"
    elif len(ph) != 10:
        check = "The phone number is not valid. Enter a 10 digit phone number"
    else:
        row.adminName = name
        row.adminEmail = email
        row.adminPhone = phone
        row.adminUser = user
        row.adminPassword = enPass
        row.adminPerms = perms
        row.save()
        check = "1"
    return check

def adminDetails(request):
    details = UserDetails.objects.filter()
    edit = Edit()
    check = ''
    sessionCheck = authenticate()
    if sessionCheck == False:
        return HttpResponseRedirect('/error404')
    else:
        if request.method == 'POST':
            edit = Edit(request.POST)
            if edit.is_valid():
                check = editForm(edit)
        html = "Changed"
    return render(request, 'user/details.html', {'html': html, 'forms': details, 'editForm': edit, 'check': check})

