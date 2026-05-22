# DeathBarrier.js - Methods & Parameters

## Requirement
**Methods & Parameters** - Functions with multiple parameters that handle game logic.

## Evidence
DeathBarrier.js demonstrates methods with parameters that handle collision detection and death triggering.

### Code Example - Methods with Parameters

```javascript
update() { // Checks for collisions, if triggered then uses the belo code
    super.update();

    if (this._hasTriggeredDeath) return; // if the death is already triggered no need to trigger it again

    const player = this.gameEnv?.gameObjects?.find(obj => obj.constructor?.name === 'Player');
    if (!player || !player.canvas || !this.canvas) return;

    this.isCollision(player);

    if (this.collisionData?.hit) {
        // Check grace period from level start time
        const timeSinceLevelStart = new Date() - DeathBarrier.levelStartTime;
        if (timeSinceLevelStart < 500) {
            console.log('[MazeDebug] Grace period active:', timeSinceLevelStart, 'ms');
            return; // we added a grace period because there was an error where the barrier would kill the player before they could even play
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
    // Store the level start time - all barriers share this for grace period
    if (!DeathBarrier.levelStartTime) {
        DeathBarrier.levelStartTime = new Date();
    }
}
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates methods with parameters through:

1. **Constructor(data, gameEnv)** - Accepts two parameters:
   - `data` - configuration object passed to parent class
   - `gameEnv` - game environment reference for accessing game state

2. **update() Method** - Inherits from parent but demonstrates parameter passing:
   - Calls `this.isCollision(player)` - passes player object as parameter
   - Calls `showDeathScreen(player, 'You got lost in the maze.')` - passes player and message string

3. **Parameter Handling** - Uses several advanced techniques:
   - Optional chaining to safely access nested properties (`gameEnv?.gameObjects`)
   - Finding objects within parameters using methods like `.find()`
   - Checking multiple conditions on parameter properties (`!player || !player.canvas`)
   - Passing parameters to other functions like `showDeathScreen()`

4. **Parameter Dependencies** - Method behavior depends on:
   - Player object state and properties
   - Canvas element availability
   - Collision detection data
   - Grace period calculations

These methods show competent parameter handling by receiving complex objects and using them to drive game logic and error handling.
