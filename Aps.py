from tkinter import *
from Crypto.Cipher import DES

# Função para esconder e mostrar Frames
def forget(item1, item2):
    item1.forget()
    item2.pack()
def retrieve(item1, item2):
    item1.pack()
    item2.forget()

# Função para codificar DES
chave = "12345678"
nonce = ""
tag = ""

def descod(chave, msg):
    global result
    if len(chave) == 8:
        key = chave.encode('ascii')
        cipher = DES.new(key, DES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
        result.set(str(ciphertext))
        return nonce, ciphertext, tag
    else:
        result.set("Chave Incorreta!")

def desdecod(nonce, ciphertext, tag):
    global result
    key = chave.encode('ascii')
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext.encode("iso-8859-8"))
    print(ciphertext)
    print(plaintext)
    print(plaintext.decode('iso-8859-8'))
    
    try:
        cipher.verify(tag)
        print(plaintext.decode('ascii'))
    except:
        return False
    
    if not plaintext:
        print('Message is corrupted!')
    else:
        print(f'Plain text: {plaintext}')

def test(chave, msg):
    global nonce, tag
    nonce, ciphertext, tag = descod(chave, msg)
    return nonce, ciphertext, tag

# menu
menu = Tk()
menu.title("Criptografia")
menu.geometry("300x250+500+250")

# Frame do menu principal
principal = Frame(menu, highlightthicknes=3)
principal.pack()

# botão DES
f1 = Frame(principal, highlightthicknes=3)
f1.pack()
btn = Button(f1, text = "DES", command = lambda: retrieve(des, principal))
btn.pack()

# DES
# Frame da Criptografia DES
des = Frame(menu, highlightbackground="red", highlightthicknes=3)
des.forget()

# label
label1 = Label(des, text = "Chave atual: "+chave)
label1.pack()

# label
label = Label(des, text = "Digite a Frase a ser Codificada!")
label.pack()

# Text box
txtcod = Entry(des)
txtcod.pack()

# botão
btn = Button(des, text = "Codificar", command = lambda: test(chave, str(txtcod.get())))
btn.pack()


# label
label1 = Label(des, text = "Digite a Frase a ser Decodificada!")
label1.pack()

# Text box
textbox2 = Entry(des)
textbox2.pack()

# botão
btn1 = Button(des, text = "Decodificar", command = lambda: desdecod(nonce, textbox2.get(), tag))
btn1.pack()


# label
result = StringVar()
resultado = Label(des, textvariable=result)
resultado.pack()

# botão voltar
voltar = Button(des, text = "Voltar", command = lambda: forget(des, principal))
voltar.pack()

menu.mainloop()
