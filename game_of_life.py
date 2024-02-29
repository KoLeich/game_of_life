import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import random
import tkinter as tk
from PIL import Image as im
import glob
from PIL import Image
import os


spdl = f"{os.getcwd()}/spdl/"

def PictureinMatrix(A, f=10):
    a,b=A.shape
    ll=[]
    print("a",a,"  b",b)
    zero=np.zeros(a*f*f*b).reshape(a*f,b*f)
    zero3=np.zeros(a*3*b).reshape(3*a,b)
    for i in range(0,b*f):
        ll.append(np.zeros(2*b*f+b))
    for i in range (0,a):
        ll.append(np.concatenate([np.zeros(b*f),A[i,:],np.zeros(b*f)]))
    for i in range(0,b*f):
        ll.append(np.zeros(2*b*f+b))
    return np.array(ll)



def regel(i,l,r,o,u,Or,ol,ul,ur):
    umgebung=l+r+o+u + Or+ol+ul+ur
    
    if(i==0):
        if (umgebung==3):
            return 1
        else:
            return 0
    if (i==1):
        if (umgebung ==3 or umgebung==2):
            return 1
        else:
            return 0
    return int(random.random()+0.5)
    


def spieldlebens(A):
    nn,mm=A.shape
    ll=[]
    for n in range(0,nn):
        for m in range(0,mm):
            #print(n,nn,m,mm)
            i = A[n,m]
            Or,ol,ul,ur=1,1,1,1
            if (n==0):
                o=0
                ol,Or=0,0
            else:
                o = A[n-1,m]
   
            if (n==nn-1):
                u=0
                ur,ul=0,0
            else:
                u = A[n+1,m]
                
            
            if (m==0):
                l=0
                ul,ol=0,0
            else:
                l = A[n,m-1]
                
            if (m==mm-1):
                r=0
                Or,ur=0,0
            else:
                r = A[n,m+1]            

            if (Or !=0):
                Or= A[n-1,m+1]
            if (ol !=0):
                ol= A[n-1,m-1]
            if (ul !=0):
                ul= A[n+1,m-1]
            if (ur !=0):
                ur= A[n+1,m+1]
                
            
            
            ll.append(regel(i,l,r,o,u,Or,ol,ul,ur))    
            
           # ll.append([ul+ur+Or+ol+l+o+r+u])
    return np.array(ll).reshape(nn,mm)



def creatfoulder(name):
#Initialize the directory name
    
    dirname = f"{spdl}{name}"
    print(dirname)
    #Check the directory name exist or not
    if os.path.isdir(dirname) == False:
        #Create the directory
        os.mkdir(dirname)
        os.mkdir(f'{dirname}/img/')
        os.mkdir(f'{dirname}/gif/')
        #Print success message
        print("The directory is created.")
    else:
        #Print the message if the directory exists
        print("The directory already exists.")


def sortgglob(globlist,name):
    #name="zwei"
    l = []
    for i in globlist:
        g=i.replace(f"{spdl}{name}/img/","")
        h=g.replace(".png","")
        #l.append(int(i.replace("/home/hagen/anaconda3/bin/spdl/{}/".format(name),"").replace(".png","")))
        l.append(int(h))
    l=sorted(l)
    L=[]
    for i in l:
        L.append(f"{spdl}{name}/img/{str(i)}.png")
    return L



def fromimagetogif(name):
    foulder = os.getcwd()
    fp_in = "spdl/{}/*.png".format(name)
    fp_out = "bin/gif/{}.gif".format(name)

    fp_in = f"{spdl}{name}/*.png"
    fp_out = f"{spdl}gif/{name}.gif"

    fp_in = f'{spdl}{name}/img/*.png'
    fp_out = f'{spdl}{name}/gif/{name}.gif'
    fp_out2 = f'{spdl}/{name}.gif'
    fp_out2 = f'{spdl}allgifs/{name}.gif'

    sortedlist = sortgglob(glob.glob(fp_in),name)
   # print(sortedlist)
    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    imgs = (Image.open(f) for f in sortedlist) # sorted(glob.glob(fp_in)))
    img = next(imgs)  # extract first image from iterator
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)
    imgs = (Image.open(f) for f in sortedlist) # sorted(glob.glob(fp_in)))
    img = next(imgs)  # extract first image from iterator
    img.save(fp=fp_out2, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=0)
    



def savethematrizen(matrixliste,name):
    creatfoulder(name)
    for i,v in enumerate (matrixliste):
        v[v<1]=20
        v[v==1]=253
        data = im.fromarray((v*255).astype(np.uint8))
#        data.save('spdl/{}/{}.png'.format(name,i))
        data.save(f'{spdl}{name}/img/{i}.png')
    fromimagetogif(name)



def spiel(matrix):
    A = PictureinMatrix(matrix)
    liste=[A]
    for i in range(0,100):
        A=spieldlebens(A)
        liste.append(A)
    return liste    

#savethematrizen(spiel(np.array([1,2,3,4,5,6,7,8,9]*4).reshape(6,6)),"test")
#savethematrizen(spiel(np.array([1,2,3,4,5,6,7,8,9]*4).reshape(6,6)),"Februar")
#savethematrizen(spiel(np.array([0,1]*18).reshape(6,6)),"März")
#savethematrizen(spiel(np.array([1,2,3,14,5,6,7,18,9]*4).reshape(6,6)),"April")