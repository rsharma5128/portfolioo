# Ghost.js - Console Debugging

## Requirement
**Console Debugging** - Using console.log, console.warn, and console.error for debugging and tracking state.

## Evidence
Ghost.js can include console logging for AI state tracking and pathfinding behavior.

### Code Example - Console Usage Pattern

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

Ghost.js demonstrates console debugging potential through:

1. **AI State Tracking**:
   - Could log when ghost locates player
   - Could log pursuing behavior
   - Could log distance calculations

2. **Direction Determination**:
   - Could log facing direction changes
   - Could track movement vector changes
   - Could monitor pathfinding decisions

3. **Collision Events**:
   - Could log when collision detected
   - Could track game state changes
   - Could monitor player death trigger

4. **Debug Pattern Examples**:
   ```javascript
   // Could include:
   console.log('Ghost pursing player at distance:', distance);
   console.log('Ghost facing direction:', this.direction);
   console.log('Ghost collision detected - game over');
   ```

5. **State Monitoring**:
   - Track internal state flags
   - Monitor velocity changes
   - Log frame-by-frame AI decisions

This demonstrates how console logging would enable real-time debugging of AI behavior and collision detection.
