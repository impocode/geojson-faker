from random import randrange, uniform

from geojson_pydantic.types import Position, Position2D, Position3D

from geojson_faker.constants import DIMENSIONS
from geojson_faker.types import Dimension


def fake_longitude() -> float:
    return uniform(-180, 180)


def fake_latitude() -> float:
    return uniform(-90, 90)


def fake_altitude() -> float:
    return uniform(-10000, 50000)


def fake_position(dimension: Dimension | None = None) -> Position:
    dimension = DIMENSIONS[randrange(len(DIMENSIONS))] if dimension is None else dimension
    if dimension == Dimension.two:
        return Position2D(longitude=fake_longitude(), latitude=fake_latitude())
    return Position3D(
        longitude=fake_longitude(), latitude=fake_latitude(), altitude=fake_altitude()
    )
