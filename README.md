# 3D Timeline Environment

This project contains a simple 3D scene rendered in the browser.
The scene shows a white timeline with year marks from **1995** to **2025** against a dark gray background.

## Running locally

1. **Start a web server** (needed because modules are loaded via ES modules):

   ```bash
   npm start
   ```

   This uses Python's built-in HTTP server and serves files on [http://localhost:8000](http://localhost:8000).

2. Open `http://localhost:8000` in your browser to view the scene.

## Testing

There are no automated tests yet. The command below prints a placeholder message:

```bash
npm test
```

## Structure

- `index.html` – entry HTML file that loads the module.
- `main.js` – sets up the Three.js scene and draws the timeline.
- `package.json` – defines helper scripts for running the project.
