from enum import Enum

class WeaponType(Enum):
    Poignard = "poignard"
    Revolver = "revolver"
    Chandelier = "chandelier"
    Corde = "corde"
    Vase = "vase"
    Matraque = "matraque"

killer_weapon = WeaponType.Matraque