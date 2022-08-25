import sys, base64

def decrypt():
    return None

"""
This function generates the new hexstring after being xor'd with a key.

key is an integer which needs to find its correct hex string

"""
def singlexor(hex, key):
    res = ""
    for i in range(int(len(hex)/2)):
        hex_byte = int(hex[(2*i):(2*i)+2],16)
        xor_byte = hex_byte ^ key
        res += chr(xor_byte)
    return res

    
    #have the two strings

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

input_string = "1c0111001f010100061a024b53535009181c"

for i in range(256):
    print(singlexor("1c0111001f010100061a024b53535009181c",i))
