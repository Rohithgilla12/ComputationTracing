# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 14:43:30 2016

@author: Rohith
"""
import pylab as p
import math as m
#x_cord=[]
#y_cord=[]
dist=lambda x1,y1,x2,y2:m.sqrt((x2-x1)**2+(y2-y1)**2)
def main(minor_axis,major_axis,x1,y1,x2,y2,m1,x_cord,y_cord):
    
    i=1
    m1=m.tan(m1*m.pi/180)
    x=(x1+x2)/2.0
    y=(y1+y2)/2.0
    x_cord.append(x)
    y_cord.append(y)
    while i==1:
        old_x = x
        k=minor_axis/float(major_axis)
        x = ( (m1**2-k**2)*x - 2*m1*y ) / ( m1**2 + k**2 )
        y = ( (k**2-m1**2)*y - 2*m1*old_x*k**2 ) / ( m1**2 + k**2 )
        if (y == 0):
            m1 = m.pi - m1
        else:
            m1 = 2*m.atan( -x*(minor_axis**2) / float(y*(major_axis**2)) ) - m.atan(m1)
            m1 = m.tan(m1)
            x_cord.append(x)
            y_cord.append(y)
    
    #break of de loop
        if (min([y1,y2]) <= y <= max([y1,y2]) and min([x1,x2]) <= x <= max([x1,x2])):
            i=0
    count=len(x_cord)-2
    path=0
    for i1 in range(count-1):
        path+=dist(x_cord[i1],y_cord[i1],x_cord[i1+1],y_cord[i1+1])
    time=path/3.0E8
    print "The number of reflections it takes inside ellipse is",count
    print "Thw total distance travelled by the ray inside the ellipse is" ,path
    print "The time it spent inside is",time
    return count,path,time
    
def plot(x1,x2,y1,y2,major_axis,minor_axis,x_cord,y_cord):
    x_c = p.linspace(-major_axis,major_axis,1000)
    y1_c = minor_axis*p.sqrt(1 - (x_c**2)/float(major_axis**2))
    y2_c = -minor_axis*p.sqrt(1 - (x_c**2)/float(major_axis**2))
    p.plot(x_c,y1_c,'r-')
    p.plot(x_c,y2_c,'r-')
    p.plot(x_cord,y_cord)
    p.plot(x1,y1,x2,y2,'go')
    p.show()