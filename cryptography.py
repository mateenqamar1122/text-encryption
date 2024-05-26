def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? (q to quit): ").lower()
        if choice == 'q':
            print("Exiting program.")
            break
        if choice not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter shift value: "))

        if choice == 'e':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        elif choice == 'd':
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
