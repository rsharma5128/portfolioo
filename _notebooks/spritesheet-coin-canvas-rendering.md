# SpriteSheetCoin.js - Canvas Rendering

## Requirement
**Canvas Rendering** - Drawing sprites and game elements to canvas.

## Evidence
SpriteSheetCoin.js renders sprite images to canvas with fallback circle rendering.

### Code Example - Canvas Drawing

```javascript
draw() {
    if (!this.ctx) return;
    
    // Clear the canvas
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    if (this.collected) return;
    
    // Draw sprite image if loaded
    if (this.isImageLoaded && this.spriteImage) {
        this.drawSpriteImage();
    } else if (this.fallbackToCircle) {
        // Fall back to the original colored circle
        this.drawCircle();
    }
    
    // Call setupCanvas to position the canvas
    this.setupCanvas();
}

drawSpriteImage() {
    const { rows, columns, frameIndex } = this.spriteFrames;
    
    // Calculate frame dimensions
    const frameWidth = this.spriteImage.width / columns;
    const frameHeight = this.spriteImage.height / rows;
    
    // Calculate which frame to display based on frameIndex
    const currentFrameIndex = frameIndex % (rows * columns);
    const row = Math.floor(currentFrameIndex / columns);
    const col = currentFrameIndex % columns;
    
    const sourceX = col * frameWidth;
    const sourceY = row * frameHeight;
    
    // Draw the sprite frame centered on the canvas
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;
    const drawWidth = this.canvas.width;
    const drawHeight = this.canvas.height;
    
    this.ctx.drawImage(
        this.spriteImage,
        sourceX, sourceY,
        frameWidth, frameHeight,
        centerX - drawWidth / 2, centerY - drawHeight / 2,
        drawWidth, drawHeight
    );
}

drawCircle() {
    this.ctx.fillStyle = this.color;
    const centerX = this.canvas.width / 2;
    const centerY = this.canvas.height / 2;
    const radius = Math.min(this.canvas.width, this.canvas.height) / 3;
    
    this.ctx.beginPath();
    this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
    this.ctx.fill();
    
    // Add a border to make it more visible
    this.ctx.strokeStyle = '#B8860B';
    this.ctx.lineWidth = 2;
    this.ctx.stroke();
}
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates canvas rendering through:

1. **Canvas Context Access**:
   ```javascript
   if (!this.ctx) return;
   this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
   ```
   - Gets canvas context reference
   - Clears canvas for redrawing

2. **Sprite Sheet Drawing**:
   ```javascript
   this.ctx.drawImage(
       this.spriteImage,
       sourceX, sourceY,
       frameWidth, frameHeight,
       centerX - drawWidth / 2, centerY - drawHeight / 2,
       drawWidth, drawHeight
   );
   ```
   - Uses drawImage() to render sprite frame
   - Extracts frame from sprite sheet based on grid
   - Centers image on canvas

3. **Frame Calculation**:
   ```javascript
   const row = Math.floor(currentFrameIndex / columns);
   const col = currentFrameIndex % columns;
   const sourceX = col * frameWidth;
   const sourceY = row * frameHeight;
   ```
   - Calculates source position from frame index
   - Handles sprite sheet grid indexing

4. **Fallback Circle Rendering**:
   ```javascript
   this.ctx.fillStyle = this.color;
   this.ctx.beginPath();
   this.ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
   this.ctx.fill();
   ```
   - Uses canvas arc() for circle rendering
   - Adds stroke for visibility

This demonstrates direct canvas rendering with sprites and shape drawing.
