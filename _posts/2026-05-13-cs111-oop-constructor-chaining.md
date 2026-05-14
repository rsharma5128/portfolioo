---
layout: post
title: "CS111: Object-Oriented Programming - Constructor Chaining"
description: Using super() to initialize parent classes
permalink: /cs111-oop-constructor-chaining
author: Rohan Sharma
---

## Constructor Chaining

### Objective
Students must use `super()` to properly initialize parent class constructors, ensuring proper object initialization in inheritance hierarchies.

### Evidence
Using super() to initialize parent class:
- **Ghost.js** - `super(data, gameEnv)` call in constructor
- **DeathBarrier.js** - `super(data, gameEnv)` call
- **SpriteSheetCoin.js** - `super(data, gameEnv)` call

### Implementation Details
- `super()` calls parent class constructor
- Must be first statement in child constructor
- Passes necessary data to parent class
- Ensures parent class initialization runs before child logic
- Parent class sets up base properties (position, velocity, rendering)

### Key Concepts
- Constructor chaining with `super()`
- Initialization order in inheritance
- Parameter passing to parent constructors
- Ensuring parent class properties are initialized
