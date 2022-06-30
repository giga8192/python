from bitarray import bitarray

bits = bitarray(endian="big")
bits.frombytes(b"\x00\x01\x02\x03")
print(bits)

bits2 = bitarray("0101")
print(bits2)

bits3 = bits+ bits2
print(bits3)

# 1の個数
print(bits3.count(1))
