#File: encrypt_decrypt
#Author: ishma-cybsec
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✅ New encryption key generated and saved as secret.key")

def load_key():
    if not os.path.exists("secret.key"):
        print("⚠️ No key found! Generating new key...")
        generate_key()
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

def main():
    key = load_key()
    while True:
        print("\n🔒 ENCRYPT / DECRYPT TOOL 🔓")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            msg = input("Enter the message to encrypt: ")
            encrypted = encrypt_message(msg, key)
            print("\n🔐 Encrypted message:")
            print(encrypted.decode())
        elif choice == "2":
            encrypted_input = input("Enter the encrypted text: ").encode()
            try:
                decrypted = decrypt_message(encrypted_input, key)
                print("\n🔓 Decrypted message:")
                print(decrypted)
            except Exception:
                print("❌ Decryption failed! Invalid key or corrupted text.")
        elif choice == "3":
            print("👋 Exiting... stay secure!")
            break
        else:
            print("⚠️ Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
