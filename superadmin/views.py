from django.shortcuts import render
from superadmin.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.

'''Provides the login Page'''
def adminLogin(request):

    '''If already Login'''
    if request.session.get("sadmin-login", False):

        args = {
                'message': "You're already Logged in!",
                'sadmin':request.session['sadmin']

                }
        return render(request, 'admin.html', args)

    return render(request,"login.html",{"message":"Please, Login In Here",})


'''validate the details filled in admin form'''
def adminLoginValidate(request):
    if request.session.get("sadmin-login", False):

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
                admin = SuperAdmin.objects.get(SadminUid=request.POST["admin-id"])
            except SuperAdmin.DoesNotExist:
                args = {"message": "Invalid ID",
                        "value":False,
                }
                return render(request, 'login.html', args)

            '''Checking the correctness of password '''
            if request.POST["password"] == SuperAdmin.SadminPass:
                request.session["sadmin-login"] = True
                request.session["sadmin"] = {
                    "SadminName" : SuperAdmin.SadminName,
                    "SadminUid":SuperAdmin.SadminUid,
                }
                request.session.set_expiry(60000)

                '''Redirecting to /adminIn'''
                return HttpResponseRedirect('/sadminIn')
            else:
                args = {"message": "Enter the valid ID and Password",
                        "value": False,}
                return render(request, 'login.html', args)

    args = {"message": "Please, Login Correctly"}
    return render(request, 'login.html', args)

'''Loads the admin page or dashboard after the validation'''
def adminIn(request):
    if request.session.get("sadmin-login",False):
        if request.session.get("sadmin",False):
            args={
                "sadmin":request.session['sadmin'],
            }
            return render(request, 'admin.html', args)
        return HttpResponseRedirect('/sadmin-validate')
    args = {
        'message': "Please Login Here!",
        "value": False,
    }
    return render(request, 'login.html', args)


def adminOut(request):

    if request.session.get("sadmin-login",False):
        request.session.pop("sadmin-login")
        return render(request,"login.html",{"message":"You're sucessfully log out"})

    return render(request, "login.html", {"message": "You're Already log out"})
