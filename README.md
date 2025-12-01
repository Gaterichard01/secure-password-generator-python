# 🔒 Secure Password Generator (Python CLI Tool)



##  Vue d'Ensemble du Projet

Ce projet est un **Générateur de Mots de Passe Sécurisés** développé en Python. Il est conçu comme un outil en ligne de commande (CLI) permettant aux utilisateurs de créer rapidement des mots de passe robustes et hautement personnalisables.

L'objectif principal est d'assurer une **force de mot de passe maximale** en garantissant que chaque mot de passe généré inclut au moins un caractère de chaque type sélectionné (majuscule, minuscule, chiffre, symbole).

---

##  Fonctionnalités Clés

* **Personnalisation de la Longueur :** Définition facile de la longueur souhaitée (`-l`).
* **Contrôle de la Composition :** Possibilité d'exclure des types de caractères (chiffres, symboles, majuscules, minuscules).
* **Robustesse Garanti :** La logique du script assure l'inclusion d'au moins un caractère de chaque catégorie choisie, renforçant l'entropie et la sécurité.
* **Gestion des Arguments :** Utilisation du module standard `argparse` pour une interface utilisateur professionnelle et une aide intégrée.

---

##  Installation et Exécution

### Prérequis

Vous devez avoir **Python 3** installé sur votre système.

### Cloner et Naviguer

Clonez le dépôt et naviguez vers le dossier du projet :

```bash
git clone [https://github.com/Gaterichard01/secure-password-generator-python.git](https://github.com/Gaterichard01/secure-password-generator-python.git)
cd secure-password-generator-python
