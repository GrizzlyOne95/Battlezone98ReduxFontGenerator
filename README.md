# Battlezone 98 Redux Font Sheet Generator
A lightweight tool for modders to create custom `bzfont.dds` font atlases.

Developed by **GrizzlyOne95**.

<img width="1102" height="982" alt="image" src="https://github.com/user-attachments/assets/9b0d8439-8a26-42b6-9b27-c5292aab1d04" />



## Features
- **Battlezone Aesthetic UI:** New dark mode theme with neon highlights using the `BZONE` font.
- **Profile System:** Save and load custom font configurations.
- **Stock-Derived Layout:** Atlas slot coordinates now follow the stock `bzfont.st` sprite table scaled to the 1024 atlas.
- **Stock Compare Overlay:** Preview your generated atlas against the stock `bzone.png` atlas with adjustable opacity.
- **Auto-Nudge Presets:** Quick-access buttons for common vertical alignment settings.
- **Dual Font Support:** Use one font for letters and another for numbers/symbols.
- **Auto-Alignment:** Automatically sit characters on the correct baseline for the BZ98 engine.
- **Modern Resolution:** Generates a 1024x1024 RGBA texture from scratch.
- **Drag-and-Drop Ready:** Outputs as `bzfont.dds` for immediate use in game assets.
- **Manual Tweak Options:** Adjust font size, horizontal/vertical alignment, show the coordinate grid, and force snapping characters.
- **Real-time Feedback:** Integrated log box to monitor actions and errors.

## How to Use
### For Users
1. Download the latest `bz_generator.exe` from the [Releases](../../releases) section.
2. Run the application.
3. Select your desired `.ttf` or `.otf` font files.
4. Click **Export DDS**.
5. Copy the resulting `bzfont.dds` into your mod's texture directory.

<img width="1024" height="1024" alt="bzone_cyber_complete" src="https://github.com/user-attachments/assets/9fa232a9-8f9f-4e41-a79c-7efdee3ccc5c" />

### Overlay comparison between generated font and original Battlezone font

<img width="700" height="225" alt="image" src="https://github.com/user-attachments/assets/0ed2a0a2-1d5c-473e-bc2f-80557a5dd336" />


### Troubleshooting
- If characters generate missing or with rectangles/invalid symbols, your font most likely is missing those characters. Try another font file.
- If characters are clipping or cut off in game, try adjusting them to be perfectly aligned in the grid. Use the "Show Layout Grid" option.
- If you run into a bug or problem please create a Github issue.

### For Developers
If you want to run from source:
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run: `python bz_generator.py`.

Compiler Command: python -m PyInstaller --noconsole --onefile --add-data "Orbitron-Bold.ttf;." --add-data "BZONE.ttf;." bz_generator.py

### Stock Coordinate Reference
If you want the stock Battlezone character sprite coordinates instead of manually measuring them, use the game's `Edit\stock\bzfont.st` file. This repo includes a helper script:

`python tools\dump_bzfont_st.py "C:\Users\istuart\Documents\Battlezone 98 Redux\Edit\stock\bzfont.st"`

That sprite table contains `char.<code> -> U V W H` entries for the stock atlas.

## Credits
- **Tool Development:** GrizzlyOne95
- **Default Font:** Orbitron (Open Font License)
- **Engine Compatibility:** Battlezone 98 Redux

## License
MIT License - See [LICENSE](LICENSE) for details.
