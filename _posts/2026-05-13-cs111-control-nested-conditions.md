---
layout: post
title: "CS111: Control Structures - Nested Conditions"
description: Complex decision logic with multiple levels of conditions
permalink: /cs111-control-nested-conditions
author: Rohan Sharma
---

## Nested Conditions

### Objective
Students must implement complex decision logic using nested conditionals to handle multiple interrelated conditions.

### Evidence
Complex decision logic with multiple conditions:
- **DeathBarrier.js** - Grace period + collision check with nested conditions
- **Ghost.js** - Nested conditions for direction and movement logic

### Implementation Details
- Conditions nested inside other conditions
- Evaluates multiple related criteria
- Outer condition gates inner conditions
- Prevents unnecessary evaluation with logical operators

### Example Patterns
- Check if entity exists, then check if collision occurred
- Check if grace period active, then check if collision valid
- Check if player in range, then check direction and speed

### Key Concepts
- Nested if/else blocks
- Guard clauses to reduce nesting depth
- Logical operators (&&, ||) to simplify conditions
- De Morgan's Laws for simplifying complex expressions
- Readability vs performance trade-offs
