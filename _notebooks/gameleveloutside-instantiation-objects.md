# GameLevelOutside.js - Instantiation & Objects

## Requirement
**Instantiation & Objects** - Creating objects and configuring them in level setup.

## Evidence
GameLevelOutside.js instantiates and configures multiple game objects with specific data.

### Code Example - Object Instantiation

```javascript
this.classes = [
    { class: GameEnvBackground, data: image_data_floor },
    { class: Player, data: sprite_data_mc },
    { class: StrictNpc, data: sprite_data_darkKnight },
    { class: StrictNpc, data: sir_morty_data },
    { class: StrictNpc, data: sprite_data_closet },
    { class: SpriteSheetCoin, data: gem_data },
    { class: SplineBarrier, data: left_wall },
    { class: SplineBarrier, data: right_wall }
];
```

### Code Example - Configuration Objects

```javascript
const image_data_floor = {
    name: 'floor',
    src: image_src_floor,
    pixels: { height: 989, width: 1582 }
};

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
    left: { row: 1, start: 0, columns: 3 },
    right: { row: 2, start: 0, columns: 3 },
    up: { row: 3, start: 0, columns: 3 },
    hitbox: { widthPercentage: 0.1, heightPercentage: 0.15 },
    keypress: { up: 87, left: 65, down: 83, right: 68 }
};

const gem_data = {
    id: 'gem',
    INIT_POSITION: { x: 0.5, y: 0.5 },
    SCALE_FACTOR: 30,
    value: 5,
    spriteImagePath: path + '/images/projects/castle-game/gems.png',
    spriteFrames: { rows: 2, columns: 4, frameIndex: Math.floor(Math.random() * 8) },
    spawnLocations: [
        { x: 340/1110*width, y: 447/760*height },
        { x: 490/1110*width, y: 510/760*height }
    ]
};
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates object instantiation through:

1. **Array of Object Pairs**:
   ```javascript
   { class: GameEnvBackground, data: image_data_floor }
   { class: Player, data: sprite_data_mc }
   ```
   - Each element pairs a class with configuration data
   - Game engine instantiates these objects

2. **Configuration Objects**:
   ```javascript
   const image_data_floor = { ... }
   const sprite_data_mc = { ... }
   const gem_data = { ... }
   ```
   - Objects created to hold configuration
   - Passed to constructors during instantiation

3. **Nested Configuration**:
   ```javascript
   INIT_POSITION: { x: 0.5 * width, y: 0.75 * height }
   orientation: { rows: 4, columns: 3 }
   spriteFrames: { rows: 2, columns: 4, frameIndex: 0 }
   ```
   - Objects contain nested objects
   - Each object properly configured before passing to class

4. **Object Properties**:
   - Strings (id, greeting, src)
   - Numbers (SCALE_FACTOR, STEP_FACTOR)
   - Objects (INIT_POSITION, pixels, orientation)
   - Arrays (spawnLocations)
   - All configured before instantiation

This demonstrates creating and configuring objects for game level setup.
