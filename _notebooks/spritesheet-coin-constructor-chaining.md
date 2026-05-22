# SpriteSheetCoin.js - Constructor Chaining

## Requirement
**Constructor Chaining** - Using `super()` to initialize parent class properties and call parent constructors.

## Evidence
SpriteSheetCoin.js uses `super()` to properly initialize the parent `Coin` class before adding sprite-rendering properties.

### Code Example - Constructor with Super Call

```javascript
class SpriteSheetCoin extends Coin {
	constructor(data = null, gameEnv = null) {
		super(data, gameEnv);
		
		this.spriteImagePath = data?.spriteImagePath || null;
		this.spriteImage = null;
		this.isImageLoaded = false;
		this.spriteFrames = data?.spriteFrames || { rows: 1, columns: 1, frameIndex: 0 };
		this.fallbackToCircle = data?.fallbackToCircle !== false; // Default true
		this.spawnLocations = Array.isArray(data?.spawnLocations) ? data.spawnLocations : null;
		
		// Load the image if provided
		if (this.spriteImagePath) {
			this.loadImage();
		}
	}
}
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates constructor chaining through:

1. **Super Call First**:
   ```javascript
   super(data, gameEnv);
   ```
   - Immediately calls parent Coin class constructor
   - Passes required `data` and `gameEnv` parameters up the chain
   - Ensures all parent collection and position logic initializes

2. **Constructor Chain Flow**:
   ```
   SpriteSheetCoin.constructor(data, gameEnv)
      ↓
   super(data, gameEnv)  [calls Coin constructor]
      ↓
   Coin passes to Character, Character passes to GameObject
      ↓
   All parent classes initialize value, position, canvas
      ↓
   SpriteSheetCoin adds sprite rendering properties
   ```

3. **Parent Initialization**:
   - Coin class initializes value tracking and collection detection
   - Character class initializes sprite data and canvas management
   - GameObject initializes transform and base properties
   - All parent functionality available after `super()` call

4. **Child-Specific Properties** (Added After Super):
   - `spriteImagePath` - URL to sprite image asset
   - `spriteImage` - loaded Image object reference
   - `isImageLoaded` - boolean flag for load state
   - `spriteFrames` - object with rows, columns, frameIndex for sprite sheet
   - `fallbackToCircle` - boolean for rendering fallback
   - `spawnLocations` - array of possible spawn positions

5. **Conditional Initialization**:
   ```javascript
   if (this.spriteImagePath) {
       this.loadImage();
   }
   ```
   - Asynchronously loads sprite image if path provided
   - Shows initialization can trigger additional setup
   - Demonstrates proper async handling in constructor

6. **Optional Parameters**:
   ```javascript
   constructor(data = null, gameEnv = null)
   ```
   - Both parameters are optional with defaults
   - Safely passes to parent even if null
   - Parent handles null cases appropriately

This demonstrates proper constructor chaining where SpriteSheetCoin correctly initializes its parent Coin hierarchy before adding sprite rendering capabilities and asynchronous image loading.
