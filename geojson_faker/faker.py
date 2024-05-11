from collections.abc import Callable
from typing import TypeVar

from geojson_pydantic.geometries import LineString, MultiPoint, Point
from geojson_pydantic.types import Position

from geojson_faker.constants import geo_keys
from geojson_faker.generators import fake_line_string, fake_multi_point, fake_point, fake_position
from geojson_faker.types import Dimension

_GeoJsonType = TypeVar("_GeoJsonType")


class GeoJsonFaker:
    def __init__(self, random_always: bool = True):
        self._random_always = random_always
        self._data = {
            geo_keys.position: None,
            geo_keys.position2d: None,
            geo_keys.position3d: None,
            geo_keys.point: None,
            geo_keys.point2d: None,
            geo_keys.point3d: None,
            geo_keys.multi_point: None,
            geo_keys.multi_point2d: None,
            geo_keys.multi_point3d: None,
            geo_keys.line_string: None,
            geo_keys.line_string2d: None,
            geo_keys.line_string3d: None,
        }

    @property
    def position(self) -> Position:
        return self._fake(func=fake_position, geo_key=geo_keys.position)

    @property
    def position2d(self) -> Position:
        return self._fake(func=fake_position, geo_key=geo_keys.position2d, dimension=Dimension.two)

    @property
    def position3d(self) -> Position:
        return self._fake(
            func=fake_position, geo_key=geo_keys.position3d, dimension=Dimension.three
        )

    @property
    def point(self) -> Point:
        return self._fake(func=fake_point, geo_key=geo_keys.point)

    @property
    def point2d(self) -> Point:
        return self._fake(func=fake_point, geo_key=geo_keys.point2d, dimension=Dimension.two)

    @property
    def point3d(self) -> Point:
        return self._fake(func=fake_point, geo_key=geo_keys.point3d, dimension=Dimension.three)

    @property
    def multi_point(self) -> MultiPoint:
        return self._fake(func=fake_multi_point, geo_key=geo_keys.multi_point)

    @property
    def multi_point2d(self) -> MultiPoint:
        return self._fake(
            func=fake_multi_point, geo_key=geo_keys.multi_point2d, dimension=Dimension.two
        )

    @property
    def multi_point3d(self) -> MultiPoint:
        return self._fake(
            func=fake_multi_point, geo_key=geo_keys.multi_point3d, dimension=Dimension.three
        )

    @property
    def line_string(self) -> LineString:
        return self._fake(func=fake_line_string, geo_key=geo_keys.line_string)

    @property
    def line_string2d(self) -> LineString:
        return self._fake(
            func=fake_line_string, geo_key=geo_keys.line_string2d, dimension=Dimension.two
        )

    @property
    def line_string3d(self) -> LineString:
        return self._fake(
            func=fake_line_string, geo_key=geo_keys.line_string3d, dimension=Dimension.three
        )

    def _fake(
        self,
        func: Callable[[Dimension | None], _GeoJsonType],
        geo_key: str,
        dimension: None | Dimension = None,
    ) -> _GeoJsonType:
        if self._random_always:
            return func(dimension)

        if self._data[geo_key] is None:
            self._data[geo_key] = func(dimension)
            return self._data[geo_key]

        return self._data[geo_key]


__all__ = ["GeoJsonFaker"]
