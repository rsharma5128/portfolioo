# Ghost.js - Mathematical Operators

## Requirement
**Mathematical Operators** - Using mathematical operations for calculations and computations.

## Evidence
Ghost.js uses mathematical operators for distance calculations, speed calculations, and coordinate transformations.

### Code Example - Mathematical Operations

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

Ghost.js demonstrates mathematical operators through:

1. **Subtraction (Distance Components)**:
   ```javascript
   const dx = playerCenter.x - ghostCenter.x;
   const dy = playerCenter.y - ghostCenter.y;
   ```
   - Calculates x and y distance components
   - Subtracts ghost position from player position

2. **Hypotenuse Calculation**:
   ```javascript
   const distance = Math.hypot(dx, dy);
   ```
   - Calculates Euclidean distance from components
   - Uses built-in Math.hypot() function

3. **Division (Speed Calculation)**:
   ```javascript
   const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
   ```
   - Divides viewport width by 2000
   - Calculates default speed based on screen size

4. **Vector Normalization (Division)**:
   ```javascript
   const nx = dx / distance;
   const ny = dy / distance;
   ```
   - Divides distance components by total distance
   - Normalizes to -1 to 1 range

5. **Multiplication (Speed Application)**:
   ```javascript
   const speed = Math.max(0.3, baseSpeed * this.followSpeedFactor);
   this.position.x += nx * speed;
   this.position.y += ny * speed;
   ```
   - Multiplies base speed by factor
   - Multiplies normalized vector by speed
   - Applies movement each frame

6. **Addition (Position Update)**:
   ```javascript
   this.position.x += nx * speed;
   this.position.y += ny * speed;
   ```
   - Uses `+=` to add movement to position
   - Accumulates movement over frames

7. **Absolute Value (Magnitude Comparison)**:
   ```javascript
   if (Math.abs(dx) >= Math.abs(dy)) {
   ```
   - Uses Math.abs() to get absolute values
   - Compares magnitudes to determine primary axis

8. **Comparison Operations**:
   ```javascript
   if (distance <= this.followStopDistance) {
   if (Math.abs(dx) >= Math.abs(dy)) {
   ```
   - Uses <= and >= for numeric comparisons

This demonstrates comprehensive use of mathematical operators for AI pathfinding physics.
