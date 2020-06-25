import firebase_admin
from firebase_admin import credentials, firestore, db


class RemoteDatabase:

    def __init__(self):
        cred = credentials.Certificate("google-service.json")
        firebase_admin.initialize_app(cred)

    def get_firestore_client(self):
        return firestore.client()

    def get_database_client(self):
        return db
