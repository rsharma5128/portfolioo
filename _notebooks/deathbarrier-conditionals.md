# DeathBarrier.js - Conditionals (if/else)

## Requirement
**Conditionals (if/else)** - Using if/else statements to make decisions and control program flow.

## Evidence
DeathBarrier.js uses multiple conditional statements to control collision detection, grace periods, and death triggers.

### Code Example - Multiple Conditionals

```javascript
update() {
    super.update();

    if (this._hasTriggeredDeath) return;

    const player = this.gameEnv?.gameObjects?.find(obj => obj.constructor?.name === 'Player');
    if (!player || !player.canvas || !this.canvas) return;

    this.isCollision(player);

    if (this.collisionData?.hit) {
        // Check grace period from level start time
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

DeathBarrier.js demonstrates conditionals through:

1. **Early Return Guard**:
   ```javascript
   if (this._hasTriggeredDeath) return;
   ```
   - Prevents processing if death already triggered
   - Early exit to save computation

2. **Null Safety Checks**:
   ```javascript
   if (!player || !player.canvas || !this.canvas) return;
   ```
   - Multiple OR conditions for safety
   - Returns if any required object is missing
   - Prevents null reference errors

3. **Collision Detection Condition**:
   ```javascript
   if (this.collisionData?.hit) {
       // Handle collision
   }
   ```
   - Only processes collision response if collision occurred
   - Uses optional chaining for safe property access

4. **Grace Period Condition**:
   ```javascript
   if (timeSinceLevelStart < 500) {
       console.log('[MazeDebug] Grace period active:', timeSinceLevelStart, 'ms');
       return;
   }
   ```
   - Prevents instant death within 500ms of level start
   - Returns early during grace period
   - Different behavior during grace period vs normal gameplay

5. **Conditional Initialization**:
   ```javascript
   if (!DeathBarrier.levelStartTime) {
       DeathBarrier.levelStartTime = new Date();
   }
   ```
   - Only initializes static property once
   - Subsequent DeathBarrier instances skip this initialization

6. **Error Handling Condition**:
   ```javascript
   try {
       showDeathScreen(player, 'You got lost in the maze.');
   } catch (error) {
       console.error('DeathBarrier failed to show death screen:', error);
       this._hasTriggeredDeath = false;
       player.isDead = false;
   }
   ```
   - Attempts death screen display
   - Rolls back state if error occurs

This demonstrates solid use of conditionals for game logic, error handling, and player protection mechanics.
