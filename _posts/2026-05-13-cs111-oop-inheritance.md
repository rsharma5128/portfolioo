---
layout: post
title: "CS111: Object-Oriented Programming - Inheritance"
description: Creating multi-level class hierarchies
permalink: /cs111-oop-inheritance
author: Rohan Sharma
---

## Inheritance (Multi-Level Hierarchies)

### Objective
Students must create class hierarchies with 2+ levels of inheritance to demonstrate understanding of inheritance chains.

### Evidence
Multi-level class hierarchy demonstrated:
- **Ghost** extends **Enemy** (base game engine class)
- **DeathBarrier** extends **Barrier** (base game engine class)
- **SpriteSheetCoin** extends **Coin** (base game engine class)

### Implementation Details
- Each custom class extends a game engine base class
- Base classes provide core functionality (position, velocity, rendering)
- Custom classes add specialized behavior
- Demonstrates proper use of inheritance to reduce code duplication

### Key Concepts
- Inheritance hierarchy (parent → child)
- Code reuse through inheritance
- Specialization of generic base classes
- The `extends` keyword
