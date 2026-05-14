---
layout: post
title: "CS111: Input/Output - API Integration"
description: Implementing Leaderboard and NPC AI integration with backend
permalink: /cs111-input-api-integration
author: Rohan Sharma
---

## Input/Output: API Integration

### Objective
Students must integrate backend APIs for features like leaderboards and AI NPC interactions.

### Evidence
API integration in game components:
- **GameLevelOutside.js** - AiNpc.showInteraction() for AI dialogue
- **GameLevelOutside.js** - Q&A data structure for NPC responses
- **Leaderboard system** - Score saving and retrieval

### Implementation Details
- Fetch API for HTTP requests
- POST requests for submitting data (scores, game state)
- GET requests for retrieving data (leaderboard, NPC responses)
- Error handling with try/catch
- Response parsing and validation

### Key Concepts
- Fetch API fundamentals
- HTTP methods (GET, POST, PUT, DELETE)
- Request headers and body
- Response handling and status codes
- Error handling and timeouts
