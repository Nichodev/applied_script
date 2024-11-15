## kryptering ##

from cryptography.fernet import Fernet

key = Fernet.generate_key()

print(f"Generate key: {key.decode()}")

with open("/Users/robertjakobsson/Documents/applied_script/secret.key" , "wb") as key_file:
    key_file.write(key)

print(f"key is saved to file 'Secret.key'")

with open("/Users/robertjakobsson/Documents/applied_script/secret.key", "rb") as key_file:
    key = key_file.read()
print(f"Key is loaded: {key.decode()}")

cipher_suite = Fernet(key)
print("Fernet object is created and ready for decryption")

message = "This is a string with a secret message".encode()

cipher_text = cipher_suite.encrypt(message)
print(f"Encrypted message: {cipher_text}")

## Steg 5: Läs in det krypterade meddelandet och dekryptera
with open ("/Users/robertjakobsson/Documents/applied_script/encrypted_message.enc", "wb") as enc_file:
    enc_file.write(cipher_text)

print("Encrypted message is saved to file 'encrypted_message.enc'")

with open ("/Users/robertjakobsson/Documents/applied_script/encrypted_message.enc" , "rb") as enc_file:
  encrypted_message = enc_file.read()
print(f"Encrypted message is loaded: {encrypted_message}")

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"Decrypted message: {plain_text.decode()}")
    