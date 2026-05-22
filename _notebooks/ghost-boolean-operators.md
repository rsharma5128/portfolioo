# Ghost.js - Boolean Operators

## Requirement
**Boolean Operators** - Using logical operators (AND, OR, NOT) to combine and evaluate conditions.

## Evidence
Ghost.js uses boolean operators extensively for condition evaluation and game logic.

### Code Example - Boolean Operators

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

Ghost.js demonstrates boolean operators through:

1. **NOT Operator (!)**:
   ```javascript
   if (!player) return;
   ```
   - Negates player existence check
   - Returns if player is falsy/null

2. **OR Operator (||) - Fallback Chain**:
   ```javascript
   { x: player.x || 0, y: player.y || 0 }
   ```
   - Uses `||` for null coalescing
   - Provides 0 as default if x/y are falsy

3. **OR Operator (||) - Default Value**:
   ```javascript
   const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
   ```
   - First tries player velocity
   - Falls back to calculated speed
   - Falls back to 800 if width unavailable
   - **Three-level fallback chain**

4. **AND Operator (&&)**:
   ```javascript
   if (player && !player.isDead) {
       this.followPlayer(player);
   }
   ```
   - Player must exist AND not be dead
   - Both conditions must be true

5. **OR Operator (||) - Multiple Conditions**:
   ```javascript
   if (this._hasTriggeredDeath || this.playerDestroyed) return;
   ```
   - Returns if EITHER condition is true
   - Exits if death triggered OR player destroyed

6. **NOT Operator (!) - Complex Negation**:
   ```javascript
   if (!player || player.isDead) return;
   ```
   - Returns if player is falsy OR if player.isDead is true
   - Logical: "return if no player OR if dead"

7. **Ternary Operator with Comparison**:
   ```javascript
   this.direction = dx >= 0 ? 'right' : 'left';
   ```
   - Uses comparison (>=) with ternary
   - IF dx >= 0, set to 'right', ELSE 'left'

This demonstrates skilled use of boolean operators for complex conditional logic in AI behavior.
