import base64
from Crypto.Cipher import AES

key = b'This is the super secret key 123'
encrypt_string = b'DTrW2VXjSoFdg0e61fHxJg==&#10'

cipher = AES.new(key, AES.MODE_CBC, b'\x00'*16)

encrypt_string = base64.b64decode(encrypt_string)

decrypt_string = cipher.decrypt(encrypt_string)
print(decrypt_string)