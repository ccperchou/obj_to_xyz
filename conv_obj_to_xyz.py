# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:33:26 2021

@author: clement perchais
"""

import glob
import os
import shutil
import random
import re

def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    
    s, t = sorted([random.random(), random.random()])
    
    
    x= s * float(pt1[0]) + (t-s)*float(pt2[0]) + (1-t)*float(pt3[0])
    y= s * float(pt1[1]) + (t-s)*float(pt2[1]) + (1-t)*float(pt3[1])
    z= s * float(pt1[2]) + (t-s)*float(pt2[2]) + (1-t)*float(pt3[2])
    return (x,y,z)
    


    


# # new derictory, clean and create
# if  os.path.exists('/convert_xyz'):    
#     shutil.rmtree('convert_xyz')

# if not os.path.exists('/convert_xyz'):
#     os.mkdir('convert_xyz')

# save path
save_path = 'convert_xyz'

# Get List of every .obj
L_files=glob.glob("*.obj")
newfiles_name=''
completeName=''

for files in L_files:
    f_list=[]
    verts=[]
    Lines=[] 
     
    List_key=[]
    Lpoints=[]
    
    f_in = open(files, "r")
    Lines = f_in.readlines()
    newfiles_name = files.replace(".obj", ".txt")
    completeName = save_path+"\\"+ newfiles_name
   
    f_out = open(completeName,"w+")
    
    # X Y Z format
    for l in Lines:
        
        if l[0] == 'f' :
            f_list.append(l)    
        if l[0] == 'v' :
             if 'vn' not in l:
                 li=l.lstrip('v')
                 f_out.write(li) 
        if l.startswith('v '):
            verts.append([float(val) for val in l.split()[1:]])
    verts.append([0,0,0])
# step 1 récupérer les numéros de sommets

    List_key=[]

    for l in f_list:
         ct_2 =l.lstrip('f ')   
         duo=ct_2.split()
         t_indice=[]     
         for x in duo:
            duo2= x.split('//')
            t_indice.append(duo2[0])    
         List_key.append(t_indice)    
# we have a list of key exp line1 : v1    line2: v2      line3 : v3 ...        
# step 2 récupérer les coordonnées correspondantes key 1 --> line4 into obj
   
   
    
        
            
         
    Lpoints=[]
    for tri in List_key:
    
        s1 =verts[int(tri[0])]
        s2 =verts[int(tri[1])]
        s3 =verts[int(tri[2])]
        points = [point_on_triangle(s1, s2, s3) for _ in range(10)]
        Lpoints.append(points)
    
    # step 3 ajouter  les points par ajout random
    
 
    
# step 4 ecrire les nouvelles coordonnées de ces points
    for newpoint in Lpoints:
        newline=''
        for i in newpoint:
            newline =  str(i[0])+" "+str(i[1])+" "+str(i[2]) + "\n"
         
            
            f_out.write(newline) 
      
f_out.close()
 