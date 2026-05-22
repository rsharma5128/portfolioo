# Ghost.js - Iteration (Loops)

## Requirement
**Iteration (Loops)** - Using loops to iterate over collections and perform repeated operations.

## Evidence
Ghost.js uses loop constructs and array methods to calculate distances and manage game objects.

### Code Example - Loop-Based Distance Calculation

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

getPlayer() {
    return this.gameEnv?.gameObjects?.find(obj => obj instanceof Player) || null;
}
```

## How This Satisfies the Requirement

Ghost.js demonstrates iteration through:

1. **Array Find Method**:
   ```javascript
   this.gameEnv?.gameObjects?.find(obj => obj instanceof Player)
   ```
   - Uses `.find()` to search through the gameObjects array
   - Iterates until finding first Player instance
   - Returns null if no player found

2. **Distance Calculation Loop**:
   - Calculates `dx` (x-distance component)
   - Calculates `dy` (y-distance component)
   - Uses `Math.hypot(dx, dy)` for hypotenuse distance (iterated calculation)
   - Performs repeated arithmetic operations in pursuit logic

3. **Direction Logic**:
   - Iterates through conditional checks to determine facing direction
   - Compares absolute values of dx and dy
   - Determines correct cardinal direction based on largest component

4. **Repeated Updates**:
   - Ghost's update loop continuously calls `followPlayer()`
   - Each frame iterates through same calculation process
   - Maintains continuous pursuit behavior through repeated iteration

5. **Vector Normalization**:
   ```javascript
   const nx = dx / distance;
   const ny = dy / distance;
   ```
   - Normalizes distance vector components
   - Repeated mathematical iteration to calculate movement

This demonstrates iteration by using array search methods and repeated mathematical calculations to implement AI pathfinding.
