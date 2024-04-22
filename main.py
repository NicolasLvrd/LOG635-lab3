import cozmo
from Piece import Piece
from cozmo_utils.map.room import RoomType
from CrimeInference import CrimeInference
import IHM as IHM
import cozmo_utils.cozmo as cutils
from cozmo_utils.map.people import VICTIME

def main(robot: cozmo.robot.Robot):

    #init world
    cutils.place_walls(robot)
    world_objs = cutils.init_object_dict(robot)
    cutils.update_world_objects(robot, world_objs)
    print("========== Monde initialisé !=================\n")

    # Initialisation de la base de connaissances
    crime_kb = CrimeInference()

    # Initialisation des pièces
    pieces = init_piece()

    # Cozmo cherche dans chaque piece
    for piece in pieces:
        print("# go to {}".format(piece.get_piece()))
        piece.move_to(robot)

        Analyse_piece(robot, crime_kb, piece, world_objs)
    
    # Conclusions
    print("Pièce du crime : ", crime_kb.get_crime_room())
    print("Arme du crime : ", crime_kb.get_crime_weapon())
    print("Personne victime : ", crime_kb.get_victim())
    print("Heure du crime : ", crime_kb.get_crime_hour())
    print("Meurtrier : ", crime_kb.get_suspect())
    print("Personnes innocentes : ", crime_kb.get_innocent())



def add_clause(robot: cozmo.robot.Robot, crime_kb: CrimeInference, clause_string: str):
    IHM.show_thought(robot, clause_string)
    crime_kb.add_clause(clause_string)

    
def Analyse_piece(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece, world_objs):
    # Cozmo cherche dans la piece son nom, l'arme et la personne
    piece.look_around(robot, world_objs)

    # Ajout des faits à la base de connaissances
    add_clause(robot, crime_kb, 'Arme_Piece('  + piece.get_arme() + ',' + piece.get_piece() +')')
    add_clause(robot, crime_kb, 'Personne_Piece(' + piece.get_personne() + ',' + piece.get_piece() +')')

    try:
        robot.abort_all_actions(True)
    except :
        pass
    
    if VICTIME == piece.get_personne():
        victime_question(robot, crime_kb, piece)
    
    else:
        suspect_question(robot, crime_kb, piece)
    

def victime_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    heure = IHM.ask_text(robot, "A quelle heure est morte la victime ?")
    crime_kb.add_clause_to_fol([heure], './grammars/personne_morte_heure.fcfg')

    marque = IHM.ask_text(robot, "Est-ce que la victime a des marques ?")   
    crime_kb.add_clause_to_fol([marque], './grammars/personne_marque.fcfg')


def suspect_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    ou = IHM.ask_text(robot, "t'étais tu ou tanto ?")
    crime_kb.add_clause_to_fol([ou], './grammars/personne_piece_heure.fcfg')

def init_piece():
    return [Piece(room) for room in RoomType]


if __name__ == '__main__':
    cozmo.run_program(main, use_3d_viewer=True)