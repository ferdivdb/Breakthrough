'''

	Breakthrough

'''

def main(n : int):
	'''

		La fonction principale du programme. Elle contient d’abord une phase 
		d’initialisation du plateau de jeu, de taille n × n, puis une boucle 
		qui permet successivement aux joueurs de proposer des coups, 
		jusqu’à ce que la condition de victoire soit satisfaite pour l’un des 
		joueurs et que la partie s’arrête. Cette fonction doit aussi afficher 
		l’état courant du plateau à chaque tour.

	'''
	return

def init_board(n : int):
	'''

		Construit et renvoie la liste de listes qui représente le plateau 
		de taille n × n de départ, selon l’encodage spécifié dans la Section 1.4.

	'''
	

def print_board(board : List[List[int]]):
	'''

		Affiche le plateau de jeu, comme spécifié dans la section 1.3.


	'''
	return


def winner(board : List[List[int]]):
	'''

		Étant donné le plateau de jeu board, vérifie si l’un des deux joueurs 
		a gagné. Renvoie 1 si le joueur blanc a gagné ; 2 si le joueur noir a gagné ; 
		None si la partie n’est pas encore terminée.

	'''
	return

def is_in_board(n : int, pos : Tuple[int, int]):
	'''

		Renvoie True si la position pos est valide pour un plateau de taille n × n ; 
		renvoie False sinon. La position pos est une paire d’indices (i, j). 
		Par exemple, sur un plateau 7 × 7, la position (0,5) est valide mais (1,7) 
		ne l’est pas.

	'''
	return

def input_move():
	'''

		Demande au joueur d’entrer un coup suivant le format décrit à la Section 
		1.5. Redemande un nouvel input tant que ce qui est entré par le joueur 
		n’est pas interprétable comme un coup. Cette fonction ne doit pas vérifier 
		que le coup est valide au sens des règles du jeu, ni que les cases décrites 
		dans le coup sont bien dans le plateau. Ici on se contente de vérifier que la 
		chaîne de caractères entrée par le joueur corresponde au format attendu, 
		c-à-d : une lettre minuscule, suivi d’un ou deux chiffres, suivi du caractère >, 
		suivi d’une lettre minuscule, suivi enfin d’un ou deux chiffres.

	'''
	return

def extract_pos(n : int, str_pos : str):
	'''

		Tuple[int, int] ou None Traduit une position str_pos donnée en format 
		notation échecs (ex : ’b5’) en la paire d’indices (i, j) correspondante. 
		Le paramètre n correspond à la taille du plateau.

	'''
	return


def check_move(board : List[List[int]], player : int, str_move : str):
	'''

		Prend en entrée le plateau de jeu et un mouvement proposé par l’un des 
		joueurs selon le format décrit à la Section 1.5 (ex : ’a2>a3’), 
		renvoie True si le coup est conforme aux règles du jeu et renvoie False sinon.
		
	'''
	return

def play_move(board : List[List[int]], move : Tuple[Tuple[int, int], Tuple[int, int]], player : int):
	'''

		Modifie le plateau de jeu board en effectuant un coup donné pour un joueur 
		donné. Cette fonction suppose que le coup respecte les règles du jeu 
		(cette fonction sera donc utilisée une fois que la validité du coup entré 
		par le joueur aura été vérifiée). Le coup est encodé sous forme d’une 
		paire de positions ((i,j), (i’, j’)), (i,j) étant la po- sition de départ 
		et (i’,j’) la position d’arrivée, chaque position étant une paire d’indices.

	'''
	return

if __name__ = '__main__':
	main()






