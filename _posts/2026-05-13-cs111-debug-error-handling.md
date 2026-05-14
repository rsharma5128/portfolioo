---
layout: post
title: "CS111: Debugging - Error Handling"
description: Using try/catch blocks for robustness
permalink: /cs111-debug-error-handling
author: Rohan Sharma
---

## Debugging: Error Handling

### Objective
Students must implement try/catch blocks to handle errors gracefully and prevent application crashes.

### Evidence
Error handling in game components:
- **GameLevelMaze.js** - Try/catch blocks for robustness
- **GameLevelOutside.js** - Error handling in async operations
- **API integration** - Fetch error catching

### Implementation Details
- Try blocks for code that might throw errors
- Catch blocks for error handling
- Finally blocks for cleanup code
- Error object with message and stack
- Throwing custom errors

### Error Handling Patterns
- API call errors with fetch
- Image loading errors
- Parsing JSON errors
- Null reference errors
- Division by zero handling

### Key Concepts
- Error types (Error, TypeError, SyntaxError, etc.)
- Try/catch/finally structure
- Error objects and properties
- Throwing custom errors
- Error propagation and bubbling
