import hashlib

#function to calculate the SHA-256 hash of a file
def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(4096):  # Read file in chunks
            sha256.update(chunk)  # Update hash
    return sha256.hexdigest()  # Return hexadecimal hash

#function to compare current file hash with known hash
def check_integrity(file_path, known_hash):
    current_hash = hash_file(file_path)
    if current_hash == known_hash:
        print("✅ File is intact.")  # Hash matches
    else:
        print("❌ File has been modified!")  # Hash mismatch

#example usage with known hash
file_path = 'important_config.txt'
known_hash = '3c62fdd2488cfbfefcc8b7c59cb110a0e8f03e024d29ea9c86dc0aaedb06d33e'
check_integrity(file_path, known_hash)
