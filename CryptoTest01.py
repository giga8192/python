import string
import random

from Crypto.Cipher import AES

# 対象文字列
plaintext = 'Pythonのpycryptoによる文字列の暗号化・復号化'
print(f'対象文字列：{plaintext}')

print(f'AESブロックサイズ：{AES.block_size}')
print(f'ASCII文字：{string.ascii_letters}')

# AESブロックサイズ分のランダムなASCII文字列を作成する
key = ''.join(
    [random.choice(string.ascii_letters) for _ in range(AES.block_size)])
print(f'key: {key}')

# 初期ベクトル(initialization vector)を生成
iv = ''.join(
    [random.choice(string.ascii_letters) for _ in range(AES.block_size)])
print(f'iv: {iv}')

print('===== 暗号化 =====')
# 暗号化用オブジェクトの準備
cipher = AES.new(key, AES.MODE_CBC, iv)
# バイト数がブロックサイズの倍数になるように詰め物(padding)の長さを計算する
padding_len = AES.block_size - len(plaintext.encode('UTF-8')) % AES.block_size
# 対象文字列にpadding長だけ文字列を追加する
plaintext += chr(padding_len) * padding_len
print(f'暗号化対象文字列：{plaintext}')
print(f'暗号化対象文字列バイト長：{len(plaintext.encode("UTF-8"))}')
# 文字列を暗号化する
cipher_text = cipher.encrypt(plaintext)
print(f'暗号化文字列：{cipher_text}')

print('===== 復号化 =====')
# 復号化用オブジェクトの準備
cipher_dec = AES.new(key, AES.MODE_CBC, iv)
# 復号化を実施
decrypted_text = cipher_dec.decrypt(cipher_text)
print(f'復号化直後：{decrypted_text.decode()}')
decrypted_text = decrypted_text[:-decrypted_text[-1]]
print(f'padding文字列除去：{decrypted_text.decode()}')

# --------------------DES------------------------
from Crypto.Cipher import DES


DesKey = "abcdefgh" # パリティビットは無視される
iv2 = "".join([random.choice(string.ascii_letters) for _ in range(DES.block_size)])
plainText2 = "helloworld"
# padding_lenは8バイトの倍数にするための調整
padding_len = DES.block_size - len(plainText2.encode("UTF-8")) % DES.block_size
plainText2 += chr(padding_len) * padding_len

# 暗号用オブジェクト
cipherDES = DES.new(DesKey, DES.MODE_CBC, iv2)
print("平文{0}".format(plainText2))
cipherText2 = cipherDES.encrypt(plainText2)
print("暗号文{0}".format(cipherText2))

#復号用オブジェクト(暗号用とは分けないとだめ。オブジェクトはステートフル)
cipherDESDec = DES.new(DesKey, DES.MODE_CBC,iv2)
decryptedText2 = cipherDESDec.decrypt(cipherText2)
print("復号文{0}".format(decryptedText2))

# -------------------RC4-----------------------
from Crypto.Cipher import ARC4
key = "abcdefghijklmn"
plainText3 = "HelloWorld"
print("平文:{0}".format(plainText3))
cipherARC4 = ARC4.new(key)
cipherText3 = cipherARC4.encrypt(plainText3)
print("暗号文]{0}".format(cipherText3))

#復号用オブジェクト
decryptARC4 = ARC4.new(key)
decryptText3 = decryptARC4.decrypt(cipherText3)
print("復号文{0}".format(decryptText3))


