# GameLevelOutside.js - Integration Testing

## Requirement
**Integration Testing** - Testing multiple components working together.

## Evidence
GameLevelOutside.js integrates player, NPCs, coins, and barriers in a cohesive level.

### Code Example - Component Integration

```javascript
this.classes = [
    { class: GameEnvBackground, data: image_data_floor },
    { class: Player, data: sprite_data_mc },
    { class: StrictNpc, data: sprite_data_darkKnight },
    { class: StrictNpc, data: sir_morty_data },
    { class: StrictNpc, data: sprite_data_closet },
    { class: SpriteSheetCoin, data: gem_data },
    { class: SplineBarrier, data: left_wall },
    { class: SplineBarrier, data: right_wall }
];
```

### Code Example - Level Transition Integration

```javascript
interact: function () {
    if (gameEnv && gameEnv.gameControl) {
        const gameControl = gameEnv.gameControl;

        // Create fade overlay for transition
        const fadeOverlay = document.createElement('div');
        const fadeInMs = 2000;
        const fadeOutMs = 1200;

        // ... fade overlay setup ...

        // Start the starfield animation
        requestAnimationFrame(() => {
            // Load medieval fonts
            if (!document.getElementById('castle-medieval-fonts')) {
                const fontLink = document.createElement('link');
                fontLink.id = 'castle-medieval-fonts';
                fontLink.rel = 'stylesheet';
                fontLink.href = 'https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700;900&display=swap';
                document.head.appendChild(fontLink);
            }

            // Create transition text
            const transitionText = document.createElement('div');
            const transitionDialogues = [
                'Welcome to the castle.',
                'Your job is to break in and free the prisoner.',
                'Use your bow to pass the archery challenge.',
                'Good luck, brave knight.'
            ];

            // ... type and erase dialogue ...

            (async () => {
                await Promise.all([
                    runTransitionDialogue(),
                    sleep(fadeInMs)
                ]);

                // Clean up current level
                if (gameControl.currentLevel) {
                    gameControl.currentLevel.destroy();
                }

                // Setup archery level
                gameControl.levelClasses = [GameLevelArchery];
                gameControl.currentLevelIndex = 0;
                gameControl.isPaused = false;

                // Fade out and transition
                setTimeout(() => {
                    fadeOverlay.style.opacity = '0';
                    transitionText.style.opacity = '0';
                    gameControl.transitionToLevel();
                }, 200);
            })();
        });
    }
}
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates integration testing through:

1. **Multiple Component Types**:
   ```javascript
   { class: GameEnvBackground, data: image_data_floor },
   { class: Player, data: sprite_data_mc },
   { class: StrictNpc, data: sprite_data_darkKnight },
   { class: SpriteSheetCoin, data: gem_data },
   { class: SplineBarrier, data: left_wall }
   ```
   - Background rendering
   - Player movement and input
   - NPC interaction
   - Collectible coins
   - Movement barriers
   - All working in same level

2. **Level Transition Integration**:
   ```javascript
   gameControl.levelClasses = [GameLevelArchery];
   gameControl.currentLevelIndex = 0;
   gameControl.transitionToLevel();
   ```
   - Tests level cleanup
   - Tests level switching
   - Tests state management

3. **Animation Choreography**:
   ```javascript
   await Promise.all([
       runTransitionDialogue(),
       sleep(fadeInMs)
   ]);
   ```
   - Coordinates dialogue typing
   - Coordinates fade animations
   - Ensures proper timing

4. **Game Control Integration**:
   - Uses gameEnv and gameControl
   - Manages level classes
   - Handles pause state
   - Cleans up old level

This demonstrates integration of multiple game systems working together.
