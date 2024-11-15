##  Pathlibs ##


import shutil


## Kopiera fil

# shutil.copy('/Users/robertjakobsson/Documents/applied_script/secret.key', 'secret.key.bak')
# print('File has been copied')

## Radera fil/folder

# shutil.rmtree('/Users/robertjakobsson/Documents/applied_script/test_folder')
# print("'Folder deleted")

## Kopiera katalog

# shutil.copytree('filnamn' , 'pathnamn')
# print('Catalog copied')

## Flytta fil / catalog

#shutil.move('/Users/robertjakobsson/Documents/applied_script/test_folder', 'testfolder2')

## Backup zip

# shutil.make_archive('backup', 'zip','pathname' )


## Hämta path

from pathlib import Path

# p = Path('/Users/robertjakobsson/Documents/applied_script/example_file.txt')

# print(p.exists()) ## Se om path finns
# print(p)

# p = Path.cwd() / 'documents' / 'file.txt'
# dest = Path.cwd() / 'backup' / 'file.txt'

# print(p)
# print(dest)


# ## Kontrollera om viss fil har en viss filhändelse
# file_path = p / 'example_file.txt'
# if file_path.suffix == '.txt':
#     print("Detta är en textfil")


## Loopa igenom filer, backupa vissa .filtyper

# p = Path.cwd()

# for file in p.glob('*'):
#     if file.suffix in ['.csv', '.json']:
#         print(f'Hittade fil: {file=}')
#         shutil.copy(file, 'backup')


                ## REGEX ##



