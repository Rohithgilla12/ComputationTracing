# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:27:10 2016

@author: B3
"""
import pylab as pyl
import ellipse_B3 as e
import Rectangle as re
import math as m
print"Bonjour!"
print "Welcome to computational tracing of light rays"
print "Choose your preferred number"
print"1)Ellipse\n" "2)Rectangle"
choice=input("Enter your choice")

if choice ==1:

    major_axis = input("Enter the length of major axis ") 
    minor_axis=input("Enter the length of minor axis  ")
    x1,y1 =input("Enter x1,y1 the starting point on the hole")
    x2,y2 =input("Enter x2,y2 the ending point of hole")
    m1=input("Enetr the angle at which it enters")
    x_cord=[]
    y_cord=[]
    e.main(minor_axis,major_axis,x1,y1,x2,y2,m1,x_cord,y_cord)
    print "If u want to see the plot press 3"
    opt=input("Press the desired key")
    if opt==3:
        e.plot(x1,x2,y1,y2,major_axis,minor_axis,x_cord,y_cord)
        print "The graph of Number of reflections V/S Slope for ellipse"        
        ll=[45,40,50,30,55,60,10,20,70]
        ll.sort()
        lll=[55,5,25,42,17,11,7,28,7]
        lll.sort()
        pyl.plot(ll,lll)
        pyl.show()
    else:
        print"Its okay if you are not intrested"
if choice==2:
    length=input("Length")
    breadth=input("Breadth")
    width=input("Slit width")
    degrees_made_by_x_axis=input("Slope of the line")
    length=float(length)
    breadth=float(breadth)
    width=float(width)
    m=re.slope_1(degrees_made_by_x_axis)    
    a=1
    point=input("point")
    p=point
    l=[point]    
    re.num_reflections(length,breadth,degrees_made_by_x_axis,point,width)
        


