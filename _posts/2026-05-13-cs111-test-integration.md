---
layout: post
title: "CS111: Testing & Verification - Integration Testing"
description: Testing level transitions, NPC dialogue, and AI responses working together
permalink: /cs111-test-integration
author: Rohan Sharma
---

## Testing & Verification: Integration Testing

### Objective
Students must test that all game systems work together correctly, including level transitions, NPC interactions, and AI responses.

### Evidence
Integration testing in custom levels:
- **GameLevelOutside.js** - Integrated NPC interaction, level transition, player customization
- **GameLevelMaze.js** - Integrated maze gameplay, enemy AI, level completion
- **All systems** - Working together seamlessly

### Implementation Details
- Testing level-to-level transitions
- Testing NPC dialogue flow
- Testing AI responses in context
- Testing game state persistence
- Testing UI integration

### Test Scenarios
- Complete first level successfully
- Trigger NPC interactions correctly
- Transition to next level
- Verify game state carries over
- Test AI responds appropriately to player actions

### Key Concepts
- Integration testing methodology
- End-to-end testing
- System interaction verification
- Data flow across systems
- State management across levels
