
# Solution
- Pièce du crime : Cuisine
- Arme du crime : Matraque
- Personne victime : Mauve
- Heure du crime : 12
- Meurtrier : Rouge
- Personnes innocentes : Bleu, Vert, Jaune, Blanc, Mauve


# Faits
## État initial
### Personnages 
- Rouge
- Bleu
- Vert
- Jaune
- Blanc
- Mauve

### Pièces
- Cuisine
- Hall
- Galerie
- Bureau
- Salon
- Chambre

### Armes
- Corde
- Matraque
- Chandelier
- Poignard
- Vase
- Revolver

### Arme_Marque
- Corde | Cou
- Matraque | Ecchymose
- Chandelier | Contusion
- Poignard | Incision
- Vase | Coupure
- Revolver | Balle

### EstMort
- Mauve

### EstVivant
- Rouge
- Bleu
- Vert
- Jaune
- Blanc

## Via obervations
### Arme_Piece
- Corde | Hall
- Matraque | Cuisine
- Chandelier | Galerie
- Poignard | Bureau
- Vase | Chambre
- Revolver | Salon

### Personne_Piece
- Rouge  | Chambre
- Bleu | Salon
- Vert | Bureau
- Jaune | Galerie
- Blanc | Hall
- Mauve | Cuisine

## Via Questions
### HeureCrime
- 12

### Personne_Marque
- Mauve | Cou

### Menaces
- Rouge | Mauve | 9

### Declare
- Vert | Rouge | Cuisine | 11
- Rouge | Bleu | Salon | 12
- Bleu | Jaune | Chambre | 12
- Rouge | Vert | Hall | 12

### Personne_Piece_Heure
- Blanc | Salon | 12

# Inférence
- Victime(Mauve)
- Innocent(Mauve; Bleu; Vert; Jaine; Blanc)
- PieceCrime(Cuisine)
- ArmeCrime(Corde)
- Mobile(Rouge)
- Personne_Piece_Heure((Rouge, Cuisine, 11); (Bleu, Salon, 12); (Jaune, Chambre 12); (Blanc, Salon; 12); (Vert, Hall, 12))
- Alibi(Bleu, Jaune, Blanc, Vert)
- Suspect(Rouge)