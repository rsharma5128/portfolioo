# GameLevelMaze.js - Arrays (Data Type)

## Requirement
**Arrays** - Using array data types to store and manage collections.

## Evidence
GameLevelMaze.js uses arrays to manage NPC objects, death barriers, and game entity collections.

### Code Example - Array Usage

```javascript
const dbarrier_list = [
    { id: 'dbarrier_1', x: 498 / 505 * width, y: 0 / 291 * height, width: 6 / 505 * width, height: 295 / 291 * height },
    { id: 'dbarrier_2', x: 0 / 505 * width, y: 0 / 291 * height, width: 7 / 505 * width, height: 296 / 291 * height },
    { id: 'dbarrier_3', x: 7 / 505 * width, y: 71 / 291 * height, width: 14 / 505 * width, height: 225 / 291 * height },
    // ... 16 more barriers
];

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

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates arrays through:

1. **Game Objects Array**:
   ```javascript
   this.classes = [
       { class: GameEnvBackground, data: bgData },
       { class: Player, data: sprite_data_mc },
       { class: Npc, data: mortyData }
   ]
   ```
   - Array of configuration objects
   - Each element is game entity to create
   - Game engine iterates through to instantiate

2. **Death Barrier Collection**:
   ```javascript
   { class: DeathBarrier, data: dbarrier_1 },
   { class: DeathBarrier, data: dbarrier_2 },
   // ... 17 more
   ```
   - 19 death barriers in single array
   - Creates maze wall structure
   - Each barrier positioned independently

3. **NPC Collection**:
   ```javascript
   { class: Npc, data: mortyData },
   { class: Npc, data: sprite_data_invis }
   ```
   - Multiple NPCs in array
   - Easier to manage than individual variables

4. **Array Elements Structure**:
   - Each element is object with class and data
   - Consistent structure enables iteration
   - Game engine processes uniformly

This demonstrates using arrays to manage complex maze geometry with 19 collision barriers.
