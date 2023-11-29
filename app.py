from function_polybe import grille, crypt_polybe, decrypt_polybe

def app():
    choice = input("Crypter (C) ou Decrypter (D) ?").upper()

    if choice == "C":
        cle = str(input("Entrer la cle du cryptage: "))
        message = str(input("Entrer le message a crypter:")) 
        print("Message crypte: ", crypt_polybe(message, grille(cle)))

    elif choice == "D":

        cle = str(input("Entrer la cle du decryptage: "))
        message = str(input("Entrer le message a decrypter:")) 
        print("Message decrypte: ", decrypt_polybe(message, grille(cle)))

    else:
        print("Choix non valide ! Veuillez entrer 'C' pour Crypter ou 'D' pour Decrypter ?")

if __name__ == "__app__":
    app()