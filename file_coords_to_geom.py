# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:13:23 2018

@author: katel
"""

import pandas as pd
from shapely.geometry import Point, LineString, Polygon


#read in the Helsinki points txt file into a dataFrame
fp = r'C:\Users\katel\Documents\AutoGIS\travelTimes_2015_Helsinki2.txt'

data = pd.read_csv(fp, sep=';', usecols=['from_x','from_y','to_x','to_y'])

#Create two lists called orig_points and dest_points
orig_points=[]
dest_points=[]

#Iterate over the rows of your DataFrame and add Shapely Point -objects into the orig_points -list and dest_point -list representing the origin locations and destination locations accordingly.
for idx, row in data.iterrows():
    orig_points.append(Point(row['from_x'], row['from_y']))
    dest_points.append(Point(row['to_x'], row['to_y']))