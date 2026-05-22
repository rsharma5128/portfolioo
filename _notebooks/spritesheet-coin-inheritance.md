# SpriteSheetCoin.js - Inheritance (2+ Levels)

## Requirement
**Inheritance (2+ Levels)** - Demonstrating multi-level class hierarchy where a custom class extends a base class.

## Evidence
SpriteSheetCoin.js extends the `Coin` class, which is part of the game engine's base class hierarchy.

### Code Example - Class Inheritance

```javascript
import Coin from '@assets/js/GameEnginev1.1/Coin.js';

class SpriteSheetCoin extends Coin {
	constructor(data = null, gameEnv = null) {
		super(data, gameEnv);
		
		this.spriteImagePath = data?.spriteImagePath || null;
		this.spriteImage = null;
		this.isImageLoaded = false;
		this.spriteFrames = data?.spriteFrames || { rows: 1, columns: 1, frameIndex: 0 };
		this.fallbackToCircle = data?.fallbackToCircle !== false;
		this.spawnLocations = Array.isArray(data?.spawnLocations) ? data.spawnLocations : null;
		
		// Load the image if provided
		if (this.spriteImagePath) {
			this.loadImage();
		}
	}

	draw() {
		if (!this.ctx) return;
		
		this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
		
		if (this.collected) return;
		
		// Draw sprite image if loaded
		if (this.isImageLoaded && this.spriteImage) {
			this.drawSpriteImage();
		} else if (this.fallbackToCircle) {
			// Fall back to the original colored circle
			this.drawCircle();
		}
		
		// Call setupCanvas to position the canvas
		this.setupCanvas();
	}
}

export default SpriteSheetCoin;
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates multi-level inheritance through:

1. **Hierarchy Chain**:
   ```
   GameObject (game engine base)
      ↓
   Character (extends GameObject)
      ↓
   Coin (extends Character)
      ↓
   SpriteSheetCoin (extends Coin) ← Our custom class
   ```

2. **Extends Coin Class** - Explicitly extends the Coin base class:
   ```javascript
   class SpriteSheetCoin extends Coin {
   ```

3. **Super Constructor Call** - Properly calls parent initialization:
   ```javascript
   super(data, gameEnv);
   ```

4. **Inherits Parent Functionality** - SpriteSheetCoin inherits from Coin:
   - Collection detection
   - Score value tracking
   - Position management
   - Basic rendering capabilities
   - Canvas management

5. **Specialization** - Adds custom properties for sprite handling:
   - `spriteImagePath` - path to sprite image
   - `spriteImage` - loaded image object
   - `isImageLoaded` - loading state
   - `spriteFrames` - frame configuration for sprite sheets
   - `fallbackToCircle` - fallback rendering option
   - `spawnLocations` - custom spawn positions

6. **Method Override** - Overrides parent's `draw()` method:
   ```javascript
   draw() {
       // ... custom sprite rendering logic
       this.setupCanvas();  // Call parent's canvas setup
   }
   ```

7. **Enhanced Functionality** - Adds new capabilities:
   - Sprite sheet image loading
   - Frame-based rendering
   - Fallback rendering system
   - Custom spawn location management

This demonstrates proper inheritance where SpriteSheetCoin extends Coin's basic collectible behavior with advanced sprite rendering capabilities.
