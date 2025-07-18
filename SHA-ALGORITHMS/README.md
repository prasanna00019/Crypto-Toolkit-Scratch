# 🛡️ SHA Hash Function Implementations in Python (From Scratch) 🔐✨

This project showcases **from-scratch implementations** of various SHA (Secure Hash Algorithm) hash functions in Python, including **SHA-1**, **SHA-224**, **SHA-256**, **SHA-384**, **SHA-512**, **SHA-512/224**, and **SHA-512/256**. It is designed for educational purposes, providing detailed insights into the internal workings of these cryptographic algorithms.

---

## 🚀 Features

- **SHA Variants**: Full implementations of SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256.
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
- [SHA Wikipedia](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm)

---

Happy hashing and learning! 🔒✨