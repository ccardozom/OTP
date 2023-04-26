import argparse

parser = argparse.ArgumentParser(description="Generador de contraseñas a partir de un hexadecimal")
parser.add_argument("hex_key", help="Clave hexadecimal de al menos 64 caracteres")
parser.add_argument("-g", dest="save_hex_key", action="store_true" , help="Guarda la clave hexadecimal en un archivo llamado ft_opt.key")
parser.add_argument("-k", dest="new_key", action="store_true", help="Genera una nueva contraseña temporal")

params = parser.parse_args()

print(params.hex_key)
print(params.save_hex_key)
print(params.new_key)