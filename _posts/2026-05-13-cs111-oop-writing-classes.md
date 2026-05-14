---
layout: post
title: "CS111: Object-Oriented Programming - Writing Classes"
description: Creating custom character classes extending base classes
permalink: /cs111-oop-writing-classes
author: Rohan Sharma
---

## Writing Classes

### Objective
Students must demonstrate the ability to create custom classes that extend base classes, implementing specialized behavior for game objects.

### Evidence
Custom character classes extending base classes:
- **Ghost.js** - Extends Enemy class with AI pathfinding behavior
- **DeathBarrier.js** - Extends Barrier class with collision-triggered death
- **SpriteSheetCoin.js** - Extends Coin class with sprite sheet animation

### Implementation Details
These custom classes demonstrate:
- Proper inheritance from game engine base classes
- Constructor implementation with `super()` calls
- Method overriding for custom behavior
- Integration with the game engine's update/draw cycle

### Key Concepts
- Class declaration using `extends` keyword
- Single responsibility principle (each class handles one entity type)
- Polymorphism through method overriding
- Composition with game engine components
