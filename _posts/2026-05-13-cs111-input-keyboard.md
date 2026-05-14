---
layout: post
title: "CS111: Input/Output - Keyboard Input"
description: Handling keyboard events for player controls
permalink: /cs111-input-keyboard
author: Rohan Sharma
---

## Input/Output: Keyboard Input

### Objective
Students must implement keyboard event listeners to handle player input and control game entities.

### Evidence
Keyboard input handling in game components:
- **GameLevelOutside.js** - W, A, S, D key handling
- **GameLevelMaze.js** - Arrow key and WASD controls
- **Multiple levels** - Event listeners for player movement

### Implementation Details
- Event listeners for keydown/keyup events
- Key code detection for specific keys
- State management for simultaneous key presses
- Integration with player movement system
- Debouncing repeated key events

### Key Concepts
- addEventListener for keyboard events
- Event object properties (key, keyCode, which)
- Key detection and handling
- Simultaneous key presses
- Key event propagation and bubbling
