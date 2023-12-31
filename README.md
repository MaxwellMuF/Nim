Disclaimer: The code published here is based on the code from the Harvard project "CS50's Introduction to Artificial Intelligence with Python" and is intended for research purposes only (Access to the harvard project: https://cs50.harvard.edu/ai/2023/projects/4/nim/).

## The reposetory presented here was created as part of a project work for the lecture "Advanced Software Engineering". It currently contains the following files:

nim.py : This is a Q-learning AI written by David J. Malan on the above Harvard project and challenge. This file has been minimally modified and should not be seen as the author's own work.

game_interface.py : This python file is a game interface and has been developed independently and exclusively by the author of this repository.

Play_nim.py : This file is to play nim. It create the class Player and activate the game by calling the _call_ function.

highscore.json : This file is the data storage for the highscore of the players and a small statistic about games played by humans against the AI.

test_play_the_game : This file contains a few unit-tests to test the game_interface. It can be executed in different env or with the vs-code Testing ground. 

## Idea of the project:
### This project has two main aspects:
1. To program a game with an intuitive interface. The interface should be simple and easy to use without prior technical knowledge. The game is an old Chinese puzzle game for two players. The user should get to know the game and at best have fun playing it.
2. Provide an introduction to the world of AIs by giving the user information about the history of the game "Nim". This was implemented in 1940 as an electromechanical machine and was able to beat humans in the game Nim (read more: https://hal.science/hal-01349260)
