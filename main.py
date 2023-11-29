from function_affine import pgcd, crypt, decrypt

def main():
    choice = input("Crypter (C) ou Decrypter (D) ?").upper()

    if choice == "C":
        message = input("Entrer le message a crypter: ")
        cle1 = int(input("Entrer la premiere cle du cryptage: "))

        if pgcd(cle1, 26) == 1:
            cle2 = int(input("Entrer la deuxieme cle du cryptage: "))
            crypt_message = crypt(message, cle1, cle2)
            print("Message crypte: ",crypt_message)
        else:
            print("Le nombre", cle1,"n'est pas premier avec 26 !")

    elif choice == "D":
        crypt_message = input("Entrer le message a decrypter: ")
        cle1 = int(input("Entrer la premiere cle du decryptage: "))

        if pgcd(cle1, 26) == 1:
            cle2 = int(input("Entrer la deuxieme cle du decryptage: "))
            decrypt_message = decrypt(crypt_message,cle1,cle2)
            print('Message decrypte:',decrypt_message)
        else:
            print('Le nombre',cle1,"n'est pas premier avec 26 !")
    else:
        print("Choix non valide ! Veuillez entrer 'C' pour Crypter ou 'D' pour Decrypter ?")

if __name__ == "__main__":
    main()