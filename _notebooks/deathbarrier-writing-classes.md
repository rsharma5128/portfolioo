# DeathBarrier.js - Writing Classes

## Requirement
**Writing Classes** - Demonstrates the ability to define custom classes with properties and methods.

## Evidence
DeathBarrier.js extends the base `Barrier` class to create a custom collision trigger that ends the game when touched.

### Code Example - Class Definition

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

    // Reset level start time when level restarts
    static resetLevelStartTime() {
        DeathBarrier.levelStartTime = new Date();
    }
}
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates writing classes through:

1. **Class Declaration**: The `DeathBarrier` class is explicitly defined using the `class` keyword, extending the `Barrier` base class.

2. **Constructor**: Initializes instance properties (`_hasTriggeredDeath`) and manages a static property (`DeathBarrier.levelStartTime`) that tracks when the level started.

3. **Instance Methods**: 
   - `update()` - overrides parent method to check collisions each frame
   - `resetLevelStartTime()` - static method for resetting level state

4. **Instance Properties**: Maintains state with `_hasTriggeredDeath` flag that tracks whether the collision event has already been triggered.

5. **Encapsulation**: All death barrier logic is contained within the class, including collision detection, grace period handling, and death screen display.

The DeathBarrier class demonstrates solid class design by creating a specialized collision trigger that manages its own state and provides static utility methods for level management.
