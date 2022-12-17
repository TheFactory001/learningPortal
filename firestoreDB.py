from heapq import merge
import random, string
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate("./thefactory-firebase-adminsdk-xxfjn-4f1eb8f607.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

def getAllData():
    try :
        doc_ref = db.collection(u'userAuth')
        for el in doc_ref.get():
            print(el.to_dict())
    except Exception as e :
        print("Error getting info", e)

def authenticateLogin(email, password):
    try :
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        current_dateTime = datetime.now()
        timeStamp = current_dateTime.timestamp()
        doc_ref = db.collection(u'userData').document(u'{}'.format(obfusMail(email)))
        data = doc_ref.get().to_dict()
        if data['password'] == password:
            db.collection(u'userData').document(u'{}'.format(obfusMail(email))).set({"sessionToken": token.lower(), "timeStamp" : timeStamp}, merge=True)
            data = doc_ref.get().to_dict()
            return data
        else :
            return "Incorrect password"
    except Exception as e :
        print("Error getting info", e)
        return "Error getting info, enter valid email"


def getUserData(email):
    try :
        print(email)
        doc_ref = db.collection(u'userData').document(email)
        data = doc_ref.get().to_dict()
        return data
    except Exception as e :
        print("Error getting info", e)
        return "Error getting info, enter valid email"


def signUpUser(data):
    print(data)
    try :
        docId = obfusMail(data['email'])
        db.collection(u'userData').document(docId).set(data)
    except Exception as e :
        print("Error getting info", e)

def userProfileData(data):
    try :
        docId = data['email']
        data.pop("email")
        db.collection(u'userData').document(docId).set(data, merge=True)
    except Exception as e :
        print("Error getting info", e)


def checkEmail(mail):
    try :
        doc_ref = db.collection(u'userData').document(mail)
        print(mail)
        doc = doc_ref.get()
        if doc.exists:
            return True
        else:
            return False
    except Exception as e :
        print("Error getting info", e)
        return "Error getting info, enter valid email"


def obfusMail(email): 
    obfus = ""
    for letter in email:
        obfus += str(ord(letter) - 96)
    return obfus

def uploadPhoto(filename, key, id):
    bucket = storage.bucket("thefactory.appspot.com")
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

    # Opt : if you want to make public access from the URL
    blob.make_public()
    try :
        db.collection(u'userData').document(id).set({key: blob.public_url}, merge=True)
    except Exception as e :
        print("Error getting info", e)

    # print("your file url", blob.public_url)
