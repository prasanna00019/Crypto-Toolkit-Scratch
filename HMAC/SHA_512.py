H0 = 0x6a09e667f3bcc908
H1 = 0xbb67ae8584caa73b
H2 = 0x3c6ef372fe94f82b
H3 = 0xa54ff53a5f1d36f1
H4 = 0x510e527fade682d1
H5 = 0x9b05688c2b3e6c1f
H6 = 0x1f83d9abfb41bd6b
H7 = 0x5be0cd19137e2179
K = [
    0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc,
    0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
    0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2,
    0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
    0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
    0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
    0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4,
    0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
    0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df,
    0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
    0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30,
    0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
    0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8,
    0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
    0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
    0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
    0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178,
    0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
    0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c,
    0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817
]
def number_to_binary(n):
    """Convert an integer to a 128-bit binary string."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return bin(n)[2:].zfill(128)  # Ensures exactly 128 bits
def preprocessing_input(input):
    """Prepares input for SHA-512 by adding padding and length encoding."""
    # input_bytes = input.encode('utf-8')  # Convert to bytes
    input_bytes = input  # Assuming input is already in bytes or string format
    n = len(input_bytes)  # Length in bytes
    message_bits = ''.join(format(byte, '08b') for byte in input_bytes)  # Convert each byte to 8-bit binary
    message_bits += '1'  # Append single '1' bit
    # Compute k (number of zero bits required)
    k = (896 - ((n * 8 + 1) % 1024)) % 1024
    # print(k)
    message_bits += '0' * k  # Append k zero bits
    # print(message_bits,' message bits')
    # Append original length in 64-bit binary
    message_bits += number_to_binary(n * 8)
    return message_bits
def right_rotate(n, b):
    """Right rotate a 64-bit integer n by b bits."""
    return ((n >> b) | (n << (64 - b))) & 0xFFFFFFFFFFFFFFFF  # Ensure 64-bit result                                     
def SHR(x,n):
    return x>>n  
def summation_0_func(x):
    return right_rotate(x, 28) ^ right_rotate(x, 34) ^ right_rotate(x, 39)
def summation_1_func(x):
    return right_rotate(x,14) ^ right_rotate(x,18) ^ right_rotate(x,41)
def sigma_0_func(x):
    return right_rotate(x,1) ^ right_rotate(x,8) ^ SHR(x,7)
def sigma_1_func(x):
    return right_rotate(x,19) ^ right_rotate(x,61) ^ SHR(x,6)
def ch(x,y,z):
     return (x & y) ^ ((~x) & z)
def maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)  
def message_schedule_16_blocks(padded_message_block):
    W = []
    for i in range(16):  # 16 words of 64 bits each
        word = padded_message_block[i * 64: (i + 1) * 64]  # Extract 64-bit chunk
        word_int = int(word, 2)  # Convert binary string to integer
        W.append(word_int)
    return W
def words_17_to_80(W):
    for i in range(16, 80):
        new_word = (sigma_1_func(W[i-2]) + W[i-7] + sigma_0_func(W[i-15]) + W[i-16]) &  0xFFFFFFFFFFFFFFFF
        W.append(new_word)  # Ensure it's 64-bit
    return W
def Nth_block_output(input,h0_temp,h1_temp,h2_temp,h3_temp,h4_temp,h5_temp,h6_temp,h7_temp):
  a, b, c, d, e, f,g,h = h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp, h6_temp,h7_temp
  W=words_17_to_80(message_schedule_16_blocks(input))
  for i in range(80):
    T1 = (h + summation_1_func(e) + ch(e, f, g) + K[i] + W[i]) & 0xFFFFFFFFFFFFFFFF
    T2 = (summation_0_func(a) + maj(a, b, c)) & 0xFFFFFFFFFFFFFFFF
    h = g
    g = f
    f = e
    e = (d + T1) & 0xFFFFFFFFFFFFFFFF
    d = c
    c = b
    b = a
    a = (T1 + T2) & 0xFFFFFFFFFFFFFFFF
  h0_temp = (h0_temp + a) &0xFFFFFFFFFFFFFFFF
  h1_temp = (h1_temp + b) &0xFFFFFFFFFFFFFFFF
  h2_temp = (h2_temp + c) &0xFFFFFFFFFFFFFFFF 
  h3_temp = (h3_temp + d) &0xFFFFFFFFFFFFFFFF
  h4_temp = (h4_temp + e) &0xFFFFFFFFFFFFFFFF
  h5_temp = (h5_temp + f) &0xFFFFFFFFFFFFFFFF
  h6_temp = (h6_temp + g) &0xFFFFFFFFFFFFFFFF
  h7_temp = (h7_temp + h) &0xFFFFFFFFFFFFFFFF
  return h0_temp,h1_temp,h2_temp,h3_temp,h4_temp,h5_temp,h6_temp,h7_temp

def generalized_SHA512(input):
   H0 = 0x6a09e667f3bcc908
   H1 = 0xbb67ae8584caa73b
   H2 = 0x3c6ef372fe94f82b
   H3 = 0xa54ff53a5f1d36f1
   H4 = 0x510e527fade682d1
   H5 = 0x9b05688c2b3e6c1f
   H6 = 0x1f83d9abfb41bd6b
   H7 = 0x5be0cd19137e2179
   h0_temp, h1_temp, h2_temp, h3_temp, h4_temp , h5_temp,h6_temp,h7_temp= H0, H1, H2, H3, H4 ,H5,H6,H7 
   length_processed_text = len(preprocessing_input(input))  
   input_temp=preprocessing_input(input); 
   for i in range(length_processed_text // 1024):
        if i == 0:
            h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp = Nth_block_output(input_temp[0:1024], H0, H1, H2, H3, H4,H5,H6,H7)
        else:    
            h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp = Nth_block_output(input_temp[i * 1024:(i + 1) * 1024], 
                                                                           h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp)

   return ''.join([
        f"{h0_temp:016x}", 
        f"{h1_temp:016x}", 
        f"{h2_temp:016x}", 
        f"{h3_temp:016x}", 
        f"{h4_temp:016x}",
        f"{h5_temp:016x}",
        f"{h6_temp:016x}",
        f"{h7_temp:016x}"
    ])



