# Ghost.js - Numbers (Data Type)

## Requirement
**Numbers** - Using numeric data types for calculations, comparisons, and game logic.

## Evidence
Ghost.js uses numbers extensively for position tracking, velocity management, distance calculations, and speed factors.

### Code Example - Numeric Properties and Calculations

```javascript
constructor(data, gameEnv) {
    super(data, gameEnv);
    this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
    this.followStopDistance = data?.followStopDistance ?? 8;
    this._hasTriggeredDeath = false;
}

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

Ghost.js demonstrates numbers through:

1. **Floating-Point Configuration**:
   ```javascript
   this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
   ```
   - Uses decimal (0.4) for precise speed multiplier
   - Default value if not provided

2. **Integer Threshold**:
   ```javascript
   this.followStopDistance = data?.followStopDistance ?? 8;
   ```
   - Uses integer (8) for distance threshold
   - Determines how close ghost gets to player

3. **Coordinate Calculations**:
   ```javascript
   const dx = playerCenter.x - ghostCenter.x;
   const dy = playerCenter.y - ghostCenter.y;
   ```
   - Arithmetic operations on position numbers
   - Calculates difference vectors

4. **Distance Calculation**:
   ```javascript
   const distance = Math.hypot(dx, dy);
   ```
   - Uses Math.hypot() for Euclidean distance
   - Returns single numeric distance value

5. **Distance Comparison**:
   ```javascript
   if (distance <= this.followStopDistance) {
   ```
   - Numeric comparison operator

6. **Velocity Components**:
   ```javascript
   this.velocity.x = 0;
   this.velocity.y = 0;
   ```
   - Sets velocity numbers to zero

7. **Speed Calculation**:
   ```javascript
   const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
   const speed = Math.max(0.3, baseSpeed * this.followSpeedFactor);
   ```
   - Divides viewport width by 2000 for base speed
   - Uses Math.max() to enforce minimum 0.3 speed
   - Multiplies by followSpeedFactor

8. **Vector Normalization**:
   ```javascript
   const nx = dx / distance;
   const ny = dy / distance;
   ```
   - Divides distance components to normalize (-1 to 1)

9. **Position Update**:
   ```javascript
   this.position.x += nx * speed;
   this.position.y += ny * speed;
   ```
   - Multiplies normalized vector by speed
   - Adds to current position for smooth movement

10. **Absolute Value Comparison**:
    ```javascript
    if (Math.abs(dx) >= Math.abs(dy)) {
    ```
    - Uses Math.abs() for magnitude comparison
    - Determines primary movement axis

This demonstrates extensive use of numeric data types for physics calculations, configuration, and AI behavior.
