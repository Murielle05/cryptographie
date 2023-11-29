# Projet Chiffrement et Déchiffrement Affine

Ce code propose une implementation simple du chiffrement et du dechiffrement affine en utilisant Python.
Le chiffrement affine est une technique de chiffrement par substitution ou chaque lettre dans le texte est remplace par une autre lettre selon une fonction mathematique affine.
Il comporte des fonctions pour vérifier si deux nombres sont premiers entre eux (`pgcd`), calculer l'inverse modulaire (`inverse`), ainsi que les fonctions de chiffrement (`crypt`) et déchiffrement (`decrypt`) utilisant le chiffrement affine.

## Fonctions Affine

### `pgcd(a, b)`

La fonction `pgcd` prend deux entiers `a` et `b` en entrée et retourne leur PGCD (Plus Grand Commun Diviseur).

### `inverse(a, m)`

La fonction `inverse` calcule l'inverse modulaire de `a` modulo `m` en utilisant l'algorithme d'Euclide étendu.

### `crypt(message, cle1, cle2)`

La fonction `crypt` chiffre un message en utilisant le chiffrement affine avec les clés `cle1` et `cle2`.

### `decrypt(message, cle1, cle2)`

La fonction `decrypt` déchiffre un message en utilisant le chiffrement affine avec les clés `cle1` et `cle2`

## Exécution

Le script `app.py` importe les fonctions du fichier `function_affine.py` pour effectuer le chiffrement et le déchiffrement.

### Cryptage
-Choississez l'option C pour crypter et suivez les instructions

### Decryptage
-Choississez l'option D pour decrypter et suivez les instructions

```bash
python app.py





