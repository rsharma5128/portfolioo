---
layout: post
title: "CS111: Testing & Verification - API Error Handling"
description: Error catching and graceful degradation for API calls
permalink: /cs111-test-api-error-handling
author: Rohan Sharma
---

## Testing & Verification: API Error Handling

### Objective
Students must test API error scenarios and ensure the game handles failures gracefully.

### Evidence
API error handling in game components:
- **GameLevelOutside.js** - API error handling for NPC interactions
- **Leaderboard system** - Error handling for score submission
- **Image loading** - Fallback handling for missing assets

### Implementation Details
- Try/catch for API call failures
- Status code checking
- Network error handling
- Timeout handling
- Fallback behaviors

### Test Scenarios
- API server unavailable
- Network timeout
- Invalid response format
- CORS errors
- Authentication failures

### Error Recovery Strategies
- Retry with exponential backoff
- Graceful feature degradation
- User-friendly error messages
- Fallback to cached data
- Log errors for debugging

### Key Concepts
- HTTP status codes and meanings
- Network error types
- Resilience patterns
- User communication for errors
