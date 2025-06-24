# Sudoku Solver in Python 🧩

This project implements a backtracking Sudoku solver using Python. The solver takes a partially filled 9x9 Sudoku grid and fills it with digits (1 to 9) so that each row, column, and 3x3 box contains all digits without repetition.

---

## 📋 Features

- Solves any valid 9x9 Sudoku puzzle using backtracking
- Uses object-oriented design (class `Board`)
- Displays the puzzle before and after solving
- Shows `*` for empty cells in unsolved puzzle
- Clean output with proper formatting

---

## 📌 How It Works

1. The program searches for the next empty cell.
2. It tries digits 1–9 one by one and checks:
   - Is the digit valid in the current row?
   - Is the digit valid in the current column?
   - Is the digit valid in the current 3x3 square?
3. If all checks pass, it assigns the number and moves to the next empty cell recursively.
4. If a guess leads to dead end, it backtracks and tries the next possible number.

---

## 🧪 Sample Puzzle

* * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
1 7 * * * 6 * * 5

## ✅ Sample Output


Puzzle to solve:
* * 2 * * 8 * * *
* * * * * 3 7 6 2
4 3 * * * * 8 * *
* 5 * * 3 * * 9 *
* 4 * * * * * 2 6
* * * 4 6 7 * * *
* 8 6 7 * 4 * * *
* * * 5 1 9 * * 8
1 7 * * * 6 * * 5


Solved puzzle:
9 6 2 1 7 8 3 5 4
8 1 5 9 4 3 7 6 2
4 3 7 6 5 2 8 1 9
6 5 8 2 3 1 4 9 7
7 4 3 8 9 5 1 2 6
2 9 1 4 6 7 5 8 3
5 8 6 7 2 4 9 3 1
3 2 4 5 1 9 6 7 8
1 7 9 3 8 6 2 4 5



## ▶️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Save the code in a file (e.g., `sudoku_solver.py`)
3. Run the script using:

```bash
python sudoku_solver.py
🧠 Files
sudoku_solver.py: Main solver logic using class Board

README.md: Project documentation

📝 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Abhishek Anand
Feel free to reach out for collaboration or suggestions!