from django.shortcuts import render

# Create your views here.
# Create your views here.
def userLogin(request):
    return render(request,"userlogin.html",{"message":"Login Here",})

def userLoginValidate(request):
    if request.session.get("user-login", False):

        args = {
                'message': "You're already Logged in!",
                }
        return render(request, 'user.html', args)

    if request.method == "POST":

        if request.POST["user-id"] == '' or request.POST["user-pass"] == '' or request.POST["user-cell"] == '' or request.POST['user-mail'] == '':
            args = {"message": "Login Credentials can't be left blank!"}
            return render(request, 'userlogin.html', args)

        else:
            if request.POST["user-pass"] == '123456' and request.POST["user-id"] == '987654321000' and request.POST["user-mail"] == 'asdf' and request.POST['user-cell'] == '9876543210':
                request.session["user-login"] = True
                return render(request, 'user.html', {})
            else:
                args = {"message": "Enter valid login credentials"}
                return render(request, 'userlogin.html', args)

    args = {"message": "Enter valid credentials!"}
    return render(request, 'userlogin.html', args)
