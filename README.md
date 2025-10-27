# Adventurer Journey - Back End
Please complete the story below and create a program to solve the problem. Commit any work back to the remote no later than 48 hours before the next interview.

*Please use whatever languages, references and tooling you would like to complete the story.*

## Story Instructions
You are an adventurer standing in the center of a map facing North, and you’re trying to weave through the terrain to your final destination. You have the directions to your destination indicating the number of steps and the direction to travel.

Adventurer Path & Instructions - [./Adventurer Path.md](./Adventurer%20Path.md)

Given the Path Instructions above, programmatically parse the instructions and determine what is the Euclidean (straight line) distance from your starting point to the destination in steps?

**Tech Notes:**
- Use whatever languages, references and tooling you would like.
- Provide any needed instructions to run program.
- Do not round to the nearest step.
- After program executes the answer should be returned.

# Adventurer Journey - Solution

## Running the program

### Requirements
- Python 3.9+ (no external libraries required)

### Quick start
```bash
py adventurer_distance.py        # Windows (py launcher)
python3 adventurer_distance.py   # macOS / Linux
```
If `py` is not available, any Python 3.9+ interpreter works (e.g., `python`). The script prints the ending coordinates and Euclidean distance for the baked-in instruction string from `Adventurer Path.md`.

### Customized runs
- Different path: `py adventurer_distance.py --path 10F5L7R`
- Show every intermediate coordinate: `py adventurer_distance.py --verbose`
- Compare fixed-axes (strafing) vs. turn-then-move behavior: `py adventurer_distance.py --fixed-axes`

The CLI validates the path format (`<steps><direction>` tokens) before running any calculations.

## Movement models
The problem statement never spells out whether `F`, `B`, `L`, and `R` should be interpreted as turns or absolute displacements, so the implementation supports both interpretations:

- **Turn-then-move (default)** – Matches typical character movement in games: `L`/`R` rotate the adventurer 90° in place, `B` rotates 180°, and then the character walks forward `steps` in the new facing direction. This is what you get when running the script with no extra flags.
- **Fixed axes (`--fixed-axes`)** – Treats the letters as absolute map directions relative to the initial north-facing orientation. `F`/`B` move along the north/south axis, while `R`/`L` strafe east/west.

## Testing

1. **Create a virtual environment**
   ```bash
   py -m venv .venv            # Windows
   python3 -m venv .venv       # macOS / Linux
   ```
2. **Activate it**
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
   - cmd.exe: `.\.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`
3. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the suite**
   ```bash
   py -m pytest tests          # or python -m pytest tests
   ```