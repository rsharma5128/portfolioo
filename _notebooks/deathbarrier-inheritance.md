# DeathBarrier.js - Inheritance (2+ Levels)

## Requirement
**Inheritance (2+ Levels)** - Demonstrating multi-level class hierarchy where a custom class extends a base class.

## Evidence
DeathBarrier.js extends the `Barrier` class, which is part of the game engine's base class hierarchy.

### Code Example - Class Inheritance

```javascript
import Barrier from '@assets/js/GameEnginev1.1/essentials/Barrier.js';
import showDeathScreen from './DeathScreen.js';

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
        // ... rest of implementation
    }

    static resetLevelStartTime() {
        DeathBarrier.levelStartTime = new Date();
    }
}

export default DeathBarrier;
```

## How This Satisfies the Requirement

DeathBarrier.js demonstrates multi-level inheritance through:

1. **Hierarchy Chain**:
   ```
   GameObject (game engine base)
      ↓
   Character (extends GameObject)
      ↓
   Barrier (extends Character)
      ↓
   DeathBarrier (extends Barrier) ← Our custom class
   ```

2. **Extends Barrier Class** - Explicitly extends the Barrier base class:
   ```javascript
   class DeathBarrier extends Barrier {
   ```

3. **Super Constructor Call** - Properly calls parent initialization:
   ```javascript
   super(data, gameEnv);
   ```

4. **Inherits Parent Functionality** - DeathBarrier inherits from Barrier:
   - Position and collision box management
   - Canvas rendering capabilities
   - Update cycle management
   - Collision detection methods

5. **Custom Properties** - Adds specialized state:
   - `_hasTriggeredDeath` - tracks if death has been triggered
   - `DeathBarrier.levelStartTime` - static property for grace period tracking

6. **Method Override** - Overrides parent's `update()` method:
   ```javascript
   update() {
       super.update();  // Call parent's update first
       // ... custom death barrier logic
   }
   ```

7. **Static Methods** - Adds class-level utility:
   ```javascript
   static resetLevelStartTime() {
       DeathBarrier.levelStartTime = new Date();
   }
   ```

This demonstrates proper inheritance where DeathBarrier specializes Barrier's collision behavior into a game-ending event.
