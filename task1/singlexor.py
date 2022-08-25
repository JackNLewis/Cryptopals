
import sys
from math import inf

"""
A dictionary representing the frequency of letters in the standard english language
"""
english_freq = {
    'a': 8.2389258,    'b': 1.5051398,    'c': 2.8065007,    'd': 4.2904556,
    'e': 12.813865,    'f': 2.2476217,    'g': 2.0327458,    'h': 6.1476691,
    'i': 6.1476691,    'j': 0.1543474,    'k': 0.7787989,    'l': 4.0604477,
    'm': 2.4271893,    'n': 6.8084376,    'o': 7.5731132,    'p': 1.9459884,
    'q': 0.0958366,    'r': 6.0397268,    's': 6.3827211,    't': 9.1357551,
    'u': 2.7822893,    'v': 0.9866131,    'w': 2.3807842,    'x': 0.1513210,
    'y': 1.9913847,    'z': 0.0746517
}

"""
This function decrypts the given cyper text using frequency analysis
"""
def decrypt(s):
    min_diff, res = inf, ""
    for i in range(256):
        val = single_xor(s,i)
        if val == None:
            continue
        f = generate_freq(val)
        diff = compute_freq_distance(english_freq,f)
        if diff < min_diff:
            min_diff = diff
            res = val
    return res

"""
This function generates the new hexstring after being xor'd with a key.
"""
def single_xor(hex_in, key):
    hex_bytes = bytearray.fromhex(hex_in)
    try:
        return bytes([h^key for h in hex_bytes]).decode("utf-8")
    except:
        return None

"""
This function generates the frequncy histogram of a given string
"""
def generate_freq(s):
    freq = {'a': 0,    'b': 0,    'c': 0,    'd': 0,
    'e': 0,    'f': 0,    'g': 0,    'h': 0,
    'i': 0,    'j': 0,    'k': 0,    'l': 0,
    'm': 0,    'n': 0,    'o': 0,    'p': 0,
    'q': 0,    'r': 0,    's': 0,    't': 0,
    'u': 0,    'v': 0,    'w': 0,    'x':0,
    'y': 0,    'z': 0}

    for c in s:
        cl = c.lower()
        if cl in freq:
            freq[cl] += 1
    for c in freq:
        freq[c] = freq[c] / 26.0
    return freq

"""
This functions calculates the average absolute distance between 2 given frequencys
"""
def compute_freq_distance(a,b):
    if len(a) != len(b):
        return -1
    count = 0.0
    for c in a:
        count += abs(a[c] - b[c])
    return count/len(a)


# Decrypt the first argument

input_str = sys.argv[1]

print(decrypt(input_str))

