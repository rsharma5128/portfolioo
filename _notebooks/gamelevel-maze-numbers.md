# GameLevelMaze.js - Numbers (Data Type)

## Requirement
**Numbers** - Using numeric data types for positioning, scaling, and calculations.

## Evidence
GameLevelMaze.js uses numbers for positioning all maze walls and game objects.

### Code Example - Numeric Values

```javascript
const sprite_data_mc = {
    id: 'Knight',
    SCALE_FACTOR: 20,
    STEP_FACTOR: 1750,
    ANIMATION_RATE: 100,
    INIT_POSITION: {
        x: 202 / 1911 * width,
        y: 760 / 851 * height
    }
};

const dbarrier_1 = {
    id: 'dbarrier_1',
    x: 498 / 505 * width,
    y: 0 / 291 * height,
    width: 6 / 505 * width,
    height: 295 / 291 * height
};

const dbarrier_2 = {
    id: 'dbarrier_2',
    x: 0 / 505 * width,
    y: 0 / 291 * height,
    width: 7 / 505 * width,
    height: 296 / 291 * height
};

const ghostData = {
    id: 'Ghost',
    SCALE_FACTOR: 12,
    ANIMATION_RATE: 20,
    INIT_POSITION: { x: 0.8 * width, y: 0.2 * height },
    followSpeedFactor: 0.4,
    followStopDistance: 12,
    zIndex: 12
};
```

## How This Satisfies the Requirement

GameLevelMaze.js demonstrates numbers through:

1. **Animation Rate**:
   ```javascript
   ANIMATION_RATE: 20
   ANIMATION_RATE: 100
   ```
   - Integer values for animation frame timing
   - Different rates for different entities

2. **Position Calculations**:
   ```javascript
   x: 202 / 1911 * width
   y: 760 / 851 * height
   ```
   - Division to calculate proportional positioning
   - Scales to viewport dimensions

3. **Scale Factors**:
   ```javascript
   SCALE_FACTOR: 20
   SCALE_FACTOR: 12
   ```
   - Integers for sprite sizing

4. **Barrier Dimensions**:
   ```javascript
   width: 6 / 505 * width
   height: 295 / 291 * height
   ```
   - Proportional sizing for maze walls
   - Multiple division calculations

5. **Floating-Point Positioning**:
   ```javascript
   x: 0.8 * width
   y: 0.2 * height
   ```
   - Decimal multipliers for positioning
   - Creates grid-based layout

6. **AI Speed Configuration**:
   ```javascript
   followSpeedFactor: 0.4
   followStopDistance: 12
   ```
   - Float for speed multiplier
   - Integer for distance threshold

This demonstrates numeric data types for responsive maze layout and game object configuration.
