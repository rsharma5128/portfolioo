# DeathBarrier.js - Nested Conditions

## Requirement
**Nested Conditions** - Using multiple levels of conditional logic with conditions within conditions.

## Evidence
DeathBarrier.js uses nested conditionals to check collision state and grace periods before triggering death.

### Code Example - Nested Collision Handling

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
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates nested conditions through:

1. **First Level: Already Triggered Check**:
   ```javascript
   if (this._hasTriggeredDeath) return;
   ```
   - First guard clause prevents redundant death checks

2. **Second Level: Player Existence and Validity**:
   ```javascript
   const player = this.gameEnv?.gameObjects?.find(...);
   if (!player || !player.canvas || !this.canvas) return;
   ```
   - Finds player in game objects array
   - Checks if player exists AND has canvas AND barrier has canvas
   - Multiple conditions with OR logic prevent null errors

3. **Third Level: Collision Detection**:
   ```javascript
   this.isCollision(player);
   
   if (this.collisionData?.hit) {
       // nested logic inside collision block
   }
   ```
   - Checks collision detection result
   - Only processes death if collision detected

4. **Fourth Level: Grace Period Check**:
   ```javascript
   if (this.collisionData?.hit) {
       const timeSinceLevelStart = new Date() - DeathBarrier.levelStartTime;
       if (timeSinceLevelStart < 500) {
           console.log('[MazeDebug] Grace period active:', timeSinceLevelStart, 'ms');
           return;
       }
   }
   ```
   - **Nested inside collision block**
   - Calculates time elapsed since level started
   - Prevents death if within 500ms grace period
   - Returns early during grace period

5. **Fifth Level: Error Handling with Rollback**:
   ```javascript
   try {
       showDeathScreen(player, 'You got lost in the maze.');
   } catch (error) {
       console.error('DeathBarrier failed to show death screen:', error);
       this._hasTriggeredDeath = false;
       player.isDead = false;
   }
   ```
   - **Nested inside successful death collision block**
   - Attempts to show death screen
   - On error, rolls back death state in catch block

## Condition Hierarchy

```
Level 1: if (this._hasTriggeredDeath) return;
    ↓
Level 2: if (!player || !player.canvas || !this.canvas) return;
    ↓
Level 3: if (this.collisionData?.hit) {
    ↓
    Level 4: if (timeSinceLevelStart < 500) return;
        ↓
        Level 5: try { showDeathScreen() } catch { rollback }
```

This demonstrates sophisticated nested conditional logic with five levels of decision-making to safely handle collision detection and death triggers.
