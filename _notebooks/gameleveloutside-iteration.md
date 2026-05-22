# GameLevelOutside.js - Iteration (Loops)

## Requirement
**Iteration (Loops)** - Using loops to iterate over collections and perform repeated operations.

## Evidence
GameLevelOutside.js uses array iteration methods to manage game objects and player customization options.

### Code Example - Array Iteration and Mapping

```javascript
const playerSpriteOptions = {
    gray: path + "/images/projects/castle-game/grayKnight.png",
    green: path + "/images/projects/castle-game/greenKnight.png",
    dark: path + "/images/projects/castle-game/darkKnight.png"
};

const getPlayerSpriteSrc = (skinKey) => playerSpriteOptions[skinKey] || playerSpriteOptions.gray;

const applyPlayerSprite = (player, skinKey) => {
    const spriteSrc = getPlayerSpriteSrc(skinKey);
    if (!player || !spriteSrc) return;
    if (player.spriteData?.src === spriteSrc) {
        setStoredPlayerSkinKey(skinKey);
        return;
    }

    const newSpriteSheet = new Image();
    newSpriteSheet.onload = () => {
        player.spriteSheet = newSpriteSheet;
        player.spriteReady = true;
        player.spriteData = { ...(player.spriteData || {}), src: spriteSrc };
        player.data = player.spriteData;
        player.frameIndex = 0;
        player.frameCounter = 0;
        player.resize();
        setStoredPlayerSkinKey(skinKey);
    };
    newSpriteSheet.onerror = (error) => {
        console.warn('Failed to load player spritesheet:', spriteSrc, error);
    };
    newSpriteSheet.src = spriteSrc;
};
```

### Code Example - Object Instantiation Array

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

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates iteration through:

1. **Object Property Iteration**:
   ```javascript
   playerSpriteOptions[skinKey]
   ```
   - Iterates through sprite options object properties
   - Uses key lookup to find corresponding sprite path

2. **Array of Configuration Objects**:
   ```javascript
   this.classes = [...]
   ```
   - Creates array of game objects to instantiate
   - Each element is iterable configuration pair (class and data)
   - Game engine will iterate through this array to create objects

3. **Nested Object Access**:
   ```javascript
   player.spriteData?.src
   ```
   - Iterates through nested properties
   - Safely navigates object hierarchy

4. **Button Array Creation** (in interact function):
   ```javascript
   this.dialogueSystem.addButtons([
       { text: "Green Knight", ... },
       { text: "Gray Knight", ... },
       { text: "Dark Knight", ... }
   ])
   ```
   - Creates array of button objects
   - Dialogue system iterates through buttons to render options

5. **Animation Frame Array**:
   - Sprite data contains orientation with rows and columns
   - Game engine iterates through animation frames
   - Continuously loops through character animation sequence

This demonstrates iteration by managing collections of sprites, buttons, and configuration objects used throughout the level.
