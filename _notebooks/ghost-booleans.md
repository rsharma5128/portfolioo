# Ghost.js - Booleans (Data Type)

## Requirement
**Booleans** - Using boolean data types for true/false values and conditional logic.

## Evidence
Ghost.js uses boolean flags to track state and control game behavior.

### Code Example - Boolean Properties and Usage

```javascript
constructor(data, gameEnv) {
    super(data, gameEnv);
    this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
    this.followStopDistance = data?.followStopDistance ?? 8;
    this._hasTriggeredDeath = false;
}

update() {
    const player = this.getPlayer();
    if (player && !player.isDead) {
        this.followPlayer(player);
    }
    super.update();
}

handleCollisionEvent() {
    if (this._hasTriggeredDeath || this.playerDestroyed) return;

    const player = this.getPlayer();
    if (!player || player.isDead) return;

    this._hasTriggeredDeath = true;
    this.playerDestroyed = true;
    player.isDead = true;

    showDeathScreen(player, 'The ghost caught you.');
}
```

## How This Satisfies the Requirement

Ghost.js demonstrates booleans through:

1. **Initialization with Boolean False**:
   ```javascript
   this._hasTriggeredDeath = false;
   ```
   - Initializes flag as false
   - Tracks whether death has been triggered

2. **Boolean Negation in Conditions**:
   ```javascript
   if (player && !player.isDead) {
   ```
   - Uses `!` (NOT) operator on boolean
   - `!player.isDead` means "player is NOT dead"
   - Only follows player if alive (isDead is false)

3. **Boolean OR Logic**:
   ```javascript
   if (this._hasTriggeredDeath || this.playerDestroyed) return;
   ```
   - Uses `||` (OR) operator
   - Returns if EITHER flag is true
   - Prevents action if already triggered OR player destroyed

4. **Boolean Assignment (Setting to True)**:
   ```javascript
   this._hasTriggeredDeath = true;
   this.playerDestroyed = true;
   player.isDead = true;
   ```
   - Sets multiple boolean flags to true
   - Marks that death has been triggered
   - Marks player as dead

5. **Boolean AND Logic with Negation**:
   ```javascript
   if (!player || player.isDead) return;
   ```
   - `!player` means player doesn't exist (is falsy)
   - `player.isDead` checks if dead boolean is true
   - Returns if either condition is true

This demonstrates proper use of boolean data types for state tracking and control flow in game logic.
