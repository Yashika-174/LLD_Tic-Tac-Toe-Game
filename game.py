from board import Board
from player import Player

class Game:
    def __init__(self,size,players):
        self.board=Board(size)
        self.players=players
        self.win_length=size


    def is_valid(self,r,c):
        if (0<=r<self.board.size and 0<=c<self.board.size):
            return True
        else:
            return False

    def count_in_line(self,r,c,dx,dy,symbol):

        count=0

        r+=dx
        c+=dy
        while (self.is_valid(r,c) and self.board.grid[r][c]==symbol):
            count+=1
            r+=dx
            c+=dy
        
        r-=dx
        c-=dy
        while (self.is_valid(r,c) and self.board.grid[r][c]==symbol):
            count+=1
            r-=dx
            c-=dy
        
        return count


    def check_win(self,r,c,symbol):
        dir=[(1,0),(0,1),(1,1),(1,-1)]
        for (dx,dy) in dir:
            if self.count_in_line(r,c,dx,dy,symbol)>=self.win_length:
                return True
        return False


    def play(self):
        current=0
        while True:
            self.board.print_board()
            player=self.players[current]
            print(f"Its Player Num:{current+1}'s chance ({player.name} : {player.symbol})")

            try:
                row=int(input("Enter row (1-based): "))-1
                col=int(input("Enter col (1-based): "))-1

            except:
                print("Please enter valid numbers.")
                continue

            if not self.board.is_valid_move(row, col):
                print("Invalid move! Try again.")
                continue

            self.board.make_move(row, col, player.symbol)

            if self.check_win(row, col,player.symbol):
                self.board.print_board()
                print(f"\n🎉 {player.name} wins!")
                break
            
            if self.board.is_full():
                self.board.print_board()
                print("\nIt's a draw!")
                break


            current=(current+1)%len(self.players)

