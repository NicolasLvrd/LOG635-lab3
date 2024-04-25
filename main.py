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
        # print("# go to {}".format(piece.get_piece()))
        piece.move_to(robot)

        Analyse_piece(robot, crime_kb, piece, world_objs)
    
    # Conclusions
    COUPABLE = crime_kb.get_suspect()

    print("Pièce du crime : ", crime_kb.get_crime_room())
    print("Arme du crime : ", crime_kb.get_crime_weapon())
    print("Personne victime : ", crime_kb.get_victim())
    print("Heure du crime : ", crime_kb.get_crime_hour())
    print("Meurtrier : ", COUPABLE)
    print("Personnes innocentes : ", crime_kb.get_innocent())

    
    # On cherche la piece du coupable
    for piece in pieces:
        if str(COUPABLE).upper() == piece.get_personne().upper():
            piece.move_to(robot)
            # je dois ramener le coupable a la police ?


def add_clause(robot: cozmo.robot.Robot, crime_kb: CrimeInference, clause_string: str):
    IHM.show_thought(robot, clause_string)
    crime_kb.add_clause(clause_string)

    
def Analyse_piece(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece, world_objs):
    # Cozmo cherche dans la piece son nom, l'arme et la personne
    piece.look_around(robot, world_objs)

    # Ajout des faits à la base de connaissances
    expr = crime_kb.add_clause_to_fol([f"Le {piece.get_arme()} est dans le {piece.get_piece()}"], 'grammars/arme_piece.fcfg')
    IHM.show_thought(robot, expr)

    expr = crime_kb.add_clause_to_fol([f"{piece.get_personne()} est dans le {piece.get_piece()}"], 'grammars/personne_piece.fcfg')
    IHM.show_thought(robot, expr)
    
    try:
        robot.abort_all_actions(True)
    except :
        pass
    
    if VICTIME == piece.get_personne():
        # on apprend que la personne est morte
        expr = crime_kb.add_clause_to_fol([f"{piece.get_personne()} est morte"], 'grammars/personne_morte.fcfg')
        IHM.show_thought(robot, expr)
        
        victime_question(robot, crime_kb, piece)
    
    else:
        # on apprend que la personne est vivante
        expr = crime_kb.add_clause_to_fol([f"{piece[2]} est vivant"], 'grammars/personne_vivant.fcfg')
        IHM.show_thought(robot, expr)

        suspect_question(robot, crime_kb, piece)
    

def victime_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    heure = IHM.ask_text(robot, "A quelle heure est morte la victime ?")
    crime_kb.add_clause_to_fol([heure], './grammars/personne_morte_heure.fcfg')

    questions = [
        ["Est-ce que la victime a des marques au cou ?", "cou"],
        ["Est-ce que la victime a des marques d'incision ?","incision"],
        ["Est-ce que la victime a des marques de coupure ?","coupure"],
        ["Est-ce que la victime a des marques de balle ?","balle"],
        ["Est-ce que la victime a des ecchymoses ?","ecchymose"],
        ["Est-ce que la victime a des marques de contusion ?","contusion"],
    ]
    current = 0

    while not IHM.ask_yes_no(robot, questions[current][0]):
        current += 1
        
        if current == len(questions):
            print ("La victime n'a pas de marques, ERROR")
            exit(0)
        

    crime_kb.add_clause_to_fol(f"{piece.get_personne()} a des marques de {questions[current][1]}", './grammars/personne_marque.fcfg')


def suspect_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    ou = IHM.ask_text(robot, "t'as tu vu quelque chose tanto ?")
    crime_kb.add_clause_to_fol([ou], './grammars/personne_piece_heure.fcfg')

def init_piece():
    return [Piece(room) for room in RoomType]


if __name__ == '__main__':
    cozmo.run_program(main, use_3d_viewer=True)