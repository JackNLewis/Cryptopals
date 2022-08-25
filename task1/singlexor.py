def decrypt():
    return None

"""
This function generates the new hexstring after being xor'd with a key.

key is an integer which needs to find its correct hex string

"""
def singlexor(hex_in, key):
    hex_bytes = bytearray.fromhex(hex_in)
    try:
        return bytes([h^key for h in hex_bytes]).decode("utf-8")
    except:
        return None


"""
This function finds the top 6 most frequently occuring characters in the string s.
"""
def etaoin(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    most_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return most_freq


"""
This functions Calculates the Hamming distance between two
"""
def hamming(a,b):
    if len(a) != len(b):
        return None
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    
    return count/len(a)

input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
for i in range(256):
    print(singlexor(input_string,i), i)