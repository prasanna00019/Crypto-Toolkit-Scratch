def reverse_bits_in_byte(b):
    return int('{:08b}'.format(b)[::-1], 2)

def str_to_keccak_bits(msg):
    return ''.join(format(reverse_bits_in_byte(b), '08b') for b in msg)
def keccak_pad(msg_bits, r, suffix_bits):
    m = list(msg_bits)
    m += list(suffix_bits)
    pad_len = (-len(m) - 1) % r
    m += ['0'] * pad_len
    m.append('1')
    return ''.join(m)

def string_to_state_array(S, x=5, y=5, w=64):
    """
    Converts a string S of b = x * y * w bits to a 3D state array A[x][y][w].
    Each A[x][y][z] is a bit (0 or 1).
    """
    if len(S) != x * y * w:
        raise ValueError("Length of input S must be x * y * w bits")

    A = [[[0 for z in range(w)] for y_ in range(y)] for x_ in range(x)]

    for i in range(x):
        for j in range(y):
            for k in range(w):
                A[i][j][k] = int(S[w * (5 * j + i) + k])

    return A

def state_array_to_string(A, x=5, y=5, w=64):
    """
    Converts a 3D state array A into a string S as per Keccak specification.
    """
    Lane_i_j = [['' for _ in range(y)] for _ in range(x)]  # 5x5 matrix of empty strings

    for i in range(x):
        for j in range(y):
            for k in range(w):
                # integer bit to string before concatenation
                Lane_i_j[i][j] += str(A[i][j][k])

    plane_j = ['' for _ in range(y)]  # one string for each plane j

    for j in range(y):
        for i in range(x):
            plane_j[j] += Lane_i_j[i][j]

    S = ''.join(plane_j)  # concatenate Plane(0) || Plane(1) || ...
    return S
def theta(A, w=64):
    """
    Keccak Theta step: modifies the state array A in-place based on the Theta transformation.

    Args:
        A: 3D state array A[x][y][z] where x, y in [0..4], z in [0..w-1]
        w: lane size (e.g., 64 for SHA3-512)

    Returns:
        A′: New state array after applying theta step.
    """
    #Compute C[x][z]
    C = [[0] * w for _ in range(5)]
    for x in range(5):
        for z in range(w):
            C[x][z] = A[x][0][z]
            for y in range(1, 5):
                C[x][z] ^= A[x][y][z]

    # Compute D[x][z]
    D = [[0] * w for _ in range(5)]
    for x in range(5):
        for z in range(w):
            D[x][z] = C[(x - 1) % 5][z] ^ C[(x + 1) % 5][(z - 1) % w]

    A_prime = [[[0] * w for _ in range(5)] for _ in range(5)]
    for x in range(5):
        for y in range(5):
            for z in range(w):
                A_prime[x][y][z] = A[x][y][z] ^ D[x][z]

    return A_prime

def rho(A, w=64):
    """
    Keccak Rho step: performs bitwise rotations on the lanes of A according to fixed offsets.

    Args:
        A: 3D state array A[x][y][z], where x, y in [0..4], z in [0..w-1]
        w: lane size (e.g., 64 for SHA3-512)

    Returns:
        A_prime: new state array after applying rho step.
    """
    A_prime = [[[0] * w for _ in range(5)] for _ in range(5)]

    for z in range(w):
        A_prime[0][0][z] = A[0][0][z]

    x, y = 1, 0

    for t in range(24):
        offset = ((t + 1) * (t + 2)) // 2

        for z in range(w):
            rotated_index = (z - offset) % w
            A_prime[x][y][z] = A[x][y][rotated_index]

        x, y = y, (2 * x + 3 * y) % 5

    return A_prime
def pi(A, w=64):
    """
    Keccak Pi step: rearranges the lanes.

    Args:
        A: 3D state array A[x][y][z], where x, y in [0..4], z in [0..w-1]
        w: lane size

    Returns:
        A_prime: new state array after applying pi step.
    """
    A_prime = [[[0] * w for _ in range(5)] for _ in range(5)]

    for x in range(5):
        for y in range(5):
            for z in range(w):
                A_prime[x][y][z] = A[(x + 3 * y) % 5][x][z]

    return A_prime
