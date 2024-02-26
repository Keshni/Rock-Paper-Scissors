# Rock-Paper-Scissors

This is a simple Rock Paper Scissors game implemented using Python and Tkinter GUI library. The game allows the user to challenge the computer in a classic game of Rock Paper Scissors.

## How to Play
The player selects one of the three options: Rock, Paper, or Scissors by clicking on the corresponding button.
The computer randomly selects its choice.
The winner is determined based on the rules:
- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock
  
The game keeps track of the user's score and the computer's score, which is displayed after each round.

## Features
- Graphical User Interface (GUI) using Tkinter.
- Random selection of the computer's choice.
- Score tracking for both the player and the computer.

## Instructions
Install the required packages if not already installed:

```bash
pip install tk
```
Download the images rock.png, paper.png, and scissors.png for the buttons.

Run the provided Python script to start the game.

## Code Explanation
The game window is created using tkinter.Tk().
Each button represents a choice (Rock, Paper, Scissors) and triggers the corresponding function when clicked.
The result() function determines the winner of each round and updates the scores.
The game interface is designed using labels and buttons.
The game loop is started using window.mainloop().

## Limitations
The game interface is basic and may require additional enhancements for improved user experience.
