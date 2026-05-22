# DeathBarrier.js - Booleans (Data Type)

## Requirement
**Booleans** - Using boolean data types for true/false values and conditional logic.

## Evidence
DeathBarrier.js uses boolean flags extensively for state management and collision detection.

### Code Example - Boolean Properties and Usage

```javascript
class DeathBarrier extends Barrier {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this._hasTriggeredDeath = false;
        // Store the level start time - all barriers share this for grace period
        if (!DeathBarrier.levelStartTime) {
            DeathBarrier.levelStartTime = new Date();
        }
    }

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
}
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates booleans through:

1. **Initialization with Boolean False**:
   ```javascript
   this._hasTriggeredDeath = false;
   ```
   - Initializes state as false
   - Tracks if death event has occurred

2. **Boolean Condition Check**:
   ```javascript
   if (this._hasTriggeredDeath) return;
   ```
   - Checks if flag is true (death already triggered)
   - Returns early if true
   - Boolean acts as gate keeper

3. **Boolean Negation in Validation**:
   ```javascript
   if (!player || !player.canvas || !this.canvas) return;
   ```
   - Uses `!` (NOT) operator on object existence checks
   - `!player` means player doesn't exist (is falsy)
   - `!player.canvas` means canvas property is falsy

4. **Boolean Property from Collision Data**:
   ```javascript
   if (this.collisionData?.hit) {
   ```
   - `collisionData.hit` is a boolean property
   - Only processes if collision actually occurred

5. **Setting Boolean to True**:
   ```javascript
   this._hasTriggeredDeath = true;
   player.isDead = true;
   ```
   - Sets flags to true when collision happens
   - Marks death has been triggered

6. **Boolean Reset in Error Handler**:
   ```javascript
   catch (error) {
       console.error('DeathBarrier failed to show death screen:', error);
       this._hasTriggeredDeath = false;
       player.isDead = false;
   }
   ```
   - Sets boolean flags back to false on error
   - Allows retry if error occurs

This demonstrates solid use of booleans for state management and error recovery in collision detection.
