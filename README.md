# World Of Games (WOG)

## Overview
This project was made as part of a DevOps course, at the DevOps Experts college.

It demonstrates the following learning concepts:
1. Coding with Python
2. Working with external packages (Flask).
3. Connecting to external 3rd party service provider using API (a forex service).
4. Working with files.
5. Using version control (Git).

### Interface
- Uses a **command-line** interface.
- Player's score is displayed on the browser (HTML page).

### Logs
A log file is being generated per each new game session.
These log files are being saved to the **logs** folder (inside the project).


## Instructions
### How to install & run
1. Download/clone this repo
2. Open a terminal & navigate to the **WOG** folder.
3. Run the following commands:
   - _pip install -r requirements.txt_ 
   - _python MainGame.py_
### How to play
1. The **main menu** prompts to choose a game to play & select the difficulty level.
2. Upon the end of each game, the program returns to the **main menu** & the player can check the current score on the browser (127.0.0.1:30000).
3. The player now can either play another game (different or same) or quit the session (by selecting **0**).


## The games
WOG consists of 3 games:
- Memory game
- Guessing game
- Currency roulette game

### Memory game
1. In this game, the player is presented with a list of numbers, in the range of 1-100.
2. The list is being displayed for a defined period of time & then it is hidden. 
3. The player is asked to repeat the list of numbers, at the **exact order**. 

Total numbers in the list & the period of time the list is displayed, are defined according to the **difficulty level**.

### Guessing game
In this game, the player is asked to guess a number randomly chosen by the program. 

The range, from which the random number is generated, is defined according to the **difficulty level**.

### Currency roulette game
1. The program generates a random amount of USD (between 1-100).
2. The player is asked to guess the amount of the corresponding ILS.

The game uses a free currency API to get the current exchange rate from USD to ILS.
The error tolerance margins for player's guess is defined according to the **difficulty level**.


## Versions change log
**3.1.0**:
- Added some changes handling the external files (logs & score)
- Moved the game files to a Games folder
- Modified the looks & feels of the UI
- Made the code a bit more "clean"

**3.0.0**:
- 3rd version of the WOG project
- Level 3:
  - implement the additional logic (players score)
  - use flask to display info on web

**2.0.0**:
- 2nd version of the WOG project
- Level 2:
  - implement the logic
  - implement the 4 games within the WOG

**1.0.0**:
- Initial version of the WOG project
- Level 1:
  - create the basic infra for WOG