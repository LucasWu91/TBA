"""
Module actions

Ce module permet de gérer les actions exécutées dans un jeu basé sur des commandes textuelles.
Chaque fonction gère une action spécifique (comme se déplacer, regarder autour de soi, parler, etc.) 
et vérifie que le nombre correct de paramètres a été fourni.
"""
# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.
# The error message is stored in the MSG0 and MSG1 variables
#  and formatted with the command_word variable,
# the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
     
    Represents a collection of static methods that define the actions a player
    can perform in the game.

    This class is designed to provide functionality for processing and executing
    player commands, such as movement or interaction with the game environment.

    Methods:
        go(game, list_of_words, number_of_parameters):
            Moves the player in the specified direction based on the input parameters.
    
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        player = game.player
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        direction = list_of_words[1]

        valid_directions = ["N", "E", "S", "O", "U", "D"]
        if direction in ['n', 'Nord', 'nord', 'NORD']:
            direction = "N"
        if direction in ['o', "Ouest", "ouest", "OUEST"]:
            direction = "O"
        if direction in ['s', "Sud", "sud", "SUD"]:
            direction = "S"
        if direction in ['e', "Est", "est", "EST"]:
            direction = "E"
        if direction in ['u', 'up', 'Up', "UP"]:
            direction = 'U'
        if direction in ['d', "Down", "down", "DOWN"]:
            direction = "D"
        if direction not in valid_directions:
            print(f"\nDirection '{direction}' non reconnue.\n")
            print(game.player.current_room.get_long_description())
            return False
        player.move(direction)
        player.get_history()
        for key, val in game.character.items():
            val.move()
        return True
    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    @staticmethod    
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        Returns:
            bool: True if the command was executed successfully, False otherwise.
        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    @staticmethod
    def back(game, list_of_words, number_of_parameters) :
        """
        Reviens à la pièce précédente.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        player = game.player
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if player.history == []:
            print("\n Vous ne pouvez pas revenir en arrière ! \n")
            return False
        player.current_room = player.history[-1]
        player.history.pop()
        print(player.current_room.get_long_description())
        player.get_history()
        return True
    @staticmethod
    def inventaire(game, list_of_words, number_of_parameters) :
        """
        Affiche l'inventaire du joueur.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        player = game.player
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if player.inventary == {}:
            print("\n Votre inventaire est vide !\n")
            return False
        print("\n Vous disposez des items suivants:")
        for obj in player.inventary.values():
            print(obj)
        print()
        return True
    @staticmethod
    def look(game, list_of_words, number_of_parameters) :
        """
        Affiche le contenu de la pièce actuelle.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if not game.player.current_room.get_inventary() and not game.player.current_room.character.items():
            print("On ne voit rien ici.")
        else:
            print("La pièce contient :")
            for name, item in game.player.current_room.inventary.items():
                print(f" - {item.name} : {item.description}")
            for name, character in game.player.current_room.character.items():
                print(f" - {character.name} : {character.description}")
        return True
    @staticmethod
    def take(game, list_of_words, number_of_parameters) :
        """
        Prend un objet dans la pièce actuelle.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        player = game.player
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if game.player.current_room.inventary == {}:
            print("\n il n'y a rien ici")
            return False
        item = list_of_words[1]
        if item not in game.player.current_room.inventary.keys():
            print("\n Cette objet n'est pas dans cette pièce!\n")
            return False
        objet = game.item[item]
        player.inventary[f'{item}'] = objet
        game.player.current_room.inventary.pop(f"{item}")
        return True
    @staticmethod
    def drop(game, list_of_words, number_of_parameters) :
        """
        Dépose un objet de l'inventaire dans la pièce actuelle.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        player = game.player
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        if player.inventary == {}:
            print("\n il n'y a rien dans votre inventaire")
            return False
        item = list_of_words[1]
        if item not in player.inventary.keys():
            print(f"L'objet '{item}' n'est pas dans votre inventaire.")
            return False
        objet = game.item[item]
        game.player.current_room.inventary[f'{item}'] = objet
        player.inventary.pop(f"{item}")
        return True
    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Parle à un personnage dans la pièce actuelle.

        Args:
            game (Game): L'objet jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendus par la commande.

        Returns:
            bool: True si la commande a été exécutée avec succès, False sinon.

        """
        l = len(list_of_words)
        player = game.player
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        
        # Récupérer le nom du personnage depuis les arguments
        character_name = list_of_words[1].lower()
            # Vérifier si le personnage est dans la pièce actuelle
        if character_name not in player.current_room.character:
                print(f"{character_name.capitalize()} n'est pas dans cette pièce.")
                return False
        # Récupérer le personnage et faire parler
        if character_name=='sebastien' and "cle" in player.inventary and "couteau" in player.inventary :
            print ("Vous êtes désormais libre, votre mission est un succès.")
            game.finished=True
        elif character_name=='george' and "couteau" in player.inventary :
            print ("! Vous êtes capturé sur-le-champ. Mission échouée.")
            game.finished=True
        character = player.current_room.character[character_name]
        print(character.get_msg())  # Appelle la méthode get_msg() sur le personnage
        return True
