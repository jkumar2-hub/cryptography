# =============================================================================
# PROGRAM 1: Caesar Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   The Caesar Cipher shifts each letter of the plaintext by a fixed number
#   (the key) along the alphabet. Decryption reverses the shift.
#
# Algorithm:
#   Encryption: C = (P + key) mod 26
#   Decryption: P = (C - key + 26) mod 26
# =============================================================================

def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            ciphertext += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += ch
    return ciphertext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():
            plaintext += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
        else:
            plaintext += ch
    return plaintext


def main():
    print("=" * 55)
    print("      CAESAR CIPHER - Encryption & Decryption")
    print("=" * 55)

    message = input("\nEnter the plaintext message : ").strip()
    key     = int(input("Enter the shift key (0-25)  : ").strip()) % 26

    encrypted = caesar_encrypt(message, key)
    decrypted = caesar_decrypt(encrypted, key)

    print("\n" + "-" * 55)
    print(f"  Plaintext  : {message.upper()}")
    print(f"  Key        : {key}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 55)


if __name__ == "__main__":
    main()
