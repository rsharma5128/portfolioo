---
layout: post
title: "CS111: Custom Class - SpriteSheetCoin (Collectible)"
description: SpriteSheetCoin class extending Coin with sprite sheet animation
permalink: /cs111-spritesheet-coin-class
author: Rohan Sharma
---

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
