import math

def is_prime(n):
    """Verifies if a number is prime."""
    if n < 2: 
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

def generate_keypair(p, q):
    """Generates Public and Private RSA keys from two primes."""
    n = p * q
    phi = (p - 1) * (q - 1)

    # Standard public exponent selection
    e = 65537
    if math.gcd(e, phi) != 1:
        e = 3
        while math.gcd(e, phi) != 1:
            e += 2

    # Calculate private exponent d
    d = pow(e, -1, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext_msg):
    """Encrypts text using the public key (e, n)."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext_msg]

def decrypt(private_key, ciphertext_list):
    """Decrypts numbers back to text using the private key (d, n)."""
    d, n = private_key
    return "".join([chr(pow(char, d, n)) for char in ciphertext_list])

def get_prime_input(prompt):
    """Gets valid prime integer from the user."""
    while True:
        try:
            val = int(input(prompt))
            if is_prime(val):
                return val
            print("Error: That number is not prime. Try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")

# --- Interactive Main Execution ---
if __name__ == "__main__":
    print("RSA Key Generation and Encryption")
    
    # 1. Get Prime Inputs from User
    p = get_prime_input("Enter prime number p (e.g., 61): ")
    while True:
        q = get_prime_input("Enter prime number q (e.g., 53): ")
        if p != q:
            break
        print("Error: q cannot be equal to p. Choose a different prime.")

    # 2. Key Generation
    public, private = generate_keypair(p, q)
    print("\nKeys Generated Successfully!")
    print(f"Public Key (e, n): {public}")
    print(f"Private Key (d, n): {private}")

    # 3. Message Handling
    print("\nMessage Processing")
    message = input("Enter the secret message to encrypt: ")
    
    # Check if the chosen primes are too small for the characters used
    max_char_val = max(ord(c) for c in message) if message else 0
    if max_char_val >= (p * q):
        print(f"Warning: Your primes are too small (n = {p*q}).")
        print(f"Characters require n to be larger than {max_char_val} to prevent data loss.")
    
    # 4. Process Encryption and Decryption
    encrypted_msg = encrypt(public, message)
    print(f"\nCiphertext (Numeric Array): {encrypted_msg}")
    
    decrypted_msg = decrypt(private, encrypted_msg)
    print(f"Decrypted Plaintext: '{decrypted_msg}'")
