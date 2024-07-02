from geojson_pydantic.features import Feature
from geojson_pydantic.geometries import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
    _GeometryBase,
)
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
    assert 0 < len(multi_point.coordinates) <= 100

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
    assert 0 < len(multi_point.coordinates) <= 100

    for coordinates in multi_point.coordinates:
        assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)


def test_multi_point3d():
    geojson_faker = GeoJsonFaker()
    multi_point = geojson_faker.multi_point3d

    assert isinstance(multi_point, MultiPoint)
    assert multi_point.type == "MultiPoint"
    assert 0 < len(multi_point.coordinates) <= 100

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
    assert 2 <= len(line_string.coordinates) <= 100

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
    assert 2 <= len(line_string.coordinates) <= 100

    for coordinates in line_string.coordinates:
        assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)


def test_line_string3d():
    geojson_faker = GeoJsonFaker()
    line_string = geojson_faker.line_string3d

    assert isinstance(line_string, LineString)
    assert line_string.type == "LineString"
    assert 2 <= len(line_string.coordinates) <= 100

    for coordinates in line_string.coordinates:
        assert isinstance(coordinates, Position3D) and not isinstance(coordinates, Position2D)
        assert isinstance(coordinates.longitude, float)
        assert isinstance(coordinates.latitude, float)
        assert isinstance(coordinates.altitude, float)


def test_multi_line_string():
    geojson_faker = GeoJsonFaker()
    multi_line_string = geojson_faker.multi_line_string

    assert isinstance(multi_line_string, MultiLineString)
    assert multi_line_string.type == "MultiLineString"
    assert 0 < len(multi_line_string.coordinates) <= 100

    for line_string in multi_line_string.coordinates:
        assert isinstance(line_string, list)
        assert 2 <= len(line_string) <= 100
        for coordinates in line_string:
            assert isinstance(coordinates, Position2D) or isinstance(coordinates, Position3D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)
            if isinstance(coordinates, Position3D):
                assert isinstance(coordinates.altitude, float)


def test_multi_line_string2d():
    geojson_faker = GeoJsonFaker()
    multi_line_string = geojson_faker.multi_line_string2d

    assert isinstance(multi_line_string, MultiLineString)
    assert multi_line_string.type == "MultiLineString"
    assert 0 < len(multi_line_string.coordinates) <= 100

    for line_string in multi_line_string.coordinates:
        assert isinstance(line_string, list)
        assert 2 <= len(line_string) <= 100
        for coordinates in line_string:
            assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)


def test_multi_line_string3d():
    geojson_faker = GeoJsonFaker()
    multi_line_string = geojson_faker.multi_line_string3d

    assert isinstance(multi_line_string, MultiLineString)
    assert multi_line_string.type == "MultiLineString"
    assert 0 < len(multi_line_string.coordinates) <= 100

    for line_string in multi_line_string.coordinates:
        assert isinstance(line_string, list)
        assert 2 <= len(line_string) <= 100
        for coordinates in line_string:
            assert isinstance(coordinates, Position3D) and not isinstance(coordinates, Position2D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)
            assert isinstance(coordinates.altitude, float)


def test_polygon():
    geojson_faker = GeoJsonFaker()
    polygon = geojson_faker.polygon

    assert isinstance(polygon, Polygon)
    assert polygon.type == "Polygon"
    assert 0 < len(polygon.coordinates) <= 100

    for linear_ring in polygon.coordinates:
        assert isinstance(linear_ring, list)
        assert 4 <= len(linear_ring) <= 100
        for coordinates in linear_ring:
            assert isinstance(coordinates, Position2D) or isinstance(coordinates, Position3D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)
            if isinstance(coordinates, Position3D):
                assert isinstance(coordinates.altitude, float)


def test_polygon2d():
    geojson_faker = GeoJsonFaker()
    polygon = geojson_faker.polygon2d

    assert isinstance(polygon, Polygon)
    assert polygon.type == "Polygon"
    assert 0 < len(polygon.coordinates) <= 100

    for linear_ring in polygon.coordinates:
        assert isinstance(linear_ring, list)
        assert 4 <= len(linear_ring) <= 100
        for coordinates in linear_ring:
            assert isinstance(coordinates, Position2D) and not isinstance(coordinates, Position3D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)


