# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:20:49 2020

@author: Thaine H. Assumpção

Reads a shapefile with one feature of 
(multipolygons or polygons) with holes.
Gets its geometry and area.

"""

from pathlib import Path
from osgeo import ogr


def build_pol(pol):
    """ Unpacks given polygon into new polygon"""

    if pol.GetGeometryCount() > 1:
        print('Number of rings (when >1): {}'.format(pol.GetGeometryCount()))

    new_polygon = ogr.Geometry(ogr.wkbPolygon)
    for i in range(pol.GetGeometryCount()):
        ring = pol.GetGeometryRef(i)
        new_polygon.AddGeometry(ring)

    return new_polygon


def main():
    
    my_dir = Path(r'D:\Python')
    # shp = r'test_shape_area.shp'
    shp = r'test_shape_area_single.shp'
    
    Driver = ogr.GetDriverByName('ESRI Shapefile')
    DataSource = Driver.Open((my_dir / shp).as_posix(), 0)
    Layer = DataSource.GetLayer()
    print('Number of features: {}'.format(Layer.GetFeatureCount()))
    
    Geom = ogr.Geometry(ogr.wkbGeometryCollection)
    
    
    for feature in Layer:
        geometry = feature.GetGeometryRef()
    
        if geometry.GetGeometryName() == 'MULTIPOLYGON':
            print('Number of polygons: {}'.format(geometry.GetGeometryCount()))
            for j in range(geometry.GetGeometryCount()):
                polygon = geometry.GetGeometryRef(j)
                Geom.AddGeometry(build_pol(polygon))
    
        elif geometry.GetGeometryName() == 'POLYGON':
            Geom.AddGeometry(build_pol(geometry))
    
    
    Geom.CloseRings()
    
    print('Number of polygons in the final geometry: {}'.format(
        Geom.GetGeometryCount()))
    print('Area of the final geometry: {}'.format(Geom.GetArea()))


if __name__ == '__main__':
    main()