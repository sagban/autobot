import sys, os
import csv

''' SETUP DJANGO ENVIRONMENT '''
BASE_DIR = os.path.dirname(
                        os.path.dirname(
                            os.path.abspath(__file__)
                        )
                    )

DJANGO_PROJECT_HOME = os.path.dirname(
                os.path.dirname(
                    BASE_DIR
                )
            )
sys.path.append(DJANGO_PROJECT_HOME)
os.environ['DJANGO_SETTINGS_MODULE'] = 'autobot.settings'
import django
django.setup()

print("Before Importing models")

from adminapp.models import *

print("Importing Done")

''' FILES AND DIRECTORIES '''
DIRECTORY_CSVFILES = "/CSV"
FILE_CSV_ADMIN = BASE_DIR + DIRECTORY_CSVFILES + "/Admin.csv"

def loadAdminData():
    dataReader = csv.reader ( open ( FILE_CSV_ADMIN ) , delimiter=',' , quotechar='"' )

    for row in dataReader:
        if row[0] == 'id':
            print("Ignoring Header\n")
        else:

            admin = Admin()
            admin.adminName = row[1]
            admin.adminUid = row[2]
            admin.adminPass = row[3]
            admin.save()


if __name__== '__main__':
    loadAdminData()