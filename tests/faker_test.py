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
    assert isinstance(position, Position2D)
    assert isinstance(position.longitude, float)
    assert isinstance(position.latitude, float)


def test_position3d():
    geojson_faker = GeoJsonFaker()
    position = geojson_faker.position3d
    assert isinstance(position, Position3D)
    assert isinstance(position.longitude, float)
    assert isinstance(position.latitude, float)
    assert isinstance(position.altitude, float)
