from django.shortcuts import render

# Create your views here.
# Create your views here.
def userLogin(request):
    return render(request,"userlogin.html",{"message":"Login Here",})

def userForgotPass (request):
    return render (request, "fgtpswd.html")

def userLoginValidate(request):
    if request.session.get("user-login", False):

        args = {
                'message': "You're already Logged in!",
                }
        return render(request, 'user.html', args)

    if request.method == "POST":

        if request.POST["user-id"] == '' or request.POST["password"] == '':
            args = {"message": "Login Credentials can't be left blank!"}
            return render(request, 'userlogin.html', args)

        else:
            if request.POST["password"] == '12345' and request.POST["admin-id"] == 'id':
                request.session["user-login"] = True
                return render(request, 'userlogin.html', {})
            else:
                args = {"message": "Enter the valid ID and Password"}
                return render(request, 'userlogin.html', args)

    args = {"message": "Enter valid credentials!"}
    return render(request, 'userlogin.html', args)

def userNewRegister (request):
    return render(request, "newuserreg.html")