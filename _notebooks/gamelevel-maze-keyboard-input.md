# GameLevelMaze.js - Keyboard Input

## Requirement
**Keyboard Input** - Handling keyboard events and player input for game control.

## Evidence
GameLevelMaze.js configures keyboard input for player movement through the maze.

### Code Example - Keyboard Configuration

```javascript
const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc,
    SCALE_FACTOR: 20,
    STEP_FACTOR: 1750,
    ANIMATION_RATE: 100,
    INIT_POSITION: {
        x: 202 / 1911 * width,
        y: 760 / 851 * height
    },
    pixels: { height: 432, width: 234 },
    orientation: { rows: 4, columns: 3 },
    down: { row: 0, start: 0, columns: 3 },
    downRight: { row: 2, start: 0, columns: 3, rotate: Math.PI / 16 },
    downLeft: { row: 1, start: 0, columns: 3, rotate: -Math.PI / 16 },
    left: { row: 1, start: 0, columns: 3 },
    right: { row: 2, start: 0, columns: 3 },
    up: { row: 3, start: 0, columns: 3 },
    upLeft: { row: 1, start: 0, columns: 3, rotate: Math.PI / 16 },
    upRight: { row: 2, start: 0, columns: 3, rotate: -Math.PI / 16 },
    hitbox: { widthPercentage: 0.1, heightPercentage: 0.15 },
    keypress: { up: 87, left: 65, down: 83, right: 68 } // W, A, S, D
};
```

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates keyboard input through:

1. **WASD Key Mapping**:
   ```javascript
   keypress: { up: 87, left: 65, down: 83, right: 68 }
   ```
   - W (87), A (65), S (83), D (68)
   - Standard game control scheme

2. **Directional Input**:
   - Each key maps to a cardinal direction
   - Enables player to navigate maze

3. **Input Processing**:
   - Game engine monitors these key codes
   - Translates input into character movement
   - Allows player to avoid death barriers

This demonstrates keyboard input configuration enabling player control in maze navigation.
