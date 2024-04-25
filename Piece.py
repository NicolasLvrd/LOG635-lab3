from cozmo_utils.map.room import RoomType, go_to_room 
from cozmo_utils.map.people import Peopletype, VICTIME
import cozmo_utils.cozmo as cutils
import cozmo

class Piece:

    def __init__(self,  _piece: RoomType, _arme = "Unknow", _personne = "Unknow"):
        self.arme = _arme
        self.piece = _piece
        self.personne =  _personne

    
    # Cozmo cherche dans la pièce son nom, l'arme et la personne
    def look_around(self, robot: cozmo.robot.Robot, world_data):
        outputs = cutils.look_for_information(robot, world_data)

        for out in outputs:
            if isinstance(out.type, Peopletype):
                self.personne = out.type.value

                if VICTIME == self.personne:
                    cutils.roll_victim(robot, out)

            else:
                self.arme = out.type.value

        #attendre qu'il est tout finis
        robot.abort_all_actions(True)

    def move_to(self,robot):
        go_to_room(robot, self.piece)
    
    def get_piece(self):
        return self.piece.value[0]
    
    def get_personne(self):
        return self.personne
    
    def get_arme(self):
        return self.arme
