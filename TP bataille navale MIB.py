-> jeu de bataille navale

un joueur humain
un adversaire numérique (IA)


->joueur humain

dessiner une grille de 10x10 
les bateaux ce place aléatoirement
lorsque tous les bateaux sont placés, on peut autoriser le jeu à commencer


 ->adversaire numérique (IA)

dessiner une grille 10x10 cases côté ordi
les bateaux ce place aléatoirement
lorsque tous les bateaux sont placés, on peut lancer la boucle du jeu


->la boucle du jeu

joueur joue :

joueur clique sur grille ordi
ordi tire au hasard un emplacement dans la grille du joueur
si emplacement cliqué != bateau alors raté, signaler "raté !"
si cliqué=bateau alors touché signalé "coulé !"
retirer bateau de la liste des bateaux encore actifs
IA joue (son tour) 


la partie se termine lorsque tous les bateaux d'un adversaire ont été coulés (liste bateaux  == 0)


#def placé bateau :
#    def definir la grille :
#        def joué au hazard:
#            def joué avec une tackique: 
#definir les variables des bateaux (placer les bateaux)
# affichage de la grille jeu(10*10)


from random import randint
print("BATAILLE NAVAL")

board = []

for x in range(10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print((" ").join(row))

board2 = []

for x in range(10):
    board2.append(["O"] * 10)

def print_board2(board2):
    for row in board2:
        print((" ").join(row))
        
board3 = []

for x in range(10):
    board3.append(["O"] * 10)

def print_board3(board3):
    for row in board3:
        print((" ").join(row))
        
board4 = []

for x in range(10):
    board4.append(["O"] * 10)

def print_board4(board3):
    for row in board4:
        print((" ").join(row))        

print("Jouons a la bataille naval")
print_board(board)
print_board2(board2)
print_board3(board3)
print_board4(board4)

#stockage du bateau

def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)
def random_row2(board2):
    return randint(0, len(board2) - 1)
def random_col2(board2):
    return randint(0, len(board2[2]) - 1)
def random_row3(board3):
    return randint(0, len(board3) - 1)
def random_col3(board3):
    return randint(0, len(boar3[3]) - 1)
def random_row4(board4):
    return randint(0, len(board4) - 1)
def random_col4(board4):
    return randint(0, len(boar4[4]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
ship_row2 = random_row2(board2)
ship_col2 = random_col2(board2)
ship_row3 = random_row3(board3)
ship_col3 = random_col3(board3)
ship_row4 = random_row4(board4)
ship_col4 = random_col4(board4)

print("C'est le tour du joueur "+str(joueur))


for turn in range(50):
    
    print ("Turn"), turn
    guess_row = int(input("rentre le numeros de ligne comrpris entre 0 et 9:"))
    guess_col = int(input("rentre le numeros de colonne entre 0 et 9: "))
    print("Vous avez joué la case ("guess_row","guess_col")")

    if guess_row == ship_row and guess_col == ship_col:
        print("bien joué tu as coulé mon bateau")
        0=0+1
        break
    else:
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print("Oups, tu n'as pas respecter les conditions.")
        elif(board[guess_row][guess_col] == "X"):
            print("tu as deja joué cette case")
        else:
            print("tu as loupé le navire")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("tu as perdu")
    turn =+ 1
    print_board(board)
    
    
 ## Fiche de travail
 
 ##     https://docs.google.com/document/d/1n7DuU4ZgGg-6WWbIESdyV5RcOtVwAdN0RtNgfVlAzB8/edit   ##
  
    
    
