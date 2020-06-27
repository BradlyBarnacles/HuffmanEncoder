import json
from bitarray import bitarray
import sys

in_filename = sys.argv[1]
out_filename = sys.argv[2]

with open('encode.txt' , 'r') as f:
    encode_dict = json.load(f)


with open(in_filename, 'r') as f:
    text = f.read()
    bit_string = ''
    
    for char in text:
        bit_string += encode_dict[char]

bits = bitarray(bit_string)
with open(out_filename, 'wb') as f:
    bits.tofile(f)

