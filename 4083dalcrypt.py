def main():
    # 1. Input public parameters (p should be a prime number)
    p = int(input("Enter value of p: "))
    g = int(input("Enter value of generator g: "))

    # 2. Input private keys (secretly held by Alice and Bob)
    a = int(input("Enter private key of Alice: "))
    b = int(input("Enter private key of Bob: "))

    print(f"\nAlice's Secret private key: {a}")
    print(f"Bob's Secret private key: {b}")
    print()

    # 3. Calculate Public Keys
    # Alice computes A = g^a mod p
    # Bob computes B = g^b mod p
    A = pow(g, a, p)
    B = pow(g, b, p)

    print(f"Alice's Public Key sent to Bob: {A}")
    print(f"Bob's Public Key sent to Alice: {B}")
    print()

    # 4. Calculate Shared Secrets
    # Alice computes secret = B^a mod p
    # Bob computes secret = A^b mod p
    alice_shared_secret = pow(B, a, p)
    bob_shared_secret = pow(A, b, p)

    print(f"Alice's calculated Secret: {alice_shared_secret}")
    print(f"Bob's calculated Secret: {bob_shared_secret}")
    print()

    # 5. Verification
    if alice_shared_secret == bob_shared_secret:
        print("Success! Both Parties have established the same secret key.")
    else:
        print("Error: Shared secrets do not match.")

if __name__ == "__main__":
    main()
