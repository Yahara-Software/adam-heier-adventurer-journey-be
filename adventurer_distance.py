"""Adventurer Journey

Usage:
  python adventurer_distance.py                  # uses default path
  python adventurer_distance.py --path 15F6B...  # custom path
  python adventurer_distance.py --fixed-axes     # fixed-axes movement model (turn-then-move is default)
  python adventurer_distance.py --verbose        # detailed coords output

Parses instructions like '16R' as (steps=16, direction='R').

Computes Euclidean distance under two models:
1) turn-then-move (default):
    - Adventurer always faces the direction of travel.
    - L/R = rotate left/right 90 degrees then move steps forward.
    - B = rotate 180 degrees then move forward.
2) fixed-axes: Direction is fixed North; F/B move +/-Y, R/L move +/-X.

Outputs the end coordinates and straight-line distance from origin.
"""

import argparse
import sys
import re
from typing import List, Tuple
from math import hypot

DEFAULT_PATH = "15F6B6B5L16R8B16F20L6F13F11R"
DEFAULT_START = (0, 0)

def validate_path(path: str) -> bool:
    """
    Returns True if path is a non-empty sequence of <positive number><direction> tokens,
    where valid directions are: F,B,R,L (case-insensitive).
    """
    if path is None:
        return False
    
    path = path.strip().upper()
    return bool(re.fullmatch(r'(?:\d+[FBRL])+', path))

def get_path_coords(s: str, turn_then_move: bool = True, start: Tuple[int, int] = DEFAULT_START) -> List[Tuple[int, int, str]]:
    """Parses the path string into a list of positions after each move."""
    tokens = re.findall(r'(\d+)([FBRL])', s, flags=re.IGNORECASE)

    # Direction order: [North, East, South, West]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    labels = ["N", "E", "S", "W"]
    current_direction = 0  # index into directions (0 = North)
    x, y = start

    coords = [(x, y, labels[current_direction])] # include starting position

    for n_str, direction in tokens:
        steps = int(n_str)
        direction = direction.upper()

        if turn_then_move:
            if direction == "L":
                current_direction = (current_direction - 1) % 4 # rotate 90° left                
            elif direction == "R":
                current_direction = (current_direction + 1) % 4 # rotate 90° right                
            elif direction == "B":                
                current_direction = (current_direction + 2) % 4 # rotate 180°                

            dx, dy = directions[current_direction]            
            x += dx * steps
            y += dy * steps

        else:
            # fixed facing (North = +Y, East = +X)
            if direction == "F": y += steps
            elif direction == "B": y -= steps
            elif direction == "R": x += steps
            elif direction == "L": x -= steps

        coords.append((x, y, labels[current_direction]))

    return coords

def main():
    parser = argparse.ArgumentParser(description="Adventurer Journey Distance Calculator")
    parser.add_argument('--path', type=str, default=None, help="Path as a string (e.g., '15F6B...').")
    parser.add_argument("--verbose", action="store_true", help="Print step-by-step coordinates.")
    parser.add_argument("--fixed-axes", action="store_true", help="Use fixed-axes movement model.")
    args = parser.parse_args()

    input_path = args.path or DEFAULT_PATH

    # Validate path.
    if not validate_path(input_path):
        print(f"Invalid path format: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Get coordinates based on movement model.
    if args.fixed_axes:
        coords = get_path_coords(input_path, turn_then_move=False)        
    else:
        coords = get_path_coords(input_path, turn_then_move=True)
    
    # Calculate Euclidean distance from start to end.
    x0, y0, _ = coords[0]
    x1, y1, _ = coords[-1]
    distance = hypot(x1 - x0, y1 - y0)

    # Output results.
    print("Adventurer Journey")
    print(f"Path: {input_path}")
    print(f'Model: {"fixed-axes" if args.fixed_axes else "turn-then-move"}')
    if args.verbose:        
        print("Coords:")
        for i, (x, y, direction) in enumerate(coords):
            print(f"({x}, {y}) direction={direction}")
    print(f"End Coords & Direction: {coords[-1]}")
    print(f"Distance: {distance}")

if __name__ == '__main__':
    main()
