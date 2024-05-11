from collections.abc import Callable
from typing import TypeVar

from geojson_pydantic.types import Position

from geojson_faker.constants import geo_keys
from geojson_faker.generators import fake_position
from geojson_faker.types import Dimension

_GeoJsonType = TypeVar("_GeoJsonType")


class GeoJsonFaker:
    def __init__(self, random_always: bool = True):
        self._random_always = random_always
        self._data = {
            geo_keys.position: None,
            geo_keys.position2d: None,
            geo_keys.position3d: None,
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
