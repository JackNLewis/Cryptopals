import sys

# TODO
# Generate all 256 combinations
# Generate frequency histogrmas
# Order based on distance between standard histogram

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

input_string = sys.argv[1]

print(hamming("hello","hallo"))
