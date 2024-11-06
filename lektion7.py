## Input validering ##

# while True:
#     user_input = input("Ange ett nummer ")
#     if user_input.isdigit():
#         user_number = int(user_input)
#         print(f"Du angav: {user_number}")
#         break
#     else:
#         print("Ogiltig input")


# try:
#     user_input = input("Ange ett nummer: ")
#     user_number =int(user_input)
#     print(f"Du avngav {user_number}")
# except valueError:
#     print("Ogiltig input")


# valid_options = ["ja", "nej", "kanske"]
# user_input = input("Vill du sova? ").lower()

# if user_input in valid_options:
#     print(f"Du valde {user_input}")
# else:
#     print("Jag förstår inte")

## Objektorienterad ##

# class Car:
#     wheels = 4

#     def __init__(self, model, year, make):
#         self.make = make
#         self.model = model
#         self.year = year

#     def description(self):
#         return(f"{self.year}, {self.make}, {self.model}")

# car1 = Car("volvo", "240", 1985)
# car2 = Car("Honda", "Civic", 2017)

# print(car1.description())


                    ## KRYPTERING ##


# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# print(f"Genererad nyckel: {key}")

# with open("secret.key" , "wb") as file:
#     file.write(key)     ## Skapa nyckel



# with open("/Users/robertjakobsson/Documents/example.txt" , "r") as file:
#     key = file.read()

# print(f"Nyckel laddad: {key}")   ## Läsa av nyckel från fil




from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()

cipher_suite = Fernet(key)

message = "här är min text".encode()
cipher_text = cipher_suite.encrypt(message)

print(f"Cipher text {cipher_text}")

with open("encrypted.enc" , "wb") as file:
    file.write(cipher_text)

with open("encrypted.enc" , "rb") as file:
    encrypted_message = file.read()

plain_text = cipher_suite.decrypt(encrypted_message)
print(f"dekrypterad text: {plain_text.decode()}")
        