# =============================================================================
# PROGRAM 6: Rail Fence Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   A transposition cipher that writes plaintext diagonally across n rails
#   in a zigzag pattern, then reads each rail left-to-right to form the
#   ciphertext.
#
# Algorithm:
#   Encryption: place characters in zigzag order, read rail by rail.
#   Decryption: determine rail lengths, fill rails from ciphertext,
#               re-read in zigzag order.
# =============================================================================

def rail_fence_encrypt(plaintext, num_rails):
    rails     = [[] for _ in range(num_rails)]
    rail      = 0
    direction = 1
    for ch in plaintext:
        rails[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in rails), rails


def rail_fence_decrypt(ciphertext, num_rails):
    n            = len(ciphertext)
    rail_pattern = []
    rail         = 0
    direction    = 1
    for _ in range(n):
        rail_pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction

    rail_lengths  = [rail_pattern.count(r) for r in range(num_rails)]
    rail_contents = []
    idx = 0
    for length in rail_lengths:
        rail_contents.append(list(ciphertext[idx:idx + length]))
        idx += length

    rail_idx = [0] * num_rails
    result   = []
    for r in rail_pattern:
        result.append(rail_contents[r][rail_idx[r]])
        rail_idx[r] += 1
    return ''.join(result)


def main():
    print("=" * 58)
    print("      RAIL FENCE CIPHER - Encryption & Decryption")
    print("=" * 58)

    message   = input("\nEnter the plaintext message : ").strip()
    num_rails = int(input("Enter the number of rails   : ").strip())

    if num_rails < 2:
        print("\n  [ERROR] Number of rails must be at least 2.")
        return

    encrypted, rails = rail_fence_encrypt(message, num_rails)
    decrypted        = rail_fence_decrypt(encrypted, num_rails)

    print(f"\n  Rail contents:")
    for i, rail_chars in enumerate(rails):
        print(f"    Rail {i} : {''.join(rail_chars)}")

    print("\n" + "-" * 58)
    print(f"  Plaintext  : {message}")
    print(f"  Rails      : {num_rails}")
    print(f"  Encrypted  : {encrypted}")
    print(f"  Decrypted  : {decrypted}")
    print("-" * 58)


if __name__ == "__main__":
    main()
