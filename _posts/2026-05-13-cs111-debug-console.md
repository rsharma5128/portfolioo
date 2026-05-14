---
layout: post
title: "CS111: Debugging - Console Debugging"
description: Using console.log for tracking game state and variables
permalink: /cs111-debug-console
author: Rohan Sharma
---

## Debugging: Console Debugging

### Objective
Students must use console.log strategically to track and debug game state, variables, and method calls.

### Evidence
Console debugging in game components:
- **DeathBarrier.js** - Logging collision detection events
- **Ghost.js** - State tracking logs
- **Multiple classes** - Strategic logging for debugging

### Implementation Details
- console.log() for general output
- console.warn() for warnings
- console.error() for errors
- console.table() for formatted output
- console.time() / console.timeEnd() for performance

### Best Practices
- Remove debug logs from production code
- Use descriptive log messages
- Log at key decision points
- Include context in log messages
- Use different console methods appropriately

### Key Concepts
- Browser DevTools console
- Console methods and their purposes
- Conditional logging
- Performance profiling with console
- Remote debugging
