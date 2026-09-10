# =============================================================================
# PROGRAM 4: Hill Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   A polygraphic substitution cipher based on linear algebra. Encrypts
#   pairs of letters using 2x2 matrix multiplication modulo 26.
#
# Algorithm:
#   Encryption: C = K x P  (mod 26)
#   Decryption: P = K_inv x C  (mod 26)
#   K_inv = det(K)^-1 x adj(K)  mod 26
# =============================================================================

import math

KEY_MATRIX = [[3, 3],
              [2, 5]]


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} mod {m}.")


def matrix_det_mod26(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26


def matrix_inverse_mod26(matrix):
    det     = matrix_det_mod26(matrix)
    det_inv = mod_inverse(det, 26)
    adj     = [[ matrix[1][1], -matrix[0][1]],
               [-matrix[1][0],  matrix[0][0]]]
    return [[(det_inv * adj[i][j]) % 26 for j in range(2)] for i in range(2)]


def hill_encrypt_block(block, key_matrix):
    p = [ord(ch) - ord('A') for ch in block]
    c = [(key_matrix[0][0] * p[0] + key_matrix[0][1] * p[1]) % 26,
         (key_matrix[1][0] * p[0] + key_matrix[1][1] * p[1]) % 26]
    return ''.join(chr(n + ord('A')) for n in c)


def hill_decrypt_block(block, inv_key):
    c = [ord(ch) - ord('A') for ch in block]
    p = [(inv_key[0][0] * c[0] + inv_key[0][1] * c[1]) % 26,
         (inv_key[1][0] * c[0] + inv_key[1][1] * c[1]) % 26]
    return ''.join(chr(n + ord('A')) for n in p)


def hill_encrypt(plaintext, key_matrix):
    text = ''.join(ch for ch in plaintext.upper() if ch.isalpha())
    if len(text) % 2 != 0:
        text += 'X'
        print(f"  [INFO] Padded with 'X': {text}")
    return ''.join(hill_encrypt_block(text[i:i+2], key_matrix)
                   for i in range(0, len(text), 2))


def hill_decrypt(ciphertext, key_matrix):
    inv = matrix_inverse_mod26(key_matrix)
    return ''.join(hill_decrypt_block(ciphertext[i:i+2], inv)
                   for i in range(0, len(ciphertext), 2))


def main():
    print("=" * 55)
    print("        HILL CIPHER - Encryption & Decryption")
    print("=" * 55)

    det = matrix_det_mod26(KEY_MATRIX)
    if math.gcd(det, 26) != 1:
        print(f"\n  [ERROR] Key matrix determinant ({det}) is not coprime with 26.")
        return

    inv = matrix_inverse_mod26(KEY_MATRIX)
    print(f"\n  Key Matrix : [[{KEY_MATRIX[0][0]}, {KEY_MATRIX[0][1]}], [{KEY_MATRIX[1][0]}, {KEY_MATRIX[1][1]}]]")
    print(f"  Inv Matrix : [[{inv[0][0]}, {inv[0][1]}], [{inv[1][0]}, {inv[1][1]}]]  (mod 26)")

    message = input("\nEnter the plaintext message : ").strip()

    encrypted = hill_encrypt(message, KEY_MATRIX)
    decrypted = hill_decrypt(encrypted, KEY_MATRIX)

    print("\n" + "-" * 55)
    print(f"  Plaintext  : {''.join(ch for ch in message.upper() if ch.isalpha())}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 55)


if __name__ == "__main__":
    main()
