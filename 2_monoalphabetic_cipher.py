# =============================================================================
# PROGRAM 2: Monoalphabetic Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   Each plaintext letter is mapped to a unique ciphertext letter using a
#   fixed scrambled alphabet as the key. Decryption uses the inverse map.
#
# Algorithm:
#   Encrypt map : plain[i]  -> cipher[i]
#   Decrypt map : cipher[i] -> plain[i]
# =============================================================================

PLAIN_ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER_ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM"


def build_cipher_key(cipher_alphabet):
    ca          = cipher_alphabet.upper()
    encrypt_map = {PLAIN_ALPHABET[i]: ca[i] for i in range(26)}
    decrypt_map = {ca[i]: PLAIN_ALPHABET[i] for i in range(26)}
    return encrypt_map, decrypt_map


def monoalphabetic_encrypt(plaintext, encrypt_map):
    return ''.join(encrypt_map[ch] if ch.isalpha() else ch
                   for ch in plaintext.upper())


def monoalphabetic_decrypt(ciphertext, decrypt_map):
    return ''.join(decrypt_map[ch] if ch.isalpha() else ch
                   for ch in ciphertext.upper())


def main():
    print("=" * 60)
    print("    MONOALPHABETIC CIPHER - Encryption & Decryption")
    print("=" * 60)
    print(f"\n  Plain Alphabet : {PLAIN_ALPHABET}")
    print(f"  Cipher Alphabet: {CIPHER_ALPHABET}")

    encrypt_map, decrypt_map = build_cipher_key(CIPHER_ALPHABET)

    message = input("\nEnter the plaintext message : ").strip()

    encrypted = monoalphabetic_encrypt(message, encrypt_map)
    decrypted = monoalphabetic_decrypt(encrypted, decrypt_map)

    print("\n" + "-" * 60)
    print(f"  Plaintext  : {message.upper()}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 60)


if __name__ == "__main__":
    main()
