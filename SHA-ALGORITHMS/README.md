# 🛡️ SHA & Keccak/SHA-3 Hash Function Implementations in Python (From Scratch) 🔐✨

This project showcases **from-scratch implementations** of various SHA (Secure Hash Algorithm) hash functions in Python, **including SHA-1, the full SHA-2 family, and now SHA-3 (Keccak) and its variants at the bit level**. It is designed for educational purposes, providing detailed insights into the internal workings of these cryptographic algorithms.

---

## 🚀 Features

- **SHA-1 & SHA-2 Variants**: Full implementations of SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256.
- **SHA-3 & Keccak Variants**:
  - **SHA-3 Family**: SHA3-224, SHA3-256, SHA3-384, SHA3-512
  - **Keccak Family**: Keccak-224, Keccak-256, Keccak-384, Keccak-512
  - **SHAKE Functions**: SHAKE128, SHAKE256 (arbitrary-length XOFs)
- **Bit-Level Implementation**: The Keccak/SHA-3 family is implemented at the bit level (not byte level), adhering closely to the FIPS 202 standard and demonstrating the internal mechanics of bitwise operations.
- **Pure Python**: No external cryptography libraries are used—everything is built from scratch.
- **Educational**: Step-by-step explanations and modular functions for easy understanding.
- **Unicode Support**: Handles inputs with diverse characters, including multilingual text.
- **Salted Hashing (SHA-224)**: Includes salt mixing and dynamic salt embedding to enhance security.
- **Testing & Validation**: Verified against standard outputs and Python's `hashlib` for correctness.

---

## 📚 How It Works

### General Workflow
1. **Preprocessing**:
   - Pads the input message and encodes its length.
   - Prepares the message for block-wise processing.
2. **Message Scheduling**:
   - Expands the message into words for processing.
   - The number of words and their size depend on the specific SHA variant.
3. **Compression**:
   - Processes each block through a series of rounds using SHA-specific transformations.
4. **Final Hash**:
   - Concatenates and formats the resulting hash values.

### Salted Hashing (SHA-224)
- Random salts are generated and dynamically mixed into the hash.
- Utilities are provided for extracting and verifying salted hashes.

### Keccak/SHA-3 Family (Bit-Level)
- **Implements the Keccak sponge construction at the bit level** (not just bytes).
- Includes support for domain separation, custom padding, and output bit reversal per the official SHA-3 standard.
- **Variants implemented:**
  - **SHA-3 Functions**: `sha3_224`, `sha3_256`, `sha3_384`, `sha3_512`
  - **Keccak Functions**: `keccak_224`, `keccak_256`, `keccak_384`, `keccak_512`
  - **SHAKE XOFs**: `shake128`, `shake256` (arbitrary-length outputs)

---

## 📝 Example Usage

### Text Hashing

- **SHA-1**:
  ```python
  print(generalized_SHA1("Your message here"))
  ```
- **SHA-256**:
  ```python
  print(generalized_SHA256("hello world"))
  # Output: b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
  ```
- **SHA-512/256**:
  ```python
  print(generalized_SHA512_256("your message here"))
  ```
- **SHA-3 (bit-level, Keccak, SHAKE)**:
  ```python
  print(sha3_256("hello world"))
  print(keccak_256("hello world"))
  print(shake128("hello world", 256))  # 256 bits (32 hex chars)
  print(shake256("hello world", 512))  # 512 bits (64 hex chars)
  ```

### Salted Hashing (SHA-224)
- **Generate Salted Hash**:
  ```python
  hashed_output, used_salt = generalized_SHA224_salt("your message here")
  print("Salted Hash:", hashed_output)
  print("Salt Used:", used_salt)
  ```
- **Verify Salted Hash**:
  ```python
  is_valid = compare_hash("your message here", hashed_output)
  print("Is Valid?", is_valid)
  ```

---

## 📦 Project Highlights

- **SHA Variants**:
  - **SHA-1**: Demonstrates the basic structure of cryptographic hash functions.
  - **SHA-2 Family**:
    - SHA-224/256/384/512: Implements each variant with its unique parameters and specifications.
    - SHA-512/224 & SHA-512/256: Variants of SHA-512 with truncated outputs.
- **SHA-3 & Keccak**:
  - Full bit-level implementations of all SHA-3 standard functions and legacy Keccak variants.
  - SHAKE128 and SHAKE256 XOFs for customizable-length output.
- **Salted Hashing**:
  - Enhances security with dynamic salt embedding (SHA-224).
  - Prevents rainbow table attacks by adding randomness to hashes.
- **Educational Value**:
  - Modular implementations for learning and experimentation.
  - Transparent logic with no black-box dependencies.

---

## ⚠️ Notes & Disclaimer

- **For Learning Only**: These implementations are designed for educational purposes. Do **not** use them for production or security-critical applications.
- **Verified Results**: Outputs are validated against Python's `hashlib` and known test vectors.

---

## 📚 References

- [FIPS PUB 180-4: Secure Hash Standard (SHS)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf)
- [FIPS PUB 202: SHA-3 Standard](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf)
- [SHA Wikipedia](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm)

---

Happy hashing and learning! 🔒✨