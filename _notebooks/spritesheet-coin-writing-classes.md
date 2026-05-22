# SpriteSheetCoin.js - Writing Classes

## Requirement
**Writing Classes** - Demonstrates the ability to define custom classes with properties and methods.

## Evidence
SpriteSheetCoin.js extends the base `Coin` class to create a collectible item that renders sprite images instead of colored circles.

### Code Example - Class Definition

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

	/**
	 * Load the sprite image asynchronously
	 */
	loadImage() {
		const img = new Image();
		img.onload = () => {
			this.spriteImage = img;
			this.isImageLoaded = true;
			console.log(`SpriteSheetCoin image loaded: ${this.spriteImagePath}`);
		};
		img.onerror = () => {
			console.warn(`Failed to load SpriteSheetCoin image: ${this.spriteImagePath}`);
			this.isImageLoaded = false;
		};
		img.src = this.spriteImagePath;
	}

	draw() {
		if (!this.ctx) return;
		
		// Clear the canvas
		this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
		
		if (this.collected) return;
		
		// Draw sprite image if loaded
		if (this.isImageLoaded && this.spriteImage) {
			this.drawSpriteImage();
		} else if (this.fallbackToCircle) {
			// Fall back to the original colored circle
			this.drawCircle();
		}
		
		// Call setupCanvas to position the canvas (normally done in Character.draw())
		this.setupCanvas();
	}

	/**
	 * Teleport to a new position and swap to a new frame for visual variety.
	 */
	randomizePosition() {
		let newX;
		let newY;
		let spawnLocation = null;

		if (Array.isArray(this.spawnLocations) && this.spawnLocations.length > 0) {
			const index = Math.floor(Math.random() * this.spawnLocations.length);
			spawnLocation = this.spawnLocations[index];
		}

		if (spawnLocation && Number.isFinite(spawnLocation.x) && Number.isFinite(spawnLocation.y)) {
			const isNormalized = spawnLocation.x >= 0 && spawnLocation.x <= 1
				&& spawnLocation.y >= 0 && spawnLocation.y <= 1;
			newX = isNormalized ? spawnLocation.x * this.gameEnv.innerWidth : spawnLocation.x;
			newY = isNormalized ? spawnLocation.y * this.gameEnv.innerHeight : spawnLocation.y;
		} else {
			const randX = Math.random() * 0.8 + 0.1;
			const randY = Math.random() * 0.8 + 0.1;
			newX = randX * this.gameEnv.innerWidth;
			newY = randY * this.gameEnv.innerHeight;
		}

		this.position.x = newX;
		this.position.y = newY;
		this.resize();
		this.applyTeleportAppearance();
	}
}
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates writing classes through:

1. **Class Declaration**: The `SpriteSheetCoin` class is explicitly defined using the `class` keyword, extending the `Coin` base class.

2. **Constructor**: Accepts `data` and `gameEnv` parameters and initializes multiple instance properties for image handling, sprite frames, and spawn locations.

3. **Instance Methods**: Multiple methods handle different responsibilities:
   - `loadImage()` - asynchronously loads sprite graphics
   - `draw()` - renders the coin with sprite or fallback graphics
   - `randomizePosition()` - moves coin to new location and updates appearance

4. **Instance Properties**: Maintains state for image data, sprite frame information, and spawn location configuration.

5. **Flexibility**: The class demonstrates good design by providing fallback behavior (showing a colored circle if sprite doesn't load) and customizable spawn locations.

The SpriteSheetCoin class shows solid class design by creating a flexible collectible object that manages sprite rendering, image loading, and position management.
