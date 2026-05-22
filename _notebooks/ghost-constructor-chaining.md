# Ghost.js - Constructor Chaining

## Requirement
**Constructor Chaining** - Using `super()` to initialize parent class properties and call parent constructors.

## Evidence
Ghost.js uses `super()` to properly initialize the parent `Enemy` class before adding ghost-specific properties.

### Code Example - Constructor with Super Call

```javascript
class Ghost extends Enemy {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
        this.followStopDistance = data?.followStopDistance ?? 8;
        this._hasTriggeredDeath = false;
    }
}
```

## How This Satisfies the Requirement

Ghost.js demonstrates constructor chaining through:

1. **Super Call First**:
   ```javascript
   super(data, gameEnv);
   ```
   - Immediately calls parent Enemy class constructor
   - Passes required `data` and `gameEnv` parameters up the chain
   - Ensures parent initialization happens before child initialization

2. **Constructor Chain Flow**:
   ```
   Ghost.constructor(data, gameEnv)
      ↓
   super(data, gameEnv)  [calls Enemy constructor]
      ↓
   Enemy passes to Character, Character passes to GameObject
      ↓
   All parent classes initialize
      ↓
   Ghost adds own properties
   ```

3. **Parent Initialization**:
   - Enemy class (parent) initializes base properties like position, velocity, sprite data
   - Ghost builds upon this foundation by adding its own properties

4. **Child-Specific Properties**:
   After `super()` call, Ghost initializes its own properties:
   - `followSpeedFactor` - controls how quickly ghost pursues player (with default 0.4)
   - `followStopDistance` - how close ghost gets to player before stopping (default 8)
   - `_hasTriggeredDeath` - tracks if ghost has triggered player death

5. **Proper Initialization Order**:
   - Parent always initializes first (via `super()`)
   - This ensures all required parent properties exist
   - Child properties then build on that foundation
   - Prevents null reference errors from uninitialized parent properties

6. **Parameter Forwarding**:
   - Ghost receives `data` and `gameEnv` from game engine
   - Passes both to parent via `super(data, gameEnv)`
   - Parent classes use these for their own initialization

This demonstrates proper constructor chaining where Ghost correctly initializes its parent class hierarchy before adding specialized properties.
