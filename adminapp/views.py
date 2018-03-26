from django.shortcuts import render
from adminapp.models import *

# Create your views here.
def adminLogin(request):
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                }
        return render(request, 'admin.html', args)

    return render(request,"login.html",{"message":"Please, Login In Here",})

def adminLoginValidate(request):
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                }
        return render(request, 'admin.html', args)

    if request.method == "POST":

        if request.POST["admin-id"] == '' or request.POST["password"] == '':
            args = {"message": "ID and Password can not be vaccant"}
            return render(request, 'login.html', args)

        else:

            try:
                admin = Admin.objects.get(adminUid=request.POST["admin-id"])
            except Admin.DoesNotExist:
                args = {"message": "Invalid ID"}
                return render(request, 'login.html', args)

            if request.POST["password"] == admin.adminPass:
                request.session["admin-login"] = True
                return render(request, 'admin.html', {})
            else:
                args = {"message": "Enter the valid ID and Password"}
                return render(request, 'login.html', args)

    args = {"message": "Please, Login Correctly"}
    return render(request, 'login.html', args)
