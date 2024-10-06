from constants import ___
from typing import Tuple


def is_point_in_square(point: Tuple[int, int], left_upper_corner: Tuple[int, int], right_bottom_corner: Tuple[int, int]) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
