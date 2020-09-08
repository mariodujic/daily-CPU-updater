import json


class SecretUtils:

    @staticmethod
    def get_url(key):
        with open('urls.json') as json_file:
            return json.load(json_file)[key]
