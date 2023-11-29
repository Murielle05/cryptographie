# Chiffrement et Déchiffrement Polybe

Ce projet propose une implémentation du chiffrement et du déchiffrement en utilisant la grille de Polybe. La structure du code est divisée en deux fichiers principaux : `function_polybe.py`, qui contient les fonctions pour la grille et les opérations de chiffrement, et `app.py`, le script principal pour utiliser ces fonctions.

## Fonctions Polybe

### `grille(cle)`

La fonction `grille` prend une clé en entrée, la formate, et crée la grille de Polybe en utilisant cette clé.

### `position_letter(letter, grille_polybe)`

La fonction `position_letter` trouve la position d'une lettre dans la grille de Polybe.

### `crypt_polybe(message, grille_polybe)`

La fonction `crypt_polybe` chiffre un message en utilisant la grille de Polybe.

### `decrypt_polybe(message, grille_polybe)`

La fonction `decrypt_polybe` déchiffre un message en utilisant la grille de Polybe.

## Utilisation dans `app.py`

Le script `app.py` importe les fonctions du fichier `function_polybe.py` pour effectuer le chiffrement et le déchiffrement. L'utilisateur peut choisir entre crypter et décrypter en répondant à une invitation.

## Exécution

Pour l'execution dans le script `app.py`. Choisissez l'option "C" pour crypter et "D" pour décrypter.

```bash
python app.py
