'''------Introduction to Programming - Homework 4-------
        Transformation of 2-Dimensional Geometric Object'''
#Name - PRASHANT
#Roll No. - 2018360
#section - B
#group - 1
#November 16, 2018

import matplotlib.pyplot as plt
from matplotlib import*
from matplotlib.patches import Ellipse
#import numpy as np
from math import*

figure=input()


# functions to multiply the two matrices  
def multiply(A,B):
        m=[]
        for i in range(len(A)):
                m2=[]
                for j in range(len(B[0])):
                        m1=0
                        for k in range(len(B[0])):
                                m1=m1+A[i][k]*B[k][j]
                        m2.append(m1)
                m.append(m2)
        return(m)

def multiply2(A,B):
	m=[]
	for i in range(len(A)):
		m1=0
		for j in range(len(B)):
			m1=m1+A[i][j]*B[j]
		m.append(m1)
	return(m)

'''---------------------------------polygon codition starting-----------------------------------'''

if(figure=='polygon'):

    a=list(map(int,input().split()))
    b=list(map(int,input().split()))

    a.append(a[0]); b.append(b[0])
    plt.plot(a,b)
    plt.show()
    
    c=[]; c.append(a); c.append(b); c1=[]
    
    # making the matrix c1 of input xy tuples
    for i in range(len(a)):
        c_temp=[]
        for j in range(len(c)):
            c_temp.append(c[j][i])
        c1.append(c_temp)
    for t in range(len(a)-1):
        c1[t].append(0)
    c1[len(a)-1].append(1)
    
    # input of scaling operation sx,sy
    sc=list(map(str,input().split()))
    sx=int(sc[1]); sy=int(sc[2])
    scale=[[sx,0,0],[0,sy,0],[0,0,1]]


    #multiplying the matrix
    scale_m=multiply(c1,scale)
    
    #extracting the cordinates from resultant matrix and print coordinates
    x1=[]; y1=[]
    for i in range(len(scale_m)):
        x1.append(scale_m[i][0]); y1.append(scale_m[i][1])
    ox1=''; oy1=''
    for i in range(len(x1)-1):
            ox1=ox1+' ' + str(x1[i])
            oy1=oy1+' ' + str(y1[i])
    print(ox1[1:]); print(oy1[1:])
    x1.append(x1[0]); y1.append(y1[0])
    plt.plot(x1,y1)
    plt.show()
    
    #input of rotation operation theta
    rot=list(map(str,input().split()))
    theta=int(rot[1]); rad=(3.14*theta)/180
    rotate=[[cos(rad),-sin(rad)],[sin(rad),cos(rad)]]

    # multiplication of matrix in a way i.e., rotate matrix to xy cordinate column matrix
    for n in range(len(scale_m)):
            scale_m[n].pop(-1)

    rotate_modified=[]
    for i in range(len(scale_m)):
            rotate_modified.append(multiply2(rotate,scale_m[i]))


    #extracting the cordinates from resultant matrix and print coordinates
    x2=[]; y2=[]
    for i in range(len(rotate_modified)):
            x2.append(rotate_modified[i][0]); y2.append(rotate_modified[i][1])
    ox2=''; oy2=''
    for i in range(len(x2)-1):
            ox2=ox2+' ' + str(x2[i])
            oy2=oy2+' ' + str(y2[i])
    print(ox2[1:]); print(oy2[1:])
    x2.append(x2[0]); y2.append(y2[0])
    plt.plot(x2,y2)
    plt.show()


    #input of translation operation dx,dy
    tra=list(map(str,input().split()))
    dx=int(tra[1]); dy=int(tra[2])
    translate=[[1,0,dx],[0,1,dy],[0,0,1]]


    #multiplication of matrix in a way i.e., translate matrix to xy cordinate column matrix
    for i in range(len(rotate_modified)):
            rotate_modified[i].append(1)
    translate_modified=[]
    for i in range(len(rotate_modified)):
            translate_modified.append(multiply2(translate,rotate_modified[i]))

    #Extracting the cordinates from resultant matrix and print coordinates
    x3=[]; y3=[]
    for i in range(len(translate_modified)):
            x3.append(translate_modified[i][0]); y3.append(translate_modified[i][1])
    ox3=''; oy3=''
    for i in range(len(x3)-1):
            ox3=ox3+' ' + str(x3[i])
            oy3=oy3+' ' + str(y3[i])
    print(ox3[1:],oy3[1:])
    x3.append(x3[0]); y3.append(y3[0])
    plt.plot(x3,y3)
    plt.show()


