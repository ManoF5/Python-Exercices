from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.key','rb')
key = file.read() # The key wil be type bytes
file.close()

# Encode the menssage
message = "my deep dark secret"
encoded = message.encode()

# Encrypt the menssage
f = Fernet(key)
encrypted = f.encrypt(encoded)  # Encrypt the bytes. The returning object is of type bytes

print(encrypted) 
# ==========================================================================  

# Get the key again (for the demonstration)
file = open('key.key','rb')
key = file.read() # The key wil be type bytes
file.close()

# Decrypt the encrypt message 
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)

# Decode the message
original_message = decrypted.decode()
print(original_message)