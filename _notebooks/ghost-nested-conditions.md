# Ghost.js - Nested Conditions

## Requirement
**Nested Conditions** - Using multiple levels of conditional logic with conditions within conditions.

## Evidence
Ghost.js uses nested if/else statements to handle complex decision-making for AI pathfinding and direction determination.

### Code Example - Nested Conditionals for Direction

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

### Code Example - Nested Type Checking

```javascript
const playerCenter = typeof player.getCenter === 'function'
    ? player.getCenter()
    : { x: player.x || 0, y: player.y || 0 };
```

## How This Satisfies the Requirement

Ghost.js demonstrates nested conditions through:

1. **Guard Clause with Type Check**:
   ```javascript
   if (!player) return;
   
   const playerCenter = typeof player.getCenter === 'function'
       ? player.getCenter()
       : { x: player.x || 0, y: player.y || 0 };
   ```
   - First condition checks if player exists
   - Second condition (nested) checks method availability
   - Uses conditional operator for nested decision-making

2. **Distance-Based Decision with Nested Logic**:
   ```javascript
   if (distance <= this.followStopDistance) {
       this.velocity.x = 0;
       this.velocity.y = 0;
       return;
   }
   ```
   - Outer condition checks if close to player
   - Inner logic stops all velocity components
   - Prevents further processing via return

3. **Multi-Level Direction Determination**:
   ```javascript
   if (Math.abs(dx) >= Math.abs(dy)) {
       this.direction = dx >= 0 ? 'right' : 'left';
   } else {
       this.direction = dy >= 0 ? 'down' : 'up';
   }
   ```
   - Outer if/else compares magnitude of x vs y distance
   - Inner ternary operators for final direction
   - **Three levels of logic**:
     1. Compare which distance is larger
     2. Within each branch, check sign of distance
     3. Assign appropriate cardinal direction

4. **Nullish Coalescing in Nested Conditionals**:
   ```javascript
   const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
   ```
   - First condition: optional chaining on player.xVelocity
   - Nested condition: if undefined, calculate from gameEnv.innerWidth
   - Third condition: if innerWidth unavailable, use default 800
   - **Three levels of fallbacks**

5. **Complex Collision Check**:
   ```javascript
   if (player && !player.isDead) {
       this.followPlayer(player);
   }
   ```
   - Checks player existence (first level)
   - Nested check for player not dead (second level)
   - Calls followPlayer only if both conditions pass

This demonstrates competent nested conditional logic by using multiple decision levels to handle complex AI pathfinding scenarios.