def chi(A, w=64):
    """
    Keccak Chi step: applies non-linear mixing of bits within each row.

    Args:
        A: 3D state array A[x][y][z], where x, y in [0..4], z in [0..w-1]
        w: lane size

    Returns:
        A_prime: new state array after applying chi step.
    """
    A_prime = [[[0] * w for _ in range(5)] for _ in range(5)]

    for x in range(5):
        for y in range(5):
            for z in range(w):
                A_prime[x][y][z] = A[x][y][z] ^ ((A[(x + 1) % 5][y][z] ^ 1) & A[(x + 2) % 5][y][z])

    return A_prime
def rc_bit(t):
    if t % 255 == 0:
        return 1

    R = ['1', '0', '0', '0', '0', '0', '0', '0']  # '10000000'

    for i in range(1, t % 255 + 1):
        R = ['0'] + R  # Prepend 0 to make it 9 bits

        # XOR operations (bitwise xor with R[8])
        R[0] = str(int(R[0]) ^ int(R[8]))
        R[4] = str(int(R[4]) ^ int(R[8]))
        R[5] = str(int(R[5]) ^ int(R[8]))
        R[6] = str(int(R[6]) ^ int(R[8]))

        R = R[:8]  # Truncate to 8 bits

    return int(R[0])

def iota(A, ir, w=64):
    """
    Keccak Iota step: adds round constant to A[0][0]

    Args:
        A: 3D state array A[x][y][z], where x, y in [0..4], z in [0..w-1]
        ir: round index (0 to 23)
        w: lane size

    Returns:
        A_prime: state array with round constant added to A[0][0]
    """
    A_prime = [[[A[x][y][z] for z in range(w)] for y in range(5)] for x in range(5)]

    RC = [0] * w
    # l = int.bit_length(w) - 1  # log2(w)
    l=6

    for j in range(l + 1):
        bit_position = (1 << j) - 1
        RC[bit_position] = rc_bit(j + 7 * ir)

    for z in range(w):
        A_prime[0][0][z] ^= RC[z]

    return A_prime
def Rnd(A, ir):
    """
    One round of the Keccak-f permutation.

    Args:
        A: 2D state array A[x][y], where x, y in [0..4], each element is a w-bit integer.
        ir: round index (0 to 23)

    Returns:
        A: State array after applying one round.
    """
    A = theta(A,64)
    A = rho(A)
    A = pi(A)
    A = chi(A)
    A = iota(A, ir)
    return A
def KECCAK_p_1600_24(S):
    A = string_to_state_array(S)
    for ir in range(24):
        A = Rnd(A, ir)
    return state_array_to_string(A)
def sponge(f, P, r, d):
    n = len(P) // r
    blocks = [P[i*r:(i+1)*r] for i in range(n)]
    c = 1600 - r
    S = '0' * 1600
    for Pi in blocks:
        Pi_padded = Pi + '0'*c
        S = bin(int(S, 2) ^ int(Pi_padded, 2))[2:].zfill(1600)
        S = f(S)
    Z = ''
    while len(Z) < d:
        Z += S[:r]
        if len(Z) >= d:
            break
        S = f(S)
    return Z[:d]
def bin_to_hex_keccak(bits):
    out = []
    for i in range(0, len(bits), 8):
        b = bits[i:i+8]
        if len(b) < 8:
            b = b.ljust(8, '0')
        out.append(reverse_bits_in_byte(int(b, 2)))
    return ''.join('{:02x}'.format(x) for x in out)
def keccak_hash(msg, r, d, suffix_bits):
    msg_bin = str_to_keccak_bits(msg)
    padded_bits = keccak_pad(msg_bin, r, suffix_bits)
    digest_bits= sponge(KECCAK_p_1600_24, padded_bits, r, d)
    return bin_to_hex_keccak(digest_bits)
def sha3_256(msg):
    return keccak_hash(msg, 1088, 256, '0110')
def sha3_512(msg):
    return keccak_hash(msg, 576, 512, '0110')
def sha3_384(msg):
    return keccak_hash(msg, 832, 384, '0110')
def sha3_224(msg):
    return keccak_hash(msg, 1152, 224, '0110')
def shake128(msg, outbits):
    return keccak_hash(msg, 1344, outbits, '11111')
def shake256(msg, outbits):
    return keccak_hash(msg, 1088, outbits, '11111')
def keccak_512(msg):
    return keccak_hash(msg, 576, 512, '1')
def keccak_256(msg):
    return keccak_hash(msg, 1088, 256, '1')
def keccak_384(msg):
    return keccak_hash(msg, 832, 384, '1')
def keccak_224(msg):
    return keccak_hash(msg, 1152, 224, '1')
