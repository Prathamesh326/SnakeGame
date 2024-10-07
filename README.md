# Snake Game

A classic snake game built with Python's `turtle` module. The game features a snake that grows as it eats food, and the player must avoid running into the walls or the snake's own tail. The project also includes a scoring system to keep track of the player's progress.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Snake Movement**: Use arrow keys to control the snake's direction.
- **Food System**: The snake grows longer when it eats food, and food appears in random positions.
- **Scoring System**: The score increases when the snake eats food. The highest score is tracked.
- **Collision Detection**:
  - If the snake collides with the walls, the game resets.
  - If the snake collides with its own tail, the game resets.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Prathamesh326/SnakeGame.git
   ```

2. Navigate to the project directory:
   ```bash
   cd SnakeGame
   ```

3. Install dependencies (if necessary):
   - The game only requires Python's built-in `turtle` module, which should be included with most Python distributions.
   - If not, you can install it with:
     ```bash
     pip install PythonTurtle
     ```

4. Run the game:
   ```bash
   python main.py
   ```

## How to Play

- Use the arrow keys to control the snake:
  - **Up Arrow**: Move up
  - **Down Arrow**: Move down
  - **Left Arrow**: Move left
  - **Right Arrow**: Move right
- The snake will grow longer each time it eats food.
- Avoid colliding with the walls or the snake's own tail to keep playing and increase your score.
- The game will automatically reset if the snake hits the walls or its tail, and the score will be reset as well.

## Technologies Used

- **Python**: The game is entirely developed using Python's `turtle` graphics module.
- **Turtle Module**: A Python library that provides simple graphics for drawing and game development.

## Contributing

Contributions are welcome! If you'd like to add new features or improve the code, feel free to create a pull request. Please ensure that your code follows the existing coding style and includes appropriate comments and documentation.
