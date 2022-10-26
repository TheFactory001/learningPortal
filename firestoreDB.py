from heapq import merge
import firebase_admin
from firebase_admin import credentials, firestore 

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
        doc_ref = db.collection(u'userData').document(u'{}'.format(obfusMail(email)))
        data = doc_ref.get().to_dict()
        if data['password'] == password:
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
        print(doc_ref)
        data = doc_ref.get().to_dict()
        print(data)
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
    print(data)
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
