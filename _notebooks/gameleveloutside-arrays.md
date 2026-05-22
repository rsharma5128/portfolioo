# GameLevelOutside.js - Arrays (Data Type)

## Requirement
**Arrays** - Using array data types to store and manage collections of data.

## Evidence
GameLevelOutside.js uses arrays to manage sprite options, dialogue strings, button configurations, and game objects.

### Code Example - Array Usage

```javascript
const playerSpriteOptions = {
    gray: path + "/images/projects/castle-game/grayKnight.png",
    green: path + "/images/projects/castle-game/greenKnight.png",
    dark: path + "/images/projects/castle-game/darkKnight.png"
};

dialogues: [
    "Enter the castle if you dare!",
    "The Dark Knight awaits inside.",
    "I heard there's a treasure in the castle.",
    "Beware of the traps in the castle!",
    "The castle has stood for centuries."
],

knowledgeBase: {
    default: [
        {
            question: "What is inside the castle?",
            answer: "Inside the castle lays a prisoner who has been locked away for years..."
        },
        {
            question: "Who are you?",
            answer: "I am Sir Morty, a brave knight of the castle..."
        },
        // ... more Q&A pairs
    ]
},

spawnLocations: [
    { x: 340/1110*width, y: 447/760*height },
    { x: 490/1110*width, y: 510/760*height },
    { x: 481/1110*width, y: 594/760*height },
    { x: (1110-340)/1110*width, y: 447/760*height },
    { x: (1110-490)/1110*width, y: 510/760*height },
    { x: (1110-481)/1110*width, y: 594/760*height }
]

this.dialogueSystem.addButtons([
    {
        text: "Green Knight",
        primary: true,
        action: () => { /* ... */ }
    },
    {
        text: "Gray Knight",
        action: () => { /* ... */ }
    },
    {
        text: "Dark Knight",
        action: () => { /* ... */ }
    }
]);

const transitionDialogues = [
    'Welcome to the castle.',
    'Your job is to break in and free the prisoner.',
    'Use your bow to pass the archery challenge.',
    'Good luck, brave knight.'
];

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

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates arrays through:

1. **Dialogue String Array**:
   ```javascript
   dialogues: [
       "Enter the castle if you dare!",
       "The Dark Knight awaits inside.",
       "Beware of the traps in the castle!"
   ]
   ```
   - Array of strings for NPC dialogue options
   - Can be indexed to retrieve specific dialogue

2. **Knowledge Base Array of Objects**:
   ```javascript
   knowledgeBase: {
       default: [
           { question: "...", answer: "..." },
           { question: "...", answer: "..." }
       ]
   }
   ```
   - Array of question-answer objects
   - Each object has two string properties
   - Used for AI knowledge management

3. **Spawn Locations Array**:
   ```javascript
   spawnLocations: [
       { x: 340/1110*width, y: 447/760*height },
       { x: 490/1110*width, y: 510/760*height }
   ]
   ```
   - Array of position objects
   - Each has x and y coordinates
   - Used for randomizing collectible positions

4. **Button Configuration Array**:
   ```javascript
   this.dialogueSystem.addButtons([
       { text: "Green Knight", ... },
       { text: "Gray Knight", ... },
       { text: "Dark Knight", ... }
   ])
   ```
   - Array of button objects
   - Each button has text and action handler
   - Dialogue system iterates to render options

5. **Transition Narrative Array**:
   ```javascript
   const transitionDialogues = [
       'Welcome to the castle.',
       'Your job is to break in and free the prisoner.',
       'Use your bow to pass the archery challenge.',
       'Good luck, brave knight.'
   ];
   ```
   - Array of strings for level transition
   - Displayed one at a time during fade transition

6. **Game Objects Array**:
   ```javascript
   this.classes = [
       { class: GameEnvBackground, data: image_data_floor },
       { class: Player, data: sprite_data_mc },
       { class: StrictNpc, data: sprite_data_darkKnight },
       { class: SpriteSheetCoin, data: gem_data },
       { class: SplineBarrier, data: left_wall }
   ]
   ```
   - Array of game object configurations
   - Game engine iterates through to instantiate level objects
   - Each element is an object with class and data properties

This demonstrates extensive use of arrays for managing game data, configuration, and collections.
