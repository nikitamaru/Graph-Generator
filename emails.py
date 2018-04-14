import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DB_ROOT = os.path.join (APP_ROOT, "files", "emails.txt")

def addMail(email):
    f = open(DB_ROOT, "r+")
    f.write(email)
    f.write("\n")
    f.close()
