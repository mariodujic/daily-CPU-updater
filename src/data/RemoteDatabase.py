import json

import firebase_admin
from firebase_admin import credentials, firestore, db


class RemoteDatabase:

    def __init__(self):
        cred = credentials.Certificate("google-service.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL': self.__get_firebase_url()
        })

    def get_firestore_client(self):
        return firestore.client()

    def get_database_client(self):
        return db

    def __get_firebase_url(self):
        with open('urls.json') as json_file:
            return json.load(json_file)["firebase_database_url"]
