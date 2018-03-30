from django.shortcuts import render
from userapp.models import *
from django.http import HttpResponseRedirect

# Create your views here.
# Create your views here.
def userLogin(request):
    return render(request,"userlogin.html",{"message":"Login Here",})

def userLoginValidate(request):
    if request.session.get("user-login", False):

        args = {
            'message': "You're already Logged in!",
            "value": True,
        }
        return render(request, 'user.html', args)

    if request.method == "POST":

        if request.POST["license"] == '' or request.POST["user-pass"] == '' or request.POST["user-cell"] == '':
            args = {"message": "Login Credentials can't be left blank!", "value": False}
            return render(request, 'userlogin.html', args)

        else:
            try:
                user = user.objects.get(userUid=request.POST["license"])
            except user.DoesNotExist:
                args = {"message": "Invalid ID","value": False,}
                return render(request, 'user-login.html', args)

            '''Checking the correctness of password '''
            if request.POST["user-pass"] == user.userPass:
                request.session["user-login"] = True
                request.session["user"] = {
                    "userName": user.userName,
                    "userUid": user.userUid,
                }

                request.session.set_expiry(60000)

                '''Redirecting to /user'''

                return HttpResponseRedirect('/userIn')

            else:

                args = {"message": "Enter the valid ID and Password",

                        "value": False, }

                return render(request, 'userlogin.html', args)

    args = {"message": "Please, Login Correctly"}

    return render(request, 'userlogin.html', args)

'''Loads the admin page or dashboard after the validation'''
def userIn(request):
    if request.session.get("user-login",False):
        if request.session.get("user",False):
            args={
                "user":request.session['user'],
            }
            return render(request, 'user.html', args)
        return HttpResponseRedirect('/user-validate')
    args = {
        'message': "Please Login Here!",
        "value": False,
    }
    return render(request, 'userlogin.html', args)




def adminOut(request):
    if request.session.get("user-login", False):
        request.session.pop("user-login")
        return render(request, "user-login.html", {"message": "You're sucessfully log out"})
    return render(request, "user-login.html", {"message": "You're Already log out"})
