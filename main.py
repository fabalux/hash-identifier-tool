import hashlib


def generate_hashes(text):
    """Generate common hash digests for the given text."""
    return {
        "MD5": hashlib.md5(text.encode()).hexdigest(),
        "SHA1": hashlib.sha1(text.encode()).hexdigest(),
        "SHA256": hashlib.sha256(text.encode()).hexdigest(),
        "SHA512": hashlib.sha512(text.encode()).hexdigest(),
    }


def identify_hash(hash_string):
    """Guess the hash algorithm based on its length and character set."""
    hash_string = hash_string.strip()
    length = len(hash_string)
    is_hex = all(c in "0123456789abcdefABCDEF" for c in hash_string)

    if not is_hex:
        return "Not a valid hexadecimal hash."

    possibilities = {
        32: "MD5",
        40: "SHA1",
        64: "SHA256",
        128: "SHA512",
    }

    return possibilities.get(length, "Unknown hash type (uncommon length)")


def main():
    print("=== Hash Identifier & Generator ===")
    print("1. Generate hashes from text")
    print("2. Identify a hash type")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        text = input("Enter text to hash: ")
        hashes = generate_hashes(text)
        print("\nGenerated Hashes:")
        for algo, value in hashes.items():
            print(f"{algo:<8}: {value}")

    elif choice == "2":
        hash_input = input("Enter hash to identify: ")
        result = identify_hash(hash_input)
        print(f"\nResult: {result}")

    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
