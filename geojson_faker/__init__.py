from geojson_faker.faker import GeoJsonFaker
from geojson_faker.generators import (
    fake_altitude,
    fake_latitude,
    fake_line_string,
    fake_longitude,
    fake_multi_line_string,
    fake_multi_point,
    fake_point,
    fake_polygon,
    fake_position,
)

__version__ = "0.3.0"

__all__ = [
    "GeoJsonFaker",
    "fake_longitude",
    "fake_latitude",
    "fake_altitude",
    "fake_position",
    "fake_point",
    "fake_multi_point",
    "fake_line_string",
    "fake_multi_line_string",
    "fake_polygon",
]
