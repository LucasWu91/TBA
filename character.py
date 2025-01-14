"""
Ce module définit une classe `Character` qui représente un personnage se déplaçant 
dans un espace constitué de pièces et pouvant transmettre des messages.
"""

import random

class Character:
    """
    Représente un personnage qui se déplace entre les pièces et peut transmettre des messages.
    """
    def __init__(self, name, description, current_room, msgs):
        """
        Initialise un personnage avec un nom, une description, 
        une pièce actuelle et une liste de messages.

        :param name: Nom du personnage
        :param description: Description du personnage
        :param current_room: Pièce actuelle du personnage
        :param msgs: Liste des messages associés au personnage
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne du personnage.
        """
        return f"{self.name} : {self.description} : {self.current_room} : {self.msgs}"

    def move(self):
        """
        Déplace le personnage de manière aléatoire vers une pièce adjacente si possible.
        """
        if random.choice([True, False]):
            self.current_room.remove_character(self)
            new_room = random.choice(
                [x for x in list(self.current_room.exits.values()) if x is not None]
            )
            print(f"{self.name} se déplace de {self.current_room.name} vers {new_room.name}")
            self.current_room = new_room
            self.current_room.add_character(self)
            return True
        return False

    def get_msg(self):
        """
        Retourne un message cyclique de la liste des messages du personnage.
        """
        if self.msgs:  # Si la liste des messages n'est pas vide
            msg = self.msgs.pop(0)  # Retire le premier message
            self.msgs.append(msg)  # Le remet à la fin de la liste pour le cycler
            return msg
        return "Ce personnage n'a rien à dire pour le moment."
