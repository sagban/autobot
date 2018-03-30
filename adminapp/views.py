from django.shortcuts import render
from adminapp.models import *
from django.http import HttpResponseRedirect
# Create your views here.

'''Provides the login Page'''
def adminLogin(request):

    '''If already Login'''
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                'admin':request.session['admin']

                }
        return render(request, 'admin.html', args)

    return render(request,"login.html",{"message":"Please, Login In Here",})


'''validate the details filled in admin form'''
def adminLoginValidate(request):
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                "value": True,
                }
        return render(request, 'admin.html', args)

    if request.method == "POST":

        if request.POST["admin-id"] == '' or request.POST["password"] == '':
            args = {"message": "ID and Password can not be vaccant",
                    "value": False,}
            return render(request, 'login.html', args)

        else:

            try:
                admin = Admin.objects.get(adminUid=request.POST["admin-id"])
            except Admin.DoesNotExist:
                args = {"message": "Invalid ID",
                        "value":False,
                }
                return render(request, 'login.html', args)

            '''Checking the correctness of password '''
            if request.POST["password"] == admin.adminPass:
                request.session["admin-login"] = True
                request.session["admin"] = {
                    "adminName" : admin.adminName,
                    "adminUid":admin.adminUid,
                }
                request.session.set_expiry(60000)

                '''Redirecting to /adminIn'''
                return HttpResponseRedirect('/adminIn')
            else:
                args = {"message": "Enter the valid ID and Password",
                        "value": False,}
                return render(request, 'login.html', args)

    args = {"message": "Please, Login Correctly"}
    return render(request, 'login.html', args)

'''Loads the admin page or dashboard after the validation'''
def adminIn(request):
    if request.session.get("admin-login",False):
        if request.session.get("admin",False):
            args={
                "admin":request.session['admin'],
            }
            return render(request, 'admin.html', args)
        return HttpResponseRedirect('/admin-validate')
    args = {
        'message': "Please Login Here!",
        "value": False,
    }
    return render(request, 'login.html', args)

'''Yet to complete, Most probably this function will call after the image processing or vehical number validation for the criminal search.'''
def addCrime(request):
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                }
        return render(request, 'addcrime.html', args)
    args = {
        'message': "Please, Login In Here",
    }
    return render(request, "login.html",args)