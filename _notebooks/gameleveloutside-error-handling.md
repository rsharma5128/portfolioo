# GameLevelOutside.js - Error Handling

## Requirement
**Error Handling** - Using try/catch blocks for robustness and error recovery.

## Evidence
GameLevelOutside.js handles storage errors and network errors gracefully.

### Code Example - Error Handling for Storage

```javascript
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

const applyPlayerSprite = (player, skinKey) => {
    const spriteSrc = getPlayerSpriteSrc(skinKey);
    if (!player || !spriteSrc) return;
    
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

GameLevelOutside.js demonstrates error handling through:

1. **Storage Access Try/Catch**:
   ```javascript
   try {
       const stored = window.localStorage.getItem(playerSkinStorageKey);
       window.localStorage.setItem(playerSkinStorageKey, 'gray');
   } catch (error) {
       return 'gray';
   }
   ```
   - Catches localStorage access errors (private browsing mode)
   - Returns default value if storage fails
   - Prevents crashes in restricted environments

2. **Environment Checks**:
   ```javascript
   if (typeof window === 'undefined' || !window.localStorage) {
       return 'gray';
   }
   ```
   - Checks if window and localStorage exist
   - Prevents errors before try/catch

3. **Image Loading Error Handler**:
   ```javascript
   newSpriteSheet.onerror = (error) => {
       console.warn('Failed to load player spritesheet:', spriteSrc, error);
   };
   ```
   - Catches image load failures
   - Logs error without crashing
   - Allows game to continue

4. **Null/Default Checks**:
   ```javascript
   if (!player || !spriteSrc) return;
   const normalized = playerSpriteOptions[skinKey] ? skinKey : 'gray';
   ```
   - Validates data before use
   - Provides sensible defaults

This demonstrates comprehensive error handling for storage, network, and environment errors.
