# fuente principal: https://www.rfc-editor.org/rfc/rfc4226
# informacion que añadido a la fuente principal se obtiene más lógica 
#   https://www.rfc-editor.org/rfc/rfc6238
#   https://www.rfc-editor.org/rfc/rfc2104


import argparse
import hashlib
import hmac
import time
import math

parser = argparse.ArgumentParser(description="Generador de contraseñas a partir de un hexadecimal")
parser.add_argument("hex_key", help="Clave hexadecimal de al menos 64 caracteres")
parser.add_argument("-g", dest="save_hex_key", action="store_true" , help="Guarda la clave hexadecimal en un archivo llamado ft_opt.key")
parser.add_argument("-k", dest="new_key", action="store_true", help="Genera una nueva contraseña temporal")

params = parser.parse_args()

print(params.hex_key)
print(params.save_hex_key)
print(params.new_key)

params = parser.parse_args()

def int_a_byte(numero, longitud):
    """Convierte un número entero en una cadena de bytes con una longitud específica"""
    return numero.to_bytes(longitud, byteorder='big')

def byte_a_int(cadena_bytes):
    """Convierte una cadena de bytes en un número entero"""
    return int.from_bytes(cadena_bytes, byteorder='big')

def generar_valor_totp(clave_secreta):
    """Genera un valor TOTP a partir de una clave secreta"""
    ts_number = math.floor(time.time() / 30)
    clave = clave_secreta.encode()
    mensaje = int_a_byte(ts_number, 8)
    valor_hmac = hmac.new(clave, mensaje, hashlib.sha1).digest()
    offset = (valor_hmac[-1]) & 0xf
    key_of_set = byte_a_int(valor_hmac[offset:offset+4]) & 0x7fffffff
    final_key = '{:06d}'.format(key_of_set % 10 ** 6)
    print()
    print(f"ts_number: {ts_number}")
    print(f"clave: {clave}")
    print(f"mensaje: {mensaje}")
    print(f"valor_hmac: {valor_hmac}")
    print(f"offset: {offset}")
    print(f"codigo1: {key_of_set}")
    print(f"codigo2: {final_key}")
    
    return final_key

hex_key = "4573746520657320656c20746578746f20706172612067656e6572617220656c2068657861646563696d616c"
key_decode = bytes.fromhex(hex_key)
print(f"key_decode: {key_decode}")
clave_secreta = key_decode.decode() # reemplazar por tu propia clave secreta
print(f"clave_secreta: {clave_secreta}")
valor_totp = generar_valor_totp(clave_secreta)
print('Tu código TOTP es:', valor_totp)