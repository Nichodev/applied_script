# import argparse
#     #Skapa parser
# parser = argparse.ArgumentParser(description= 'Krypterings verktyg')
#     #Lägg till argument
# parser.add_argument('name', help='Här anger du ditt namn')
# parser.add_argument('age' , type=int, help='Angge din ålder')
#     #Frivillig
# parser.add_argument('-c', '--city', help="Ange din stad", default='Okänd stad')
#     #Frivilligt argument (flaggad)
# # parser.add_argument('-v', '--verbose', action='store_true' , help='Visa detaljerad information')

# parser.add_argument('-m', '--mode', choices=['enkel', 'detaljerad'], help='Välj läge')
#     #Anropa parse
# args = parser.parse_args()

# if args.mode == 'detaljerad':
#     print(f"Hej {args.name}. Du är {args.age}. Du bor i {args.city}")

# print(f'Hej {args.name}')


                    ## KAP 7 ##

                    ## Undantagshantering ##

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Fel : Division med 0 är inte tillåtet")
# else:
#     print(f"Resultat: {result}")
# finally:
#     print("Slut på try except")

# try: 
#     with open('exempel.txt', 'r') as file:
#         content = file.read()
# except FileNotFoundError:
#     print('Fel: Filen hittades inte')
# else:
#     print(content)

                ## Os-modulen ##

import os

# os.chdir('exempel.txt')

# cwd = os.getcwd()
# print(cwd)

# if os.path.exists('exempel.txt'):
#     print('Filen existerar')
#     os.remove('exempel.txt')

# else:
#     print('Filen existerar ej')

# file_info = os.stat("bild.png")
# print(f"Filstorlek : {file_info.st_size}")

#os.system('dir') #Windows

filepath = os.path.join('lektion1.py' , 'lektion2.py')
print(filepath)




