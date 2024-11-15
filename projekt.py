from cryptography.fernet import Fernet
import argparse
import os

def generate_key(din_key_path):
    key = Fernet.generate_key()
    with open(din_key_path, 'wb') as file:
        file.write(key)
    print(f'Key saved in {din_key_path}')

def load_key(din_key_path):
    with open(din_key_path, 'rb') as file:
        return file.read()

def encrypt_file(input_file, din_key_path):
    key = load_key(din_key_path)
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(input_file, 'wb') as file:
        file.write(encrypted_data)
    print(f'File encrypted and saved to {input_file}')

def decrypt_file(input_file, din_key_path):
    key = load_key(din_key_path)
    fernet_2 = Fernet(key)

    with open(input_file, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet_2.decrypt(encrypted_data)

    with open(input_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    print(f'File decrypted and saved to {input_file}')

def main():
    parser = argparse.ArgumentParser(description='Cryptography tool')
    parser.add_argument('-g', '--generate', action='store_true', help='Generate a key')
    parser.add_argument('-e', '--encrypt', help='Encrypt the input file in place')
    parser.add_argument('-d', '--decrypt', help='Decrypt the input file in place')
    parser.add_argument('-k', '--key', required=True, help='Path to encryption key file')

    args = parser.parse_args()

    din_key_path = os.path.abspath(args.key)

    if args.generate:
        generate_key(din_key_path)
    elif args.encrypt:
        input_file = os.path.abspath(args.encrypt)
        encrypt_file(input_file, din_key_path)
    elif args.decrypt:
        input_file = os.path.abspath(args.decrypt)
        decrypt_file(input_file, din_key_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()