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

## Quick Concept
The ghost uses axis selection to decide its facing direction by comparing horizontal and vertical distances. It picks the larger absolute delta (|dx| vs |dy|) and chooses left/right when horizontal is larger or up/down when vertical is larger. This simple heuristic selects a primary movement/facing axis without needing full pathfinding.

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

## Code Example - Class Definition with Inheritance

```javascript
import Enemy from '@assets/js/GameEnginev1.1/essentials/Enemy.js';
import Player from '@assets/js/GameEnginev1.1/essentials/Player.js';
import showDeathScreen from './DeathScreen.js';

class Ghost extends Enemy {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
        this.followStopDistance = data?.followStopDistance ?? 8;
        this._hasTriggeredDeath = false;
    }

    getPlayer() {
        return this.gameEnv?.gameObjects?.find(obj => obj instanceof Player) || null;
    }

    followPlayer(player) {
        if (!player) return;

        const ghostCenter = this.getCenter();
        const playerCenter = typeof player.getCenter === 'function'
            ? player.getCenter()
            : { x: player.x || 0, y: player.y || 0 };

        const dx = playerCenter.x - ghostCenter.x;
        const dy = playerCenter.y - ghostCenter.y;
        const distance = Math.hypot(dx, dy);

        if (distance <= this.followStopDistance) {
            this.velocity.x = 0;
            this.velocity.y = 0;
            return;
        }

        const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
        const speed = Math.max(0.3, baseSpeed * this.followSpeedFactor);
        const nx = dx / distance;
        const ny = dy / distance;

        this.position.x += nx * speed;
        this.position.y += ny * speed;

        if (Math.abs(dx) >= Math.abs(dy)) {
            this.direction = dx >= 0 ? 'right' : 'left';
        } else {
            this.direction = dy >= 0 ? 'down' : 'up';
        }
    }

    update() {
        const player = this.getPlayer();
        if (player && !player.isDead) {
            this.followPlayer(player);
        }
        super.update();
    }

    handleCollisionEvent() {
        if (this._hasTriggeredDeath || this.playerDestroyed) return;

        const player = this.getPlayer();
        if (!player || player.isDead) return;

        this._hasTriggeredDeath = true;
        this.playerDestroyed = true;
        player.isDead = true;

        showDeathScreen(player, 'The ghost caught you.');
    }
}

export default Ghost;
```

## Key Features Demonstrated

1. **Class Definition**: `class Ghost extends Enemy` - shows inheritance syntax
2. **Constructor Chaining**: `super(data, gameEnv)` - calls parent constructor
3. **Method Overriding**: `update()` method overrides parent implementation
4. **Method Implementation**: `followPlayer()`, `getPlayer()`, `handleCollisionEvent()`
5. **Distance Calculation**: `Math.hypot(dx, dy)` for accurate distance
6. **Direction Logic**: Nested conditionals to determine ghost facing direction
