# x = 0 
# while x < 10:
#         print(x)
#         if x == 5:
#                 break
#         x += 1

# user_input = input("Ange kommando: ")
# print(user_input)


# while True:
#     user_input = input("Ange kommando: ")
#     if user_input == "exit":
#         break
#     elif user_input == "5":
#         print("Du skrev 5")
#         break
#     else:
#         print("Fel input, skriv igen")


# age = int(input("Ange din ålder: "))
# if 18 <= age <= 65:
#     print("Du kan jobba")
# else:
#     print("Du kan inte jobba")


# x = 5
# print(1 < x < 10)
# print(1 < x and x < 10)

# # FILES ##

# file = open('/Users/robertjakobsson/Documents/testfile.txt' , 'r')
# content = file.read()
# print(content)

# file.close()


# file = open('/Users/robertjakobsson/Documents/example.txt' , 'r')
# line = file.readline()
# while line:
#     print(line , end='')
#     line = file.readline()
# file.close()


# file = open('/Users/robertjakobsson/Documents/example.txt' , 'r')
# lines = file.readlines()
# for line in lines:
#     print(line, end= '')
#     file.close()


# file = open('/Users/robertjakobsson/Documents/example.txt' , 'r')
# lines = file.read().splitlines()
# print(lines)
# file.close()


# file = open('/Users/robertjakobsson/Documents/example.txt' , 'w')
# file.write("Nu har jag ändrat \n")
# file.write("En till rad")
# file.close()

with open('/Users/robertjakobsson/Documents/example.txt' , 'r') as file:
    content = file.read()
    print(content)



