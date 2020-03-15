"""Pos.joueur.x = 12
Pos.joueur.y = 7

si la direction est vers la droite:
	si fleche_up appuyée:
		ajouter 1 à pos.joueur.x
	si fleche_down appuyée:
		ajouter -1 à pos.joueur.x
	si fleche_left appuyée:
		ajouter -1 à pos.joueur.y
	si fleche_right appuyée:
		ajouter 1 à pos.joueur.y
"""


posPlayerX = 0
posPlayerY = 0

direction = 'droite'


edit = "▶☐☐☐\n" \
	   "☐☐☐☐\n" \
	   "☐☐☐☐\n"


while True:
	if posPlayerY == 0:
		if posPlayerX == 0:
			edit = "▶☐☐☐\n" \
				   "☐☐☐☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 1:
			edit = "☐▶☐☐\n" \
				   "☐☐☐☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 2:
			edit = "☐☐▶☐\n" \
				   "☐☐☐☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 3:
			edit = "☐☐☐▶\n" \
				   "☐☐☐☐\n" \
				   "☐☐☐☐\n"
	elif posPlayerY == 1:
		if posPlayerX == 0:
			edit = "☐☐☐☐\n" \
				   "▶☐☐☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 1:
			edit = "☐☐☐☐\n" \
				   "☐▶☐☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 2:
			edit = "☐☐☐☐\n" \
				   "☐☐▶☐\n" \
				   "☐☐☐☐\n"
		elif posPlayerX == 3:
			edit = "☐☐☐☐\n" \
				   "☐☐☐▶\n" \
				   "☐☐☐☐\n"
	elif posPlayerY == 2:
		if posPlayerX == 0:
			edit = "☐☐☐☐\n" \
				   "☐☐☐☐\n" \
				   "▶☐☐☐\n"
		elif posPlayerX == 1:
			edit = "☐☐☐☐\n" \
				   "☐☐☐☐\n" \
				   "☐▶☐☐\n"
		elif posPlayerX == 2:
			edit = "☐☐☐☐\n" \
				   "☐☐☐☐\n" \
				   "☐☐▶☐"
		elif posPlayerX == 3:
			edit = "☐☐☐☐\n" \
				   "☐☐☐☐\n" \
				   "☐☐☐▶\n"
	print(edit)
	print('Votre position actuelle : X =', posPlayerX, 'Y =', posPlayerY)
	print('Vous regardez vers la droite')
	sens = str(input('Vers où voullez-vous aller ? (devant, derriere, gauche, droite)'))
	if direction == 'droite':
		if sens == 'devant':
			if posPlayerX <=2:
				posPlayerX = posPlayerX + 1
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			else:
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print("\nAttention ! Il y a du vide ici ! N'y allons pas :)")
		elif sens == 'derriere':
			if posPlayerX >=1:
				posPlayerX = posPlayerX - 1
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			else:
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print("\nAttention ! Il y a du vide ici ! N'y allons pas :)")
		elif sens == 'gauche':
			if posPlayerY >= 1:
				posPlayerY = posPlayerY - 1
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			else:
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print("\nAttention ! Il y a du vide ici ! N'y allons pas :)")
		elif sens == 'droite':
			if posPlayerY <= 1:
				posPlayerY = posPlayerY + 1
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			else:
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print("\nAttention ! Il y a du vide ici ! N'y allons pas :)")
