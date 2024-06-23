from random import randint, randrange, uniform

from geojson_pydantic.geometries import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from geojson_pydantic.types import Position, Position2D, Position3D

from geojson_faker.constants import DIMENSIONS
from geojson_faker.types import Dimension


def _get_dimension(dimension: Dimension | None = None) -> Dimension:
    return dimension or DIMENSIONS[randrange(len(DIMENSIONS))]


def _randintrange(min_value: int, max_value: int) -> range:
    return range(0, randint(min_value, max_value))


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


def fake_multi_point(dimension: Dimension | None = None, max_coordinates: int = 100) -> MultiPoint:
    return MultiPoint(
        type="MultiPoint",
        coordinates=[fake_position(dimension=dimension) for _ in _randintrange(1, max_coordinates)],
    )


def fake_line_string(dimension: Dimension | None = None, max_coordinates: int = 100) -> LineString:
    min_coordinates = 2
    if max_coordinates < min_coordinates:
        max_coordinates = min_coordinates
    return LineString(
        type="LineString",
        coordinates=[
            fake_position(dimension=dimension)
            for _ in _randintrange(min_coordinates, max_coordinates)
        ],
    )


def fake_multi_line_string(
    dimension: Dimension | None = None,
    max_coordinates: int = 100,
    max_line_string_coordinates: int = 100,
) -> MultiLineString:
    min_line_string_coordinates = 2
    if max_line_string_coordinates < min_line_string_coordinates:
        max_line_string_coordinates = min_line_string_coordinates
    coordinates = []
    for _ in _randintrange(1, max_coordinates):
        coordinates.append(
            [
                fake_position(dimension=dimension)
                for _ in _randintrange(min_line_string_coordinates, max_line_string_coordinates)
            ]
        )
    return MultiLineString(type="MultiLineString", coordinates=coordinates)


def fake_polygon(
    dimension: Dimension | None = None,
    max_coordinates: int = 100,
    max_linear_ring_coordinates: int = 100,
) -> Polygon:
    min_linear_ring_coordinates = 4
    if max_linear_ring_coordinates < min_linear_ring_coordinates:
        max_linear_ring_coordinates = min_linear_ring_coordinates
    coordinates = []
    for _ in _randintrange(1, max_coordinates):
        start_coordinates = end_coordinates = fake_position(dimension=dimension)
        linear_ring = []
        linear_ring.append(start_coordinates)
        linear_ring.extend(
            [
                fake_position(dimension=dimension)
                for _ in _randintrange(
                    min_linear_ring_coordinates - 2, max_linear_ring_coordinates - 2
                )
            ]
        )
        linear_ring.append(end_coordinates)
        coordinates.append(linear_ring)
    return Polygon(type="Polygon", coordinates=coordinates)


def fake_multi_polygon(
    dimension: Dimension | None = None,
    max_coordinates: int = 100,
    max_polygon_coordinates: int = 100,
    max_linear_ring_coordinates: int = 100,
) -> MultiPolygon:
    min_linear_ring_coordinates = 4
    if max_linear_ring_coordinates < min_linear_ring_coordinates:
        max_linear_ring_coordinates = min_linear_ring_coordinates
    coordinates = []
    for _ in _randintrange(1, max_coordinates):
        polygon_coordinates = []
        for _ in _randintrange(1, max_polygon_coordinates):
            start_coordinates = end_coordinates = fake_position(dimension=dimension)
            linear_ring = []
            linear_ring.append(start_coordinates)
            linear_ring.extend(
                [
                    fake_position(dimension=dimension)
                    for _ in _randintrange(
                        min_linear_ring_coordinates - 2, max_linear_ring_coordinates - 2
                    )
                ]
            )
            linear_ring.append(end_coordinates)
            polygon_coordinates.append(linear_ring)
        coordinates.append(polygon_coordinates)
    return MultiPolygon(type="MultiPolygon", coordinates=coordinates)


def fake_geometry_collection(
    dimension: Dimension | None = None,
    # points
    max_points: int = 10,
    # multi_points
    max_multi_points: int = 10,
    # line_strings
    max_line_strings: int = 10,
    # multi_line_strings
    max_multi_line_strings: int = 10,
    # polygons
    max_polygons: int = 10,
    # multi_polygons
    max_multi_polygons: int = 10,
) -> GeometryCollection:
    geometries = []
    if max_points > 0:
        geometries.extend([fake_point(dimension=dimension) for _ in _randintrange(1, max_points)])
    if max_multi_points > 0:
        geometries.extend(
            [fake_multi_point(dimension=dimension) for _ in _randintrange(1, max_multi_points)]
        )
    if max_line_strings > 0:
        geometries.extend(
            [fake_line_string(dimension=dimension) for _ in _randintrange(1, max_line_strings)]
        )
    if max_multi_line_strings > 0:
        geometries.extend(
            [
                fake_multi_line_string(dimension=dimension)
                for _ in _randintrange(1, max_multi_line_strings)
            ]
        )
    if max_polygons > 0:
        geometries.extend(
            [fake_polygon(dimension=dimension) for _ in _randintrange(1, max_polygons)]
        )
    if max_multi_polygons > 0:
        geometries.extend(
            [fake_multi_polygon(dimension=dimension) for _ in _randintrange(1, max_multi_polygons)]
        )

    return GeometryCollection(type="GeometryCollection", geometries=geometries)
