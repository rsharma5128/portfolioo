# GameLevelMaze.js - Error Handling

## Requirement
**Error Handling** - Using try/catch blocks for robustness and error recovery.

## Evidence
GameLevelMaze.js handles errors in dialogue system initialization and function calls.

### Code Example - Try/Catch Error Handling

```javascript
const mortyData = {
    id: 'morty',
    interact: function () {
        // Clear any existing dialogue first to prevent duplicates
        if (this.dialogueSystem && this.dialogueSystem.isDialogueOpen()) {
            this.dialogueSystem.closeDialogue();
        }

        // Create a new dialogue system if needed - lazy initialization
        if (!this.dialogueSystem) {
            try {
                this.dialogueSystem = new DialogueSystem();
            } catch (error) {
                console.error('Error creating DialogueSystem:', error);
                return;
            }
        }

        // Select random dialogue message
        const whattosay = "Welcome to the coolest maze this side of the atlantic ocean, escape or get rekt lol"

        // Display dialogue with NPC sprite
        try {
            this.dialogueSystem.showDialogue(
                whattosay,
                "mr portensen",
                this.spriteData.src,
                {
                    columns: 3,
                    rows: 4,
                    frameX: 0,
                    frameY: 0,
                    frameWidth: 78,
                    frameHeight: 108
                }
            );

            this.dialogueSystem.addButtons([
                {
                    text: "Enter the maze",
                    primary: true,
                    action: () => {
                        this.dialogueSystem.closeDialogue();
                        this.destroy();
                    }
                }
            ]);

        } catch (error) {
            console.error('Error calling showDialogue:', error);
        }
    }
};
```

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates error handling through:

1. **DialogueSystem Initialization Try/Catch**:
   ```javascript
   try {
       this.dialogueSystem = new DialogueSystem();
   } catch (error) {
       console.error('Error creating DialogueSystem:', error);
       return;
   }
   ```
   - Catches errors if DialogueSystem constructor fails
   - Logs error for debugging
   - Returns early to prevent further errors

2. **Dialogue Display Try/Catch**:
   ```javascript
   try {
       this.dialogueSystem.showDialogue(...);
       this.dialogueSystem.addButtons([...]);
   } catch (error) {
       console.error('Error calling showDialogue:', error);
   }
   ```
   - Wraps dialogue display in try block
   - Catches display errors
   - Logs error without crashing game

3. **Defensive Null Checking**:
   ```javascript
   if (this.dialogueSystem && this.dialogueSystem.isDialogueOpen()) {
       this.dialogueSystem.closeDialogue();
   }
   ```
   - Checks object existence before using
   - Prevents null reference errors

4. **Graceful Degradation**:
   - If DialogueSystem fails to create, function returns
   - If dialogue fails to display, error logged but game continues
   - Player can still play despite UI errors

This demonstrates defensive error handling with try/catch blocks and null checks.
