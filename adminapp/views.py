import pytesseract
# import cv2
from PIL import Image, ImageFilter
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from adminapp.models import *
from django.http import HttpResponseRedirect
from adminapp.fusioncharts import *
from django.http import HttpResponseRedirect, JsonResponse

#importing user models here
from userapp.models import *
import re

# Create your views here.
'''The image processing function. Extract number plate in text from image'''


@csrf_exempt
def index(request):
    if request.method == 'POST':
        with Image.open(request.FILES['image']).convert("RGB") as image:
            new_size = tuple(2 * x for x in image.size)
            image.compression_quality = 99
            image = image.resize(new_size, Image.ANTIALIAS)
            sharpened_image = image.filter(ImageFilter.SHARPEN)
            utf8_text = pytesseract.image_to_string(sharpened_image)
        regex_strings = re.search("^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$",utf8_text)
        regex_string = regex_strings[0]
        #if regex_string is not Null:
        request.session['utf-image'] = regex_string
        return JsonResponse({'utf8_text': regex_string})
        #return JsonResponse({'utf8_text': 'sagar'})
    return render(request, 'admin.html')

'''Provides the login Page'''
def adminLogin(request):

    '''If already Login'''
    if request.session.get("admin-login", False):

        args = {
                'message': "You're already Logged in!",
                'admin':request.session['admin'],

                }
        return render(request, 'admin.html', args)

    return render(request,"login.html",{"message":"Please, Login In Here",'type': 'policeadmin',})


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


def numberValidate(request):
    # if request.session.get("admin-login",False):


        # if request.POST["image-input"] != '':
        #     if request.session.get("utf-image",False):
        #         request.session["utf-text"] = request.POST["text-input"]
        #         if request.session["utf-text"] == '':
        #             regNumber = request.session["utf-image"];
        #         regNumber= request.session["utf-text"]
        #         return HttpResponseRedirect("/addcrime")
        #     return HttpResponseRedirect("/adminIn")
        if request.POST["image-input"] != None and request.POST["text-input"] != None :
            return HttpResponseRedirect("/addcrime")
        else:
            return HttpResponseRedirect("/adminIn")


    # return HttpResponseRedirect("/admin-login")

'''Yet to complete, Most probably this function will call after the image processing or vehical number validation for the criminal search.'''
def addCrime(request):
    if request.session.get("admin-login", False):

        offences = Crime.objects.all()
        args = {
                'message': "Make the charge sheet here",
                "offences" : offences,
                "admin": request.session['admin'],
                }
        return render(request, 'addcrime.html', args)
    args = {
        'message': "Please, Login In Here",
    }
    return render(request, "login.html",args)





def adminOut(request):

    if request.session.get("admin-login",False):
        request.session.pop("admin-login")
        return render(request,"login.html",{"message":"You're sucessfully log out"})

    return render(request, "login.html", {"message": "You're Already log out"})
