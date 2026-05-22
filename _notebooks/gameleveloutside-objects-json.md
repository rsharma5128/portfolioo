# GameLevelOutside.js - Objects (JSON Data)

## Requirement
**Objects (JSON)** - Using object and JSON data structures to organize and manage complex data.

## Evidence
GameLevelOutside.js extensively uses JavaScript objects as configuration structures and data containers.

### Code Example - Object/JSON Usage

```javascript
const image_data_floor = {
    name: 'floor',
    src: image_src_floor,
    pixels: { height: 989, width: 1582 }
};

const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc,
    SCALE_FACTOR: 15,
    STEP_FACTOR: 1500,
    ANIMATION_RATE: 40,
    INIT_POSITION: {
        x: 0.5 * width,
        y: 0.75 * height
    },
    pixels: { height: 432, width: 234 },
    orientation: { rows: 4, columns: 3 },
    down: { row: 0, start: 0, columns: 3 },
    downRight: { row: 2, start: 0, columns: 3, rotate: Math.PI / 16 },
    left: { row: 1, start: 0, columns: 3 },
    right: { row: 2, start: 0, columns: 3 },
    up: { row: 3, start: 0, columns: 3 },
    hitbox: { widthPercentage: 0.1, heightPercentage: 0.15 },
    keypress: { up: 87, left: 65, down: 83, right: 68 }
};

const sir_morty_data = {
    id: "Sir Morty",
    greeting: sir_morty_greeting,
    src: sir_morty,
    expertise: "default",
    knowledgeBase: {
        default: [
            {
                question: "What is inside the castle?",
                answer: "Inside the castle lays a prisoner who has been locked away for years..."
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
        { x: 490/1110*width, y: 510/760*height }
    ]
};

const left_wall = {
    id: 'left-wall-1',
    greeting: "This is a curved barrier, you cannot pass through it!",
    splinePoints: [
        { x: 318/1110*width, y: 749/760*height },
        { x: 435/1110*width, y: 587/760*height }
    ],
    visible: false,
    color: '#8B4513',
    lineWidth: 5
};

this.classes = [
    { class: GameEnvBackground, data: image_data_floor },
    { class: Player, data: sprite_data_mc }
];
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates objects/JSON through:

1. **Nested Configuration Objects**:
   ```javascript
   const image_data_floor = {
       name: 'floor',
       src: image_src_floor,
       pixels: { height: 989, width: 1582 }
   };
   ```
   - Object with string and nested object properties
   - `pixels` is itself an object with height/width

2. **Complex Game Configuration Object**:
   ```javascript
   const sprite_data_mc = {
       id: 'Knight',
       SCALE_FACTOR: 15,
       INIT_POSITION: { x: 0.5 * width, y: 0.75 * height },
       pixels: { height: 432, width: 234 },
       orientation: { rows: 4, columns: 3 },
       down: { row: 0, start: 0, columns: 3 },
       keypress: { up: 87, left: 65, down: 83, right: 68 }
   };
   ```
   - Multiple levels of nested objects
   - Each animation direction is an object
   - Keypress configuration is an object mapping

3. **Knowledge Base Object Structure**:
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
   - Nested object containing array of Q&A objects
   - Each Q&A is an object with properties

4. **Sprite Sheet Configuration Object**:
   ```javascript
   spriteFrames: { rows: 2, columns: 4, frameIndex: Math.floor(Math.random() * 8) }
   ```
   - Object containing grid information
   - Used for sprite sheet rendering

5. **Array of Configuration Objects**:
   ```javascript
   this.classes = [
       { class: GameEnvBackground, data: image_data_floor },
       { class: Player, data: sprite_data_mc }
   ];
   ```
   - Array of objects, each with class and data
   - Game engine processes this structure

6. **Spline Points Array of Objects**:
   ```javascript
   splinePoints: [
       { x: 318/1110*width, y: 749/760*height },
       { x: 435/1110*width, y: 587/760*height }
   ]
   ```
   - Array of coordinate objects
   - Each point is an object with x and y

This demonstrates comprehensive use of objects and JSON structures for organizing complex game configuration and data.
