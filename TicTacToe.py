import random
   

class TicTacToe:

    def __init__(self):

        self.board = [int(i) for i in range(1,10)]
        self.player1 = []
        self.player2 = []
         

    def play(self, Toggle = True):        

        if Toggle:
            print("Player1 Turn:")
            input1 = int(input())
           
        else:
            print("Player2 Turn:")
            input1 = random.choice([i+1  for i in range(0,9) if isinstance(self.board[i] , int) ])
            print(input1)
            
        print("Enter Location to put the coin: ")
        
        
        
        if (input1 in range(1,10)) and (isinstance(self.board[input1-1] , int)):
            if Toggle:
                self.board[input1-1] = 'X'
                self.player1.append(input1)
        
            else:
                self.board[input1-1] = 'O'
                self.player2.append(input1)
            
        else:
            raise  ValueError('check the board an enter the value')
            


    def win(self, player_arr):

        diagonal = [[1,5,9], [3,5,7]]
        horizontal = [[1,2,3] , [4,5,6] , [7,8,9]]
        vertical = [[1,4,7] , [2,5,8] , [3,6,9]]

        arr = diagonal + horizontal + vertical
        for i in arr:
            
            if (set(i).issubset(set(player_arr))):
                return True
        else:
            return False

    def start_game(self):
        
        print(" You (X) Vs Computer (O)")
        print("ready , set, go!!!!")
        index  = 0
        Toggle = True
        while True:
            if index == 9:
                break
            else:
                self.print()
                self.play(Toggle)
                if self.win(self.player1):
                    self.print()
                    print ("player1 (You)  : win!!")
                    print ("The game ends")
                    break
                elif self.win(self.player2):
                    self.print()
                    print ("player2 (Computer Win) : win!!")
                    print ("The game ends")
                    
                    break
                else:
                    Toggle = not Toggle                 
            
                    

    def print(self):

        print("----------------------")
       # print("|      |      |      |")
        print("| ", self.board[0],"  | " , self.board[1],"  |  " , self.board[2]," |")
        #print("|      |      |      |")
        print("----------------------")
        #print("|      |      |      |")
        print("| ", self.board[3],"  | " , self.board[4],"  |  " , self.board[5]," |")
        #print("|      |      |      |")
        print("----------------------")
        #print("|      |      |      |")
        print("| ", self.board[6],"  | " , self.board[7],"  |  " , self.board[8]," |")
        #print("|      |      |      |")
        print("----------------------")
    


if __name__== "__main__":

    t = TicTacToe()
    t.start_game()
    
    
