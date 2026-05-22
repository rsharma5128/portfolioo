# GameLevelOutside.js - Keyboard Input

## Requirement
**Keyboard Input** - Handling keyboard events and player input for game control.

## Evidence
GameLevelOutside.js configures keyboard input mappings for the player character.

### Code Example - Keyboard Configuration

```javascript
const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc,
    SCALE_FACTOR: 15,
    STEP_FACTOR: 1500,
    ANIMATION_RATE: 40,
    INIT_POSITION: {
        x: 0.5 * width,
        y: 0.75 * height
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
    keypress: { up: 87, left: 65, down: 83, right: 68 }, // W, A, S, D
};
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates keyboard input through:

1. **Keyboard Mapping Configuration**:
   ```javascript
   keypress: { up: 87, left: 65, down: 83, right: 68 }
   ```
   - Maps four directions to keyboard key codes
   - W (87), A (65), S (83), D (68)

2. **Key Code Values**:
   - `87` = 'W' key (forward/up)
   - `65` = 'A' key (left)
   - `83` = 'S' key (backward/down)
   - `68` = 'D' key (right)

3. **Standard WASD Layout**:
   - Uses common game keyboard scheme
   - W-A-S-D allows left-hand movement control
   - Standard layout familiar to game players

4. **Direction-to-Key Mapping**:
   - Each cardinal direction mapped to specific key
   - Game engine uses these values to detect key presses
   - Enables player movement control

This demonstrates keyboard input configuration that enables the player to control character movement using WASD keys.
