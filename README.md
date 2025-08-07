# 🎮 Scalable Tic Tac Toe Game

A fully customizable, console-based Tic Tac Toe game built using Python OOP (Object-Oriented Programming). Supports:

- ✅ Any board size (e.g. 3x3, 5x5, 10x10)
- ✅ Any number of players
- ✅ Any custom symbols or emojis (e.g. ❌, ⭕, 🐱, 🔺)
- ✅ Win detection in all directions (↔, ↕, ↘, ↙)

---

## 📁 Folder Structure (Bottom-Up Design)

```
tic_tac_toe/
├── main.py         # Entry point of the game
├── player.py       # Player class (name, symbol)
├── board.py        # Board class (grid, print, valid moves)
└── game.py         # Game engine (turns, win checks, game loop)
```

---

## 🧠 How It Works

- **Board** class: Handles grid display, move validation, and updates.
- **Player** class: Stores each player’s name and symbol.
- **Game** class: Controls game loop, turn switching, and win detection using a dynamic direction-based algorithm.

---

## 🛠️ Requirements

- Python 3.6+

No external packages needed.

---

## ▶️ Run the Game

```bash
python main.py
```

### Sample Input Flow:

```
Enter board size (e.g. 3 for 3x3): 3
Enter number of players: 2
Enter name for Player 1: Alice
Enter symbol for Alice: X
Enter name for Player 2: Bob
Enter symbol for Bob: O
```

---

## 📸 Demo Screenshot

```
 X | O | X
-----------
 O | X | O
-----------
 X |   |  
🎉 Alice wins!
```

---

## 🧩 Features

| Feature                        | Status |
|-------------------------------|--------|
| Multiple players              | ✅     |
| Any symbol or emoji           | ✅     |
| Dynamic win-check logic       | ✅     |
| Modular OOP code structure    | ✅     |
| Easy to extend (GUI, AI, etc) | ✅     |

---

## 🧑‍💻 Author

Made with ❤️ by Yashika
