from player import Player
from game import Game

def main():
    size=int(input("Enter board size (e.g. 3 for 3x3): "))
    num_players = int(input("Enter number of players: "))

    players=[]
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        symbol = input(f"Enter symbol for {name}: ")
        players.append(Player(name, symbol))

    game = Game(size, players)
    game.play()


if __name__ == "__main__":
    main()
