import hmac
import hashlib

message = b'Hello World!'
key = b'secret'

hmac_sha1 = hmac.new(key, message, hashlib.sha1)
hex_digest = hmac_sha1.hexdigest()

print(hex_digest)
