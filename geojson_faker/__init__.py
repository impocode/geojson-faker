from geojson_faker.faker import GeoJsonFaker
from geojson_faker.generators import (
    fake_altitude,
    fake_latitude,
    fake_line_string,
    fake_longitude,
    fake_multi_point,
    fake_point,
    fake_position,
)

__version__ = "0.1.0"

__all__ = [
    "GeoJsonFaker",
    "fake_longitude",
    "fake_latitude",
    "fake_altitude",
    "fake_position",
    "fake_point",
    "fake_multi_point",
    "fake_line_string",
]
