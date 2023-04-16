from private_firebase import *
import pyrebase
import random
import os

config = {
    "apiKey": apiKey,
    "authDomain": authDomain,
    "projectId": projectId,
    "storageBucket": storageBucket,
    "messagingSenderId": messagingSenderId,
    "appId": appId,
    "measurementId": measurementId,
    "databaseURL": None
}
class Firebase:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)  # connect to firebase
        self.storage = self.firebase.storage()  # configure and connect to the storage

    @staticmethod
    def generate_name(basename: str, base=8):
        # This function will generate name for the file.
        filename = os.path.splitext(basename)   # separate file name with file extension
        return filename[0] + '-' + ''.join([str(random.randint(0, 9)) for _ in range(base)]) + filename[1]

    def upload(self, filename, filepath):
        response = self.storage.child(f'/profile/{self.generate_name(filename)}').put(filepath)
        return response['name'], response['downloadTokens']     # return file name and file token, so we can access it.

    def get_url(self, filename, token):
        url = self.storage.child(filename).get_url(token)
        return url

