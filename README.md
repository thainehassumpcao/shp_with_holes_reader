# shp_with_holes_reader
Objective:
Read a shapefile with one feature of [multipolygons or polygons] with holes.
Gets its geometry and area.

-> shp_with_holes_reader.py: unpacking only a multipolygon with GDAL/OGR, not working

-> shp_with_holes_reader_updated.py: unpacking multipolygons and polygons with GDAL/OGR, not working

-> shp_with_holes_reader_WORKING.py: unpacking only a multipolygon with Shapely (GEOS), working
