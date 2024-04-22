import cozmo
from Piece import Piece
from CrimeInference import CrimeInference
from IHM import IHM

def main(robot: cozmo.robot.Robot):

    # Initialisation de la base de connaissances
    crime_kb = CrimeInference()

    # Initialisation des pièces
    pieces = init_piece()

    # Cozmo cherche dans chaque piece
    for piece in pieces:
        piece.move_to()

        Analyse_piece(robot, crime_kb, piece)
    pass


def add_clause(robot: cozmo.robot.Robot, crime_kb: CrimeInference, clause_string: str):
    IHM.show_thought(robot, clause_string)
    crime_kb.add_clause()

    
def Analyse_piece(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    # Cozmo cherche dans la piece son nom, l'arme et la personne
    piece.look_around(robot)

    # Ajout des faits à la base de connaissances
    add_clause(robot, crime_kb, 'Arme_Piece('  + piece.get_arme() + ',' + piece.get_piece() +')')
    add_clause(robot, crime_kb, 'Personne_Piece(' + piece.get_personne() + ',' + piece.get_piece() +')')

    if crime_kb.get_victim() == piece.get_personne():
        victime_question(robot, crime_kb, piece)
    
    else:
        suspect_question(robot, crime_kb, piece)
    

def victime_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    heure = IHM.ask_text(robot, "A quelle heure est morte la victime ?")
    crime_kb.add_clause_to_fol(heure, './grammars/personne_morte_heure.fcfg')

    marque = IHM.ask_text(robot, "Est-ce que la victime a des marques ?")   
    crime_kb.add_clause_to_fol(marque, './grammars/personne_marque.fcfg')


def suspect_question(robot: cozmo.robot.Robot, crime_kb: CrimeInference, piece: Piece):
    ou = IHM.ask_text(robot, "t'étais tu ou dans les 2 dernières heures ?")
    crime_kb.add_clause_to_fol(ou, './grammars/personne_piece_heure.fcfg')

def init_piece():
    return [Piece.Piece() for i in range(4)]


