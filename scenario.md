
# Solution
- Pièce du crime : Cuisine
- Arme du crime : Couteau
- Personne victime : Noir
- Heure du crime : 12
- Meurtrier : Rouge
- Personnes innocentes : Bleu, Vert, Jaune, Mauve, Noir

# Faits
## État initial
### Personnages 
- Rouge
- Bleu
- Vert
- Jaune
- Mauve
- Noir

### Pièces
- Cuisine
- Hall
- Galerie
- Bureau
- Salon
- Chambre

### Armes
- Corde
- Couteau
- Fusil
- Marteau
- Vase
- Pistolet

### Arme_Marque
- Corde | Cou
- Couteau | Incision
- Fusil | Balle
- Marteau | Ecchymose
- Vase | Coupure
- Pistolet | Trou

### EstMort
- Noir

### EstVivant
- Rouge
- Bleu
- Vert
- Jaune
- Mauve

## Via obervations
### Arme_Piece
- Corde | Hall
- Couteau | Cuisine
- Fusil | Galerie
- Marteau | Bureau
- Vase | Chambre
- Pistolet | Salon

### Personne_Piece
- Rouge  | Chambre
- Bleu | Salon
- Vert | Bureau
- Jaune | Galerie
- Mauve | Hall
- Noir | Cuisine

## Via Questions
### HeureCrime
- 12

### Personne_Marque
- Noir | Cou

### Menaces
- Rouge | Noir | 9

### Declare
- Vert | Rouge | Cuisine | 11
- Rouge | Bleu | Salon | 12
- Bleu | Jaune | Chambre | 12
- Rouge | Vert | Hall | 12

### Personne_Piece_Heure
- Mauve | Salon | 12

# Inférence
- Victime(Noir)
- Innocent(Noir; Bleu; Vert; Jaine; Mauve)
- PieceCrime(Cuisine)
- ArmeCrime(Corde)
- Mobile(Rouge)
- Personne_Piece_Heure((Rouge, Cuisine, 11); (Bleu, Salon, 12); (Jaune, Chambre 12); (Mauve, Salon; 12); (Vert, Hall, 12))
- Alibi(Bleu, Jaune, Mauve, Vert)
- Suspect(Rouge)