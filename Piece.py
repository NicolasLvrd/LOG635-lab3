from cozmo_utils.map.room import RoomType, go_to_room 
from cozmo_utils.map.people import Peopletype, VICTIME
import cozmo_utils.cozmo as cutils

class Piece:

    def __init__(self,  _piece: RoomType, _arme = "Unknow", _personne = "Unknow"):
        self.arme = _arme
        self.piece = _piece
        self.personne =  _personne

    
    # Cozmo cherche dans la pièce son nom, l'arme et la personne
    def look_around(self, robot, world_data):
        outputs = cutils.look_for_information(robot, world_data)

        for out in outputs:
            if isinstance(out, Peopletype):
                self.personne = out.value

                if VICTIME == self.personne:
                    cutils.roll_victim(robot, out)
            
            else:
                self.arme = out.value

    def move_to(self,robot):
        go_to_room(robot, self.piece)
    
    def get_piece(self):
        return self.piece
    
    def get_personne(self):
        return self.personne
    
    def get_arme(self):
        return self.arme
