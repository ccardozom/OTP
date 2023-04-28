
import hmac

msgg = "Python is easy."

key_val = "abcxyzzz"

hmac_one = hmac.new(key=key_val.encode(), msg=msgg.encode(), digestmod="sha1")

message_digest_one = hmac_one.digest()

print("{} - Message Digest One : {}".format(hmac_one.name, message_digest_one))

hmac_two = hmac.new(key=key_val.encode(), digestmod="sha1")

hmac_two.update(bytes(msgg, encoding="utf-8"))

message_digest_two = hmac_two.digest()

print("{} - Message Digest Two : {}".format(hmac_two.name, message_digest_two))

 

hmac_three = hmac.new(key=key_val.encode(), digestmod="sha1")

hmac_three.update(bytes("Programming is fun", encoding="utf-8"))

hmac_three.update(bytes("easy and fun", encoding="utf-8"))

 

message_digest_three = hmac_three.digest()

 

print("{} - Message Digest Three : {}".format(hmac_three.name, message_digest_three))

print("\nMessage Digest Size for 1 : {}, 2 : {} and 3 : {}".format(hmac_one.digest_size, hmac_two.digest_size,hmac_three.digest_size,))

print("Message Block Size for 1 : {}, 2 : {} and 3 : {}".format(hmac_one.block_size, hmac_two.block_size,hmac_three.block_size,))