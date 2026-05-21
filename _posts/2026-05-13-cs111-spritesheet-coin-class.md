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

## Code Example
```javascript
async loadSpriteSheet(src) {
  this.spriteImage = new Image();
  await new Promise((res, rej) => {
    this.spriteImage.onload = res;
    this.spriteImage.onerror = rej;
    this.spriteImage.src = src;
  });
  this.loaded = true;
}

draw(ctx) {
  if (!this.loaded) return super.draw(ctx);
  const fw = this.frameWidth;
  ctx.drawImage(this.spriteImage, this.currentFrame * fw, 0, fw, this.frameHeight, this.x, this.y, fw, this.frameHeight);
}
```
