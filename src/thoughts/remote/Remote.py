import firebase_admin
from firebase_admin import credentials, firestore


class Remote:

    def __init__(self):
        cred = credentials.Certificate("../google-service.json")
        firebase_admin.initialize_app(cred)

    def get_client(self):
        return firestore.client()
