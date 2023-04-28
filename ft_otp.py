import time
import math
import base64
import hmac
from hashlib import sha1
time_step = 30
hex_array_size = 16
key = b"acin ofel eTno icad nuF"


""" import argparse

parser = argparse.ArgumentParser(description="Generador de contraseñas a partir de un hexadecimal")
parser.add_argument("hex_key", help="Clave hexadecimal de al menos 64 caracteres")
parser.add_argument("-g", dest="save_hex_key", action="store_true" , help="Guarda la clave hexadecimal en un archivo llamado ft_opt.key")
parser.add_argument("-k", dest="new_key", action="store_true", help="Genera una nueva contraseña temporal")

params = parser.parse_args()

print(params.hex_key)
print(params.save_hex_key)
print(params.new_key)

params = parser.parse_args() """

def get_number_from_time():
    time_in_seconds = time.time()
    number_of_step = time_in_seconds / time_step
    return math.floor(number_of_step)


""" def str_add_zero(str, new_len, value):
    return value*(new_len - len(str)) + str

def create_array(str, elem_size):
    return [str[i:i+elem_size] for i in range(0, len(str), elem_size)] """

ts_number = get_number_from_time()
msj = "hola que tal"
hex_msj = msj.encode().hex() #esto es solo para prueba de concepto, se supone que nos pasan el hexadecimal del mensaje

msj_bytearray = bytearray.fromhex(hex_msj)

number = ts_number.to_bytes(8, byteorder='big', signed=False)

hashed = hmac.new(msj_bytearray, number ,sha1) #key: esto tiene que ser un bytesarray, hex_mej: tambien tiene que ser un bytesarray, sha1: el tipo de encriptacion que vamos a utilizar para generar el hash


hex_hash = hashed.digest().hex()
print(hex_hash)

lista_pares = []
[lista_pares.append(hex_hash[i:i+2]) for i in range(0, len(hex_hash), 2)]  

index = lista_pares[-1][-1]
for_bits = ord(index)

print(index)
print(for_bits)
#index = int(hex_hash[-1])