# GameLevelMaze.js - Strings (Data Type)

## Requirement
**Strings** - Using string data types for text, paths, identifiers, and configuration.

## Evidence
GameLevelMaze.js uses strings for NPC identifiers, asset paths, and dialogue.

### Code Example - String Usage

```javascript
const bgData = {
    name: "custom_bg",
    src: path + "/images/projects/castle-game/dungeonMaze.png",
    pixels: { height: 772, width: 1134 }
};

const sprite_data_mc = {
    id: 'Knight',
    greeting: "Hi, I am a Knight.",
    src: sprite_src_mc
};

const mortyData = {
    id: 'morty',
    greeting: 'Hey there!',
    src: path + "/images/projects/castle-game/morty.png",
    INIT_POSITION: {
        x: 250 / 1911 * width,
        y: 760 / 851 * height
    },
    dialogues: ["a"],
    interact: function () {
        const whattosay = "Welcome to the coolest maze this side of the atlantic ocean, escape or get rekt lol"
    }
};

const ghostData = {
    id: 'Ghost',
    greeting: false,
    src: path + "/images/projects/castle-game/ghost.png"
};

const sprite_src_invis = path + "/images/projects/castle-game/invisDoorCollisionSprite.png";
const sprite_data_invis = {
    id: 'Villager',
    greeting: sprite_greet_invis,
    src: sprite_src_invis
};

this.classes = [
    { class: GameEnvBackground, data: bgData },
    { class: Player, data: sprite_data_mc },
    { class: Npc, data: mortyData },
    { class: Npc, data: sprite_data_invis },
    { class: Ghost, data: ghostData }
];
```

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates strings through:

1. **Asset Paths** (String Concatenation):
   ```javascript
   src: path + "/images/projects/castle-game/dungeonMaze.png"
   ```
   - Combines base path with sprite filename
   - Constructs dynamic asset URLs

2. **NPC Identifiers**:
   ```javascript
   id: 'Knight'
   id: 'morty'
   id: 'Ghost'
   ```
   - String identifiers for game objects
   - Used for tracking and reference

3. **Greeting Text**:
   ```javascript
   greeting: "Hi, I am a Knight."
   greeting: 'Hey there!'
   ```
   - String dialogue for NPC interactions

4. **Dialogue Content**:
   ```javascript
   dialogues: ["a"]
   const whattosay = "Welcome to the coolest maze..."
   ```
   - Array of string dialogue options
   - NPC response content

5. **Background Configuration**:
   ```javascript
   name: "custom_bg"
   ```
   - String identifier for background layer

This demonstrates string data types for asset management and NPC dialogue.
