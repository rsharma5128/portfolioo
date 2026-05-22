# GameLevelOutside.js - Asynchronous I/O

## Requirement
**Asynchronous I/O** - Using async/await and promises for asynchronous operations like image loading.

## Evidence
GameLevelOutside.js uses asynchronous image loading and async/await for level transitions.

### Code Example - Asynchronous Image Loading

```javascript
const applyPlayerSprite = (player, skinKey) => {
    const spriteSrc = getPlayerSpriteSrc(skinKey);
    if (!player || !spriteSrc) return;
    if (player.spriteData?.src === spriteSrc) {
        setStoredPlayerSkinKey(skinKey);
        return;
    }

    const newSpriteSheet = new Image();
    newSpriteSheet.onload = () => {
        player.spriteSheet = newSpriteSheet;
        player.spriteReady = true;
        player.spriteData = { ...(player.spriteData || {}), src: spriteSrc };
        player.data = player.spriteData;
        player.frameIndex = 0;
        player.frameCounter = 0;
        player.resize();
        setStoredPlayerSkinKey(skinKey);
    };
    newSpriteSheet.onerror = (error) => {
        console.warn('Failed to load player spritesheet:', spriteSrc, error);
    };
    newSpriteSheet.src = spriteSrc;
};
```

### Code Example - Async/Await in Transition

```javascript
(async () => {
    // Keep sync with fade-in so both effects complete before changing levels.
    await Promise.all([
        runTransitionDialogue(),
        sleep(fadeInMs)
    ]);

    // Clean up current level properly
    if (gameControl.currentLevel) {
        // ... cleanup code
    }

    console.log("Setting up battle room level...");

    // Change the level classes to GameLevelEnd
    gameControl.levelClasses = [GameLevelArchery];
    gameControl.currentLevelIndex = 0;
    gameControl.isPaused = false;

    // Fade out overlay after transition.
    setTimeout(() => {
        fadeOverlay.style.transition = `opacity ${fadeOutMs}ms ease-in-out`;
        transitionText.style.transition = `opacity ${fadeOutMs}ms ease-in-out`;
        fadeOverlay.style.opacity = '0';
        transitionText.style.opacity = '0';

        // Remove both elements after fade-out completes
        setTimeout(() => {
            try { document.body.removeChild(fadeOverlay); } catch (e) { }
            // ... more cleanup
        }, fadeOutMs + 150);
    }, 200);

    // Start the boss fight with the same control
    console.log("Transitioning to archery level...");
    gameControl.transitionToLevel();
})();

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates asynchronous I/O through:

1. **Image Loading Callbacks**:
   ```javascript
   const newSpriteSheet = new Image();
   newSpriteSheet.onload = () => { /* update player */ };
   newSpriteSheet.onerror = (error) => { /* handle error */ };
   newSpriteSheet.src = spriteSrc;
   ```
   - Creates async image loading
   - onload callback fires when image downloads
   - onerror callback handles load failures

2. **Async/Await Pattern**:
   ```javascript
   (async () => {
       await Promise.all([
           runTransitionDialogue(),
           sleep(fadeInMs)
       ]);
   })();
   ```
   - Uses async IIFE (Immediately Invoked Function Expression)
   - await waits for promises to complete
   - Promise.all waits for both operations in parallel

3. **Promise Creation**:
   ```javascript
   const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
   ```
   - Creates promise that resolves after delay
   - Used for async timing control

4. **Sequential Promises**:
   - First: await Promise.all for dialogue and fade
   - Then: await various setTimeout callbacks
   - Creates choreographed async sequence

This demonstrates async/await for managing image loading and complex timed transitions.
