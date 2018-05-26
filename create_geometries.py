# -*- coding: utf-8 -*-
"""
Auth: katelynrm
Problem 1 of Lesson 1 in Auto GIS course
"""
from shapely.geometry import Point, LineString, Polygon


def createPointGeom(x, y):
    '''This will create a point
    Parameters
    ---------
    x <numerical>
    y <numerical>
    
    Returns
    ---------
    One point
    '''
    return Point(x,y)