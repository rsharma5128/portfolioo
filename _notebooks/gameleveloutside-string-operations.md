# GameLevelOutside.js - String Operations

## Requirement
**String Operations** - Using string manipulation and concatenation.

## Evidence
GameLevelOutside.js concatenates strings for file paths and dialogue assembly.

### Code Example - String Concatenation

```javascript
const image_src_floor = path + "/images/projects/castle-game/castleOutsideV2.png";

const playerSpriteOptions = {
    gray: path + "/images/projects/castle-game/grayKnight.png",
    green: path + "/images/projects/castle-game/greenKnight.png",
    dark: path + "/images/projects/castle-game/darkKnight.png"
};

const sir_morty = path + "/images/projects/castle-game/mortyKnight.png";

const sprite_src_closet = path + "/images/projects/castle-game/closet.png";

const gem_data = {
    spriteImagePath: path + '/images/projects/castle-game/gems.png'
};
```

### Code Example - String Property Access

```javascript
const getPlayerSpriteSrc = (skinKey) => playerSpriteOptions[skinKey] || playerSpriteOptions.gray;

const getStoredPlayerSkinKey = () => {
    try {
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
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates string operations through:

1. **String Concatenation**:
   ```javascript
   const image_src_floor = path + "/images/projects/castle-game/castleOutsideV2.png";
   ```
   - Uses `+` operator to combine base path with file path
   - Creates full asset URLs

2. **Multiple String Concatenations**:
   ```javascript
   path + "/images/projects/castle-game/grayKnight.png"
   path + "/images/projects/castle-game/greenKnight.png"
   path + "/images/projects/castle-game/darkKnight.png"
   ```
   - Repeatedly concatenates for different sprites

3. **String Property Access**:
   ```javascript
   playerSpriteOptions[skinKey]
   ```
   - Accesses string properties by key
   - Returns stored string paths

4. **String Fallback**:
   ```javascript
   playerSpriteOptions[skinKey] || playerSpriteOptions.gray
   ```
   - Uses OR operator to fall back to gray sprite
   - Returns default string if key not found

This demonstrates string concatenation and manipulation for asset path construction.
