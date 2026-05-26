# GameLevelMaze.js - Instantiation & Objects

## Requirement
**Instantiation & Objects** - Creating objects and configuring them in level setup.

## Evidence
GameLevelMaze.js instantiates game objects using configured data objects.

### Code Example - Object Instantiation Array

```javascript
this.classes = [
    { class: GameEnvBackground, data: bgData },
    { class: Player, data: sprite_data_mc },
    { class: Npc, data: mortyData },
    { class: Npc, data: sprite_data_invis },
    { class: Ghost, data: ghostData },
    { class: DeathBarrier, data: dbarrier_1 },
    { class: DeathBarrier, data: dbarrier_2 },
    { class: DeathBarrier, data: dbarrier_3 },
    { class: DeathBarrier, data: dbarrier_4 },
    { class: DeathBarrier, data: dbarrier_5 },
    { class: DeathBarrier, data: dbarrier_6 },
    { class: DeathBarrier, data: dbarrier_7 },
    { class: DeathBarrier, data: dbarrier_8 },
    { class: DeathBarrier, data: dbarrier_9 },
    { class: DeathBarrier, data: dbarrier_10 },
    { class: DeathBarrier, data: dbarrier_11 },
    { class: DeathBarrier, data: dbarrier_12 },
    { class: DeathBarrier, data: dbarrier_13 },
    { class: DeathBarrier, data: dbarrier_14 },
    { class: DeathBarrier, data: dbarrier_15 },
    { class: DeathBarrier, data: dbarrier_16 },
    { class: DeathBarrier, data: dbarrier_17 },
    { class: DeathBarrier, data: dbarrier_18 },
    { class: DeathBarrier, data: dbarrier_19 }
];
```

### Code Example - Configuration Objects

```javascript
const bgData = {
    name: "custom_bg",
    src: path + "/images/projects/castle-game/dungeonMaze.png",
    pixels: { height: 772, width: 1134 }
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
    down: { row: 0, start: 0, columns: 6 },
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

GameLevelMaze.js demonstrates object instantiation through:

1. **Array of Class-Data Pairs**:
   ```javascript
   { class: GameEnvBackground, data: bgData }
   { class: Ghost, data: ghostData }
   { class: DeathBarrier, data: dbarrier_1 }
   ```
   - Multiple objects paired with configuration
   - 19 DeathBarrier instances created from configurations

2. **Configuration Objects**:
   - Each barrier created from individual data object
   - Each NPC created from configuration object
   - Player created from sprite_data_mc configuration

3. **Object Reuse**:
   - Ghost instantiated once with ghostData
   - DeathBarrier instantiated 19 times with different barrier configs
   - Demonstrates creating multiple instances from same class

This demonstrates creating multiple game objects from configuration data.
