---
layout: post
title: "CS111: Game Level - Castle Grounds (GameLevelOutside)"
description: First level with NPC interactions and player customization
permalink: /cs111-castle-grounds-level
author: Rohan Sharma
---

<div style="position:fixed;top:5.5rem;left:1rem;z-index:99999;">
  <a href="/cs111-objectives" style="display:inline-block;padding:1.1rem 1.4rem;background:#ff4d4d;color:#fff;border-radius:1rem;text-decoration:none;font-weight:900;font-size:1rem;letter-spacing:0.03em;box-shadow:0 8px 24px rgba(0,0,0,0.3);border:2px solid rgba(255,255,255,0.9);">Go back to homepage</a>
</div>

## Game Level: Castle Grounds (GameLevelOutside)

### Overview
Castle Grounds is the first game level introducing player customization, NPC interactions, and narrative progression. This demonstrates full OOP implementation with multiple game systems working together.

### File Location
`_projects/games/castle-game/levels/GameLevelOutside.js`

## Quick Concept
`localStorage` persistence stores small pieces of data in the browser so they survive page reloads. It is commonly used to remember player preferences like chosen skins without a server round-trip. Using `localStorage` allows simple, persistent customization across sessions.

### Level Features
- **Player Customization**: Choose between 3 knight skins
- **Persistent Storage**: localStorage saves player preferences
- **NPC Interactions**: 
  - Sir Morty: Knowledge base AI providing hints
  - DarkKnight: Triggers progression to next level
- **Scene Transitions**: Elaborate fade-in with starfield parallax
- **Typed Dialogue**: Animated text reveal for story progression

### Configuration
- **Canvas Dimensions**: Width, height set per difficulty level
- **Game Path**: Asset paths for sprites and backgrounds
- **Background**: Castle exterior with parallax scrolling

### Game Objects
- Player (customizable)
- Sir Morty (friendly NPC with AI Q&A)
- DarkKnight (progression trigger NPC)
- Environmental elements (coins, barriers)

### Key Methods
- `init()` - Initializes level with configuration
- `update()` - Updates game state each frame
- `draw()` - Renders all game objects
- `handleNPCInteraction()` - Manages dialogue with NPCs
- `transitionToMaze()` - Level progression

### Technical Implementation
- Complex object instantiation with configuration
- Async operations for image loading
- API integration for NPC AI responses
- State management for player progression
- Canvas rendering for parallax effects

## Code Example - Level Configuration and Object Instantiation

```javascript
class GameLevelOutside {
    constructor(gameEnv) {
        const width = gameEnv.innerWidth;
        const height = gameEnv.innerHeight;
        const path = gameEnv.path;

        // Floor background configuration
        const image_src_floor = path + "/images/projects/castle-game/castleOutsideV2.png";
        const image_data_floor = {
            name: 'floor',
            src: image_src_floor,
            pixels: { height: 989, width: 1582 }
        };

        // Player skin selection with localStorage persistence
        const playerSpriteOptions = {
            gray: path + "/images/projects/castle-game/grayKnight.png",
            green: path + "/images/projects/castle-game/greenKnight.png",
            dark: path + "/images/projects/castle-game/darkKnight.png"
        };
        const playerSkinStorageKey = 'castleGame.playerSkin';
        const getPlayerSpriteSrc = (skinKey) => playerSpriteOptions[skinKey] || playerSpriteOptions.gray;
        const getStoredPlayerSkinKey = () => {
            try {
                if (typeof window === 'undefined' || !window.localStorage) {
                    return 'gray';
                }
                const stored = window.localStorage.getItem(playerSkinStorageKey);
                if (stored && playerSpriteOptions[stored]) {
                    return stored;
                }
                window.localStorage.setItem(playerSkinStorageKey, 'gray');
                return 'gray';
            } catch (error) {
                return 'gray';
            }
        };

        // Sir Morty NPC with AI knowledge base
        const sir_morty = path + "/images/projects/castle-game/mortyKnight.png";
        const sir_morty_data = {
            id: "Sir Morty",
            greeting: "Hello! I'm Sir Morty!",
            src: sir_morty,
            SCALE_FACTOR: 7,
            INIT_POSITION: { x: 1259/1667 * width, y: 430/1137 * height },
            expertise: "default",
            chatHistory: [],
            dialogues: [
                "Enter the castle if you dare!",
                "The Dark Knight awaits inside."
            ],
            knowledgeBase: {
                default: [
                    {
                        question: "What is inside the castle?",
                        answer: "Inside the castle lays a prisoner who has been locked away for years. The Dark Knight guards the castle and challenges anyone who dares to enter with an archery test, a maze, and a showdown inside the fortress."
                    },
                    {
                        question: "How do I win the game?",
                        answer: "To win the game, you need to successfully navigate through the castle grounds, complete the archery challenge, solve the maze, and defeat the Dark Knight in the fortress."
                    }
                ]
            },
            interact: function () {
                AiNpc.showInteraction(this);
            }
        };

        // Level object instantiation
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
    }
}

export default GameLevelOutside;
```

## Key Features Demonstrated

1. **Constructor Parameter**: `constructor(gameEnv)` receives game environment
2. **Configuration Objects**: Multiple configuration objects for different game objects
3. **localStorage API**: `window.localStorage.getItem()` and `setItem()` for persistence
4. **Error Handling**: Try/catch blocks for storage access (lines 27-34)
5. **Conditional Logic**: Fallback values and validation (lines 31-35)
6. **API Integration**: `knowledgeBase` object provides context for NPC AI responses
7. **Object Instantiation Array**: `this.classes` array pairs classes with their configuration data
8. **Multiple Object Types**: Background, Player, NPCs, Collectibles, and Barriers all instantiated together
