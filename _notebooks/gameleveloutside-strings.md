# GameLevelOutside.js - Strings (Data Type)

## Requirement
**Strings** - Using string data types for text, paths, identifiers, and character data.

## Evidence
GameLevelOutside.js uses strings extensively for sprite paths, NPC names, dialogue, and configuration identifiers.

### Code Example - String Usage

```javascript
const image_src_floor = path + "/images/projects/castle-game/castleOutsideV2.png";

const playerSpriteOptions = {
    gray: path + "/images/projects/castle-game/grayKnight.png",
    green: path + "/images/projects/castle-game/greenKnight.png",
    dark: path + "/images/projects/castle-game/darkKnight.png"
};

const playerSkinStorageKey = 'castleGame.playerSkin';

const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc,
    // ... other properties
};

const sir_morty_data = {
    id: "Sir Morty",
    greeting: sir_morty_greeting,
    src: sir_morty,
    expertise: "default",
    chatHistory: [],
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
                answer: "Inside the castle lays a prisoner who has been locked away for years. The Dark Knight guards the castle and challenges anyone who dares to enter with an archery test, a maze, and a showdown inside the fortress."
            },
            // ... more Q&A
        ]
    }
};

const sprite_src_closet = path + "/images/projects/castle-game/closet.png";
const sprite_data_closet = {
    id: 'Closet',
    greeting: "Need a new suit of armor?",
    src: sprite_src_closet,
    dialogues: [
        "Pick a knight look."
    ]
};

const transitionDialogues = [
    'Welcome to the castle.',
    'Your job is to break in and free the prisoner.',
    'Use your bow to pass the archery challenge.',
    'Good luck, brave knight.'
];
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates strings through:

1. **File Paths** (String Concatenation):
   ```javascript
   const image_src_floor = path + "/images/projects/castle-game/castleOutsideV2.png";
   ```
   - Combines base path with sprite file location
   - Uses string concatenation with `+` operator

2. **String Properties in Objects**:
   ```javascript
   const sprite_data_mc = {
       id: 'Knight',
       greeting: "Hi, I am a Knight.",
       src: sprite_src_mc
   };
   ```
   - Stores identifiers as strings
   - Stores greeting dialogue as strings

3. **Storage Keys** (String Identifiers):
   ```javascript
   const playerSkinStorageKey = 'castleGame.playerSkin';
   window.localStorage.setItem(playerSkinStorageKey, 'gray');
   ```
   - Uses strings as localStorage keys
   - Strings used for persistent data references

4. **Dialog Arrays** (Multiple Strings):
   ```javascript
   dialogues: [
       "Enter the castle if you dare!",
       "The Dark Knight awaits inside.",
       "Beware of the traps in the castle!"
   ]
   ```
   - Array of string dialogue options
   - Provides variety in NPC responses

5. **Question-Answer Pairs** (Knowledge Base):
   ```javascript
   knowledgeBase: {
       default: [
           {
               question: "What is inside the castle?",
               answer: "Inside the castle lays a prisoner..."
           }
       ]
   }
   ```
   - Strings for AI conversation topics
   - Strings for knowledge base content

6. **Expertise Categories** (String Identifiers):
   ```javascript
   expertise: "default"
   ```
   - String to categorize NPC expertise

7. **Transition Narrative** (String Array):
   ```javascript
   const transitionDialogues = [
       'Welcome to the castle.',
       'Your job is to break in and free the prisoner.',
       'Use your bow to pass the archery challenge.',
       'Good luck, brave knight.'
   ];
   ```
   - Series of strings for story progression
   - Type-written dialogue for level transition

This demonstrates extensive use of strings for game configuration, dialogue, file paths, and narrative content.
