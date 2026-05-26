---
layout: post
title: "CS111: Custom Class - SpriteSheetCoin (Collectible)"
description: SpriteSheetCoin class extending Coin with sprite sheet animation
permalink: /cs111-spritesheet-coin-class
author: Rohan Sharma
---

<div style="position:fixed;top:5.5rem;left:1rem;z-index:99999;">
  <a href="/cs111-objectives" style="display:inline-block;padding:1.1rem 1.4rem;background:#ff4d4d;color:#fff;border-radius:1rem;text-decoration:none;font-weight:900;font-size:1rem;letter-spacing:0.03em;box-shadow:0 8px 24px rgba(0,0,0,0.3);border:2px solid rgba(255,255,255,0.9);">Go back to homepage</a>
</div>

## SpriteSheetCoin Class: Collectible

### Overview
The SpriteSheetCoin class extends the Coin base class to implement collectible items with sprite sheet animation. This demonstrates inheritance, asynchronous image loading, and sprite rendering.

### File Location
`_projects/games/castle-game/levels/SpriteSheetCoin.js`

## Quick Concept
Asynchronous image loading means starting an image request and continuing execution while the file downloads. The code listens for an onload or resolves a promise when the image is ready, avoiding frame freezes. This pattern ensures sprites render only after resources are available and allows graceful fallbacks.

### Class Hierarchy
```
GameObject (base engine class)
  ↓
  Coin (game engine class)
    ↓
    SpriteSheetCoin (custom class)
```

### Key Features
- **Inheritance**: Extends Coin class for collectible behavior
- **Sprite Sheet Rendering**: Animates coins using sprite frames
- **Async Image Loading**: Handles image loading asynchronously
- **Fallback Rendering**: Graceful degradation if sprites unavailable
- **Frame Animation**: Cycles through sprite frames for animation

### Methods
- `constructor(data, gameEnv)` - Initializes coin with sprite configuration
- `loadSpriteSheet()` - Asynchronously loads sprite sheet image
- `draw()` - Overridden to render sprite frame instead of basic shape
- `update()` - Updates animation frame

### Properties
- `spriteImage` - Loaded sprite sheet Image object
- `currentFrame` - Current animation frame index
- `frameWidth`, `frameHeight` - Dimensions of individual sprites
- `animationSpeed` - Speed of frame cycling

### Technical Implementation
- Image object with onload callback for async loading
- Sprite coordinate calculation for frame rendering
- Canvas drawImage() with source region
- Error handling for image load failures

## Code Example - Class Definition with Inheritance

```javascript
import Coin from '@assets/js/GameEnginev1.1/Coin.js';

/**
 * SpriteSheetCoin extends the basic Coin class to support image/spritesheet rendering.
 * Instead of a colored circle, you can now display any image asset (gem, star, etc).
 */
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

	/**
	 * Draw the coin using spritesheet if available, otherwise fall back to colored circle
	 */
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
	 * Draw the sprite image on the canvas
	 */
	drawSpriteImage() {
		const { rows, columns, frameIndex } = this.spriteFrames;
		
		// Calculate frame dimensions
		const frameWidth = this.spriteImage.width / columns;
		const frameHeight = this.spriteImage.height / rows;
		
		// Calculate which frame to display based on frameIndex
		const currentFrameIndex = frameIndex % (rows * columns);
		const row = Math.floor(currentFrameIndex / columns);
		const col = currentFrameIndex % columns;
		
		const sourceX = col * frameWidth;
		const sourceY = row * frameHeight;
		
		// Draw the sprite frame centered on the canvas
		const centerX = this.canvas.width / 2;
		const centerY = this.canvas.height / 2;
		const drawWidth = this.canvas.width;
		const drawHeight = this.canvas.height;
		
		this.ctx.drawImage(
			this.spriteImage,
			sourceX, sourceY,           // Source position
			frameWidth, frameHeight,    // Source size
			centerX - drawWidth / 2, centerY - drawHeight / 2, // Destination position (centered)
			drawWidth, drawHeight       // Destination size
		);
	}

	/**
	 * Draw the fallback colored circle (original Coin behavior)
	 */
	drawCircle() {
		this.ctx.fillStyle = this.color;
		const centerX = this.canvas.width / 2;
		const centerY = this.canvas.height / 2;
		const radius = Math.min(this.canvas.width, this.canvas.height) / 3;
		
		this.ctx.beginPath();
		this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
		this.ctx.fill();
		
		// Add a border to make it more visible
		this.ctx.strokeStyle = '#B8860B'; // Dark gold
		this.ctx.lineWidth = 2;
		this.ctx.stroke();
	}
}

export default SpriteSheetCoin;
```

## Key Features Demonstrated

1. **Class Definition**: `class SpriteSheetCoin extends Coin` - shows inheritance syntax
2. **Constructor Chaining**: `super(data, gameEnv)` - calls parent constructor
3. **Asynchronous Image Loading**: `loadImage()` method with Image onload/onerror callbacks (lines 26-36)
4. **Method Overriding**: `draw()` method overrides parent implementation with conditional logic
5. **Fallback Pattern**: Checks if image loaded, falls back to circle rendering if not (lines 50-54)
6. **Canvas API Usage**: `drawImage()`, `arc()`, `fillStyle`, `fillPath()` for rendering
7. **JSDoc Comments**: Comprehensive documentation for class and methods
