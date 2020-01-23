# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:58:12 2020

@author: Thaine H. Assumpção

Reads a shapefile with one feature of multipolygons with holes.
Gets its geometry and area.

"""

from pathlib import Path
import shapefile
from shapely.geometry import shape

my_dir = Path(r'D:\Python')
shp = r'test_shape_area.shp'

my_shape = shapefile.Reader((my_dir / shp).as_posix())
print('Number of features: {}'.format(len(my_shape.shapeRecords())))
feature = my_shape.shapeRecords()[0]

first = feature.shape.__geo_interface__
shp_geom = shape(first)

print('Number of polygons in the final geometry: {}'.format(len(shp_geom)))
print('Area of the final geometry: {}'.format(shp_geom.area))