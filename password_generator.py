import random
import string
import argparse
import sys # Pour la gestion propre des sorties d'erreur

def generate_secure_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Génère un mot de passe sécurisé en garantissant qu'au moins un caractère 
    de chaque type requis est inclus.

    Args:
        length (int): Longueur totale du mot de passe.
        use_upper (bool): Inclure des majuscules.
        use_lower (bool): Inclure des minuscules.
        use_digits (bool): Inclure des chiffres.
        use_symbols (bool): Inclure des symboles.

    Returns:
        str: Le mot de passe généré.
    """
    
    # 1. Définition des ensembles de caractères et des exigences
    char_sets = []
    must_include = []

    if use_upper:
        char_sets.append(string.ascii_uppercase)
        # Garanti qu'au moins un caractère de ce type sera présent
        must_include.append(random.choice(string.ascii_uppercase))
    
    if use_lower:
        char_sets.append(string.ascii_lowercase)
        must_include.append(random.choice(string.ascii_lowercase))
        
    if use_digits:
        char_sets.append(string.digits)
        must_include.append(random.choice(string.digits))
        
    if use_symbols:
        # On peut choisir des symboles plus spécifiques/sécurisés si besoin
        char_sets.append(string.punctuation) 
        must_include.append(random.choice(string.punctuation))

    # Vérification: Si aucune option n'est sélectionnée ou si la longueur est insuffisante
    if not char_sets:
        print("Erreur : Veuillez sélectionner au moins un type de caractère.", file=sys.stderr)
        sys.exit(1)
        
    if length < len(must_include):
        print(f"Erreur : La longueur ({length}) doit être au moins égale au nombre de types de caractères requis ({len(must_include)}).", file=sys.stderr)
        sys.exit(1)

    # 2. Création de l'ensemble de caractères total
    all_characters = "".join(char_sets)
    
    # 3. Génération des caractères restants
    # Le nombre de caractères à générer est la longueur totale moins les caractères déjà garantis
    remaining_length = length - len(must_include)
    
    # Choisir les caractères restants aléatoirement
    other_characters = random.choices(all_characters, k=remaining_length)
    
    # 4. Assemblage et mélange
    final_password_list = must_include + other_characters
    random.shuffle(final_password_list)
    
    return "".join(final_password_list)

def main():
    """
    Fonction principale pour gérer les arguments de la ligne de commande.
    """
    parser = argparse.ArgumentParser(
        description="Générateur de mots de passe sécurisés et personnalisables.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Exemples d'utilisation :
  python password_generator.py -l 14 --no-sym --no-dig
  python password_generator.py -l 20 
"""
    )
    
    # Argument pour la longueur du mot de passe
    parser.add_argument(
        '-l', '--length', 
        type=int, 
        default=16, 
        help='Spécifie la longueur du mot de passe (par défaut: 16)'
    )
    
    # Arguments pour exclure des types de caractères (utiliser store_false=True)
    parser.add_argument(
        '--no-upper', 
        dest='use_upper', 
        action='store_false', 
        help="Exclut les lettres MAJUSCULES."
    )
    parser.add_argument(
        '--no-lower', 
        dest='use_lower', 
        action='store_false', 
        help="Exclut les lettres minuscules."
    )
    parser.add_argument(
        '--no-dig', 
        dest='use_digits', 
        action='store_false', 
        help="Exclut les CHIFFRES (0-9)."
    )
    parser.add_argument(
        '--no-sym', 
        dest='use_symbols', 
        action='store_false', 
        help="Exclut les SYMBOLES (!@#$...)."
    )
    
    args = parser.parse_args()
    
    # Génération et affichage du mot de passe
    password = generate_secure_password(
        length=args.length,
        use_upper=args.use_upper,
        use_lower=args.use_lower,
        use_digits=args.use_digits,
        use_symbols=args.use_symbols
    )
    
    print("-" * 50)
    print(f"🔑 Mot de Passe Sécurisé ({len(password)} caractères) : **{password}**")
    print("-" * 50)
    
if __name__ == '__main__':
    main()