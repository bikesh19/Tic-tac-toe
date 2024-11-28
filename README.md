
# 🕹️ Tic-Tac-Toe Game in Python 🎲

This is a simple **Tic-Tac-Toe** (or Noughts and Crosses) game built with Python. The game allows a human player (`*`) to compete against the computer (`0`) in a 3x3 grid. The first player to align three symbols wins! If no one wins after all moves, the game ends in a draw.

---

## ✨ Features

- 🖱️ **Interactive Gameplay**: Input-based player moves.  
- 🤖 **AI Opponent**: The computer selects random moves.  
- 🎮 **Classic Rules**: Follow traditional Tic-Tac-Toe winning rules.  
- 🔁 **Turn-based Mechanics**: Alternates between player and computer turns.  
- 🎉 **Win, Lose, or Draw**: The program declares the result after each game.

---

## 🛠️ How It Works

1. **Setup**:  
   - The grid is displayed as a 3x3 matrix with numbered cells (1-9).  

2. **Player's Turn**:
   - Enter a number (1-9) corresponding to the cell where you want to place your marker (`*`).  
   - Invalid or already-used inputs are rejected with appropriate prompts.  

3. **Computer's Turn**:  
   - The computer randomly selects an unused cell and places its marker (`0`).  

4. **Winning Logic**:  
   - A win is declared if any row, column, or diagonal has the same marker (`*` or `0`).

5. **Game End**:  
   - The game ends with a win, loss, or draw after all cells are filled.  

---

## 📋 Rules

- Each player takes turns placing their marker (`*` or `0`) in an empty cell.  
- The first player to align three markers (horizontally, vertically, or diagonally) wins.  
- If all cells are filled without a winner, the game ends in a draw.  

---

## 🚀 How to Run

1. Install Python (if not already installed).  
2. Copy the code into a file, e.g., `tic_tac_toe.py`.  
3. Run the script in your terminal/IDE:  
   ```bash
   python tic_tac_toe.py
   ```
4. Follow the on-screen instructions to play the game.

---

## 🎨 Example Gameplay

```text
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
----------
Player's turn (*):
Enter a number for *: 5
1 | 2 | 3
4 | * | 6
7 | 8 | 9
----------
Computer's turn (0):
1 | 2 | 3
4 | * | 6
0 | 8 | 9
...
```

---

## 🌟 Future Improvements

- Add smarter AI using minimax or heuristic algorithms. 🤖  
- Include a GUI for better user interaction. 🖼️  
- Add multiplayer support for two human players. 👥  

---

🎮 **Enjoy the game! Feedback is welcome!** 😊
