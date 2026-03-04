# Recursive-Tower-of-Hanoi-Solver

A clean and elegant Python implementation of the classic **Tower of Hanoi** mathematical puzzle. This script uses a recursive algorithm to solve the puzzle for any given number of disks, meticulously tracking and returning the state of the three rods after every single move.

## 🚀 Features

* **Complete State Tracking:** Unlike basic solvers that just print "move disk from A to B", this script maintains a live internal state (`rods = [[], [], []]`) and captures a visual snapshot of the entire puzzle board at every step.
* **Recursive Elegance:** Demonstrates the power of recursion to solve complex problems with minimal code. The inner `solve` function elegantly handles the divide-and-conquer logic.
* **Customizable Complexity:** Easily change the number of disks by modifying the argument passed to `hanoi_solver(n)`.
* **Zero Dependencies:** Built entirely with standard Python. No external libraries required.

## 🧠 How the Algorithm Works


The Tower of Hanoi consists of three rods and a number of different-sized disks. The objective is to move the entire stack to the target rod, obeying the rules: only one disk can be moved at a time, and a larger disk cannot be placed on top of a smaller disk. 

To move $n$ disks from the **Source** rod to the **Target** rod using the **Auxiliary** rod, the recursive algorithm follows these three fundamental steps:
1. Recursively move the top $n-1$ disks from the **Source** to the **Auxiliary** rod.
2. Move the remaining largest disk (the $n$-th disk) directly from the **Source** to the **Target**.
3. Recursively move the $n-1$ disks from the **Auxiliary** rod onto the **Target** rod.

The total number of minimum moves required to solve the puzzle for $n$ disks is exactly:
$$ 2^n - 1 $$

## 🛠️ Requirements & Running

This project requires **Python 3.x**.

1. Clone the repository or download the `tower_of_hanoi_algorithm.py` file.
2. Open your terminal or command prompt.
3. Run the script using:

```bash
python tower_of_hanoi_algorithm.py
```

## 💻 Code Example & Usage

By default, the script is set to solve the puzzle for 5 disks. You can easily adjust this by changing `print(hanoi_solver(5))` to any other positive integer. 

```python
# Solve for 3 disks to see a shorter output
print(hanoi_solver(3))
```

**Expected Output Example (for 3 disks):**
*(The lists represent the 3 rods. Numbers represent disk sizes, where 3 is the largest and 1 is the smallest).*
```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

## 🤝 Contributing

Contributions are always welcome! If you'd like to build upon this project—perhaps by adding a graphical user interface (GUI) using `tkinter` or `pygame`, or by calculating and displaying the total number of moves taken—feel free to fork the repository and submit a Pull Request.
