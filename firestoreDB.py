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
        doc_ref = db.collection(u'userAuth').document(u'{}'.format(email))
        data = doc_ref.get().to_dict()
        if data['password'] == password:
            return data
        else :
            return "Incorrect password"
    except Exception as e :
        print("Error getting info", e)
        return "Error getting info, enter valid email"
