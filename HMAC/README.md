# 🔐 Custom HMAC Implementation

A comprehensive implementation of Hash-based Message Authentication Code (HMAC) using custom SHA-2 and SHA-3 family hash functions.

## 📋 Overview

This project implements HMAC (Hash-based Message Authentication Code) as defined in **RFC 2104** and **FIPS PUB 198-1**, using custom implementations of various cryptographic hash functions from the SHA-2 and SHA-3 families. The implementation has been thoroughly tested and verified against Python's standard `hashlib` HMAC implementation.

## 🔑 What is HMAC?

HMAC (Hash-based Message Authentication Code) is a specific type of message authentication code (MAC) involving a cryptographic hash function and a secret cryptographic key. It provides both data integrity and authenticity verification.

### Key Features:
- **Authentication**: Verifies the sender's identity
- **Integrity**: Ensures message hasn't been tampered with  
- **Non-repudiation**: Sender cannot deny sending the message
- **Efficiency**: Fast computation using underlying hash functions

## 🏗️ Architecture

### Core Algorithm
The HMAC algorithm follows this structure:
```
HMAC(K, m) = H((K ⊕ opad) || H((K ⊕ ipad) || m))
```

Where:
- `K` is the secret key
- `m` is the message
- `H` is the hash function
- `opad` is the outer padding (0x5c repeated)
- `ipad` is the inner padding (0x36 repeated)
- `||` denotes concatenation
- `⊕` denotes XOR operation

## 🛠️ Implementation Details

### Custom Hash Functions Used
- **SHA-2 Family**: SHA-224, SHA-256, SHA-384, SHA-512
- **SHA-3 Family**: SHA3-224, SHA3-256, SHA3-384, SHA3-512
- **SHAKE Functions**: SHAKE128, SHAKE256 (Extendable Output Functions)

### Key Components

#### 1. Generic HMAC Function
```python
def generalized_hmac(key: str, message: str, hash_fn, block_size: int, outlen: int = None) -> str
```
- Supports any hash function with configurable block sizes
- Handles variable output lengths for SHAKE functions
- Returns hexadecimal digest

#### 2. SHAKE Handling
Special implementation for SHAKE128 and SHAKE256 due to their extendable output nature:
- SHAKE128: Block size = 168 bytes
- SHAKE256: Block size = 136 bytes
- Default output length: 64 bytes (512 bits)

## 📊 Supported Configurations

| Hash Function | Block Size (bytes) | Output Length | Status |
|---------------|-------------------|---------------|---------|
| SHA-224       | 64                | 28 bytes      | ✅ Verified |
| SHA-256       | 64                | 32 bytes      | ✅ Verified |
| SHA-384       | 128               | 48 bytes      | ✅ Verified |
| SHA-512       | 128               | 64 bytes      | ✅ Verified |
| SHA3-224      | 144               | 28 bytes      | ✅ Verified |
| SHA3-256      | 136               | 32 bytes      | ✅ Verified |
| SHA3-384      | 104               | 48 bytes      | ✅ Verified |
| SHA3-512      | 72                | 64 bytes      | ✅ Verified |
| SHAKE128      | 168               | Variable      | ✅ Verified |
| SHAKE256      | 136               | Variable      | ✅ Verified |

## 🧪 Testing Framework

### Comprehensive Test Suite
The implementation includes **310 test cases** (31 test vectors × 10 hash functions) covering:

#### Edge Cases:
- ✅ Empty keys and messages
- ✅ Keys longer than block size (requiring hashing)
- ✅ Keys shorter than block size (requiring padding)
- ✅ Binary data with control characters
- ✅ Unicode and emoji characters
- ✅ Very long keys and messages (>1000 characters)

#### Data Types:
- 📝 Plain text messages
- 🔢 Numeric data
- 🌍 Unicode/UTF-8 characters
- 🎯 Special characters and symbols
- 📋 JSON formatted data
- 📄 Multi-line text with newlines

#### Verification Method:
All outputs are cross-verified against Python's standard `hashlib.hmac` implementation to ensure correctness.

## 🚀 Usage Example

```python
# Import custom hash functions
from SHA_256 import generalized_SHA256 as SHA256
from SHA_3 import sha3_256

# Calculate HMAC-SHA256
key = "secret_key"
message = "Hello, World!"
hmac_result = generalized_hmac(key, message, SHA256, 64)
print(f"HMAC-SHA256: {hmac_result}")

# Calculate HMAC-SHA3-256  
hmac_sha3 = generalized_hmac(key, message, sha3_256, 136)
print(f"HMAC-SHA3-256: {hmac_sha3}")
```

## 🔬 Technical Specifications

### Key Processing:
1. **Key > Block Size**: Hash the key and use result as new key
2. **Key < Block Size**: Pad with zeros to block size  
3. **Key = Block Size**: Use key as-is

### Padding Constants:
- **Inner Pad (ipad)**: `0x36` repeated for block size
- **Outer Pad (opad)**: `0x5c` repeated for block size

### Security Considerations:
- Keys should be at least as long as the hash output
- Use cryptographically secure random key generation
- Protect keys from unauthorized access

## 📚 References

1. **RFC 2104**: "HMAC: Keyed-Hashing for Message Authentication" - Krawczyk, Bellare, Canetti (1997)
2. **FIPS PUB 198-1**: "The Keyed-Hash Message Authentication Code (HMAC)"
3. **RFC 6234**: "US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)"
4. **NIST SP 800-185**: "SHA-3 Derived Functions: cSHAKE, KMAC, TupleHash and ParallelHash"

## 🏆 Test Results

```
🔍 Testing HMAC-SHA-224: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA-256: ✅ PASSED (31/31 tests) 
🔍 Testing HMAC-SHA-384: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA-512: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA3-224: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA3-256: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA3-384: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHA3-512: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHAKE128: ✅ PASSED (31/31 tests)
🔍 Testing HMAC-SHAKE256: ✅ PASSED (31/31 tests)
```

**Total: 310/310 tests passed ✅**

## 📁 Project Structure

```
HMAC-Implementation/
├── HMAC.ipynb              # Main implementation notebook
├── SHA_224.py              # Custom SHA-224 implementation  
├── SHA_256.py              # Custom SHA-256 implementation
├── SHA_384.py              # Custom SHA-384 implementation
├── SHA_512.py              # Custom SHA-512 implementation
├── SHA_3.py                # Custom SHA-3 family implementations
└── README.md               # This file
```

## 🎯 Key Achievements

- ✅ **100% Test Coverage**: All 310 test cases pass
- ✅ **Standard Compliance**: Matches `hashlib.hmac` output exactly
- ✅ **Multiple Hash Functions**: Supports 10 different hash algorithms
- ✅ **Edge Case Handling**: Robust handling of all input types
- ✅ **Performance**: Efficient implementation with proper key processing
- ✅ **Documentation**: Comprehensive documentation and testing

## 🔐 Security Note

This implementation is for educational and research purposes. For production use, always prefer well-established, audited cryptographic libraries.

---

*Implementation verified against Python's standard library • All test vectors pass • RFC 2104 compliant*