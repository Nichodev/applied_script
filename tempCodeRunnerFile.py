p = Path('/Users/robertjakobsson/Documents/applied_script/example_file.txt')

print(p.exists()) ## Se om path finns
print(p)

p = Path.cwd() / 'documents' / 'file.txt'
dest = Path.cwd() / 'backup' / 'file.txt'

print(p)
print(dest)