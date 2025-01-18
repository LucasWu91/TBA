"""
Module contenant une classe Player permettant de modéliser un joueur dans un jeu.
"""

class Player():
    """
    Classe représentant un joueur.

    Attributs :
        name (str) : Nom du joueur.
        current_room (Room) : Salle actuelle dans laquelle se trouve le joueur.
        history (list) : Liste des salles déjà visitées.
        inventary_name (list) : Liste des noms des objets dans l'inventaire.
        inventary (dict) : Dictionnaire contenant les objets de l'inventaire.
    """

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventary_name=[]
        self.inventary={}

    # Define the move method.
    def move(self, direction):
        """Permet de déplacer le joueur dans une direction donnée."""
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        self.history.append(self.current_room)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """Affiche l'historique des salles visitées par le joueur."""
        print("\nVous avez déjà visité les pièces suivantes :")
        for i in range(len(self.history)):
            print('  - ' + self.history[i].description)
