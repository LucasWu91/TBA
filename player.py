# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventary_name=[]
        self.inventary={}

    
    # Define the move method.
    def move(self, direction):
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
    def get_history(self) :
        print("\nVous avez déjà visité les pièces suivantes :")
        for i in range(len(self.history)) :
            print('  - ' + self.history[i].description)
    

    
    def get_inventary(self,game,item):
        objet=game.items[item]
        self.inventary_name.append(objet.name)
        self.inventary[f'{item}']=objet
        print(f"\n Vous avez ramasseé, {objet.name} !\n")

        return True