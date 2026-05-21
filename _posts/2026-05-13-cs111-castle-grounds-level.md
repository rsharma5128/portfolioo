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

## Code Example
```javascript
// Level instantiation + localStorage skin
const cfg = { width: 800, height: 600, skinKey: localStorage.getItem('skin') || 'knight1' };
const outside = new GameLevelOutside(cfg, gameEnv);

outside.init();

// keyboard input example
window.addEventListener('keydown', e => {
  if (e.key === 'ArrowUp' || e.key === 'w') player.moveUp();
});

// simple API fetch for NPC
async function fetchNpcHints(npcId) {
  const res = await fetch(`/api/npc/${npcId}`);
  if (!res.ok) throw new Error(res.statusText);
  return res.json();
}
```
