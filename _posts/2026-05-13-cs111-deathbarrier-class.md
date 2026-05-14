---
layout: post
title: "CS111: Custom Class - DeathBarrier (Collision Trigger)"
description: DeathBarrier class extending Barrier with collision-triggered death
permalink: /cs111-deathbarrier-class
author: Rohan Sharma
---

## DeathBarrier Class: Collision Trigger

### Overview
The DeathBarrier class extends the Barrier base class to implement collision-triggered death barriers. This demonstrates inheritance, collision handling, and game state management.

### File Location
`_projects/games/castle-game/levels/DeathBarrier.js`

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
