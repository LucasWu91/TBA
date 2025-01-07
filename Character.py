import random

class Character :
    def __init__(self,name,description,current_room,msgs) :
        self.name=name
        self.description=description
        self.current_room=current_room
        self.msgs=msgs

    def __str__(self):
        return f"{self.name} : {self.description} : {self.current_room} : {self.msgs}"
    
    def move(self):
        if random.choice([True,False]):
            self.current_room.character.remove(self)
            new_room=random.choice(list(self.current_room.exits.values()))
            print(f"{self.name} se déplace de {self.current_room.name} vers {new_room.name}")
            self.current_room=new_room
            self.current_room.add_character(self)

            return True
        return False