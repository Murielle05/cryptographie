# Verifier si a et b sont premiers entre eux
def pgcd(a:int,b:int)->int:
    while(b != 0):
        temp = b
        b = a % b
        a = temp
    return a

def inverse(a:int, m:int)-> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m 
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def crypt(message:str,cle1:int,cle2:int)-> str:
    liste=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    crypt_message = ""

    for letter in message:
        if letter.isalpha():
            x =  liste.index(letter.upper())
            y = (cle1*x+cle2)%26
            crypt_letter = liste[y]
            crypt_message += crypt_letter if letter.isupper() else crypt_letter.lower()
        else:
            crypt_message += letter

    return crypt_message


def decrypt(message: str, cle1: int, cle2: int)-> str:
    liste=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    cle1_inv = inverse(cle1, 26)
    decrypt_message = ""

    for letter in message:
        if letter.isalpha():
            y =  liste.index(letter.upper())
            x = (cle1_inv*(y-cle2))%26
            decrypt_letter = liste[x]
            decrypt_message += decrypt_letter if letter.isupper() else decrypt_letter.lower()
        else:
            decrypt_message += letter

    return decrypt_message
