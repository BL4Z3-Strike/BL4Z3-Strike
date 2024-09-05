import hashlib


def hash_function(algorithm):
    if algorithm == 'md5':
        return hashlib.md5
    elif algorithm == 'sha1':
        return hashlib.sha1
    elif algorithm == 'sha256':
        return hashlib.sha256
    elif algorithm == 'sha512':
        return hashlib.sha512
    else:
        raise ValueError("Not Found.")


def hash_text(algorithm, text):
    hasher = hash_function(algorithm)()
    hasher.update(text.encode())
    return hasher.hexdigest()


def brute_force_hash(target_hash, algorithm, worklist):
    for guess in worklist:
        hashed_guess = hash_text(algorithm, guess)
        if hashed_guess == target_hash:
            return guess
        print(f"{guess} [-] - {hashed_guess}")  
    return None


def main():
    algorithm = input("Enter hash algorithm (md5, sha1, sha256, sha512): ").strip().lower()
    if algorithm not in ['md5', 'sha1', 'sha256', 'sha512']:
        print("Enter an algorithm.")
        return

    target_hash = input("Enter Hash: ").strip()
    worklist_path = input("Wordlist: ").strip()

    try:
        with open(worklist_path, 'r') as file:
            worklist = [line.strip() for line in file]
    except FileNotFoundError:
        print("Wordlist not found.")
        return

    print("Starting Brute Force ...")
    result = brute_force_hash(target_hash, algorithm, worklist)

    if result:
        print(f"Hash found: {result} [+]")
    else:
        print("Hash not found.")


if __name__ == "__main__":
    main()
