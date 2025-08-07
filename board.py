class Board:
    def __init__(self,size):
        self.size=size
        self.grid=[[" " for i in range(self.size)] for j in range(self.size)]

    def print_board(self):
        for row in self.grid:
            print(" | ".join(row))
            print("-" * (self.size * 4 - 3))

    def is_full(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]==" ":
                    return False
        
        return True

    def is_valid_move(self,r,c):
        if (0<=r<self.size and 0<=c<self.size  and self.grid[r][c] == " "):
            return True
        else:
            return False

    def make_move(self,r,c,symbol):
        self.grid[r][c]=symbol

    
