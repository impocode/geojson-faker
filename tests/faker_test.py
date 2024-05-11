from geojson_pydantic.geometries import LineString, MultiPoint, Point
from geojson_pydantic.types import Position, Position2D, Position3D

from geojson_faker import GeoJsonFaker


def test_random_always():
    geojson_faker = GeoJsonFaker()
    position_one = geojson_faker.position
    position_two = geojson_faker.position
    assert position_one != position_two
    assert id(position_one) != id(position_two)

    geojson_faker = GeoJsonFaker(random_always=True)
    position_one = geojson_faker.position
    position_two = geojson_faker.position
    assert position_one != position_two
    assert id(position_one) != id(position_two)

    geojson_faker = GeoJsonFaker(random_always=False)
    position_one = geojson_faker.position
    position_two = geojson_faker.position
    assert position_one == position_two
    assert id(position_one) == id(position_two)


def test_position():
    geojson_faker = GeoJsonFaker()
    position = geojson_faker.position
    assert isinstance(position, Position)
    assert isinstance(position, Position2D) or isinstance(position, Position3D)
    assert isinstance(position.longitude, float)
    assert isinstance(position.latitude, float)
    if isinstance(position, Position3D):
        assert isinstance(position.altitude, float)


def test_position2d():
    geojson_faker = GeoJsonFaker()
    position = geojson_faker.position2d
    assert isinstance(position, Position2D) and not isinstance(position, Position3D)
    assert isinstance(position.longitude, float)
    assert isinstance(position.latitude, float)


def test_position3d():
    geojson_faker = GeoJsonFaker()
    position = geojson_faker.position3d
    assert isinstance(position, Position3D) and not isinstance(position, Position2D)
    assert isinstance(position.longitude, float)
    assert isinstance(position.latitude, float)
    assert isinstance(position.altitude, float)


def test_point():
    geojson_faker = GeoJsonFaker()
    point = geojson_faker.point

    assert isinstance(point, Point)
    assert point.type == "Point"

    assert isinstance(point.coordinates, Position2D) or isinstance(point.coordinates, Position3D)
    assert isinstance(point.coordinates.longitude, float)
    assert isinstance(point.coordinates.latitude, float)
    if isinstance(point.coordinates, Position3D):
        assert isinstance(point.coordinates.altitude, float)


def test_point2d():
    geojson_faker = GeoJsonFaker()
    point = geojson_faker.point2d

    assert isinstance(point, Point)
    assert point.type == "Point"

    assert isinstance(point.coordinates, Position2D) and not isinstance(
        point.coordinates, Position3D
    )
    assert isinstance(point.coordinates.longitude, float)
    assert isinstance(point.coordinates.latitude, float)


def test_point3d():
    geojson_faker = GeoJsonFaker()
    point = geojson_faker.point3d

    assert isinstance(point, Point)
    assert point.type == "Point"

    assert isinstance(point.coordinates, Position3D) and not isinstance(
        point.coordinates, Position2D
    )
    assert isinstance(point.coordinates.longitude, float)
    assert isinstance(point.coordinates.latitude, float)
    assert isinstance(point.coordinates.altitude, float)


def test_multi_point():
    geojson_faker = GeoJsonFaker()
    multi_point = geojson_faker.multi_point

    assert isinstance(multi_point, MultiPoint)
    assert multi_point.type == "MultiPoint"
    assert 0 < len(multi_point.coordinates) < 1000

    for coordinates in multi_point.coordinates:
        assert isinstance(coordinates, Position2D) or isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)
        if isinstance(coordinates, Position3D):
            assert isinstance(coordinates.altitude, float)


def test_multi_point2d():
    geojson_faker = GeoJsonFaker()
    multi_point = geojson_faker.multi_point2d

    assert isinstance(multi_point, MultiPoint)
    assert multi_point.type == "MultiPoint"
    assert 0 < len(multi_point.coordinates) < 1000

    for coordinates in multi_point.coordinates:
        assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)


def test_multi_point3d():
    geojson_faker = GeoJsonFaker()
    multi_point = geojson_faker.multi_point3d

    assert isinstance(multi_point, MultiPoint)
    assert multi_point.type == "MultiPoint"
    assert 0 < len(multi_point.coordinates) < 1000

    for coordinates in multi_point.coordinates:
        assert isinstance(coordinates, Position3D) and not isinstance(coordinates, Position2D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)
        assert isinstance(coordinates.altitude, float)


def test_line_string():
    geojson_faker = GeoJsonFaker()
    line_string = geojson_faker.line_string

    assert isinstance(line_string, LineString)
    assert line_string.type == "LineString"
    assert 2 < len(line_string.coordinates) < 1000

    for coordinates in line_string.coordinates:
        assert isinstance(coordinates, Position2D) or isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)
        if isinstance(coordinates, Position3D):
            assert isinstance(coordinates.altitude, float)


def test_line_string2d():
    geojson_faker = GeoJsonFaker()
    line_string = geojson_faker.line_string2d

    assert isinstance(line_string, LineString)
    assert line_string.type == "LineString"
    assert 2 < len(line_string.coordinates) < 1000

    for coordinates in line_string.coordinates:
        assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)


def test_line_string3d():
    geojson_faker = GeoJsonFaker()
    line_string = geojson_faker.line_string3d

    assert isinstance(line_string, LineString)
    assert line_string.type == "LineString"
    assert 2 < len(line_string.coordinates) < 1000

    for coordinates in line_string.coordinates:
        assert isinstance(coordinates, Position3D) and not isinstance(coordinates, Position2D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)
        assert isinstance(coordinates.altitude, float)
