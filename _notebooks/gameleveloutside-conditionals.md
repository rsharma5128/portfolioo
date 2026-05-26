# GameLevelOutside.js - Conditionals (if/else)

## Requirement
**Conditionals (if/else)** - Using if/else statements to make decisions and control program flow.

## Evidence
GameLevelOutside.js uses conditionals for configuration checks, fallback logic, and gameplay decisions.

### Code Example - Conditional Configuration

```javascript
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

### Code Example - Conditional Sprite Selection

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
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates conditionals through:

1. **Environment Check**:
   ```javascript
   if (typeof window === 'undefined' || !window.localStorage) {
       return 'gray';
   }
   ```
   - Checks if browser window exists
   - Returns default if not available

2. **Storage Retrieval with Conditional**:
   ```javascript
   const stored = window.localStorage.getItem(playerSkinStorageKey);
   if (stored && playerSpriteOptions[stored]) {
       return stored;
   }
   ```
   - Checks if value exists AND is valid key
   - AND operator requires both conditions

3. **Sprite Source Fallback**:
   ```javascript
   const normalized = playerSpriteOptions[skinKey] ? skinKey : 'gray';
   ```
   - Ternary operator for conditional assignment
   - Uses provided key if valid, otherwise gray

4. **Player Validation Check**:
   ```javascript
   if (!player || !spriteSrc) return;
   ```
   - Returns if player missing OR sprite source missing
   - Guard clause prevents further execution

5. **Duplicate Prevention**:
   ```javascript
   if (player.spriteData?.src === spriteSrc) {
       setStoredPlayerSkinKey(skinKey);
       return;
   }
   ```
   - Checks if already loaded
   - Returns early if no change needed
   - Prevents redundant loading

This demonstrates conditional logic for configuration, validation, and duplicate prevention.
