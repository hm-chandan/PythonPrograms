import base64


encoded = base64.b64encode( bytes("sachin", "utf-8") )
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)



encoded = base64.b64encode(b"sachin")
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)
