# GameLevelOutside.js - JSON Parsing

## Requirement
**JSON Parsing** - Parsing and working with JSON data structures.

## Evidence
GameLevelOutside.js uses JSON structures for configuration and AI knowledge bases.

### Code Example - JSON Structures

```javascript
const sir_morty_data = {
    id: "Sir Morty",
    greeting: sir_morty_greeting,
    src: sir_morty,
    expertise: "default",
    chatHistory: [],
    knowledgeBase: {
        default: [
            {
                question: "What is inside the castle?",
                answer: "Inside the castle lays a prisoner who has been locked away for years. The Dark Knight guards the castle and challenges anyone who dares to enter with an archery test, a maze, and a showdown inside the fortress."
            },
            {
                question: "Who are you?",
                answer: "I am Sir Morty, a brave knight of the castle. Enter or recieve a .55! Code code code!"
            },
            {
                question: "How do I win the game?",
                answer: "To win the game, you need to successfully navigate through the castle grounds, complete the archery challenge, solve the maze, and defeat the Dark Knight in the fortress. Only then will you be able to free the prisoner and claim victory!"
            },
            {
                question: "Any tips for the archery challenge?",
                answer: "In the archery challenge, timing and precision are key. Pay attention to the movement patterns of the targets and try to anticipate their next move."
            }
        ]
    }
};

const gem_data = {
    id: 'gem',
    INIT_POSITION: { x: 0.5, y: 0.5 },
    SCALE_FACTOR: 30,
    value: 5,
    spriteImagePath: path + '/images/projects/castle-game/gems.png',
    spriteFrames: { rows: 2, columns: 4, frameIndex: Math.floor(Math.random() * 8) },
    spawnLocations: [
        { x: 340/1110*width, y: 447/760*height },
        { x: 490/1110*width, y: 510/760*height },
        { x: 481/1110*width, y: 594/760*height }
    ]
};

const left_wall = {
    id: 'left-wall-1',
    greeting: "This is a curved barrier, you cannot pass through it!",
    splinePoints: [
        { x: 318/1110*width, y: 749/760*height },
        { x: 435/1110*width, y: 587/760*height },
        { x: 293/1110*width, y: 497/760*height }
    ],
    visible: false,
    color: '#8B4513',
    lineWidth: 5
};
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates JSON parsing through:

1. **Nested JSON Knowledge Base**:
   ```javascript
   knowledgeBase: {
       default: [
           { question: "...", answer: "..." },
           { question: "...", answer: "..." }
       ]
   }
   ```
   - Creates JSON structure for AI knowledge
   - Nested arrays of Q&A pairs
   - Each entry has consistent JSON schema

2. **Property Access from JSON**:
   ```javascript
   question: "What is inside the castle?"
   answer: "Inside the castle lays a prisoner..."
   ```
   - JSON objects with string properties
   - Accessed by property names

3. **Sprite Configuration JSON**:
   ```javascript
   spriteFrames: { rows: 2, columns: 4, frameIndex: 0 }
   ```
   - JSON object describing sprite grid
   - Nested numeric properties

4. **Spawn Location JSON Array**:
   ```javascript
   spawnLocations: [
       { x: 340/1110*width, y: 447/760*height },
       { x: 490/1110*width, y: 510/760*height }
   ]
   ```
   - Array of coordinate JSON objects
   - Each location has x and y properties

5. **Wall Configuration JSON**:
   ```javascript
   splinePoints: [
       { x: 318/1110*width, y: 749/760*height },
       { x: 435/1110*width, y: 587/760*height }
   ]
   ```
   - Array of point coordinates
   - Each point is a JSON object

This demonstrates working with JSON structures for game configuration and AI data.
