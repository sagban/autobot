from django.shortcuts import render
from django_otp.oath import TOTP
from django_otp.util import random_hex
from unittest import mock
import time

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

'''OTP Verification'''
class TOTPVerification:

    def __init__(self):
        # secret key that will be used to generate a token,
        # User can provide a custom value to the key.
        self.key = random_hex(20)
        # counter with which last token was verified.
        # Next token must be generated at a higher counter value.
        self.last_verified_counter = -1
        # this value will return True, if a token has been successfully
        # verified.
        self.verified = False
        # number of digits in a token. Default is 6
        self.number_of_digits = 6
        # validity period of a token. Default is 30 second.
        self.token_validity_period = 35
