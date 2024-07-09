

### Update Description 3.9 June

**Version 3.9 - June 4th Update**

**New Features and Improvements:**

1. **Heart System for Lives:**
   - Added a new heart system to represent player lives.
   - Players start with 8 lives.
   - Each lost life decreases the score by 10 points.
   - If all lives are lost, the game displays a "Game Over" message and returns to the main menu.
   - Hearts are displayed at the bottom of the screen during gameplay.

2. **Main Menu Enhancements:**
   - Added an option to start a new game, continue a saved game, access the shop, or exit the game.
   - Displayed the total time spent in the game.
   - Added version and update date information at the bottom of the menu.

3. **Shop System:**
   - Players can now spend points to purchase different types of balls and a special sound effect.
   - Available items:
     - Basketball - 400 points
     - Football - 525 points
     - Geometry Dash ball - 1500 points
     - Super Mario ball - 3000 points
     - Point sound effect - 2000 points

4. **Game State Saving and Loading:**
   - Implemented game state saving and loading using pickle.
   - The game state includes the ball position, paddle position, score, level, remaining lives, purchased items, and more.

5. **Sound Effects:**
   - Added sound effects for game startup and shutdown.
   - Added an optional sound effect for scoring points, which can be purchased in the shop.

6. **Bug Fixes and Performance Improvements:**
   - Fixed issues with image loading before initializing the display.
   - Improved game loop and event handling for smoother gameplay.

**Files Updated:**
- `projekt.py`

---



# arkadion Update


## Project Description

This is a computer game written in Python using the Pygame library. The game involves bouncing a ball using a paddle, breaking bricks, and earning points. It includes features for saving and loading game states, a shop with different balls, and difficulty levels. The player can progress through various levels, earn points, and purchase different balls in the shop with the points earned.

## Code Structure

1. **Importing Modules and Changing the Working Directory:**
   The code starts by importing necessary modules like `os`, `pygame`, `sys`, `random`, and `pickle`. It then changes the working directory to a specified path.

2. **Constants for Shop Prices:**
   Defines a dictionary `CENY` that stores the prices of different balls available in the shop.

3. **Global Variables:**
   Defines several global variables such as `punkty` (points), `czas_w_grze` (game time), `zakupione_pilki` (purchased balls), `aktualna_pilka` (current ball), `poziom` (level), `ruch_x` (ball speed in the x direction), `ruch_y` (ball speed in the y direction), `ruch_pada` (paddle speed), `odtwarzaj_point_wav` (play point.wav), which are used throughout the program.

4. **Helper Functions:**
   - `reset()`: Resets the position of the ball and paddle, and the ball speed.
   - `generuj_cegielki()`: Generates bricks in random positions on the screen.
   - `przejscie_na_kolejny_poziom()`: Moves to the next level, increasing the game difficulty.
   - `zapisz_stan_gry()`: Saves the current game state to a file `stan_gry.pkl`.
   - `wczytaj_stan_gry()`: Loads the game state from the file `stan_gry.pkl`.
   - `odtworz_dzwiek(plik)`: Plays a sound from the specified file.
   - `rysuj_tekst(tekst, pozycja, rozmiar=36)`: Draws text on the screen at a specified position and size.
   - `pokaz_menu()`: Displays the main menu of the game.
   - `sklepik()`: Displays the shop where the player can buy different balls.

5. **Pygame Initialization:**
   Initializes Pygame, sets the game window size, and loads sounds and images. It handles exceptions related to image loading.

6. **Game Loop:**
   - Displays the main menu and waits for the player's choice.
   - Depending on the player's choice (new game, continue game, or shop), the corresponding functions are called.
   - The main game loop handles game logic, including ball movement, collisions with paddles and bricks, updating points, level transitions, and drawing all elements on the screen.

7. **Ending the Game:**
   If the player completes all levels, a winning message is displayed, and the game ends.

## Running the Game

To run the game, you need to have the Pygame library installed. You can do this using the command:
```bash
pip install pygame
```

Then simply run the script in Python:
```bash
python projekt.py
```

### Main Controls in the Game:
- Arrow keys left/right or A/D keys: Move the paddle left/right.
- ESC: Save the game state and return to the menu.
- In the menu:
  - 1: New game.
  - 2: Continue game.
  - 3: Shop.
  - 4: Exit the game.

### In the Shop:
- 1: Buy the basketball.
- 2: Buy the football.
- 3: Buy the geometry_dash ball.
- 4: Buy the super_mario ball.
- 5: Buy the point.mp3 sound.
- ESC: Return to the menu.

That's all! Now you can upload this description along with the code to GitHub to share your game with others.

# Arkanoid Clone Game

This is a simple clone of the classic Arkanoid game built using Pygame. The objective of the game is to break all the bricks on the screen by bouncing a ball off a paddle. The game includes multiple levels, increasing difficulty, and a win condition after completing all levels.

## Features

- **Five Levels**: The game consists of five levels, each with an increasing number of bricks.
- **Score Tracking**: Points are awarded for breaking bricks, with a random score between 1 and 12 points per brick.
- **Level Progression**: Players progress to the next level upon reaching 1000 points. Each new level introduces more bricks.
- **Winning Condition**: The game ends with a victory message after completing all five levels.
- **Paddle Control**: The paddle can be controlled using the arrow keys or `A` and `D` keys and is restricted to the screen boundaries.
- **Random Brick Placement**: Bricks are randomly placed on the screen at the start of each level.

## Installation

1. Ensure you have Python installed. If not, download and install it from [python.org](https://www.python.org/).
2. Install Pygame library if you haven't already. You can install it using pip:

    ```bash
    pip install pygame
    ```

3. Clone the repository:

    ```bash
    git clone https://github.com/Lukas7759/arkadion
    ```

4. Navigate to the project directory:

    ```bash
    cd arkanoid-clone
    ```

## Running the Game

1. Make sure you have all the required assets (images for the background, paddle, and ball) in the same directory as the script.
2. Run the game using Python:

    ```bash
    python arkanoid_clone.py
    ```

## Controls

- **Left Arrow / A Key**: Move paddle left
- **Right Arrow / D Key**: Move paddle right

## How to Play

1. Use the paddle to bounce the ball and break all the bricks on the screen.
2. Gain points for every brick you break.
3. Reach 1000 points to progress to the next level.
4. The game consists of five levels. Each level has more bricks to break.
5. Complete all five levels to win the game.

## Game Over

- If the ball falls below the paddle, the game will reset to the current level.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This game was built using the Pygame library. Special thanks to the Pygame community for their excellent documentation and resources.

