# =============================================================================
# PROGRAM 3: Polyalphabetic Cipher (Vigenere) – Encryption & Decryption
# =============================================================================
# Description:
#   Uses a repeating keyword to apply a different Caesar shift to each letter,
#   making frequency analysis significantly harder than monoalphabetic ciphers.
#
# Algorithm:
#   Encryption: C[i] = (P[i] + K[i mod len(K)]) mod 26
#   Decryption: P[i] = (C[i] - K[i mod len(K)] + 26) mod 26
# =============================================================================

def vigenere_encrypt(plaintext, key):
    key       = key.upper()
    result    = ""
    key_index = 0
    for ch in plaintext.upper():
        if ch.isalpha():
            shift  = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += ch
    return result


def vigenere_decrypt(ciphertext, key):
    key       = key.upper()
    result    = ""
    key_index = 0
    for ch in ciphertext.upper():
        if ch.isalpha():
            shift  = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
            key_index += 1
        else:
            result += ch
    return result


def main():
    print("=" * 60)
    print("  POLYALPHABETIC (VIGENERE) CIPHER - Encryption & Decryption")
    print("=" * 60)

    message = input("\nEnter the plaintext message : ").strip()
    key     = input("Enter the keyword           : ").strip()

    if not key.isalpha():
        print("\n  [ERROR] Key must contain only alphabetic characters.")
        return

    encrypted = vigenere_encrypt(message, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("\n" + "-" * 60)
    print(f"  Plaintext  : {message.upper()}")
    print(f"  Keyword    : {key.upper()}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 60)


if __name__ == "__main__":
    main()
