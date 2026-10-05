# Lordicon animated icon demo

- Player: `@lordicon/element` 3.0.0, standalone `dist/lordicon.js`, copied without modification.
- Bundled dependencies: `@lordicon/web` and `@lordicon/utils-lottie`. MIT notices are included alongside the player.
- Six selected example icons from the official player repository:
  https://github.com/lordicondev/player-element/tree/22a6250b69f4a968de2b0185cdf0cf3df4a71d07/examples/icons
- Icon artwork remains subject to Lordicon's icon license, separate from the MIT player:
  https://lordicon.com/docs/license/free
- Visible attribution is included on `icon-animated.html`. This integration is for the owner's personal template.

`npm run build` embeds the six local JSON assets into `assets/js/animated-icon-data.js` so the gallery also works without fetching JSON via `file://`. The copyable snippets use the individual JSON paths; serve those snippets over HTTP (`npm run dev`).

Load the player once before `assets/js/animated-icons.js`. The gallery supports hover/focus, click/touch, timed loops, speed selection, pause/resume, and explicit JavaScript playback. It pauses offscreen/hidden animations and respects reduced motion. Vendor files are loaded only on the Animated Icons page.
