# Wordle Solver

A lightweight Python CLI tool that helps you solve Wordle puzzles using an entropy-like information theory heuristic.

The solver suggests optimal starting words (default: `CRANE`) and calculates the best next guesses by simulating how much each guess narrows down the remaining pool of possible words.

## How it Works

1. **Entropy Heuristic**: For any set of remaining candidate words, the solver evaluates each guess against all possible target words. It measures how much the word list shrinks under each scenario (using a square-root-based ratio of the remaining set sizes) to estimate the average information gain.
2. **Interactive Loop**: You run the solver, input your guess and the resulting color feedback, and the script suggests the next best words sorted by their information score.

## Installation

No external dependencies are required. The project runs entirely on the Python standard library.

1. Clone this repository.
2. Ensure you have Python 3 installed.
3. Make sure `words.txt` is in the same directory as the scripts.

## Usage

Run the main script to start the interactive loop:

```bash
python main.py
```

### Game Loop Example

1. The solver suggests a starting word (e.g., `CRANE`).
2. Input the word you guessed into the CLI:
   ```
   >>> CRANE
   ```
3. Input the Wordle coloring feedback using:
   - `G` for **Green** (correct letter, correct spot)
   - `O` for **Orange/Yellow** (correct letter, wrong spot)
   - Any other character (e.g., `B` or `X`) for **Grey** (incorrect letter)
   
   For example, if C and A are grey, R is yellow, N is green, and E is grey:
   ```
   >>> BXGOG
   ```
4. The solver will output the remaining possible words and rank the best next guesses by their expected information value.