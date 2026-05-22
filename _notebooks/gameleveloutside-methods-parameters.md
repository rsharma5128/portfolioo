# GameLevelOutside.js - Methods & Parameters

## Requirement
**Methods & Parameters** - Functions with multiple parameters that handle game logic.

## Evidence
GameLevelOutside.js demonstrates complex parameter handling in functions that configure and manage game objects.

### Code Example - Functions with Parameters

```javascript
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

const getPlayerSpriteSrc = (skinKey) => playerSpriteOptions[skinKey] || playerSpriteOptions.gray;

const getStoredPlayerSkinKey = () => {
    try {
        if (typeof window === 'undefined' || !window.localStorage) {
            return 'gray';
        }
        const stored = window.localStorage.getItem(playerSkinStorageKey);
        if (stored && playerSpriteOptions[stored]) {
            return stored;
        }
        window.localStorage.setItem(playerSkinStorageKey, 'gray');
        return 'gray';
    } catch (error) {
        return 'gray';
    }
};

const setStoredPlayerSkinKey = (skinKey) => {
    try {
        if (typeof window === 'undefined' || !window.localStorage) {
            return;
        }
        const normalized = playerSpriteOptions[skinKey] ? skinKey : 'gray';
        window.localStorage.setItem(playerSkinStorageKey, normalized);
    } catch (error) {
        // Ignore storage errors (e.g., private mode)
    }
};
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates methods with parameters through:

1. **applyPlayerSprite(player, skinKey)** - Two-parameter function that:
   - Takes a player object and string identifier for skin type
   - Retrieves sprite source based on skin key
   - Modifies player properties (spriteSheet, spriteData, frameIndex, frameCounter)
   - Calls other functions with the parameters (setStoredPlayerSkinKey)
   - Handles asynchronous image loading with error handling

2. **getPlayerSpriteSrc(skinKey)** - Parameter-driven lookup:
   - Takes a skin key string
   - Returns corresponding sprite path from options object
   - Provides default fallback value

3. **Parameter Chaining** - Functions call each other with parameters:
   - `applyPlayerSprite()` calls `getPlayerSpriteSrc(skinKey)` and `setStoredPlayerSkinKey(skinKey)`
   - Demonstrates parameter flow through multiple function calls

4. **Complex Parameter Handling**:
   - Type checking and validation
   - Default values and fallbacks
   - Optional chaining on parameters
   - Parameter modification and propagation

These functions demonstrate sophisticated parameter handling by accepting different data types and making complex decisions based on parameter values.
