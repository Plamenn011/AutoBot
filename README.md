# AutoBot - Anti-AFK Control Module

AutoBot is a high-performance, automated utility tool designed to prevent idle-state disconnections (AFK) in video games and applications. Developed in Python, it features a custom cyber-industrial user interface built on the CustomTkinter graphical engine, mimicking professional gaming telemetry software.

## Key Features

- **Multi-Key Simulation:** Easily switch inputs via a dropdown menu supporting standard movement controls (`W`, `A`, `S`, `D`), `Spacebar`, and directional arrow keys.
- **Dynamic Timing & Security:** Set custom minimum and maximum delay intervals (from 0 to 10 minutes). The system calculates a completely randomized cooldown between actions to prevent anti-cheat pattern detection.
- **Real-Time Telemetry ProgressBar:** Integrated visual supervisor showcasing a live progression bar and precise process percentage before triggering the next hardware key command.
- **Asynchronous Execution:** Built utilizing multi-threading protocols (`threading`) to keep the background macro injection operating fluidly without freezing the front-end interface.
- **Full-Screen Matrix Design:** Seamless borderless full-screen application rendering with a custom technological grid canvas backdrop.

## Built With

- **Python 3.14+** - Core programming language.
- **CustomTkinter** - Modern dark-themed UI components.
- **PyAutoGUI** - Hardware-level keyboard event simulation.
- **Pillow (PIL)** - High-fidelity background rendering.

## Deployment & Compilation

To compile this script into a standalone windows executable application (`.exe`), navigate to the project directory and run PyInstaller:

```bash
pyinstaller --noconfirm --onefile --windowed --add-data "fondo.png;." --icon="logo.ico" "AutoBot.py"
```

## License

This project is licensed under the **MIT License** - see the LICENSE file for details. Developed by Plamen T. (Plamenn011).
