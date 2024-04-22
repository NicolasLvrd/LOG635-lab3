class Piece:

    def __init__(self, _piece = "Unknow", _arme = "Unknow", _personne = "Unknow"):
        self.arme = _arme
        self.piece = _piece
        self.personne =  _personne

    
    # Cozmo cherche dans la pièce son nom, l'arme et la personne
    def look_around(self):
        pass

    def move_to(self):
        pass
    
    def get_piece(self):
        return self.piece
    
    def get_personne(self):
        return self.personne
    
    def get_arme(self):
        return self.arme
