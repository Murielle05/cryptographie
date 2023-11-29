def grille(cle):
# Convertir la cle en majuscules et supprimer les doublons
    cle_formate =[]
    for char in cle:
        if char in cle.upper() and char not in cle_formate:
          cle_formate.append(char)

    for char in cle.upper():
        if char not in cle and char not in cle_formate:
          cle_formate.append(char)
# Creer l'alphabet sans la cle
    alphabet ="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabet ="".join(filter(lambda x: x not in cle, alphabet))

# Concatener la cle et l'alphabet pour former la grille
   
    alphabet_grille ="".join(cle_formate) + alphabet

# Creer la grille de polybe
    grille_polybe = [list(alphabet_grille[i:i+5])for i in range(0,25,5)]

    return grille_polybe

def position_letter(letter, grille_polybe):
    letter = letter.replace("J","I")
    for i in range(5):
        for j in range(5):
            if grille_polybe[i][j]==letter:
                return i, j
    return None

def crypt_polybe(message, grille_polybe):
    crypt_message=""
    for letter in message.upper():
        if letter.isalpha() :
            position = position_letter(letter, grille_polybe)
            if position:
                crypt_message += str(position[0] + 1) + str(position[1] + 1)
        else:
            crypt_message += letter
    return crypt_message

def decrypt_polybe(message, grille_polybe):
    decrypt_message=""
    position = [int(double) for double in message if double.isdigit()]
    for i in range(0, len(position), 2):
        if i+1 < len(position):
            row, column= position[i] - 1, position[i+1]-1
            if 0 <= row < 5 and 0 <= column < 5:
                decrypt_message += grille_polybe[row][column]+' '
            else:
                decrypt_message += '?'
        else:
            decrypt_message += '?'
    return decrypt_message
