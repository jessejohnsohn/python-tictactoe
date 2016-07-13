

print('Welcome to the game!\n')

class Game():
    def __init__(self):
        self.python_board = [[1,2,3],[4,5,6],[7,8,9]]
        self.used = []
        self.z = 0

        print("X's turn\n")
        
        for c in range(0,3):
            print('|'.join(map(str, self.python_board[c])))

        self.turn()

    def newgame(self):
        self.python_board = [[1,2,3],[4,5,6],[7,8,9]]
        self.used = []
        self.z = 0

        print("X's turn\n")
        
        for c in range(0,3):
            print('|'.join(map(str, self.python_board[c])))

        self.turn()

    def catsgame(self):
        if len(self.used) == 9:
            return True
        else:
            return False
    def winning_combinationsX(self):
        if (str(self.python_board[0][0]) + str(self.python_board[0][1]) + str(self.python_board[0][2])) == 'XXX':
            return True
        if (str(self.python_board[1][0]) + str(self.python_board[1][1]) + str(self.python_board[1][2])) == 'XXX':
            return True
        if (str(self.python_board[2][0]) + str(self.python_board[2][1]) + str(self.python_board[2][2])) == 'XXX':
            return True
        if (str(self.python_board[1][0]) + str(self.python_board[1][1]) + str(self.python_board[1][2])) == 'XXX':
            return True
        if (str(self.python_board[0][0]) + str(self.python_board[1][0]) + str(self.python_board[2][0])) == 'XXX':
            return True
        if (str(self.python_board[0][1]) + str(self.python_board[1][1]) + str(self.python_board[2][1])) == 'XXX':
            return True
        if (str(self.python_board[0][2]) + str(self.python_board[1][2]) + str(self.python_board[2][2])) == 'XXX':
            return True
        if (str(self.python_board[2][0]) + str(self.python_board[1][1]) + str(self.python_board[0][2])) == 'XXX':
            return True
        if (str(self.python_board[0][0]) + str(self.python_board[1][1]) + str(self.python_board[2][2])) == 'XXX':
            return True
        else:
            return False
        
    def winning_combinationsO(self):
        if (str(self.python_board[0][0]) + str(self.python_board[0][1]) + str(self.python_board[0][2])) == 'OOO':
            return True
        if (str(self.python_board[1][0]) + str(self.python_board[1][1]) + str(self.python_board[1][2])) == 'OOO':
            return True
        if (str(self.python_board[2][0]) + str(self.python_board[2][1]) + str(self.python_board[2][2])) == 'OOO':
            return True
        if (str(self.python_board[1][0]) + str(self.python_board[1][1]) + str(self.python_board[1][2])) == 'OOO':
            return True
        if (str(self.python_board[0][0]) + str(self.python_board[1][0]) + str(self.python_board[2][0])) == 'OOO':
            return True
        if (str(self.python_board[0][1]) + str(self.python_board[1][1]) + str(self.python_board[2][1])) == 'OOO':
            return True
        if (str(self.python_board[0][2]) + str(self.python_board[1][2]) + str(self.python_board[2][2])) == 'OOO':
            return True
        if (str(self.python_board[2][0]) + str(self.python_board[1][1]) + str(self.python_board[0][2])) == 'OOO':
            return True
        if (str(self.python_board[0][0]) + str(self.python_board[1][1]) + str(self.python_board[2][2])) == 'OOO':
            return True
        else:
            return False
        
        
    def board(self):
        if self.z % 2 == 1:    
            self.python_board[self.y][self.x]='X'
        else:
            self.python_board[self.y][self.x]='O'

        print()

        for c in range(0,3):
            print('|'.join(map(str, self.python_board[c])))

        if self.winning_combinationsX() == True:
            print('X wins! \n')
            self.playagain = str(input('Play again?')).strip()
            if self.playagain.lower() == 'yes' or 'y' or 'okay':
                self.newgame()
            else:
                quit()
        if self.winning_combinationsO() == True:
            print('O wins! \n')
            self.playagain = str(input('Play again?')).strip()
            if self.playagain.lower() == 'yes' or 'y' or 'okay':
                self.newgame()
            else:
                quit()
        if self.catsgame() == True:
            print("Cats's Game!")
            self.playagain = str(input('Play again?')).strip()
            if self.playagain.lower() == 'yes' or 'y' or 'okay':
                self.newgame()
            else:
                quit()

        if self.z % 2 == 1:
            print("\nO's turn")
        else:
            print("\nX's turn")

        
                    
            
        self.turn()
            
    def turn(self):
            print()
            self.x = int(input("Choose: "))
            
            if self.x in self.used:
                print("Unavailable location. Try again.\n")
                for c in range(0,3):
                    print('|'.join(map(str, self.python_board[c])))
                self.turn()
            else:
                self.used.append(self.x)
                
            if 8 < self.x < 10:
                self.y = 2
                self.x = self.x - 7
            elif 9 > self.x > 6:
                self.y = 2
                self.x = self.x - 7
            elif 7 > self.x > 3:
                self.y = 1
                self.x = self.x - 4
            elif 0 < self.x < 4:
                self.y = 0
                self.x = self.x - 1
            else:
                print("Please give a valid answer")
                self.turn()            
    
            self.z = self.z + 1

            self.board()

            
    
g = Game()


