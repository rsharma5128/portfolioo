# Ghost.js - Method Overriding

## Requirement
**Method Overriding** - Overriding parent class methods with custom implementations to provide specialized behavior.

## Evidence
Ghost.js overrides the parent `Enemy` class's `update()` method with custom AI pathfinding logic.

### Code Example - Method Override

```javascript
update() {
    const player = this.getPlayer();
    if (player && !player.isDead) {
        this.followPlayer(player);
    }
    super.update();
}
```

### Code Example - Custom Collision Handling

```javascript
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

### Code Example - followPlayer Method (Custom Addition)

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

## How This Satisfies the Requirement

Ghost.js demonstrates method overriding through:

1. **Override update() Method**:
   - Parent Enemy class has a default `update()` that handles basic animation and movement
   - Ghost overrides this to add custom logic before calling the parent implementation

2. **Custom Game Logic**:
   - Instead of random movement, Ghost implements AI pathfinding via `followPlayer()`
   - The ghost actively pursues the player each frame
   - Only calls `super.update()` after custom logic executes

3. **Direction-Based Behavior**:
   - Ghost calculates which direction to face based on player location
   - Updates `this.direction` to control animation rendering
   - Provides proper facing direction for visual feedback

4. **Custom Collision Response**:
   - Overrides default collision handling with `handleCollisionEvent()`
   - Instead of generic collision, triggers game-over screen
   - Manages state to prevent multiple death triggers

5. **Specialized Behavior Chain**:
   - `update()` calls `followPlayer()` before parent update
   - Creates a specialized NPC that hunts the player actively
   - Demonstrates pattern of "pre-processing" before parent method call

This demonstrates competent method overriding where Ghost replaces the default Enemy update logic with specialized ghost-specific AI behavior.
