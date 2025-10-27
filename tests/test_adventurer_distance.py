from math import hypot
import pytest
from adventurer_distance import DEFAULT_PATH, get_path_coords, validate_path

def euclidean_distance(coords):
    (x0, y0, _), (x1, y1, _) = coords[0], coords[-1]
    return hypot(x1 - x0, y1 - y0)

@pytest.mark.parametrize(
    "path,expected",
    [
        (DEFAULT_PATH, True),
        ("1F2B3L4R", True),
        ("01f5R", True),  # zeros allowed, case-insensitive
        ("", False),
        (None, False),
        ("12X", False),
        ("F10", False),
    ],
)

def test_validate_path(path, expected):
    assert validate_path(path) == expected

def test_turn_then_move_default_path_distance():
    coords = get_path_coords(DEFAULT_PATH, turn_then_move=True)
    assert coords[-1][:2] == (34, -4)
    assert euclidean_distance(coords) == pytest.approx(34.23448553724738)

def test_fixed_axes_default_path_distance():
    coords = get_path_coords(DEFAULT_PATH, turn_then_move=False)
    assert coords[-1][:2] == (2, 30)
    assert euclidean_distance(coords) == pytest.approx(30.066592756745816)


@pytest.mark.parametrize(
    "path,turn_then_move,expected_end",
    [
        ("1F1R1F", True, (2, 1)), # rotate then advance twice facing east
        ("1F1R1F", False, (1, 2)), # strafing interpretation
        ("1R1R1R1R", True, (0, 0)), # makes a square, ends at origin
        ("1R1R1R1R", False, (4, 0)), # always moves east
        ("1F1B1R1L", False, (0, 0)), # cancels out in fixed-axis mode
        ("3r2l", False, (1, 0)), # lowercase handling, strafing
        ("1F2R2R1F4B", True, (2, 2)) # complex turn-then-move
        ("1F2R2R1F4B", False, (2, 2)) # complex turn-then-move
    ],
)
def test_endpoints_match_expected(path, turn_then_move, expected_end):
    coords = get_path_coords(path, turn_then_move=turn_then_move)
    assert coords[-1][:2] == expected_end

def test_zero_step_turn_changes_heading_without_moving():
    coords = get_path_coords("0L4F", turn_then_move=True)
    # First token rotates left but keeps position, second walks west
    assert coords[-1] == (-4, 0, "W")
