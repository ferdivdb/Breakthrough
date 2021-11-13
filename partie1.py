'''

	Breakthrough

'''
alphabet =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z']
num = '0123456789'
char = '<>'

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
	board=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==n-1 or i==n-2: board[i][j]=1 
            if i==0 or i==1: board[i][j]=2
    return board



def print_board(board : List[List[int]]):
	'''

		Affiche le plateau de jeu, comme spécifié dans la section 1.3.


	'''
	ligne = ""
    horizontale = "  "
    n = len(board[0])
    for i in range(n):
        for j in range(n):
            horizontale = horizontale+"- "
            if(board[i][j]==2): ligne = ligne + "B "
            if (board[i][j] == 1): ligne = ligne + "W "
            if (board[i][j] == 0): ligne = ligne + ". "
        if i==0: print("  "+horizontale)
        if n-i <= 9 : print(str(n-i)+"  "+"|"+" "+ligne+"|")
        if n-i > 9 : print(str(n-i)+" "+"|"+" "+ligne+"|")
        ligne=""
        if i==n-1:
            lettreaph = ""
            for k in range(n): lettreaph = lettreaph + alphabet[k]+" "
            print("    " + horizontale)
            print("    " + lettreaph)

        horizontale = ""
	


def winner(board : List[List[int]]):
	'''

		Étant donné le plateau de jeu board, vérifie si l’un des deux joueurs 
		a gagné. Renvoie 1 si le joueur blanc a gagné ; 2 si le joueur noir a gagné ; 
		None si la partie n’est pas encore terminée.

	'''
	n=len(board[0])
    for j in range(n):
        if board[0][j]==1:
            return 1
        elif board[n-1][j]==2:
            return 2
        else:
            return None
	


def is_in_board(n : int, pos : Tuple[int, int]):
	'''

		Renvoie True si la position pos est valide pour un plateau de taille n × n ; 
		renvoie False sinon. La position pos est une paire d’indices (i, j). 
		Par exemple, sur un plateau 7 × 7, la position (0,5) est valide mais (1,7) 
		ne l’est pas.

	'''
	if (pos[0]>=0 and pos[0]<n) and (pos[1]>=0 and pos[1]<n):
        return True
    else:
        return False
	


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
	#     moove = input()
#     i = 0
#     if len(moove) in range(5, 8):
#         for index in moove:
#             flag = True if moove[i] in alphabet or moove[i] in num or moove[i] in char and moove[0] in alphabet and moove[3] in alphabet or moove[4] in alphabet and moove[2] in char or moove[3] in char and moove[1] in num[1:3]  else False
#             if moove[2] in char: # a1<a1 or a1<a10
#                 # if len(moove) == 6 : 
#                 #     if moove[2] != '<': 
#                 #         input_moove()
#                 #     else:
#                 #         flag == True
#                 # else:
#                 #     x = int(moove[1])
#                 #     y = int(moove[4])
#                 #     if x > y :
#                 #         if moove[2] != '>': 
#                 #             input_moove()
#                 #         else:
#                 #             flag == True
#                 #     elif x == y:
#                 #         input_moove()
#                 #     else:
#                 #         if moove[2] != '<': 
#                 #             input_moove()
#                 #         else:
                            
#             flag = True if moove[4] in num[1:3] and moove[5] in num[0:7] else False 
#             if moove[3] in char:  # a10<a1 or a10<a10
#                 flag = True if moove[2] in num[0:7] and moove[6] in num[0:7] and moove[1] in num[1:3] and moove[5] in num[1:3] and moove[4] in alphabet  else False
#             else:
#                 flag = False    
#             #flag = True if   else False
#             i+=1
#         if flag == False : input_moove() 
#         else : return True
#     else:
#         input_moove()
    moove = input()
    if len(moove) in range(5,8):
        for index in moove:
        if index in alphabet or index in num or index in char:
                if moove[0] in alphabet and moove[1] in num:
                    if len(moove) == 5:
                        flag = True if moove[2] in char and moove[3] in alphabet and moove[4] in num else False
                    elif len(moove) == 6:
                        if moove[2] in char:
                            if moove[2] == '<':
                                if moove[4] in num[1:3]:
                                    flag == True if moove[5] in num[0:7] else False
                                else:
                                    input_moove()
                            else:
                                input_moove()
                        else:
                            flag = True if moove[2] in num[0:7] else False
                            if flag == True:
                                
                            else:
                                input_moove()
                    else:
                        #
                    if flag == False:
                        input_moove()
                else:
                    input_moove()
            else:
                input_moove()
    else:
        input_moove()
input_moove()
	


def extract_pos(n : int, str_pos : str):
	'''

		Tuple[int, int] ou None Traduit une position str_pos donnée en format 
		notation échecs (ex : ’b5’) en la paire d’indices (i, j) correspondante. 
		Le paramètre n correspond à la taille du plateau.

	'''
	num = int(str_pos[1])
    i = n - num
    if str_pos[0] not in alphabet:
        return None
    else:
        k=0
        for lettre in alphabet:
            k+=1
            if str_pos[0]==lettre:
                j=k-1
                return (i,j)
	


def check_move(board : List[List[int]], player : int, str_move : str):
	'''

		Prend en entrée le plateau de jeu et un mouvement proposé par l’un des 
		joueurs selon le format décrit à la Section 1.5 (ex : ’a2>a3’), 
		renvoie True si le coup est conforme aux règles du jeu et renvoie False sinon.
		
	'''
	 n=len(board[0])
    if (str_move[1]<=n and str_move[1]>0) and (str_move[4]<=n and str_move[1]>0):
        if player==1:
            if (str[0]>=str[3] and str[1]<str[4]) or (str[0]<=str[3] and str[1]<str[4]):
                return True
            else:
                return False
        elif player==2:
            if (str[0]>=str[3] and str[1]>str[4]) or (str[0]<=str[3] and str[1]>str[4]):
                return True
            else:
                return False
    else:
        return False

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






