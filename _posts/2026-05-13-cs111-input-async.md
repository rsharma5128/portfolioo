---
layout: post
title: "CS111: Input/Output - Asynchronous I/O"
description: Using async/await and promises for non-blocking operations
permalink: /cs111-input-async
author: Rohan Sharma
---

## Input/Output: Asynchronous I/O

### Objective
Students must use async/await and promises to handle non-blocking operations like image loading and API calls.

### Evidence
Asynchronous operations in game components:
- **SpriteSheetCoin.js** - Image onload callback for sprite loading
- **GameLevelOutside.js** - Async/await for transitions and level changes
- **Multiple APIs** - Promise chains for data fetching

### Implementation Details
- Callback functions for asynchronous operations
- Promise objects representing future values
- Async/await syntax for readable async code
- Error handling with .catch() or try/catch
- Loading game assets asynchronously

### Key Concepts
- Callbacks and callback hell
- Promise states: pending, fulfilled, rejected
- Promise methods: .then(), .catch(), .finally()
- Async/await syntax
- Error handling in promises
