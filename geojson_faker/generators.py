from random import randint, randrange, uniform

from geojson_pydantic.geometries import LineString, MultiPoint, Point
from geojson_pydantic.types import Position, Position2D, Position3D

from geojson_faker.constants import DIMENSIONS
from geojson_faker.types import Dimension


def _get_dimension(dimension: Dimension | None = None) -> Dimension:
    return dimension or DIMENSIONS[randrange(len(DIMENSIONS))]


def fake_longitude() -> float:
    return uniform(-180, 180)


def fake_latitude() -> float:
    return uniform(-90, 90)


def fake_altitude() -> float:
    return uniform(-10000, 50000)


def fake_position(dimension: Dimension | None = None) -> Position:
    dimension = _get_dimension(dimension=dimension)
    if dimension == Dimension.two:
        return Position2D(longitude=fake_longitude(), latitude=fake_latitude())
    return Position3D(
        longitude=fake_longitude(), latitude=fake_latitude(), altitude=fake_altitude()
    )


def fake_point(dimension: Dimension | None = None) -> Point:
    return Point(type="Point", coordinates=fake_position(dimension=dimension))


def fake_multi_point(dimension: Dimension | None = None, max_length: int = 1000) -> MultiPoint:
    return MultiPoint(
        type="MultiPoint",
        coordinates=[fake_position(dimension=dimension) for _ in range(0, randint(0, max_length))],
    )


def fake_line_string(dimension: Dimension | None = None, max_length: int = 1000) -> LineString:
    min_length = 2
    if max_length < min_length:
        max_length = min_length
    return LineString(
        type="LineString",
        coordinates=[
            fake_position(dimension=dimension) for _ in range(0, randint(min_length, max_length))
        ],
    )
