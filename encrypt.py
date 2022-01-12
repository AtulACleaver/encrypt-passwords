from cryptography.fernet import Fernet

# Generating a key
key = Fernet.generate_key()
# Saving a key to variable
crypt = Fernet(key)

# Encrypt your String
pw = crypt.encrypt(b'this is not my password or maybe it is')

# Decrypt your String
decryptString = crypt.decrypt(pw)

# Just a simple print statement
print(f"My encrypted password is {str(pw, 'utf8')} and, \nhere's my real = {str(decryptString, 'utf8')}")
