import json
from bitarray import bitarray
from bitstring import ConstBitStream
import sys


in_filename = sys.argv[1]
out_filename = sys.argv[2]

with open('decode.txt', 'r') as f:
    deccode_list = json.load(f)


bits = ConstBitStream(filename=in_filename)

text = ''
list_de = deccode_list
for bit in bits:
    list_de = list_de[bit]
    if isinstance(list_de, str):
        text += list_de
        list_de = deccode_list

with open(out_filename, 'w') as f:
    f.write(text)
