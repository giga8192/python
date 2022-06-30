from Crypto.Cipher import DES

message1 = "HelloWorld"
padding_len = DES.block_size - len(message1.encode('utf-8')) % DES.block_size
message1 += "0"*padding_len
print(message1)

key = "12345678"
iv = "abcdefgh"
encDES = DES.new(key,DES.MODE_CBC, iv)
encData = encDES.encrypt(message1)

filePath = "encDES.bin"
with open(filePath, "wb") as fout:
    fout.write(encData)

decDES = DES.new(key,DES.MODE_CBC,iv)
decryptText = decDES.decrypt(encData)
print(decryptText)

print("完了")
