# GameLevelOutside.js - API Integration

## Requirement
**API Integration** - Integrating with external APIs and backend services.

## Evidence
GameLevelOutside.js integrates with AI NPC system that connects to backend for question-answering.

### Code Example - AI NPC Integration

```javascript
const sir_morty_data = {
    id: "Sir Morty",
    greeting: sir_morty_greeting,
    src: sir_morty,
    expertise: "default",
    chatHistory: [],
    dialogues: [
        "Enter the castle if you dare!",
        "The Dark Knight awaits inside.",
        "I heard there's a treasure in the castle."
    ],
    knowledgeBase: {
        default: [
            {
                question: "What is inside the castle?",
                answer: "Inside the castle lays a prisoner who has been locked away for years. The Dark Knight guards the castle and challenges anyone who dares to enter with an archery test, a maze, and a showdown inside the fortress."
            },
            {
                question: "Who are you?",
                answer: "I am Sir Morty, a brave knight of the castle."
            },
            {
                question: "How do I win the game?",
                answer: "To win the game, you need to successfully navigate through the castle grounds, complete the archery challenge, solve the maze, and defeat the Dark Knight in the fortress."
            }
        ]
    },
    reaction: function () {
        if (this.dialogueSystem) {
            this.showReactionDialogue();
        } else {
            console.log(sir_morty_greeting);
        }
    },
    interact: function () {
        // Delegate to AiNpc utility for full AI conversation interface
        AiNpc.showInteraction(this);
    }
};
```

## How This Satisfies the Requirement

GameLevelOutside.js demonstrates API integration through:

1. **Knowledge Base Structure**:
   ```javascript
   knowledgeBase: {
       default: [
           { question: "...", answer: "..." },
           { question: "...", answer: "..." }
       ]
   }
   ```
   - Structured knowledge base for AI responses
   - Provides context for backend AI service

2. **Expertise Specification**:
   ```javascript
   expertise: "default"
   ```
   - Identifies NPC expertise domain
   - Backend uses to select appropriate AI model/responses

3. **Chat History Tracking**:
   ```javascript
   chatHistory: []
   ```
   - Array to store conversation history
   - Sent to backend API for context-aware responses

4. **API Delegation**:
   ```javascript
   interact: function () {
       AiNpc.showInteraction(this);
   }
   ```
   - Calls AiNpc utility which connects to backend
   - Passes NPC data to API service
   - Backend processes questions and returns answers

5. **Dynamic Response System**:
   - Dialogues array provides fallback responses
   - KnowledgeBase provides context for AI
   - API integrates multiple data sources

This demonstrates game integration with backend AI service through structured data.
