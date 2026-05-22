# GameLevelMaze.js - Objects (JSON Data)

## Requirement
**Objects (JSON)** - Using object and JSON data structures to organize and manage complex data.

## Evidence
GameLevelMaze.js uses objects extensively for game configuration and barrier positioning.

### Code Example - Object/JSON Structures

```javascript
const bgData = {
    name: "custom_bg",
    src: path + "/images/projects/castle-game/dungeonMaze.png",
    pixels: { height: 772, width: 1134 }
};

const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc,
    SCALE_FACTOR: 20,
    STEP_FACTOR: 1750,
    ANIMATION_RATE: 100,
    INIT_POSITION: { x: 202 / 1911 * width, y: 760 / 851 * height },
    pixels: { height: 432, width: 234 },
    orientation: { rows: 4, columns: 3 },
    hitbox: { widthPercentage: 0.1, heightPercentage: 0.15 },
    keypress: { up: 87, left: 65, down: 83, right: 68 }
};

const ghostData = {
    id: 'Ghost',
    greeting: false,
    src: path + "/images/projects/castle-game/ghost.png",
    SCALE_FACTOR: 12,
    ANIMATION_RATE: 20,
    INIT_POSITION: { x: 0.8 * width, y: 0.2 * height },
    pixels: { width: 3000, height: 1000 },
    orientation: { rows: 2, columns: 6 },
    hitbox: { widthPercentage: 0.15, heightPercentage: 0.2 },
    followSpeedFactor: 0.4,
    followStopDistance: 12,
    zIndex: 12
};

const dbarrier_1 = {
    id: 'dbarrier_1',
    x: 498 / 505 * width,
    y: 0 / 291 * height,
    width: 6 / 505 * width,
    height: 295 / 291 * height,
    visible: false,
    hitbox: { widthPercentage: 0.0, heightPercentage: 0.0 },
    fromOverlay: true
};
```

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates objects/JSON through:

1. **Background Configuration Object**:
   ```javascript
   const bgData = {
       name: "custom_bg",
       src: path + "/images/projects/castle-game/dungeonMaze.png",
       pixels: { height: 772, width: 1134 }
   };
   ```
   - Top-level object with nested object
   - pixels is itself an object with dimensions

2. **Player Sprite Configuration Object**:
   ```javascript
   const sprite_data_mc = {
       id: 'Knight',
       INIT_POSITION: { x: 202 / 1911 * width, y: 760 / 851 * height },
       orientation: { rows: 4, columns: 3 },
       keypress: { up: 87, left: 65, down: 83, right: 68 }
   };
   ```
   - Multiple nested objects
   - INIT_POSITION, orientation, keypress are objects
   - Complex configuration hierarchy

3. **Enemy (Ghost) Configuration Object**:
   ```javascript
   const ghostData = {
       INIT_POSITION: { x: 0.8 * width, y: 0.2 * height },
       orientation: { rows: 2, columns: 6 },
       hitbox: { widthPercentage: 0.15, heightPercentage: 0.2 }
   };
   ```
   - Nested objects for position, sprite, collision
   - Consistent structure with player config

4. **Death Barrier Configuration Object**:
   ```javascript
   const dbarrier_1 = {
       id: 'dbarrier_1',
       x: 498 / 505 * width,
       y: 0 / 291 * height,
       width: 6 / 505 * width,
       height: 295 / 291 * height,
       visible: false,
       hitbox: { widthPercentage: 0.0, heightPercentage: 0.0 },
       fromOverlay: true
   };
   ```
   - Nested hitbox object
   - Mix of numeric and boolean properties

This demonstrates comprehensive use of nested objects for game configuration.
