from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()

def hashid(id):
    cipher = Fernet(os.get_env('fernet_key').encode())
    return cipher.encrypt(id.encode()).decode()

def check_hashid(id):
    cipher = Fernet(os.get_env('fernet_key').encode())
    return cipher.decrypt(id.encode()).decode()