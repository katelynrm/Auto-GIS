# -*- coding: utf-8 -*-
"""
Auth: katelynrm
Problem 1 of Lesson 1 in Auto GIS course
"""
from shapely.geometry import Point, LineString, Polygon

#Create a function that will create a shapely point
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

#Function that will only recieve shapely points to create line
def createLineGeom(points):
    if all(isinstance(x, Point) for x in points):
        return LineString(points)
    else:
        return 'Not a list of shapely points'

#Function that will create a polygon from Points or a tuple
def createPolyGeom(givePoly):
    for x in givePoly:
        return Polygon([[p.x, p.y] for p in givePoly])
    else:
        return 'givePoly must contain point objects or point tuples'
    