'''-------------------------------------------disc condition starting----------------------------------------'''

if(figure=='disc'):

    a,b,rx,ry=map(int,input().split())

    mat_d=[[rx,0,0],[0,ry,0],[0,0,1]]

    #plotting the initial center and radii of disc
    plt.axes()
    ellipse = Ellipse(xy=(a,b), width=rx*2, height=ry*2, edgecolor='r' ,fc ='None' , lw=2)
    plt.gca().add_patch(ellipse)
    plt.axis('scaled')
    plt.show()

    #input of scaling operation sx,sy
    sc_d=list(map(str,input().split()))
    sx_d=int(sc_d[1]); sy_d=int(sc_d[2])
    scale_d=[[sx_d,0,0],[0,sy_d,0],[0,0,1]]

    #multilication of matrix
    scale_md=multiply(mat_d,scale_d)

    #Extracting the modified radii from resultant matrix and print center and radii
    x1_d=scale_md[0][0]; y1_d=scale_md[1][1]
    print(a,b,x1_d,y1_d)

    #plotting the modified center and radii of disc
    plt.axes()
    ellipse = Ellipse(xy=(a,b), width=x1_d, height=y1_d, edgecolor='r' ,fc ='None' , lw=2)
    plt.gca().add_patch(ellipse)
    plt.axis('scaled')
    plt.show()

    #input of rotation operatio theta and makes the rotate_d matrix
    rot_d=list(map(str,input().split()))
    theta_d=int(rot_d[1]); rad_d=(3.14*theta_d)/180
    rotate_d=[[cos(rad_d),-sin(rad_d)],[sin(rad_d),cos(rad_d)]]


    #multiplication of matrix and extracting the modified center from the resultant matrix
    rotate_d_modi=multiply2(rotate_d,[x1_d,y1_d])
    x2_d=rotate_d_modi[0]; y2_d=rotate_d_modi[1]
    print(x2_d,y2_d,x1_d,y1_d)

    #ploting of modified coordinates of center and radii of disc
    plt.axes()
    ellipse = Ellipse(xy=(x2_d,y2_d), width=x1_d, height=y1_d, edgecolor='r' ,fc ='None' , lw=2)
    plt.gca().add_patch(ellipse)
    plt.axis('scaled')
    plt.show()

    #input of translation operatio dx,dy and makes the translate_d matrix
    tra_d=list(map(str,input().split()))
    dx=int(tra_d[1]); dy=int(tra_d[2])
    translate_d=[[1,0,dx],[0,1,dy],[0,0,1]]

    trans_temp=[x2_d,y2_d,1]


    #multiplication of matrix and extracting the modified center from the resultant matrix
    translate_d_modi=multiply2(translate_d,trans_temp)
    x3_d=translate_d_modi[0]; y3_d=translate_d_modi[1]
    print(x3_d,y3_d,x1_d,y1_d)

    #ploting of modified coordinates of center and radii of disc
    plt.axes()
    ellipse = Ellipse(xy=(x3_d,y3_d), width=x1_d, height=y1_d, edgecolor='r' ,fc ='None' , lw=2)
    plt.gca().add_patch(ellipse)
    plt.axis('scaled')
    plt.show()

choice=input()
