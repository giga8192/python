from Crypto.Cipher import DES
from bitarray import bitarray
from binascii import b2a_hex

# baseStrは7文字で
def GenerateDESKey(passData:bytes):
    startBits = bitarray(endian="big")
    startBits.frombytes(passData)
    bits = bitarray()
    for i in range(0,8):
        tmp = startBits[7*i:7*(i+1)]
        if (tmp.count(1) % 2) ==1:
            bits += (tmp + bitarray("1"))
        else:
            bits += (tmp + bitarray("0"))
    return bits.tobytes()

def LM_Hash(password:str):
    # \x00をつなげて14文字にする
    passData = bytes(password.upper(),"ascii") + b"\x00"*(14-len(password))
    key1 = GenerateDESKey(passData[0:7])
    key2 = GenerateDESKey(passData[7:14])

    plain = "KGS!@#$%"
    objDES1 = DES.new(key1, DES.MODE_ECB)
    enc1 = objDES1.encrypt(plain)
    
    objDES2 = DES.new(key2, DES.MODE_ECB)
    enc2 = objDES2.encrypt(plain)
    return enc1 + enc2        

plainPassword = "P@ssw0rd"
print(plainPassword)
print(b2a_hex(LM_Hash(plainPassword)))
