# Ghost.js - Canvas Rendering

## Requirement
**Canvas Rendering** - Drawing sprites and game elements to canvas.

## Evidence
Ghost.js relies on parent Enemy class rendering but configures sprite data for canvas display.

### Code Example - Sprite Configuration for Rendering

```javascript
const ghostData = {
    id: 'Ghost',
    greeting: false,
    src: path + "/images/projects/castle-game/ghost.png",
    SCALE_FACTOR: 12,
    ANIMATION_RATE: 20,
    INIT_POSITION: { x: 0.8 * width, y: 0.2 * height },
    pixels: { width: 3000, height: 1000 },
    orientation: { rows: 2, columns: 6 },
    down: { row: 0, start: 0, columns: 6 },
    left: { row: 1, start: 0, columns: 6 },
    right: { row: 1, start: 0, columns: 6 },
    hitbox: { widthPercentage: 0.15, heightPercentage: 0.2 },
    followSpeedFactor: 0.4,
    followStopDistance: 12,
    zIndex: 12,
    canvasFilter: 'drop-shadow(0 0 8px rgba(150, 220, 255, 0.7))'
};
```

## How This Satisfies the Requirement

Ghost.js demonstrates canvas rendering through:

1. **Sprite Image Source**:
   ```javascript
   src: path + "/images/projects/castle-game/ghost.png"
   ```
   - Specifies sprite sheet image to load
   - Game engine loads and renders this image to canvas

2. **Sprite Sheet Grid Configuration**:
   ```javascript
   pixels: { width: 3000, height: 1000 },
   orientation: { rows: 2, columns: 6 }
   ```
   - Defines sprite sheet dimensions (3000x1000 pixels)
   - Specifies 2 rows and 6 columns for animation frames
   - Game engine uses this to extract and render frames

3. **Animation Frame Selection**:
   ```javascript
   down: { row: 0, start: 0, columns: 6 },
   left: { row: 1, start: 0, columns: 6 },
   right: { row: 1, start: 0, columns: 6 }
   ```
   - Defines which rows contain animation frames for each direction
   - Game engine renders different frames based on direction

4. **Rendering Scale**:
   ```javascript
   SCALE_FACTOR: 12,
   ANIMATION_RATE: 20
   ```
   - Scale determines rendered size on canvas
   - Animation rate controls frame update speed

5. **Visual Effects**:
   ```javascript
   canvasFilter: 'drop-shadow(0 0 8px rgba(150, 220, 255, 0.7))'
   zIndex: 12
   ```
   - Canvas filter applies drop-shadow effect
   - zIndex controls rendering layer order

Ghost inherits actual canvas drawing implementation from Enemy class while providing configuration data for sprite rendering.
