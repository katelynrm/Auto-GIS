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

#create two new columns that will create shapely points out of the original columns

data['orig_points'] = 
data['dest_points']
