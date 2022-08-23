import sys
import base64

hex_in = sys.argv[1]
hex_bytes = bytes.fromhex(hex_in)
b64_string = base64.b64encode(hex_bytes).decode()

print(b64_string)