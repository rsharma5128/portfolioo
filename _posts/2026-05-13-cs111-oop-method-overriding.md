---
layout: post
title: "CS111: Object-Oriented Programming - Method Overriding"
description: Overriding parent methods with custom implementations
permalink: /cs111-oop-method-overriding
author: Rohan Sharma
---

## Method Overriding

### Objective
Students must override parent class methods to implement specialized behavior while maintaining the interface contract.

### Evidence
Override parent methods with custom implementations:
- **Ghost.js** - Overrides `update()` method with AI pathfinding logic
- **Ghost.js** - Custom `handleCollision()` with death detection
- **DeathBarrier.js** - Overrides parent barrier update method

### Implementation Details
- Parent classes define method signatures that child classes override
- Overridden methods maintain the same method name and parameters
- Custom logic executes instead of parent implementation
- Demonstrates polymorphism - same interface, different behavior

### Key Concepts
- Method override vs method overload
- Polymorphic behavior
- Respecting parent method contracts
- Using `super()` to call parent methods when needed
