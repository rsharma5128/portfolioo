---
layout: post
title: "CS111: Custom Class - DeathBarrier (Collision Trigger)"
description: DeathBarrier class extending Barrier with collision-triggered death
permalink: /cs111-deathbarrier-class
author: Rohan Sharma
---

<div style="position:fixed;top:5.5rem;left:1rem;z-index:99999;">
  <a href="/cs111-objectives" style="display:inline-block;padding:1.1rem 1.4rem;background:#ff4d4d;color:#fff;border-radius:1rem;text-decoration:none;font-weight:900;font-size:1rem;letter-spacing:0.03em;box-shadow:0 8px 24px rgba(0,0,0,0.3);border:2px solid rgba(255,255,255,0.9);">Go back to homepage</a>
</div>

## DeathBarrier Class: Collision Trigger

### Overview
The DeathBarrier class extends the Barrier base class to implement collision-triggered death barriers. This demonstrates inheritance, collision handling, and game state management.

### File Location
`_projects/games/castle-game/levels/DeathBarrier.js`

## Quick Concept
A "grace period" is a short time interval after an event during which repeated triggers are ignored. In collision handling it prevents immediate retriggering from jittery contact or overlapping frames. This helps avoid unfair double-deaths and gives the player a small recovery window.

### Class Hierarchy
```
GameObject (base engine class)
  ↓
  Barrier (game engine class)
    ↓
    DeathBarrier (custom class)
```

### Key Features
- **Inheritance**: Extends Barrier class for collision detection
- **Grace Period**: Implements delay before applying death penalty
- **Collision Detection**: Detects player collision with barrier
- **State Logging**: Tracks collisions for debugging
- **Level Management**: Triggers game over state

### Methods
- `constructor(data, gameEnv)` - Initializes barrier with configuration
- `update()` - Overridden to include grace period logic
- `handleCollision(player, direction)` - Detects player collision and triggers death
- `applyDeathPenalty()` - Handles death consequence

### Properties
- `gracePeriod` - Time delay before death penalty (in frames)
- `isActive` - Boolean tracking if barrier is active
- `collisionDetected` - Flag for collision state

### Technical Implementation
- Uses nested conditionals for complex collision logic
- Grace period prevents instant death on edge cases
- Boolean logic for state management
- Strategic console logging for debugging

## Code Example - Class Definition with Inheritance

```javascript
import Barrier from '@assets/js/GameEnginev1.1/essentials/Barrier.js';
import showDeathScreen from './DeathScreen.js';

class DeathBarrier extends Barrier {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this._hasTriggeredDeath = false;
        // Store the level start time - all barriers share this for grace period
        if (!DeathBarrier.levelStartTime) {
            DeathBarrier.levelStartTime = new Date();
        }
    }

    update() { // Checks for collisions, if triggered then uses the below code
        super.update();

        if (this._hasTriggeredDeath) return; // if the death is already triggered no need to trigger it again

        const player = this.gameEnv?.gameObjects?.find(obj => obj.constructor?.name === 'Player');
        if (!player || !player.canvas || !this.canvas) return;

        this.isCollision(player);

        if (this.collisionData?.hit) {
            // Check grace period from level start time
            const timeSinceLevelStart = new Date() - DeathBarrier.levelStartTime;
            if (timeSinceLevelStart < 500) {
                console.log('[MazeDebug] Grace period active:', timeSinceLevelStart, 'ms');
                return; // we added a grace period because there was an error where the barrier would kill the player before they could even play
            }

            this._hasTriggeredDeath = true;
            player.isDead = true;

            console.log('[MazeDebug] DeathBarrier hit player:', this.canvas?.id || this.id || 'unknown');
            console.log('[MazeDebug] Player Position:', player.x, player.y);

            try {
                showDeathScreen(player, 'You got lost in the maze.');
            } catch (error) {
                console.error('DeathBarrier failed to show death screen:', error);
                this._hasTriggeredDeath = false;
                player.isDead = false;
            }
        }
    }

    // Reset level start time when level restarts
    static resetLevelStartTime() {
        DeathBarrier.levelStartTime = new Date();
    }
}

export default DeathBarrier;
```

## Key Features Demonstrated

1. **Class Definition**: `class DeathBarrier extends Barrier` - shows inheritance syntax
2. **Constructor Chaining**: `super(data, gameEnv)` - calls parent constructor
3. **Grace Period Logic**: Nested conditionals with timestamp comparison (line 28-31)
4. **Method Overriding**: `update()` method overrides parent implementation
5. **Error Handling**: Try/catch block wrapping death screen display (lines 42-46)
6. **Static Method**: `resetLevelStartTime()` for class-level functionality
7. **Console Debugging**: Multiple console.log and console.error statements with [MazeDebug] tags
