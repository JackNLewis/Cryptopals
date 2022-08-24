import sys

hex_a, hex_b = sys.argv[1], sys.argv[2]
int_a, int_b = int(hex_a,16),int(hex_b,16)

xor_res = hex(int_a ^ int_b)[2:]

print(xor_res)

