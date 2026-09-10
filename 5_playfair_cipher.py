# =============================================================================
# PROGRAM 5: Playfair Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   Encrypts digraphs (letter pairs) using a 5x5 key matrix built from a
#   keyword (I and J share one cell).
#
# Encryption rules for each digraph (A, B):
#   Same row    -> shift each letter right (wrap)
#   Same column -> shift each letter down  (wrap)
#   Rectangle  -> each letter takes the other's column
# Decryption reverses row/column shifts; rectangle rule is identical.
# =============================================================================

def build_playfair_matrix(key):
    key  = key.upper().replace('J', 'I')
    seen = set()
    chars = []
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch); chars.append(ch)
    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in seen:
            seen.add(ch); chars.append(ch)
    return [chars[i * 5:(i + 1) * 5] for i in range(5)]


def get_position(matrix, ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == ch:
                return r, c


def prepare_plaintext(plaintext):
    text   = ''.join(ch for ch in plaintext.upper().replace('J', 'I') if ch.isalpha())
    result = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 == len(text):
            result += [a, 'X']; i += 1
        elif text[i] == text[i + 1]:
            result += [a, 'X']; i += 1
        else:
            result += [a, text[i + 1]]; i += 2
    return ''.join(result)


def playfair_encrypt_digraph(matrix, a, b):
    r1, c1 = get_position(matrix, a)
    r2, c2 = get_position(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]


def playfair_decrypt_digraph(matrix, a, b):
    r1, c1 = get_position(matrix, a)
    r2, c2 = get_position(matrix, b)
    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]


def playfair_encrypt(plaintext, key):
    matrix   = build_playfair_matrix(key)
    prepared = prepare_plaintext(plaintext)
    return ''.join(playfair_encrypt_digraph(matrix, prepared[i], prepared[i+1])
                   for i in range(0, len(prepared), 2))


def playfair_decrypt(ciphertext, key):
    matrix = build_playfair_matrix(key)
    return ''.join(playfair_decrypt_digraph(matrix, ciphertext[i], ciphertext[i+1])
                   for i in range(0, len(ciphertext), 2))


def main():
    print("=" * 58)
    print("      PLAYFAIR CIPHER - Encryption & Decryption")
    print("=" * 58)

    key     = input("\nEnter the keyword           : ").strip()
    message = input("Enter the plaintext message : ").strip()

    matrix   = build_playfair_matrix(key)
    prepared = prepare_plaintext(message)

    print(f"\n  Key Matrix (5x5) for keyword '{key.upper()}':")
    for row in matrix:
        print("  " + "  ".join(row))

    encrypted = playfair_encrypt(message, key)
    decrypted = playfair_decrypt(encrypted, key)

    prep_fmt = ' '.join(prepared[i:i+2] for i in range(0, len(prepared), 2))
    enc_fmt  = ' '.join(encrypted[i:i+2] for i in range(0, len(encrypted), 2))
    dec_fmt  = ' '.join(decrypted[i:i+2] for i in range(0, len(decrypted), 2))

    print("\n" + "-" * 58)
    print(f"  Plaintext  : {message.upper()}")
    print(f"  Prepared   : {prep_fmt}")
    print(f"  Encrypted  : {enc_fmt}")
    print(f"  Decrypted  : {dec_fmt}")
    print("-" * 58)


if __name__ == "__main__":
    main()
