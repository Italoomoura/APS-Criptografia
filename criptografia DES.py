from des import DesKey
import string, random

chave = input("Digite uma chave: ")

if len(chave) < 8:
    while len(chave) < 8:
        chave += random.choice(string.ascii_letters)
elif len(chave) < 16:
    while len(chave) < 16:
        chave += random.choice(string.ascii_letters)
elif len(chave) < 24:
    while len(chave) < 24:
        chave += random.choice(string.ascii_letters)
else:
    while len(chave) > 24:
        chave = chave[:-1]
        
key = DesKey(chave.encode('latin-1'))

cripto = key.encrypt(bytes(input("Digite uma frase: "), 'latin-1'), padding=True)

print("Sua chave:",chave)
print("Sua criptografia:",cripto)

descriptChave = input("Digite sua chave: ")

if descriptChave != chave:
    print("chave errada!")
else:
    decripto = key.decrypt(cripto, padding=True).decode('latin-1')
    print("Descriptografado:",decripto)
