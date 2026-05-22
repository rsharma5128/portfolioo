# Ghost.js - Inheritance (2+ Levels)

## Requirement
**Inheritance (2+ Levels)** - Demonstrating multi-level class hierarchy where a custom class extends a base class.

## Evidence
Ghost.js extends the `Enemy` class, which is itself part of the game engine's base class hierarchy, creating a multi-level inheritance chain.

### Code Example - Class Inheritance

```javascript
import Enemy from '@assets/js/GameEnginev1.1/essentials/Enemy.js';
import Player from '@assets/js/GameEnginev1.1/essentials/Player.js';
import showDeathScreen from './DeathScreen.js';

class Ghost extends Enemy {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
        this.followStopDistance = data?.followStopDistance ?? 8;
        this._hasTriggeredDeath = false;
    }

    // ... methods override parent behavior
}

export default Ghost;
```

## How This Satisfies the Requirement

Ghost.js demonstrates multi-level inheritance through:

1. **Hierarchy Chain**:
   ```
   GameObject (game engine base)
      ↓
   Character (extends GameObject)
      ↓
   Enemy (extends Character)
      ↓
   Ghost (extends Enemy) ← Our custom class
   ```

2. **Extends Enemy Class** - The `Ghost` class explicitly extends `Enemy`:
   ```javascript
   class Ghost extends Enemy {
   ```

3. **Super Constructor Call** - Calls parent class constructor to properly initialize:
   ```javascript
   super(data, gameEnv);
   ```

4. **Inherits Parent Functionality** - Ghost inherits all methods and properties from Enemy, including:
   - Position and velocity tracking
   - Update cycle management
   - Canvas rendering
   - Collision detection

5. **Specialization** - Ghost adds custom properties:
   - `followSpeedFactor` - custom speed control
   - `followStopDistance` - custom stopping distance
   - `_hasTriggeredDeath` - death state tracking

6. **Method Override** - Ghost overrides the parent's `update()` method:
   ```javascript
   update() {
       const player = this.getPlayer();
       if (player && !player.isDead) {
           this.followPlayer(player);
       }
       super.update();  // Call parent implementation
   }
   ```

This demonstrates a proper multi-level inheritance pattern where Ghost builds upon Enemy's functionality while adding specialized ghost-specific behavior.
