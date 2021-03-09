# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 12:33:26 2021

@author: clement perchais
"""

import glob
import os
import shutil
# new derictory, clean and create
    
shutil.rmtree('convert_xyz')

if not os.path.exists('/convert_xyz'):
    os.mkdir('convert_xyz')

# save path
save_path = 'convert_xyz'

# Get List of every .obj
L_files=glob.glob("*.obj")
newfiles_name=''
completeName=''
for files in L_files:
    f_in = open(files, "r")
    Lines = f_in.readlines()
    newfiles_name = files.replace(".obj", ".txt")
    completeName = save_path+"\\"+ newfiles_name
   
    f_out = open(completeName,"w+")
    
    # X Y Z format
    for l in Lines:
        if l[0] == 'v' :
             if 'vn' not in l:
                 li=l.lstrip('v')
                 f_out.write(li) 
          
      
 
f_in.close()
f_out.close()
