
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

def preprocessing_input(input):
    n=len(input)
    k= (448-(1+n*8))%512
    print('1'+ k*'0'+ number_to_binary(n*8))
    print(len('1'+ k*'0'+ number_to_binary(n*8)))
def number_to_binary(n):
    """Convert an integer to a 64-bit binary string."""
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    return bin(n)[2:].zfill(64)  # Ensures exactly 64 bits

def preprocessing_input(input,type='string'):
    """Prepares input for SHA-1 by adding padding and length encoding."""
    input_bytes = input
    # if(type=='string'):
    #  input_bytes = input.encode('utf-8')  # Convert to bytes
    # elif(type=='bytes'): 
    #  input_bytes = input   
    n = len(input_bytes)  # Length in bytes
    message_bits = ''.join(format(byte, '08b') for byte in input_bytes)  # Convert each byte to 8-bit binary
    message_bits += '1'  # Append single '1' bit
    # Compute k (number of zero bits required)
    k = (448 - ((n * 8 + 1) % 512)) % 512
    message_bits += '0' * k  # Append k zero bits
    # Append original length in 64-bit binary
    message_bits += number_to_binary(n * 8)
    return message_bits
def right_rotate(n, b):
    """Right rotate a 32-bit integer n by b bits."""
    return ((n >> b) | (n << (32 - b))) & 0xFFFFFFFF  # Ensure 32-bit result    
def SHR(x,n):
    return x>>n
def summation_0_func(x):
    # print(f"Length of x in bits: {x.bit_length()}")  # Print bit length of x
    return right_rotate(x,2) ^ right_rotate(x,13) ^ right_rotate(x,22)
def summation_1_func(x):
    return right_rotate(x,6) ^ right_rotate(x,11) ^ right_rotate(x,25)
def sigma_0_func(x):
    return right_rotate(x,7) ^ right_rotate(x,18) ^ SHR(x,3)
def sigma_1_func(x):
    return right_rotate(x,17) ^ right_rotate(x,19) ^ SHR(x,10)
def ch(x,y,z):
     return (x & y) ^ ((~x) & z)
def maj(x,y,z):
    return (x & y) ^ (y & z) ^ (x & z)
def message_schedule_16_blocks(padded_message_block):
    """
    Extracts W₀ to W₁₅ from a 512-bit padded message block and converts to hex.
    Assumes input is a string of '0' and '1' (binary representation).
    """
    W = []
    for i in range(16):  # 16 words of 32 bits each
        word = padded_message_block[i * 32: (i + 1) * 32]  # Extract 32-bit chunk
        word_int = int(word, 2)  # Convert binary string to integer
        W.append(word_int)
    return W
def words_17_to_64(W):
    """
    Expands W₀ to W₆₃ using:
    Wₜ = (σ₁(Wₜ₋₂) + Wₜ₋₇ + σ₀(Wₜ₋₁₅) + Wₜ₋₁₆) mod 2³²
    """
    for i in range(16, 64):
        new_word = (sigma_1_func(W[i-2]) + W[i-7] + sigma_0_func(W[i-15]) + W[i-16]) & 0xFFFFFFFF
        W.append(new_word)  # Ensure it's 32-bit
    return W
def Nth_block_output(input,h0_temp,h1_temp,h2_temp,h3_temp,h4_temp,h5_temp,h6_temp,h7_temp):
  a, b, c, d, e, f,g,h = h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp, h6_temp,h7_temp
  W=words_17_to_64(message_schedule_16_blocks(input))
  for i in range(64):
    T1=(h + summation_1_func(e) + ch(e,f,g) + K[i] + W[i]) & 0xFFFFFFFF 
    T2= (summation_0_func(a) + maj(a,b,c)) & 0xFFFFFFFF 
    h=g
    g=f
    f=e
    e=(d+ T1) & 0xFFFFFFFF
    d=c
    c=b
    b=a
    a= (T1+ T2) & 0xFFFFFFFF 

  h0_temp = (h0_temp + a) & 0xFFFFFFFF
  h1_temp = (h1_temp + b) & 0xFFFFFFFF
  h2_temp = (h2_temp + c) & 0xFFFFFFFF   
  h3_temp = (h3_temp + d) & 0xFFFFFFFF
  h4_temp = (h4_temp + e) & 0xFFFFFFFF
  h5_temp = (h5_temp + f) & 0xFFFFFFFF
  h6_temp = (h6_temp + g) & 0xFFFFFFFF
  h7_temp = (h7_temp + h) & 0xFFFFFFFF
  return h0_temp,h1_temp,h2_temp,h3_temp,h4_temp,h5_temp,h6_temp,h7_temp
def generalized_SHA256(input):
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19
    h0_temp, h1_temp, h2_temp, h3_temp, h4_temp , h5_temp,h6_temp,h7_temp= h0, h1, h2, h3, h4 ,h5,h6,h7 
    length_processed_text = len(preprocessing_input(input))  
    input_temp=preprocessing_input(input); 
    for i in range(length_processed_text // 512):
        if i == 0:
            h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp = Nth_block_output(input_temp[0:512], h0, h1, h2, h3, h4,h5,h6,h7)
        else:    
            h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp = Nth_block_output(input_temp[i * 512:(i + 1) * 512], 
                                                                           h0_temp, h1_temp, h2_temp, h3_temp, h4_temp,h5_temp,h6_temp,h7_temp)

    return ''.join([
        f"{h0_temp:08x}", 
        f"{h1_temp:08x}", 
        f"{h2_temp:08x}", 
        f"{h3_temp:08x}", 
        f"{h4_temp:08x}",
        f"{h5_temp:08x}",
        f"{h6_temp:08x}",
        f"{h7_temp:08x}"
    ])
