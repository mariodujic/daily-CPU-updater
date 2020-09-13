import firebase_admin
import requests
from firebase_admin import credentials, firestore, db, messaging

from src.environment.Environment import Environment
from src.utils.SecretUtils import SecretUtils


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

    def get_firebase_messaging(self):
        return messaging

    def __get_firebase_url(self):
        return SecretUtils.get_url("firebase_database_url")

    def get_middleware_post_request(self, data, api):
        return requests.post(
            url=Environment.get().MIDDLEWARE_URL + self.__middleware_thought_route() + api,
            data=data,
            headers=self.__middleware_headers()
        )

    def __middleware_headers(self):
        return {SecretUtils.get_url("middleware_header_auth_key"): SecretUtils.get_url("middleware_header_auth_secret")}

    def __middleware_thought_route(self):
        return "/thoughts/"
