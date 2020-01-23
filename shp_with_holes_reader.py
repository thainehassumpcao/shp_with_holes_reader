# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:34:47 2020

@author: Thaine H. Assumpção

Reads a shapefile with one feature of multipolygons with holes.
Gets its geometry and area.

"""

from pathlib import Path
from osgeo import ogr

my_dir = Path(r'D:\Python')
shp = r'test_shape_area.shp'


Driver = ogr.GetDriverByName('ESRI Shapefile')
DataSource = Driver.Open((my_dir / shp).as_posix(), 0)
Layer = DataSource.GetLayer()
print('Number of features: {}'.format(Layer.GetFeatureCount()))

Geom = ogr.Geometry(ogr.wkbGeometryCollection)


for feature in Layer:
    multipolygon = feature.GetGeometryRef()
    print('Number of polygons: {}'.format(multipolygon.GetGeometryCount()))

    for j in range(multipolygon.GetGeometryCount()):
        polygon = multipolygon.GetGeometryRef(j)
        if polygon.GetGeometryCount() > 1:
            print('Number of rings (when >1): {}'.format(
                polygon.GetGeometryCount()))

        newPolygon = ogr.Geometry(ogr.wkbPolygon)

        for i in range(polygon.GetGeometryCount()):
            ring = polygon.GetGeometryRef(i)
            newPolygon.AddGeometry(ring)

        Geom.AddGeometry(newPolygon)


Geom.CloseRings()

print('Number of polygons in the final geometry: {}'.format(
    Geom.GetGeometryCount()))
print('Area of the final geometry: {}'.format(Geom.GetArea()))
