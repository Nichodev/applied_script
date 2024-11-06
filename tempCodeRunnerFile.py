valid_options = ["ja", "nej", "kanske"]
user_input = input("Vill du sova? ")

if user_input in valid_options:
    print(f"Du valde {user_input}")
else:
    print("Jag förstår inte")
