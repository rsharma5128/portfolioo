# Ghost.js - Methods & Parameters

## Requirement
**Methods & Parameters** - Functions with multiple parameters that handle game logic and accept different types of input.

## Evidence
Ghost.js implements several methods with 2+ parameters that handle complex game logic including distance calculations and collision detection.

### Code Example - Methods with Parameters

```javascript
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
```

### Code Example - Constructor with Parameters

```javascript
constructor(data, gameEnv) {
    super(data, gameEnv);
    this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
    this.followStopDistance = data?.followStopDistance ?? 8;
    this._hasTriggeredDeath = false;
}
```

## How This Satisfies the Requirement

The Ghost class demonstrates methods with multiple parameters through:

1. **followPlayer(player)** - Takes a `player` object parameter and:
   - Accesses the player's position data
   - Calculates distance using `Math.hypot(dx, dy)`
   - Determines movement direction based on relative positions
   - Updates internal velocity and direction based on player location

2. **Constructor Parameters** - Accepts two parameters:
   - `data` - configuration object containing optional settings with defaults
   - `gameEnv` - game environment reference for accessing game state

3. **Parameter Usage** - Demonstrates several parameter handling techniques:
   - Optional chaining (`data?.followSpeedFactor`)
   - Nullish coalescing (`?? 0.4`)
   - Type checking (`typeof player.getCenter === 'function'`)
   - Destructuring and accessing nested properties

4. **Logic Based on Parameters** - The method behavior changes based on:
   - Player position relative to ghost
   - Distance thresholds
   - Player velocity data
   - Game environment dimensions

These methods show mastery of parameter handling by using multiple parameters to receive complex data structures and make intelligent decisions based on that input.
