# DeathBarrier.js - Boolean Operators

## Requirement
**Boolean Operators** - Using logical operators (AND, OR, NOT) to combine and evaluate conditions.

## Evidence
DeathBarrier.js uses boolean operators for safety checks and state management.

### Code Example - Boolean Operators

```javascript
update() {
    super.update();

    if (this._hasTriggeredDeath) return;

    const player = this.gameEnv?.gameObjects?.find(obj => obj.constructor?.name === 'Player');
    if (!player || !player.canvas || !this.canvas) return;

    this.isCollision(player);

    if (this.collisionData?.hit) {
        const timeSinceLevelStart = new Date() - DeathBarrier.levelStartTime;
        if (timeSinceLevelStart < 500) {
            console.log('[MazeDebug] Grace period active:', timeSinceLevelStart, 'ms');
            return;
        }

        this._hasTriggeredDeath = true;
        player.isDead = true;

        console.log('[MazeDebug] DeathBarrier hit player:', this.canvas?.id || this.id || 'unknown');
        console.log('[MazeDebug] Player Position:', player.x, player.y);

        try {
            showDeathScreen(player, 'You got lost in the maze.');
        } catch (error) {
            console.error('DeathBarrier failed to show death screen:', error);
            this._hasTriggeredDeath = false;
            player.isDead = false;
        }
    }
}

constructor(data, gameEnv) {
    super(data, gameEnv);
    this._hasTriggeredDeath = false;
    if (!DeathBarrier.levelStartTime) {
        DeathBarrier.levelStartTime = new Date();
    }
}
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates boolean operators through:

1. **NOT Operator (!) - Early Exit**:
   ```javascript
   if (this._hasTriggeredDeath) return;
   ```
   - Exits early if death already triggered

2. **NOT Operator (!) - Null Checks**:
   ```javascript
   if (!player || !player.canvas || !this.canvas) return;
   ```
   - Uses `!` to check for falsy/null values
   - Exits if player, player.canvas, or barrier canvas are missing

3. **OR Operator (||) - Multiple Conditions**:
   ```javascript
   if (!player || !player.canvas || !this.canvas) return;
   ```
   - Returns if ANY of the three conditions are true
   - **Three-way OR condition**

4. **Optional Chaining with Property Check**:
   ```javascript
   if (this.collisionData?.hit) {
   ```
   - Uses `?.` for safe property access
   - Checks if hit property is truthy

5. **OR Operator (||) - Fallback Values**:
   ```javascript
   console.log('[MazeDebug] DeathBarrier hit player:', this.canvas?.id || this.id || 'unknown');
   ```
   - First tries canvas.id
   - Falls back to barrier id
   - Falls back to 'unknown' string
   - **Three-level OR fallback chain**

6. **NOT Operator (!) - Conditional Initialization**:
   ```javascript
   if (!DeathBarrier.levelStartTime) {
       DeathBarrier.levelStartTime = new Date();
   }
   ```
   - Initializes only if NOT already initialized
   - Prevents overwriting existing time

This demonstrates effective use of boolean operators for robust null checking and fallback handling.
