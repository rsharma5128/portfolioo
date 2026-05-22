# SpriteSheetCoin.js - Asynchronous I/O

## Requirement
**Asynchronous I/O** - Using async/await and callbacks for asynchronous operations like image loading and file I/O.

## Evidence
SpriteSheetCoin.js uses asynchronous image loading to load sprite sheets dynamically.

### Code Example - Asynchronous Image Loading

```javascript
loadImage() {
    const img = new Image();
    img.onload = () => {
        this.spriteImage = img;
        this.isImageLoaded = true;
        console.log(`SpriteSheetCoin image loaded: ${this.spriteImagePath}`);
    };
    img.onerror = () => {
        console.warn(`Failed to load SpriteSheetCoin image: ${this.spriteImagePath}`);
        this.isImageLoaded = false;
    };
    img.src = this.spriteImagePath;
}

constructor(data = null, gameEnv = null) {
    super(data, gameEnv);
    
    this.spriteImagePath = data?.spriteImagePath || null;
    this.spriteImage = null;
    this.isImageLoaded = false;
    this.spriteFrames = data?.spriteFrames || { rows: 1, columns: 1, frameIndex: 0 };
    this.fallbackToCircle = data?.fallbackToCircle !== false;
    this.spawnLocations = Array.isArray(data?.spawnLocations) ? data.spawnLocations : null;
    
    // Load the image if provided
    if (this.spriteImagePath) {
        this.loadImage();
    }
}

draw() {
    if (!this.ctx) return;
    
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    if (this.collected) return;
    
    // Draw sprite image if loaded
    if (this.isImageLoaded && this.spriteImage) {
        this.drawSpriteImage();
    } else if (this.fallbackToCircle) {
        // Fall back to the original colored circle
        this.drawCircle();
    }
    
    this.setupCanvas();
}

setSprite(imagePath) {
    this.spriteImagePath = imagePath;
    this.isImageLoaded = false;
    this.loadImage();
}
```

## How This Satisfies the Requirement

SpriteSheetCoin.js demonstrates asynchronous I/O through:

1. **Asynchronous Image Loading**:
   ```javascript
   const img = new Image();
   img.src = this.spriteImagePath;
   ```
   - Creates Image object that loads asynchronously
   - Setting src triggers background image download

2. **onload Callback**:
   ```javascript
   img.onload = () => {
       this.spriteImage = img;
       this.isImageLoaded = true;
       console.log(`SpriteSheetCoin image loaded: ${this.spriteImagePath}`);
   };
   ```
   - Fires when image successfully loads
   - Updates state to mark image ready
   - Logs successful load

3. **onerror Callback**:
   ```javascript
   img.onerror = () => {
       console.warn(`Failed to load SpriteSheetCoin image: ${this.spriteImagePath}`);
       this.isImageLoaded = false;
   };
   ```
   - Fires if image fails to load
   - Handles error gracefully
   - Marks image as not loaded

4. **Fallback Rendering**:
   ```javascript
   if (this.isImageLoaded && this.spriteImage) {
       this.drawSpriteImage();
   } else if (this.fallbackToCircle) {
       this.drawCircle();
   }
   ```
   - Checks if async load completed
   - Falls back to circle if not loaded yet
   - Prevents rendering errors

5. **Deferred Image Setting**:
   ```javascript
   setSprite(imagePath) {
       this.spriteImagePath = imagePath;
       this.isImageLoaded = false;
       this.loadImage();
   }
   ```
   - Allows changing sprite after construction
   - Triggers new async load

This demonstrates non-blocking asynchronous image loading with fallback rendering.
