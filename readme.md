# geojson-faker

## Description

`geojson-faker` is a fake GeoJson data generator.

## Supported GeoJSON objects

|   GeoJSON object   |    Status   |
|:------------------:|:-----------:|
|      Position      |     done    |
|       Point        |     done    |
|     MultiPoint     |     done    |
|     LineString     |     done    |
|  MultiLineString   |     done    |
|      Polygon       |     done    |
|    MultiPolygon    |     done    |
| GeometryCollection |     done    |
|      Feature       | in progress |
|  FeatureCollection | in progress |

## Usage

To generate fake geodata, you can use both methods and a special class `GeoJsonFaker`.

Example of generation a random `Point` using the `fake_point` method:

```python
>>> from geojson_faker import fake_point, Dimension
>>> # Point2D or Point3D
>>> fake_point()
Point(bbox=None, type='Point', coordinates=Position2D(longitude=-97.30689091127957, latitude=56.891859157037686))
>>> fake_point()
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-23.91579574348077, latitude=-29.49843686198053, altitude=38061.79569985675))
>>> # Point2D
>>> fake_point(dimension=Dimension.two)
Point(bbox=None, type='Point', coordinates=Position2D(longitude=-165.04984397840835, latitude=76.97108937919282))
>>> # Point3D
>>> fake_point(dimension=Dimension.three)
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-118.39348949345089, latitude=27.81106033708747, altitude=8475.464707933897))
```

Example of generation using the class:

```python
>>> from geojson_faker import GeoJsonFaker
>>> geojson_faker = GeoJsonFaker()
>>> # Point2D or Point3D
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position2D(longitude=-50.56703965217093, latitude=19.72513434718111))
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position3D(longitude=111.84911865610678, latitude=-19.488979926988165, altitude=7921.968274391678))
>>> # Point2D
>>> geojson_faker.point2d
Point(bbox=None, type='Point', coordinates=Position2D(longitude=29.98434638920918, latitude=36.476444735501616))
>>> # Point3D
>>> geojson_faker.point3d
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-76.36126084558762, latitude=30.682266859380533, altitude=15816.987234147065))
```

The class has some advantages, so I would recommend using it preferably.

### Random always

The `random_always` setting allows you to specify whether to generate random data permanently or to remember the last result and reuse it.

An example with `Point`:

```python
>>> from geojson_faker import GeoJsonFaker
>>> # random_always is True by default
>>> geojson_faker = GeoJsonFaker()
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position2D(longitude=136.68932246536838, latitude=-69.51345731343906))
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-86.5130499597834, latitude=-32.985220372899015, altitude=39772.673364264505))
>>>
>>> # Set random_always to False
>>> geojson_faker = GeoJsonFaker(random_always=False)
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-124.54510003846121, latitude=25.225529991773328, altitude=-423.45973067919476))
>>> geojson_faker.point
Point(bbox=None, type='Point', coordinates=Position3D(longitude=-124.54510003846121, latitude=25.225529991773328, altitude=-423.45973067919476))
```
