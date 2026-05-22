# Ghost.js - Writing Classes

## Requirement
**Writing Classes** - Demonstrates the ability to define custom classes with properties and methods.

## Evidence
Ghost.js extends the base `Enemy` class to create a custom hostile NPC with specialized behavior for the game.

### Code Example - Class Definition and Inheritance

```javascript
class Ghost extends Enemy {
    constructor(data, gameEnv) {
        super(data, gameEnv);
        this.followSpeedFactor = data?.followSpeedFactor ?? 0.4;
        this.followStopDistance = data?.followStopDistance ?? 8;
        this._hasTriggeredDeath = false;
    }

    getPlayer() {
        return this.gameEnv?.gameObjects?.find(obj => obj instanceof Player) || null;
    }

    followPlayer(player) {
        if (!player) return;

        const ghostCenter = this.getCenter();
        const playerCenter = typeof player.getCenter === 'function'
            ? player.getCenter()
            : { x: player.x || 0, y: player.y || 0 };

        const dx = playerCenter.x - ghostCenter.x;
        const dy = playerCenter.y - ghostCenter.y;
        const distance = Math.hypot(dx, dy);

        if (distance <= this.followStopDistance) {
            this.velocity.x = 0;
            this.velocity.y = 0;
            return;
        }

        const baseSpeed = player?.xVelocity || (this.gameEnv?.innerWidth || 800) / 2000;
        const speed = Math.max(0.3, baseSpeed * this.followSpeedFactor);
        const nx = dx / distance;
        const ny = dy / distance;

        this.position.x += nx * speed;
        this.position.y += ny * speed;

        if (Math.abs(dx) >= Math.abs(dy)) {
            this.direction = dx >= 0 ? 'right' : 'left';
        } else {
            this.direction = dy >= 0 ? 'down' : 'up';
        }
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
}
```

## How This Satisfies the Requirement

Ghost.js demonstrates writing classes through:

1. **Class Declaration**: The `Ghost` class is explicitly defined using the `class` keyword, extending the `Enemy` base class.

2. **Constructor**: The constructor accepts `data` and `gameEnv` parameters and initializes instance properties like `followSpeedFactor`, `followStopDistance`, and `_hasTriggeredDeath`. This shows proper initialization of object state.

3. **Instance Methods**: Multiple methods are defined:
   - `getPlayer()` - finds and returns the player object
   - `followPlayer()` - implements AI pathfinding logic
   - `update()` - overrides parent behavior
   - `handleCollisionEvent()` - handles collision logic

4. **Properties**: Instance variables track state (`followSpeedFactor`, `followStopDistance`, `_hasTriggeredDeath`) that persist across method calls, demonstrating proper encapsulation of data within the class.

5. **Behavior**: The class encapsulates all ghost-related logic in one cohesive unit, making it a well-designed custom class that can be instantiated and used throughout the game.

The Ghost class shows mastery of class-based OOP by creating a reusable, self-contained entity that manages its own state and behavior within the game engine.
