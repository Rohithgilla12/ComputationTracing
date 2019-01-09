# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:01:19 2016

@author: B3
"""

import math as m
import pylab as pl
def distance(p_1,p_2):
    k=m.sqrt((p_1[0]-p_2[0])**2+(p_1[1]-p_2[1])**2)
    return k

        
def totaldistance(p):
    dis=0
    for x in range(0,len(p)-1):
        dis +=distance(p[x],p[x+1])        
    return dis
                
def slope_1(s):
   s=m.tan((m.pi*s)/180)
   return s
               
                
                
def num_reflections(length,breadth,degrees_made_by_x_axis,point,width):
    """
    "1. length cannot be greater than breadth\
     2. the slope can be anything but except the multiples of 90(except 90)\
     if you want 180 and 360…so on you should take 0 as its similar\
     as direction does not matter as you have selected the input point\
     3. the rectangle is constructed in such away that the x and y axis are its adjacent sides\
     4. check whether the point given is in the boundary\
     5.  check whether the given width does not exceed the side"
     """    
    
    length=float(length)
    breadth=float(breadth)
    width=float(width)
    m=slope_1(degrees_made_by_x_axis)    
    a=1
    p=point
    l=[point]
    if(point[0]==length or point[0]==0 or point[1]==breadth or point[1]==0):
        c_1=True
    else:
        c_1=False
    if(point[0]>=0 and point[0]<=length and point[1]>=0 and point[1]<=breadth):
        c_2=True
    else:
        c_2=False
    if(point[1]==0 or point[1]==breadth):
        if(point[0]>length/2):
            c_3=(length-point[0]>=width/2)
        elif(point[0]<length/2):
            c_3=(point[0]>=width/2)
        else:
            c_3=(length>=width)
    elif(point[0]==0 or point[0]==length):
        if(point[1]<breadth/2):
            c_3=(point[1]>=width/2)
        elif(point[1]>breadth/2):
            c_3=(breadth-point[1]>=width/2)
        else:
            c_3=(breadth>width)
    else:
        c_3=False 
    c_4=(degrees_made_by_x_axis!=0 and degrees_made_by_x_axis!=90)
    c_5=(length>=breadth)    
    boolean=c_1 and c_2 and c_3 and c_4 and c_5
    while(boolean):
        if(p[1]==0):
            c=-m*p[0]
            if(p[0]<=point[0]+(width)/2 and p[0]>=point[0]-(width)/2 and point[1]==0):
                a=a+1
                if(a>2):
                    break
            if(m>0):
                if(m*(length)+c<breadth):
                    p=(length,m*(length-p[0])+p[1])
                    m=-m
                    l.append(p)
                    continue
                elif(m*(length)+c>breadth):
                    p=((breadth-p[1]+m*p[0])/(m),breadth)
                    m=-m
                    l.append(p)
                    continue
                else:
                    p=(length,breadth)
                    l.append(p)
                    break
                continue                  
            elif(m<0):
                if(c<breadth):
                    p=(0,c)
                    m=-m
                    l.append(p)
                    continue
                elif(c>breadth):
                    p=((breadth-c)/(m),breadth)
                    m=-m
                    l.append(p)
                    continue
                else:
                    p=(0,breadth)
                    l.append(p)
                    break
                continue
            continue
        if(p[0]==length):
            if(p[1]<=point[1]+(width)/2 and p[1]>=point[1]-(width)/2 and point[0]==length):
                a=a+1
                if(a>2):
                    break
            c=p[1]-m*length    
            if(m>0):
                if(c>0):
                    p=(0,c)
                    m=-m
                    l.append(p)
                    continue
                elif(c<0):
                    p=(-c/m,0)
                    m=-m
                    l.append(p)
                    continue
                else:
                    p=(0,0)
                    l.append(p)
                    break
                continue
            elif(m<0):
                if(c<breadth):
                    p=(0,c)
                    m=-m
                    l.append(p)
                    continue
                elif(c>0):
                    p=((breadth-c)/m,breadth)
                    m=-m
                    l.append(p)
                    continue
                else:
                    l.append(0,breadth)
                    break
                continue
            continue
        if(p[1]==breadth):
            if(p[0]<=point[0]+(width)/2 and p[0]>=point[0]-(width)/2 and point[1]==breadth):
                a=a+1
                if(a>2):
                    break
            c=breadth-m*p[0]
            if(m>0):
                if(c>0):
                    p=(0,c)
                    m=-m
                    l.append(p)
                    continue
                elif(c<0):
                    p=(-c/m,0)
                    m=-m
                    l.append(p)
                    continue
                else:
                    l.append(0,0)
                    break
                continue
            elif(m<0):
                if(-c/m<length):
                    p=(-c/m,0)
                    m=-m
                    l.append(p)
                    continue
                elif(-c/m>0):
                    p=(length,m*length+c)
                    m=-m
                    l.append(p)
                    continue
                else:
                    l.append(length,0)
                    break
                continue
            continue
        if(p[0]==0):
            if(p[1]<=point[1]+(width)/2 and p[1]>=point[1]-(width)/2 and point[0]==0):
                a=a+1
                if(a>2):
                    break
            c=float(p[1])
            if(m>0):
                if(m*(length)+p[1]<breadth):
                    p=(length,m*length+p[1])
                    m=-m
                    l.append(p)
                    continue
                elif(m*(length)+p[1]>breadth):
                    p=((breadth-p[1])/m,breadth)
                    m=-m
                    l.append(p)
                    continue
                else:
                    l.append(length,breadth)
                    break
                continue
            if(m<0):
                if(-c/m<length):
                    p=(-c/m,0)
                    m=-m
                    l.append(p)
                    continue
                elif(-c/m>0):
                    p=(length,m*length+c)
                    m=-m
                    l.append(p)
                    continue
                else:
                    l.append(length,0)
                    break
                continue
            continue
        continue

    if(boolean==True):
        if(l[-1]==(0,0) or l[-1]==(length,0) or l[-1]==(length,breadth) or l[-1]==(0,breadth)):
            print "corner"
            print "total distance traveled in the box is",2*totaldistance(l)
            print 'number of reflections are',2*len(l)-1
            print "the time for which it stays in the cavity is",(2*totaldistance(l))/(3*(10**8))
        else:
            print "total distance traveled in the box is",totaldistance(l)
            print 'number of reflections are',len(l)-2
            print "the time for which it stays in the cavity is",totaldistance(l)/(3*(10**8))
    else:
        print "the input given does not exist please type num_reflections? in phython console\
 to know the conditions  "
    if(boolean==True):
            x_cord=[]
            for i1 in range(len(l)):
                x_cord.append(l[i1][0])
            y_cord=[]
            for i2 in range(len(l)):
                y_cord.append(l[i2][1])
            x_cord=tuple(x_cord)
            y_cord=tuple(y_cord)
            pl.plot(x_cord,y_cord)
            print " You see this, it's an awesome, awesome, cool stuff" 
    if(boolean==False):
        wrong_condition=input("enter number '1' if you want to know what is the wrong input")
        if(wrong_condition==1):
            if(c_1==False or c_2==False):
                print "the rectangle exist in co-ordinate plane as x and y axis as its adjacent sides\
 and the given point does not exist on the boundary of rectangle"
            if(c_3==False):
                print "the given window cannot be constructed on the rectangle for the given dimensions\
 of rectangle or at that point"
            if(c_4==False):
                if(point[1]==0 or point[1]==breadth):
                    if(degrees_made_by_x_axis==90):
                        print "donot cry that the console is shouting at you actually it's a simple reflections the light ray is retraced in its first reflection"
                        print "number of reflections are 1"
                        print "distance travelled",2*breadth
                        print "the time for which it stays in the cavity is",(2*breadth)/(3*(10**8))
                    elif(degrees_made_by_x_axis==0):
                        print "this is an error as you cannot send the ray along the axis"
                elif(point[0]==0 or point[0]==length):
                    if(degrees_made_by_x_axis==0):
                        print "donot cry that the console is shouting at you it's a simple reflections the light ray is retraced in its first reflection"
                        print "number of reflections are 1"
                        print "distance travelled",2*length
                        print "the time for which it stays in the cavity is",(2*length)/(3*(10**8))
                    elif(degrees_made_by_x_axis==90):
                        print "this is an error as you cannot send the ray along the the axis" 
            if(c_5==False):
                print "length of a rectangle can be equal or greater than breadth"
        else:
            print "the program ends here ALVIDAAAAA, Ciao"
        
        
                
                    
                
                
        
                    
                    
                    
                    
                
            
                    
                    
                    
                
                    
                    
                    
            
                    
                    
                

            
            
        