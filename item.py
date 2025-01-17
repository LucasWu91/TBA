class Item:
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"


if __name__ == "__main__":
    clou=Item("clou", "Permet d'ouvrir la porte de la cellule.",0.14)  
    print(clou)
    lampe_portable = Item("lampe portable", "Éclaire les zones sombres.",0.850)
    print(lampe_portable)
    cle = Item("cle", "Ouvre la Grande Porte.", 0.3)
    print(cle)
    couteau = Item("couteau", "Couteau avec une lame assez tranchante .",1)
    print(couteau)
    livre = Item("livre", "Permet de passer le temps.",0.5)
    print(livre)
    halteres = Item("halteres", "Permet aux prisonniers de se muscler.",8)
    print(halteres)