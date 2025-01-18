# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.item={}
        self.character={}
    
    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back=Command("back", "<direction> : retour à la dernière position", Actions.back,0 )
        self.commands["back"] = back
        inventaire=Command("inventaire", "<direction> : affiche l'inventaire", Actions.inventaire,0 )
        self.commands["inventaire"] = inventaire
        look=Command('look', "<direction> : affiche les objets de la salle", Actions.look,0 )
        self.commands["look"] = look
        take=Command('take', "<direction> : Prend un objet", Actions.take,1 )
        self.commands["take"] = take
        drop=Command('drop', "<direction> : Dépose un objet", Actions.drop,1 )
        self.commands["drop"] = drop
        talk=Command('talk',"<description> : Parle à un personnage", Actions.talk,1)
        self.commands["talk"] = talk

        # Setup rooms
        cellule = Room("Cellule","Une petite pièce sombre avec un lit cassé et une porte en métal.")
        self.rooms.append(cellule)
        couloir=Room("Couloir des Cellules","Un long passage éclairé par une lampe au mur.")
        self.rooms.append(couloir)
        salle_des_gardes = Room("Salle des gardes","Une pièce où les gardes prennent leurs pauses.")
        self.rooms.append(salle_des_gardes)
        cantine = Room("cantine", "Une simple cantine pour se restaurer.")
        self.rooms.append(cantine)
        salle_de_douche = Room("salle de douche", "Salle où les prisonniers se lavent.")
        self.rooms.append(salle_de_douche)
        cour = Room("cour", "Un grand espace libre pour se promener.")
        self.rooms.append(cour)
        bibliotheque=Room("bibliotheque","Une grande salle pour travailler.")
        self.rooms.append(bibliotheque)
        salle_musculation = Room("salle musculation", "Une grille qui mène à l'extérieur.")
        self.rooms.append(salle_musculation)

        #Objets

        clou=Item("clou", "Permet d'ouvrir la porte de la cellule.",0.14)  
        self.item['clou']=clou
        lampe_portable = Item("lampe portable", "Éclaire les zones sombres.",0.850)
        self.item['lampe_portable']=lampe_portable
        cle = Item("cle", "Ouvre la Grande Porte.", 0.3)
        self.item['cle']=cle
        couteau = Item("couteau", "Couteau avec une lame assez tranchante .",1)
        self.item['couteau']=couteau
        livre = Item("livre", "Permet de passer le temps.",0.5)
        self.item['livre']=livre
        halteres = Item("halteres", "Permet aux prisonniers de se muscler.",8)
        self.item['halteres']=halteres
        


        #Objets dans les lieux

        cellule.inventary={'clou':clou}
        couloir.inventary={'lampe portable':lampe_portable}
        salle_des_gardes.inventary={'cle':cle}
        bibliotheque.inventary={'livre':livre}
        cantine.inventary={'couteau':couteau}

        
        #Personnages
        George = Character("George", "un garde", couloir, ["Oh retourne dans ta cellule !"])
        self.character['george']=George
        Sebastien = Character("Sebastien", " le prisonnier qui compte s'évader", cellule, [" J'ai quelque chose à te proposer"])
        self.character['sebastien']=Sebastien

        #Personngaes dans les lieux
        couloir.character={'george': George}
        cellule.character={'sebastien': Sebastien}

        
        # Create exits for rooms

        cellule.exits = {"N": couloir,"S": None,
                          "O": None, "E": None}
        couloir.exits = {"N": salle_des_gardes, "S": cellule,
                        "E": salle_musculation, "O": salle_de_douche}
        salle_des_gardes.exits = {"O": couloir, "S": None,
                                  "E": None, "N": None}
        cantine.exits = {"N": salle_musculation, "S": None, "E":None, "O": cour}
        salle_de_douche.exits = {"N": bibliotheque, "S": None, "E":couloir, "O": None}
        cour.exits = {"S": salle_musculation, "N": None, "O": None, "E": cantine}
        bibliotheque.exits = {"N": None, "E": None, "O": None, "S":salle_de_douche}
        salle_musculation.exits = {"S": cour, "N": None, "O": couloir, "E":None}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = cellule

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player and show the history after each command
            self.process_command(input("> "))

        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print()
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()