# 🛡️ AES Encryption & Decryption in Python (From Scratch) 🔐✨

This project demonstrates complete, from-scratch implementations of the **AES-128**, **AES-192**, and **AES-256** encryption algorithms in Python. It includes both encryption and decryption workflows, supporting UTF-8 text, emojis, and even file encryption (AES-256).

---

## 🚀 Features

- **AES Variants**: Full implementations of AES-128, AES-192, and AES-256.
- **Key Expansion**: Generates round keys (11 for AES-128, 13 for AES-192, 15 for AES-256).
- **Block Cipher**: Operates on 128-bit (16-byte) blocks with proper padding.
- **Encryption/Decryption**: Step-by-step processes for each AES variant.
- **File Encryption (AES-256)**: Encrypt and decrypt files (binary or text).
- **UTF-8 Compatibility**: Handles Unicode, multilingual text, and emojis seamlessly.
- **No External Crypto Libraries**: All cryptographic logic is implemented manually.
- **Educational Value**: Transparent implementation of all AES transformations (SubBytes, ShiftRows, MixColumns, AddRoundKey, etc.).

---

## 📚 How It Works

1. **Key Expansion**:
   - AES-128: Expands a 16-character ASCII key into 11 round keys.
   - AES-192: Expands a 24-character ASCII key into 13 round keys.
   - AES-256: Expands a 32-character ASCII key into 15 round keys.

2. **Encryption Pipeline**:
   - Converts input to UTF-8 hex and pads it to 16-byte blocks.
   - Each block undergoes:
     - AddRoundKey
     - SubBytes
     - ShiftRows
     - MixColumns (except the final round).
   - Final round omits MixColumns.

3. **Decryption Pipeline**:
   - Reverses the encryption steps using inverse AES transformations:
     - InvSubBytes
     - InvShiftRows
     - InvMixColumns (except the final round).
   - Removes padding and converts hex output back to the original UTF-8 string.

4. **File Utilities (AES-256)**:
   - Encrypts and decrypts files using the implemented AES logic.

---

## 📝 Usage

### Text Encryption/Decryption
- **AES-128**:
  ```python
  cipher_text = generalized_encrypt_AES("Your message", "16-char-key-here")
  plain_text = generalized_decrypt_AES(cipher_text, "16-char-key-here")
  ```
- **AES-192**:
  ```python
  cipher_text = generalized_encrypt_AES("Your message", "24-char-key-here")
  plain_text = generalized_decrypt_AES(cipher_text, "24-char-key-here")
  ```
- **AES-256**:
  ```python
  cipher_text = generalized_encrypt_AES("Your message", "32-char-key-here")
  plain_text = generalized_decrypt_AES(cipher_text, "32-char-key-here")
  ```

### File Encryption/Decryption (AES-256)
- **Encrypt a File**:
  ```python
  encrypt_file("your_file.pdf")
  ```
- **Decrypt a File**:
  ```python
  decrypt_file("your_file.pdf.enc", "restored_file.pdf")
  ```

---

## 📦 Project Highlights

- **Step-by-step Implementation**: Each AES transformation is modularized and explained.
- **Unicode Ready**: Handles emojis and non-ASCII characters effortlessly.
- **No Black Boxes**: All cryptographic operations are implemented manually for educational clarity.

---

## ⚠️ Notes & Disclaimer

- **Key Length**: Ensure the key length matches the AES variant (16, 24, or 32 ASCII characters).
- **Educational Purpose**: This implementation is for learning and demonstration. For production, use well-tested libraries like `cryptography` or `PyCrypto`.
- **File Support**: File encryption/decryption is available only for AES-256.

---

## 📚 References

- [AES (Wikipedia)](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [FIPS-197: Advanced Encryption Standard (AES)](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf)

---

Happy encrypting and decrypting! 🎉🔒