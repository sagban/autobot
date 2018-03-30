from django.shortcuts import render
from superadmin.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.

'''Provides the login Page'''
def sadminLogin(request):

    '''If already Login'''
    if request.session.get("sadmin-login", False):

        args = {
                'message': "You're already Logged in!",
                'sadmin':request.session['sadmin'],


                }
        return render(request, 'sadmin.html', args)

    return render(request,"slogin.html",{"message":"Please, Login In Here",'type' : "superadmin",})


'''validate the details filled in admin form'''
def sadminLoginValidate(request):
    if request.session.get("sadmin-login", False):

        args = {
                'message': "You're already Logged in!",
                "value": True,
                }
        return render(request, 'sadmin.html', args)

    if request.method == "POST":

        if request.POST["sadmin-id"] == '' or request.POST["password"] == '':
            args = {"message": "ID and Password can not be vaccant",
                    "value": False,}
            return render(request, 'slogin.html', args)

        else:

            try:
                sadmin = SuperAdmin.objects.get(SadminUid=request.POST["sadmin-id"])
            except SuperAdmin.DoesNotExist:
                args = {"message": "Invalid ID",
                        "value":False,
                }
                return render(request, 'slogin.html', args)

            '''Checking the correctness of password '''
            if request.POST["password"] == SuperAdmin.SadminPass:
                request.session["sadmin-login"] = True
                request.session["sadmin"] = {
                    "SadminName" : sadmin.SadminName,
                    "SadminUid": sadmin.SadminUid,
                }
                request.session.set_expiry(60000)

                '''Redirecting to /sadminIn'''
                return HttpResponseRedirect('/sadminIn')
            else:
                args = {"message": "Enter the valid ID and Password",
                        "value": False,}
                return render(request, 'slogin.html', args)

    args = {"message": "Please, Login Correctly"}
    return render(request, 'slogin.html', args)

'''Loads the admin page or dashboard after the validation'''
def sadminIn(request):
    if request.session.get("sadmin-login",False):
        if request.session.get("sadmin",False):
            args={
                "sadmin":request.session['sadmin'],
            }
            return render(request, 'sadmin.html', args)
        return HttpResponseRedirect('/sadmin-validate')
    args = {
        'message': "Please Login Here!",
        "value": False,
    }
    return render(request, 'slogin.html', args)


def sadminOut(request):

    if request.session.get("sadmin-login",False):
        request.session.pop("sadmin-login")
        return render(request,"slogin.html",{"message":"You're sucessfully log out"})

    return render(request, "slogin.html", {"message": "You're Already log out"})
