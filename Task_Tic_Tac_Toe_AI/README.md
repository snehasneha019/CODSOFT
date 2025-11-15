#  Tic-Tac-Toe AI (Beginner Project)

This project is a simple **Tic-Tac-Toe game** where the user plays against the computer.
The computer uses a basic **Minimax algorithm**, which allows it to make the best possible move every time.
This makes the AI very strong and hard to beat, while still keeping the code beginner-friendly and easy to understand.
##  **Project Features**

* Play Tic-Tac-Toe in the terminal
* Human player = **O**
* Computer (AI) = **X**
* AI uses the **Minimax algorithm** to choose the best move
* Detects win, loss, or draw
* Clear and simple code suitable for beginners or internship tasks
##  **How It Works**

### 1. **Game Board**

The board is stored as a list of 9 spaces:


[ " ", " ", " ", 
  " ", " ", " ",
  " ", " ", " " ]


Each position represents a cell in the 3×3 grid.

### 2. **Player Moves**

* User enters a number from **1 to 9**
* The number represents a position on the grid
* The game checks if the spot is empty before placing the move

### 3. **Minimax Algorithm (Simple Version)**

The AI tries all possible moves and chooses the one that leads to the best outcome:

* **+1** → AI will win
* **0** → Draw
* **–1** → Human will win

This ensures the AI never loses.

##  **How to Run the Program**

1. Make sure you have **Python installed**
2. Save the code in a file, for example:
   tic_tac_toe.py
3. Open a terminal or command prompt
4. Run the game:
   python tic_tac_toe.py

##  **Game Controls**

Enter a number **1–9** where you want to place your “O”.

Board layout for reference
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

##  **Why Minimax?**

Minimax helps the AI:

* Look ahead at possible future moves
* Avoid losing situations
* Pick the move with the best score

This teaches important concepts used in game development and AI:

* Recursion
* Search trees
* Decision making


##  **What I Learned**

This project helped me understand:

* How to work with lists and functions in Python
* How turn-based games work
* How AI can predict future moves
* Basic game theory concepts
