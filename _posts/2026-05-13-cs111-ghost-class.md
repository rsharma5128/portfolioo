---
layout: post
title: "CS111: Custom Class - Ghost (Hostile NPC)"
description: Ghost class extending Enemy with AI pathfinding behavior
permalink: /cs111-ghost-class
author: Rohan Sharma
---

<div style="position:fixed;top:5.5rem;left:1rem;z-index:99999;">
  <a href="/cs111-objectives" style="display:inline-block;padding:1.1rem 1.4rem;background:#ff4d4d;color:#fff;border-radius:1rem;text-decoration:none;font-weight:900;font-size:1rem;letter-spacing:0.03em;box-shadow:0 8px 24px rgba(0,0,0,0.3);border:2px solid rgba(255,255,255,0.9);">Go back to homepage</a>
</div>

## Ghost Class: Hostile NPC

### Overview
The Ghost class extends the Enemy base class to implement a hostile NPC with pathfinding AI. This demonstrates inheritance, method overriding, and game AI implementation.

### File Location
`_projects/games/castle-game/levels/Ghost.js`

### Class Hierarchy
```
GameObject (base engine class)
  ↓
  Enemy (game engine class)
    ↓
    Ghost (custom class)
```

### Key Features
- **Inheritance**: Extends Enemy class for base hostile behavior
- **AI Pathfinding**: Implements followPlayer() method for enemy movement
- **Distance Calculation**: Uses Math.hypot() for accurate distance tracking
- **Collision Detection**: Handles collision with player and other entities
- **Death Handling**: Manages ghost elimination on player defeat

### Methods
- `constructor(data, gameEnv)` - Initializes ghost with game configuration
- `update()` - Overridden to include AI pathfinding logic
- `followPlayer()` - AI behavior to move toward player
- `handleCollision(other, direction)` - Custom collision logic

### Properties
- `velocity.x`, `velocity.y` - Movement speed in pixels/frame
- `isActive` - Boolean tracking if ghost is in play
- Direction flags for movement

### Technical Implementation
- Uses ES6 class syntax with extends
- Super() call ensures parent initialization
- Overrides parent methods for custom behavior
- Implements distance calculation with physics math
