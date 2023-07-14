import bcrypt
def changepasshash(passwordin):
    password=passwordin.encode('ASCII')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed