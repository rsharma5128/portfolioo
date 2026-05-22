# SpriteSheetCoin.js - JSDoc Comments

## Requirement
**JSDoc Comments** - Comprehensive documentation using JSDoc comment syntax.

## Evidence
SpriteSheetCoin.js includes extensive JSDoc documentation for all methods.

### Code Example - JSDoc Documentation

```javascript
/**
 * SpriteSheetCoin extends the basic Coin class to support image/spritesheet rendering.
 * Instead of a colored circle, you can now display any image asset (gem, star, etc).
 * 
 * @example
 * const gemCoin = new SpriteSheetCoin({
 *   id: 'gem-coin',
 *   INIT_POSITION: { x: 0.5, y: 0.5 },
 *   SCALE_FACTOR: 30,
 *   value: 5,
 *   spriteImagePath: '/images/gem.png',
 *   spriteFrames: { rows: 2, columns: 2, frameIndex: 0 }
 * }, gameEnv);
 */
class SpriteSheetCoin extends Coin {

	/**
	 * Load the sprite image asynchronously
	 */
	loadImage() {
		// ... implementation
	}

	/**
	 * Draw the coin using spritesheet if available, otherwise fall back to colored circle
	 */
	draw() {
		// ... implementation
	}

	/**
	 * Draw the sprite image on the canvas
	 */
	drawSpriteImage() {
		// ... implementation
	}

	/**
	 * Draw the fallback colored circle (original Coin behavior)
	 */
	drawCircle() {
		// ... implementation
	}

	/**
	 * Teleport to a new position and swap to a new frame for visual variety.
	 */
	randomizePosition() {
		// ... implementation
	}

	/**
	 * Update the frame index if using animation frames
	 * Call this to animate through spritesheet frames
	 * @param {number} frameIndex - The frame index to display
	 */
	setFrameIndex(frameIndex) {
		this.spriteFrames.frameIndex = frameIndex;
	}

	/**
	 * Change the sprite image
	 * @param {string} imagePath - Path to the new image
	 */
	setSprite(imagePath) {
		// ... implementation
	}

	/**
	 * Get whether the sprite image is ready to render
	 */
	isSpriteReady() {
		return this.isImageLoaded && this.spriteImage !== null;
	}
}
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates JSDoc documentation through:

1. **Class Documentation with Example**:
   ```javascript
   /**
    * SpriteSheetCoin extends the basic Coin class...
    * @example
    * const gemCoin = new SpriteSheetCoin({...}, gameEnv);
    */
   ```
   - @example tag with usage code
   - Shows how to use the class

2. **Method Documentation**:
   ```javascript
   /**
    * Load the sprite image asynchronously
    */
   loadImage() {
   ```
   - Brief description of method purpose

3. **Complex Method Documentation**:
   ```javascript
   /**
    * Update the frame index if using animation frames
    * Call this to animate through spritesheet frames
    * @param {number} frameIndex - The frame index to display
    */
   ```
   - Detailed explanation of behavior
   - @param for parameters with type

4. **Return Value Documentation**:
   ```javascript
   /**
    * Get whether the sprite image is ready to render
    */
   isSpriteReady() {
   ```
   - Describes return value purpose

This demonstrates comprehensive JSDoc documentation for public API methods.
