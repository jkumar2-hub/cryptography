# =============================================================================
# PROGRAM 7: Double Columnar Transposition Cipher – Encryption & Decryption
# =============================================================================
# Description:
#   Applies columnar transposition twice using two separate keywords for
#   stronger security than a single transposition.
#
# Algorithm:
#   1. Pad plaintext with 'X', write row-by-row into a grid (width = len(Key1)).
#   2. Read columns in alphabetical key order -> intermediate ciphertext.
#   3. Apply the same process with Key2 -> final ciphertext.
#   Decryption reverses both transpositions in reverse order.
# =============================================================================

def get_column_order(key):
    indexed = sorted(enumerate(key.upper()), key=lambda x: (x[1], x[0]))
    return [i for i, _ in indexed]


def columnar_encrypt(text, key):
    key_len   = len(key)
    padded    = text.upper()
    remainder = len(padded) % key_len
    if remainder != 0:
        padded += 'X' * (key_len - remainder)
    num_rows = len(padded) // key_len
    grid     = [list(padded[r * key_len:(r + 1) * key_len]) for r in range(num_rows)]
    order    = get_column_order(key)
    result   = ''.join(grid[row][col] for col in order for row in range(num_rows))
    return result, num_rows


def columnar_decrypt(ciphertext, key, num_rows):
    key_len = len(key)
    order   = get_column_order(key)
    cols    = {}
    idx     = 0
    for col in order:
        cols[col] = list(ciphertext[idx:idx + num_rows])
        idx += num_rows
    return ''.join(cols[c][r] for r in range(num_rows) for c in range(key_len))


def double_columnar_encrypt(plaintext, key1, key2):
    inter,  rows1 = columnar_encrypt(plaintext, key1)
    cipher, rows2 = columnar_encrypt(inter,    key2)
    return cipher, rows1, rows2


def double_columnar_decrypt(ciphertext, key1, key2, rows1, rows2):
    inter     = columnar_decrypt(ciphertext, key2, rows2)
    plaintext = columnar_decrypt(inter,      key1, rows1)
    return plaintext.rstrip('X')


def main():
    print("=" * 65)
    print("  DOUBLE COLUMNAR TRANSPOSITION - Encryption & Decryption")
    print("=" * 65)

    message = input("\nEnter the plaintext message : ").strip()
    key1    = input("Enter first keyword  (Key 1): ").strip()
    key2    = input("Enter second keyword (Key 2): ").strip()

    if not key1.isalpha() or not key2.isalpha():
        print("\n  [ERROR] Keys must contain only alphabetic characters.")
        return

    encrypted, r1, r2 = double_columnar_encrypt(message, key1, key2)
    decrypted         = double_columnar_decrypt(encrypted, key1, key2, r1, r2)

    print("\n" + "-" * 65)
    print(f"  Plaintext  : {message.upper()}")
    print(f"  Key 1      : {key1.upper()}")
    print(f"  Key 2      : {key2.upper()}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 65)


if __name__ == "__main__":
    main()
