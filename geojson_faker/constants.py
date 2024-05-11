from typing import NamedTuple

from geojson_faker.types import Dimension


class geo_keys(NamedTuple):
    position = "position"
    position2d = "position2d"
    position3d = "position3d"


DIMENSIONS = [Dimension.two, Dimension.three]

__all__ = ["geo_keys", "DIMENSIONS"]