def test_polygon3d():
    geojson_faker = GeoJsonFaker()
    polygon = geojson_faker.polygon3d

    assert isinstance(polygon, Polygon)
    assert polygon.type == "Polygon"
    assert 0 < len(polygon.coordinates) <= 100

    for linear_ring in polygon.coordinates:
        assert isinstance(linear_ring, list)
        assert 4 <= len(linear_ring) <= 100
        for coordinates in linear_ring:
            assert isinstance(coordinates, Position3D) and not isinstance(coordinates, Position2D)
            assert isinstance(coordinates.longitude, float)
            assert isinstance(coordinates.latitude, float)
            assert isinstance(coordinates.altitude, float)


def test_multi_polygon():
    geojson_faker = GeoJsonFaker()
    multi_polygon = geojson_faker.multi_polygon

    assert isinstance(multi_polygon, MultiPolygon)
    assert multi_polygon.type == "MultiPolygon"
    assert 0 < len(multi_polygon.coordinates) <= 100

    for polygon in multi_polygon.coordinates:
        assert isinstance(polygon, list)
        for linear_ring in polygon:
            assert isinstance(linear_ring, list)
            assert 4 <= len(linear_ring) <= 100
            for coordinates in linear_ring:
                assert isinstance(coordinates, Position2D) or isinstance(coordinates, Position3D)
                assert isinstance(coordinates.longitude, float)
                assert isinstance(coordinates.latitude, float)
                if isinstance(coordinates, Position3D):
                    assert isinstance(coordinates.altitude, float)


def test_multi_polygon2d():
    geojson_faker = GeoJsonFaker()
    multi_polygon = geojson_faker.multi_polygon2d

    assert isinstance(multi_polygon, MultiPolygon)
    assert multi_polygon.type == "MultiPolygon"
    assert 0 < len(multi_polygon.coordinates) <= 100

    for polygon in multi_polygon.coordinates:
        assert isinstance(polygon, list)
        for linear_ring in polygon:
            assert isinstance(linear_ring, list)
            assert 4 <= len(linear_ring) <= 100
            for coordinates in linear_ring:
                assert isinstance(coordinates, Position2D) and not isinstance(
                    coordinates, Position3D
                )
                assert isinstance(coordinates.longitude, float)
                assert isinstance(coordinates.latitude, float)


def test_multi_polygon3d():
    geojson_faker = GeoJsonFaker()
    multi_polygon = geojson_faker.multi_polygon3d

    assert isinstance(multi_polygon, MultiPolygon)
    assert multi_polygon.type == "MultiPolygon"
    assert 0 < len(multi_polygon.coordinates) <= 100

    for polygon in multi_polygon.coordinates:
        assert isinstance(polygon, list)
        for linear_ring in polygon:
            assert isinstance(linear_ring, list)
            assert 4 <= len(linear_ring) <= 100
            for coordinates in linear_ring:
                assert isinstance(coordinates, Position3D) and not isinstance(
                    coordinates, Position2D
                )
                assert isinstance(coordinates.longitude, float)
                assert isinstance(coordinates.latitude, float)
                assert isinstance(coordinates.altitude, float)


def test_geometry_collection():
    geojson_faker = GeoJsonFaker()
    geometry_collection = geojson_faker.geometry_collection

    assert isinstance(geometry_collection, GeometryCollection)
    assert geometry_collection.type == "GeometryCollection"
    assert len(geometry_collection.geometries) > 0

    for geometry in geometry_collection.geometries:
        assert isinstance(geometry, _GeometryBase)


def test_geometry_collection2d():
    geojson_faker = GeoJsonFaker()
    geometry_collection = geojson_faker.geometry_collection2d

    assert isinstance(geometry_collection, GeometryCollection)
    assert geometry_collection.type == "GeometryCollection"
    assert len(geometry_collection.geometries) > 0

    for geometry in geometry_collection.geometries:
        assert isinstance(geometry, _GeometryBase)


def test_geometry_collection3d():
    geojson_faker = GeoJsonFaker()
    geometry_collection = geojson_faker.geometry_collection3d

    assert isinstance(geometry_collection, GeometryCollection)
    assert geometry_collection.type == "GeometryCollection"
    assert len(geometry_collection.geometries) > 0

    for geometry in geometry_collection.geometries:
        assert isinstance(geometry, _GeometryBase)


def test_country():
    geojson_faker = GeoJsonFaker()
    country = geojson_faker.country

    assert isinstance(country, Feature)
    assert country.type == "Feature"
    assert isinstance(country.geometry, Polygon) or isinstance(country.geometry, MultiPolygon)
    assert country.properties is not None
