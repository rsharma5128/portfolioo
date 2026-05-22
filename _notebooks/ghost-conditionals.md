# Ghost.js - Conditionals (if/else)

## Requirement
**Conditionals (if/else)** - Using if/else statements to make decisions and control program flow.

## Evidence
Ghost.js uses multiple conditional branches to control AI behavior, collision detection, and player pursuit.

### Code Example - Multiple Conditionals

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
```

## How This Satisfies the Requirement

Ghost.js demonstrates conditionals through:

1. **Guard Clauses** (Early Returns):
   ```javascript
   if (!player) return;
   ```
   - Checks if player exists before continuing
   - Returns early if condition fails
   - Prevents null reference errors

2. **Distance-Based Decision**:
   ```javascript
   if (distance <= this.followStopDistance) {
       this.velocity.x = 0;
       this.velocity.y = 0;
       return;
   }
   ```
   - Stops ghost movement when close enough to player
   - Different behavior based on distance threshold

3. **Type Checking**:
   ```javascript
   typeof player.getCenter === 'function' ? player.getCenter() : { x: player.x || 0, y: player.y || 0 }
   ```
   - Ternary conditional for method availability
   - Provides fallback if method doesn't exist

4. **Direction Logic**:
   ```javascript
   if (Math.abs(dx) >= Math.abs(dy)) {
       this.direction = dx >= 0 ? 'right' : 'left';
   } else {
       this.direction = dy >= 0 ? 'down' : 'up';
   }
   ```
   - Determines facing direction based on distance components
   - Multiple conditional branches for cardinal directions

5. **Update Condition**:
   ```javascript
   if (player && !player.isDead) {
       this.followPlayer(player);
   }
   ```
   - Only pursues if player exists and is alive
   - Stops AI when player dies

6. **Collision Response**:
   ```javascript
   if (this._hasTriggeredDeath || this.playerDestroyed) return;
   if (!player || player.isDead) return;
   ```
   - Multiple guards to prevent duplicate death triggers
   - Safely handles null and dead states

This demonstrates competent use of conditionals for controlling ghost behavior, decision-making, and error prevention.
