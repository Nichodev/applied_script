# Lista över användarnamn och deras korrekta lösenord
user_credentials = {
    "user1": "Password123",
    "admin": "Admin@2023",
    "user2": "Welcome123",
    "guest": "Guest1234"
}

# En lista över vanligt använda lösenord
password_list = ["Password123", "123456", "Welcome123", "Guest1234", "password"]




with open('/Users/robertjakobsson/Documents/applied_script/results.txt', 'w') as file:
    for username in user_credentials.keys():
        for password in password_list:
            if password == user_credentials[username]:
                result =   'success'
            else:
                result = 'failed'

            file.write(f'{username}: {password} => {result}\n')
            print(f'{username}: {password} => {result}')