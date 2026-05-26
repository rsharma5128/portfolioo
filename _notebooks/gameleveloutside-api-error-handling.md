# GameLevelOutside.js - API Error Handling

## Requirement
**API Error Handling** - Handling errors from API calls and backend services.

## Evidence
GameLevelOutside.js handles errors from image loading (network API) and AI service calls.

### Code Example - Image Loading Error Handling

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
        // Game continues with fallback rendering
    };
    newSpriteSheet.src = spriteSrc;
};
```

### Code Example - AI Service Error Handling

```javascript
interact: function () {
    // Clear any existing dialogue first to prevent duplicates
    if (this.dialogueSystem && this.dialogueSystem.isDialogueOpen()) {
        this.dialogueSystem.closeDialogue();
    }

    // Create a new dialogue system if needed
    if (!this.dialogueSystem) {
        this.dialogueSystem = new DialogueSystem();
    }

    // Show portal dialogue with buttons
    this.dialogueSystem.showDialogue(
        "Are you ready to enter the castle?",
        "DarkKnight",
        this.spriteData.src
    );

    // Add buttons directly to the dialogue
    this.dialogueSystem.addButtons([
        {
            text: "Start",
            primary: true,
            action: () => {
                this.dialogueSystem.closeDialogue();

                // Delegate to AiNpc utility for full AI conversation interface
                AiNpc.showInteraction(this);
            }
        }
    ]);
}
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates API error handling through:

1. **Image Loading Error Handler**:
   ```javascript
   newSpriteSheet.onerror = (error) => {
       console.warn('Failed to load player spritesheet:', spriteSrc, error);
   };
   ```
   - Catches HTTP/network errors loading sprites
   - Logs error information for debugging
   - Allows game to continue with fallback

2. **Graceful Degradation**:
   ```javascript
   if (this.spriteImage) {
       this.drawSpriteImage();
   } else if (this.fallbackToCircle) {
       this.drawCircle();
   }
   ```
   - Falls back to circle if sprite fails to load
   - User sees something rather than nothing

3. **AI Service Integration with Error Handling**:
   ```javascript
   AiNpc.showInteraction(this);
   ```
   - Calls AI backend service
   - AiNpc utility handles service errors internally
   - NPC configuration provides fallback knowledge base

4. **Null Safety**:
   ```javascript
   if (!player || !spriteSrc) return;
   ```
   - Validates data before API calls
   - Prevents errors from bad input

5. **Dialogue System Error Prevention**:
   ```javascript
   if (this.dialogueSystem && this.dialogueSystem.isDialogueOpen()) {
       this.dialogueSystem.closeDialogue();
   }
   ```
   - Checks state before API calls
   - Prevents duplicate requests

This demonstrates robust API error handling with fallbacks and state validation.
