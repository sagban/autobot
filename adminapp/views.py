from django.shortcuts import render


# Create your views here.
def adminLogin(request):
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
            if request.POST["password"] == '12345' and request.POST["admin-id"] == 'id':
                request.session["admin-login"] = True
                return render(request, 'admin.html', {})
            else:
                args = {"message": "Enter the valid ID and Password"}
                return render(request, 'login.html', args)

    args = {"message": "Please, Login Correctly"}
    return render(request, 'login.html', args)
