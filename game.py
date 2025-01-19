"""
Game class
Ce module contient la classe Game, qui gère la logique principale du jeu.
"""

# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:
    """
    Classe principale du jeu.
    Gère les commandes, les pièces, les objets, les personnages et le joueur.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de la classe Game.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.item = {}
        self.character = {}

    def setup(self):
        """
        Configure les commandes, les pièces, les objets, les personnages
        et les relations entre eux.
        """
        # Configuration des commandes
        help_command = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help_command
        quit_command = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit_command
        go = Command("go", "<direction>: se déplacer dans une direction (N,E,S,O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", "<direction> : retour à la dernière position", Actions.back, 0)
        self.commands["back"] = back
        inventaire = Command("inventaire", "<direction> :affiche l'inventaire",Actions.inventaire,0)
        self.commands["inventaire"] = inventaire
        look = Command('look', "<direction> : affiche les objets de la salle", Actions.look, 0)
        self.commands["look"] = look
        take = Command('take', "<direction> : Prend un objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command('drop', "<direction> : Dépose un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        talk = Command('talk', "<description> : Parle à un personnage", Actions.talk, 1)
        self.commands["talk"] = talk

        # Configuration des pièces
        cellule = Room("Cellule", " dans une cellule, petite pièce sombre avec un lit superposé .")
        self.rooms.append(cellule)
        couloir = Room("Couloir des Cellules", "Un long passage éclairé par une lampe au mur.")
        self.rooms.append(couloir)
        salle_des_gardes = Room("Salle des gardes","Une pièce où les gardes prennent leurs pauses.")
        self.rooms.append(salle_des_gardes)
        cantine = Room("cantine", "Une simple cantine pour se restaurer.")
        self.rooms.append(cantine)
        salle_de_douche = Room("salle de douche", "Salle où les prisonniers se lavent.")
        self.rooms.append(salle_de_douche)
        cour = Room("cour", "Un grand espace libre pour se promener.")
        self.rooms.append(cour)
        bibliotheque = Room("bibliotheque", "Une grande salle pour travailler.")
        self.rooms.append(bibliotheque)
        salle_musculation = Room("salle musculation", "Une grille qui mène à l'extérieur.")
        self.rooms.append(salle_musculation)

        # Objets
        clou = Item("clou", "Permet d'ouvrir la porte de la cellule.", 0.14)
        self.item['clou'] = clou
        lampe_portable = Item("lampe portable", "Éclaire les zones sombres.", 0.850)
        self.item['lampe_portable'] = lampe_portable
        cle = Item("cle", "Ouvre la Grande Porte.", 0.3)
        self.item['cle'] = cle
        couteau = Item("couteau", "Couteau avec une lame assez tranchante .", 1)
        self.item['couteau'] = couteau
        livre = Item("livre", "Permet de passer le temps.", 0.5)
        self.item['livre'] = livre
        halteres = Item("halteres", "Permet aux prisonniers de se muscler.", 8)
        self.item['halteres'] = halteres

        # Objets dans les lieux
        cellule.inventary = {'clou': clou}
        couloir.inventary = {'lampe portable': lampe_portable}
        salle_des_gardes.inventary = {'cle': cle}
        bibliotheque.inventary = {'livre': livre}
        cantine.inventary = {'couteau': couteau}

        # Personnages
        george = Character("george", "un garde", couloir, ["Oh retourne dans ta cellule !"])
        self.character['george'] = george
        sebastien = Character("sebastien", "le prisonnier qui compte s'évader",
                              cellule, [" J'ai quelque chose à te proposer",
                                        "Mais pour cela il va falloir que tu me ramènes un couteau et la cle de la cellule des gardes"])
        self.character['sebastien'] = sebastien

        # Personnages dans les lieux
        couloir.character = {'george': george}
        cellule.character = {'sebastien': sebastien}

        # Exits des pièces
        cellule.exits = {"N": couloir, "S": None, "O": None, "E": None}
        couloir.exits = {"N": salle_des_gardes, "S": cellule, "E": cour,
                        "O": salle_de_douche}
        salle_des_gardes.exits = {"O": None, "S": couloir, "E": None, "N": None}
        cantine.exits = {"N": cour, "S": None, "E": None, "O": None}
        salle_de_douche.exits = {"N": None, "S": None, "E":couloir, "O": None}
        cour.exits = {"S": cantine, "N": salle_musculation, "O": couloir, "E": bibliotheque}
        bibliotheque.exits = {"N": None, "S": None, "E": None, "O": cour}
        salle_musculation.exits = {"S": cour, "N": None, "O": None, "E": None}

        # Joueur et position de départ
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cellule

    def play(self):
        """
        Lance le jeu et maintient la boucle principale jusqu'à la fin.
        """
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string) -> None:
        """
        Traite la commande saisie par le joueur.

        Args:
            command_string (str): La commande saisie par le joueur.
        """
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]
        if command_word not in self.commands.keys():
            print()
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        """
        Affiche le message de bienvenue au joueur.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\n")
        print("Vous ouvrez les yeux lentement... Les murs froids de la cellule vous entourent.")
        print("Une lumière traverse les barreaux de la petite fenêtre au-dessus de vous.")
        print("Votre mission : trouver un moyen de sortir de cette prison.")
        print("Faites les bons choix, et peut-être obtiendrez-vous la liberté.\n")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())


def main():
    """
    Point d'entrée principal pour lancer le jeu.
    """
    Game().play()


if __name__ == "__main__":
    main()
