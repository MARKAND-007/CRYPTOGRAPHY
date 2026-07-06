import rsa

# 1. Key Generation
# Generate a public and private key pair. 
# 2048 bits is the recommended minimum standard for secure communication.
public_key, private_key = rsa.newkeys(2048)

# 2. Defining the Message
# Data must be converted to bytes before processing.
message = "Confidential Data Entry".encode('utf-8')

# 3. Encryption
# The sender uses the recipient's public key to encrypt the data.
ciphertext = rsa.encrypt(message, public_key)

print(f"Encrypted Ciphertext: {ciphertext.hex()[:60]}...")

# 4. Decryption
# The recipient uses their private key to decrypt the data.
decrypted_message = rsa.decrypt(ciphertext, private_key)

print(f"Decrypted Message: {decrypted_message.decode('utf-8')}")
