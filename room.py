"""
Module définissant la classe Room, représentant une pièce avec des sorties,
un inventaire et des personnages présents.
"""

class Room:
    """
    Représente une pièce dans un jeu d'aventure.
    Chaque pièce a un nom, une description, des sorties, un inventaire,
    et peut contenir des personnages.
    """

    def __init__(self, name, description):
        """
        Initialise une pièce avec un nom, une description, des sorties et un inventaire vide.

        :param name: Nom de la pièce
        :param description: Description de la pièce
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventary_name = []
        self.inventary = {}
        self.character = {}

    def get_exit(self, direction):
        """
        Retourne la pièce dans la direction donnée si elle existe, sinon None.
    
        :param direction: La direction de la sortie
        :return: La pièce correspondante ou None
        """
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        return None


    def get_exit_string(self):
        """
        Retourne une chaîne décrivant les sorties disponibles de la pièce.
        """
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    def get_long_description(self):
        """
        Retourne une description complète de la pièce, incluant ses sorties.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventary(self):
        """
        Retourne l'inventaire de la pièce.
        """
        return self.inventary

    def add_character(self, character):
        """
        Ajoute un personnage à la pièce.
        
        :param character: Le personnage à ajouter
        """
        self.character[character.name] = character

    def remove_character(self, character):
        """
        Retire un personnage de la pièce.
        
        :param character: Le personnage à retirer
        """
        del self.character[character.name.lower()]