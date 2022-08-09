from cryptography.fernet import Fernet

def decrypt(token):
    key = b'BR5qw3w4L9C64ayfXuwxT1GQyzf3AGq6atSmyTGFYRg='
    f = Fernet(key)
    return f.decrypt(token)