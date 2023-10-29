import hashlib

def calculate_md5(data):
    md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash

input_data = "Hello World"
md5 = calculate_md5(input_data.encode('utf-8'))
print("MD5 Hash of the input data is: ", md5)
