# arkadion

Oto przykładowy opis gry, który możesz wykorzystać do umieszczenia na GitHubie:

---

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
    git clone https://github.com/yourusername/arkanoid-clone.git
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

## Screenshots

(Add screenshots of your game here to give users a preview.)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This game was built using the Pygame library. Special thanks to the Pygame community for their excellent documentation and resources.

