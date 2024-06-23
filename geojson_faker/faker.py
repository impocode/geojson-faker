from collections.abc import Callable
from typing import TypeVar

from geojson_pydantic.geometries import (
    GeometryCollection,
    LineString,
    MultiLineString,
    MultiPoint,
    MultiPolygon,
    Point,
    Polygon,
)
from geojson_pydantic.types import Position

from geojson_faker.constants import geo_keys
from geojson_faker.generators import (
    fake_geometry_collection,
    fake_line_string,
    fake_multi_line_string,
    fake_multi_point,
    fake_multi_polygon,
    fake_point,
    fake_polygon,
    fake_position,
)
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
            geo_keys.multi_line_string: None,
            geo_keys.multi_line_string2d: None,
            geo_keys.multi_line_string3d: None,
            geo_keys.polygon: None,
            geo_keys.polygon2d: None,
            geo_keys.polygon3d: None,
            geo_keys.multi_polygon: None,
            geo_keys.multi_polygon2d: None,
            geo_keys.multi_polygon3d: None,
            geo_keys.geometry_collection: None,
            geo_keys.geometry_collection2d: None,
            geo_keys.geometry_collection3d: None,
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

    @property
    def multi_line_string(self) -> MultiLineString:
        return self._fake(func=fake_multi_line_string, geo_key=geo_keys.multi_line_string)

    @property
    def multi_line_string2d(self) -> MultiLineString:
        return self._fake(
            func=fake_multi_line_string,
            geo_key=geo_keys.multi_line_string2d,
            dimension=Dimension.two,
        )

    @property
    def multi_line_string3d(self) -> MultiLineString:
        return self._fake(
            func=fake_multi_line_string,
            geo_key=geo_keys.multi_line_string3d,
            dimension=Dimension.three,
        )

    @property
    def polygon(self) -> Polygon:
        return self._fake(func=fake_polygon, geo_key=geo_keys.polygon)

    @property
    def polygon2d(self) -> Polygon:
        return self._fake(func=fake_polygon, geo_key=geo_keys.polygon2d, dimension=Dimension.two)

    @property
    def polygon3d(self) -> Polygon:
        return self._fake(func=fake_polygon, geo_key=geo_keys.polygon3d, dimension=Dimension.three)

    @property
    def multi_polygon(self) -> MultiPolygon:
        return self._fake(func=fake_multi_polygon, geo_key=geo_keys.multi_polygon)

    @property
    def multi_polygon2d(self) -> MultiPolygon:
        return self._fake(
            func=fake_multi_polygon, geo_key=geo_keys.multi_polygon2d, dimension=Dimension.two
        )

    @property
    def multi_polygon3d(self) -> MultiPolygon:
        return self._fake(
            func=fake_multi_polygon, geo_key=geo_keys.multi_polygon3d, dimension=Dimension.three
        )

    @property
    def geometry_collection(self) -> GeometryCollection:
        return self._fake(func=fake_geometry_collection, geo_key=geo_keys.geometry_collection)

    @property
    def geometry_collection2d(self) -> GeometryCollection:
        return self._fake(
            func=fake_geometry_collection,
            geo_key=geo_keys.geometry_collection2d,
            dimension=Dimension.two,
        )

    @property
    def geometry_collection3d(self) -> GeometryCollection:
        return self._fake(
            func=fake_geometry_collection,
            geo_key=geo_keys.geometry_collection3d,
            dimension=Dimension.three,
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
