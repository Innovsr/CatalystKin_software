from __future__ import division
from Tkinter import *
import numpy as np
import math
import turtle

#############################################################
######################### root section  #####################
## creating the root window, Canvas, all the frames inside ##
## the root in this section #################################
#############################################################
root = Tk()
root.title("Program for calculations of Catalytic Cycles")
frame=Frame(root, bg='purple',height=700, width= 200,bd=6)
frame.pack(side=LEFT,anchor=N)
frame1=Frame(root, bg='black',height=700, width= 800,bd=2 )
frame1.pack(side=LEFT)
canvas=Canvas(frame1, height=720, width= 700, bg='white',bd=2)
canvas.pack()
frame2=Frame(root,bd=2 )
frame2.pack(side=LEFT,anchor=N)
frame3=Frame(frame2, height=700, width= 200,bd=2 )
frame3.pack(side=LEFT,anchor=N)
frame4=Frame(frame2, height=700, width= 200,bd=2 )
frame4.pack(side=LEFT,anchor=N)
frame5=Frame(frame3,height=700, width= 52,bd=2 )
frame5.grid(row=2,column=0)
frame6=Frame(frame3,height=700, width= 128,bd=2 )
frame6.grid(row=2, column=1)
frame7=Frame(frame4,height=700, width= 26,bd=2 )
frame7.grid(row=2,column=0)
frame9=Frame(frame4,height=700, width= 26,bd=2 )
frame9.grid(row=2,column=1)
frame8=Frame(frame4,height=700, width= 128,bd=2 )
frame8.grid(row=2, column=2)

#####################     entry boxes   #######################

e5=Entry(frame3,width=15)
e5.grid(row=1, column=1)
e5.insert(0,"Intermediates")
e6=Entry(frame4,width=15)
e6.grid(row=1, column=2)
e6.insert(0,"Transition States")
e11=Entry(frame3,width=15)
e11.grid(row=0, column=1)
e11.insert(0,"Delta G")

########## declaration of the width of the figure #############
########## and the colour of background colors    #############

pickWidths = [1, 2, 5, 10, 20]
pickFills = [None,'white','blue','red','black','yellow','green','purple']

global count_circle, circ, dcirc, count_arrow
global e1,tx,ty,m1,k3,k4,k5,tca,b19

########## initialization of the lists ###########################

tca=[]
tca=np.append(tca,1)
midnln=[]
c=[]
cent=[]
centr=[]
l=[]
ln=[]
line=[]
dl=[]
val=[]
vall=[]
midln=[]
circle1=[]
centr=[]
cent=[]
lnr=[]

########## initialization of global variables  ###########################

mm=0
nn=1
mm1=1
kent=1
k4=1
count_circle=0
count_arrow=0
count=0
circ=0
dcirc=0
flag=0
flg3=1
flg4=1
k3=0
k5=0
k9=0
k12=0
k16=1
arind=0
delG=0.0
tca_n=0

####################################################################################
# this function call function "drawcircle" by put a left click on the canvas       #
#                                                                                  #
####################################################################################
def circle():
# ##############  left click on the canvas   #######################################

    canvas.bind('<Button-1>',drawcircle)
################ do nothing when release the click ################################

    canvas.bind('<ButtonRelease-1>',blind)
    return

#####################################################################################
# This function draw the circle of radius 20 on the clicked point on canvas         #
# count_circle is => the running number of circles                                  #
# c => array or list where centre of the circles are stored                         #                                          #####################################################################################

def drawcircle(evnt):
    global count_circle, c
    centx=evnt.x
    centy=evnt.y
    circ=canvas.create_oval(evnt.x-20, evnt.y-20, evnt.x+20, evnt.y+20, width=pickWidths[2])
    count_circle=count_circle+1
    c=np.append(c,(evnt.x,evnt.y))
    print '****',count_circle,c
    return
def blind(event):
    return()

#########################################################################################
# This function call the function (put_number) to create a serial numbering on the      #
# circles if the click pount is inside the circle.                                      #
# k3 => the parameter specifies that the drawing is complete (value 1), it is connected #
# with button "Done"                                                                    #
#########################################################################################

def Numbering():
    global k3,cap4
    if k3==1:
        canvas.bind('<Button-1>',put_number)
    if k3 == 0:
        cap4=Tk()
        dl7=Label(cap4,text='complete the drawing of the cycle first',bg='yellow',bd=2)
        dl7.pack()
        b17=Button(cap4,text='ok',command=Exit6,bd=2)
        b17.pack( anchor=S)
    return

##########################################################################################
# This function put serial numbers inside the circles and create the entry boxes for     #
# intermediates and transition states. global variable "k12" generate the                #
# serial numbers.                                                                        #
##########################################################################################

def put_number(event):
    global c,k3,cap4,count_circle,k12,mm,mm1,k4,count_arrow,flg3,flg4
    k=1
    k1=1
    k7=0
    
    print 'mm',mm,mm1
    k4=k12*(mm-mm1)+k4
    if (mm-mm1)==0:
        k7=1
    print k4
    mm1=mm
    print 'flg3',flg3
    if k3 == 1:
        while k<count_circle+1 : 
            if math.sqrt(((c[2*k-2]-event.x)**2)+((c[2*k-1]-event.y)**2))<=20 and flg4<=count_circle:
                k12=k12+1
                canvas.create_text(c[2*k-2],c[2*k-1], text=k12)
                e6=Entry(frame5,width=5)
                e6.pack(side=TOP)
                e6.insert(0,k12)
                e5=Entry(frame6,width=15)
                e5.pack(side=TOP)
                e5.bind('<Return>',get1)
                flg4=flg4+1
            k=k+1
        print 'k12',k12,k
        k2=k12+1
        if flg3<=count_arrow:
            if k12==count_arrow:
                k2=1
                print 'kkk',k,count_arrow+1
            if k2>2 and k7==1:
                e8=Entry(frame7,width=2)
                e8.pack(side=TOP)
                e8.insert(0,k12-1)
                e9=Entry(frame9,width=2)
                e9.pack(side=TOP)
                e9.insert(0,k12)
                e7=Entry(frame8,width=15)
                e7.pack(side=TOP)
                e7.bind('<Return>',get2)
                flg3=flg3+1
            if k2==1:
                e8=Entry(frame7,width=2)
                e8.pack(side=TOP)
                e8.insert(0,k12-1)
                e7=Entry(frame8,width=15)
                e7.pack(side=TOP)
                e7.bind('<Return>',get2)
                e9=Entry(frame9,width=2)
                e9.pack(side=TOP)
                e9.insert(0,k12)
                e10=Entry(frame7,width=2)
                e10.pack(side=TOP)
                e10.insert(0,k12)
                e11=Entry(frame8,width=15)
                e11.pack(side=TOP)
                e11.bind('<Return>',get2)
                e12=Entry(frame9,width=2)
                e12.pack(side=TOP)
                e12.insert(0,k4)
                flg3=flg3+2

###### reading the values from the entry boxes #################

def get1(event):
    global val
    Entry=event.widget
    val=np.append(val,(Entry.get()))
def get2(event):
    global vall
    Entry=event.widget
    vall=np.append(vall,(Entry.get()))
def get3(event):
    global delG
    Entry=event.widget
    delG=Entry.get()
e12=Entry(frame4,width=15)
e12.grid(row=0, column=1)
e12.bind('<Return>',get3)

##############################################################################################
# Exit button of the popup warning it destroy the popup widow.                               #
##############################################################################################
def Exit6():
    global cap4
    cap4.destroy()
    return


##############################################################################################
# This function call the function firstlast by left clicking on the circles                  #
##############################################################################################

def connector():
    canvas.bind('<Button-1>',firstlast)
    return

##############################################################################################
# This function store the two consecutively clicked points and call the function             #
# "draw_connector" to draw the connecting line between two circles.                          #
# "l" => is the list where the clicked points are stored.                                    #
##############################################################################################
def firstlast(event):
    global l, circ
    l=np.append(l,(event.x,event.y))
    circ=circ+1
    if circ==2:
       draw_connector()
       circ=0
###############################################################################################
# This subroutine arrange the diagrams in a regular shape as user click the button "rearrange"#
# after the cycle is closed.                                                                  #
# no_circ_arr=> provides the number of closed circles.                                        #
# count_arrow=> number of connectors.                                                         #
# centr => list to store the radius of the circle on which the final arranged pattern is      #
# created                                                                                     #
# cent => list of the centre of the final circle.                                             #
# midln=> list to store the middle point of the connector                                     #
# local variable k1 and k2 specify the 1st and the 2nd circle                                 #
# c2=> the list for temporary storage of circle coordinate                                    #
###############################################################################################
def arrange():
    global circle1,no_circ_arr, midln,c,count_circle,mm,cent,centr,tca,midnln,count_arrow,k9
    global arind,line,ln,lnr,tca_n,b19
    k1=1
    j=1
    c2=[]
    print 'midln',midln
    if no_circ_arr<=7:
        diam=100
        centr=np.append(centr,(diam))
        cc=int(k9/2)+1
#        print 'cc',cc
        cx=(circle1[0]+circle1[cc*2-2])/2
        cy=(circle1[1]+circle1[cc*2-1])/2
#        print 'mm',mm,cx,cy
#        if mm!=0:
#            mm1=1
#            while mm1<=k9:
#                print 'pp',math.sqrt((circle1[2*mm1-2]-cx)**2+(circle1[2*mm1-1]-cy)**2),centr[mm-1]
#                if math.sqrt((circle1[2*mm1-2]-cx)**2+(circle1[2*mm1-1]-cy)**2)<=centr[mm-1]:
#                    if cx+centr[mm-1]+100+30<=580:
#                        cx=cx+centr[mm-1]+100+30
#                    else:
#                        cy=cy-centr[mm-1]+100+30

#                    print 'cccccxxxx',cx,cy,math.sqrt((centr[mm-1]-100)**2),centr[mm-1]
#                mm1=mm1+1
        cent=np.append(cent,(cx,cy))
#        print 'centre',circle1[0],circle1[cc*2-2],cx,circle1[1],circle1[cc*2-1],cy
        ang=2*3.14159265359/k9
        if cx!=circle1[0]:
############### p7 => slope of the line connected two centres of two clicked circles ##################
            p7=(-cy+circle1[1])/(-cx+circle1[0])
############### p8 => create + or - 1 depending on x coordinate of the two circles to specify which is
############### on left of which
            p8=(cx-circle1[0])/math.sqrt((cx-circle1[0])**2)

############### cx1, cy1 are the centre of the first circle ############################################

            cx1=(-p8)*(diam/math.sqrt((p7**2)+1))+cx
            cy1=(-p8)*(p7*diam/math.sqrt((p7**2)+1))+cy
        if cx==circle1[0]:
#        p8=(cy-circle1[1])/math.sqrt((cy-circle1[1])**2)
            cx1=cx
#        cy1=(-p8)*diam+cy
            cy1=diam+cy
        diffx=circle1[0]-cx1
        diffy=circle1[1]-cy1
#        print diffx,diffy
        object=canvas.find_closest(circle1[0],circle1[1])
        canvas.move(object,-diffx,-diffy)
        c2=np.append(c2,(cx1,cy1))
        ll1=1
        while ll1<=count_circle:
            if circle1[0]==c[2*ll1-2] and circle1[1]==c[2*ll1-1]:
                ll2=ll1
            ll1=ll1+1

#        c=np.delete(c,[0,1])
        c=np.delete(c,[2*tca[mm]-2,2*tca[mm]-1])
        c=np.append(c,(cx1,cy1))
        print 'tca[mm]',mm,tca[mm]
        kk=1
        while kk<=k9-1:

############ rotate the cx1 and cy1 by an angle "ang" with the rotational matrix shown below #############
############ cx2, cy2 are the centre of the next circle     ##############################################

            cx2=(cx1-cx)*math.cos(kk*ang)-(cy1-cy)*math.sin(kk*ang)
            cy2=(cy1-cy)*math.cos(kk*ang)+(cx1-cx)*math.sin(kk*ang)
            cx3=cx2+cx
            cy3=cy2+cy
#            canvas.create_oval(cx3-5,cy3-5,cx3+5,cy3+5)
            difx=circle1[2*(kk+1)-2]-cx3
            dify=circle1[2*(kk+1)-1]-cy3
            object4=canvas.find_closest(circle1[2*(kk+1)-2],circle1[2*(kk+1)-1])
            canvas.move(object4,-difx,-dify)
            c2=np.append(c2,(cx3,cy3))
            ll1=1
            while ll1<=count_circle:
                if circle1[2*(kk+1)-2]==c[2*ll1-2] and circle1[2*(kk+1)-1]==c[2*ll1-1]:
                    ll2=ll1
                ll1=ll1+1

############ update the position of the circle shifted due to rearrangement ###############################

            c=np.delete(c,[2*tca[mm]-2,2*tca[mm]-1])
#            c=np.delete(c,[0,1])
            c=np.append(c,(cx3,cy3))
#            print 'cccccccc',mm,tca[mm]

            kk=kk+1

        while k1<=k9:
#            print 'k999',k9
            print 'tca[tca_n-1]',tca[tca_n-1],tca_n-1
           
            k2=k1+1
            if k1==k9:
                k2=1
#            object5=canvas.find_closest(midln[2*k1-2],midln[2*k1-1])
            print 'midln[2*tca[tca_n-1]-2],midln[2*k1-2]',midln[2*tca[tca_n-1]-2],midln[2*k1-2]
            object5=canvas.find_closest(midln[2*tca[tca_n-1]-2],midln[2*tca[tca_n-1]-1])
            canvas.delete(object5)
            if c2[2*k1-2] != c2[2*k2-2] and arind!=1 :
                
############### p7 => slope of the line connected two centres of two clicked circles ##################

                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])

############### p8 => create + or - 1 depending on x coordinate of the two circles to specify which is
############### on left of which

                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))

############### if two circles have typically same x cordinate ########################################

            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))

############### if two circles have typically same y cordinate ########################################

            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))

############### if the connector is the last one (k2=1) then it will be arrow in place of a line ######
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2==1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2==1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2==1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2!=1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20
                ,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1]
                ,c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
#            nn=nn+1
#            print 'tca[tca_n]-tca[tca_n-1]',tca[tca_n]-tca[tca_n-1]
#            while j<=tca[tca_n]-tca[tca_n-1]: 
            midln=np.delete(midln,[2*tca[tca_n-1]-2,2*tca[tca_n-1]-1])
            lnr=np.delete(lnr,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            line=np.delete(line,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            ln=np.delete(ln,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
#            print 'midlnoooo',midln

            k1=k1+1
        
############### if the number of circle need to be arranged is larger than 7 and less than 10 ###########

    if no_circ_arr>7 and no_circ_arr<=10:
        diam=200
        cc=int(k9/2)+1
        cx=(circle1[0]+circle1[cc*2-2])/2
        cy=(circle1[1]+circle1[cc*2-1])/2
#        print 'centre',circle1[0],circle1[cc*2-2],cx,circle1[1],circle1[cc*2-1],cy
        ang=2*3.14159265359/k9
        if cx!=circle1[0]:
            p7=(-cy+circle1[1])/(-cx+circle1[0])
            p8=(cx-circle1[0])/math.sqrt((cx-circle1[0])**2)
            cx1=(-p8)*(diam/math.sqrt((p7**2)+1))+cx
            cy1=(-p8)*(p7*diam/math.sqrt((p7**2)+1))+cy
        if cx==circle1[0]:
            p8=(cy-circle1[1])/math.sqrt((cy-circle1[1])**2)
            cx1=cx
            cy1=(-p8)*diam+cy
            
        diffx=circle1[0]-cx1
        diffy=circle1[1]-cy1
#        print diffx,diffy
        object=canvas.find_closest(circle1[0],circle1[1])
        canvas.move(object,-diffx,-diffy)
        c2=np.append(c2,(cx1,cy1))
        ll1=1
        while ll1<=count_circle:
            if circle1[0]==c[2*ll1-2] and circle1[1]==c[2*ll1-1]:
                ll2=ll1
            ll1=ll1+1

        c=np.delete(c,[0,1])
        c=np.append(c,(cx1,cy1))
        kk=1
        while kk<=k9-1:
            cx2=(cx1-cx)*math.cos(kk*ang)-(cy1-cy)*math.sin(kk*ang)
            cy2=(cy1-cy)*math.cos(kk*ang)+(cx1-cx)*math.sin(kk*ang)
            cx3=cx2+cx
            cy3=cy2+cy
#            canvas.create_oval(cx3-5,cy3-5,cx3+5,cy3+5)
            difx=circle1[2*(kk+1)-2]-cx3
            dify=circle1[2*(kk+1)-1]-cy3
            object4=canvas.find_closest(circle1[2*(kk+1)-2],circle1[2*(kk+1)-1])
#            print 'cccccccc',circle1[2*(kk+1)-2],circle1[2*(kk+1)-1],cx3,cy3
            canvas.move(object4,-difx,-dify)
            c2=np.append(c2,(cx3,cy3))
#            print 'c111',c,circle1[2*(kk+1)-2],circle1[2*(kk+1)-1]
            ll1=1
            while ll1<=count_circle:
#               print 'cc**',c
                if circle1[2*(kk+1)-2]==c[2*ll1-2] and circle1[2*(kk+1)-1]==c[2*ll1-1]:
                    ll2=ll1
                ll1=ll1+1

            c=np.delete(c,[2*ll2-2,2*ll2-1])
            c=np.append(c,(cx3,cy3))

#            print 'c222',c
            kk=kk+1
        
        while k1<=k9:
#            print 'c2',c2,k1
#            print 'midln',midln
            k2=k1+1
            if k1==k9:
                k2=1
            object5=canvas.find_closest(midln[2*k1-2],midln[2*k1-1])
            canvas.delete(object5)
            if c2[2*k1-2] != c2[2*k2-2] and arind!=1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20
                ,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1]
                ,c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2==1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2==1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20
                ,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2==1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1]
                ,c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2!=1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20
                ,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1]
                ,c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            midln=np.delete(midln,[2*tca[tca_n-1]-2,2*tca[tca_n-1]-1])
            lnr=np.delete(lnr,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            line=np.delete(line,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            ln=np.delete(ln,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])

            k1=k1+1
#            nn=nn+1

############### if the number of circle need to be arranged is larger than 10 ###########

    if no_circ_arr>10:
        diam=300
        cc=int(k9/2)+1
#        print 'cc',cc
        cx=(circle1[0]+circle1[cc*2-2])/2
        cy=(circle1[1]+circle1[cc*2-1])/2
#        print 'centre',circle1[0],circle1[cc*2-2],cx,circle1[1],circle1[cc*2-1],cy
        ang=2*3.14159265359/k9
        if cx!=circle1[0]:
            p7=(-cy+circle1[1])/(-cx+circle1[0])
            p8=(cx-circle1[0])/math.sqrt((cx-circle1[0])**2)
            cx1=(-p8)*(diam/math.sqrt((p7**2)+1))+cx
            cy1=(-p8)*(p7*diam/math.sqrt((p7**2)+1))+cy
        if cx==circle1[0]:
            p8=(cy-circle1[1])/math.sqrt((cy-circle1[1])**2)
            cx1=cx
            cy1=(-p8)*diam+cy
            
        diffx=circle1[0]-cx1
        diffy=circle1[1]-cy1
#        print diffx,diffy
        object=canvas.find_closest(circle1[0],circle1[1])
        canvas.move(object,-diffx,-diffy)
        c2=np.append(c2,(cx1,cy1))
        ll1=1
        while ll1<=count_circle:
            if circle1[0]==c[2*ll1-2] and circle1[1]==c[2*ll1-1]:
                ll2=ll1
            ll1=ll1+1

        c=np.delete(c,[0,1])
        c=np.append(c,(cx1,cy1))
        kk=1
        while kk<=k9-1:
            cx2=(cx1-cx)*math.cos(kk*ang)-(cy1-cy)*math.sin(kk*ang)
            cy2=(cy1-cy)*math.cos(kk*ang)+(cx1-cx)*math.sin(kk*ang)
            cx3=cx2+cx
            cy3=cy2+cy
#            canvas.create_oval(cx3-5,cy3-5,cx3+5,cy3+5)
            difx=circle1[2*(kk+1)-2]-cx3
            dify=circle1[2*(kk+1)-1]-cy3
            object4=canvas.find_closest(circle1[2*(kk+1)-2],circle1[2*(kk+1)-1])
#            print 'cccccccc',circle1[2*(kk+1)-2],circle1[2*(kk+1)-1],cx3,cy3
            canvas.move(object4,-difx,-dify)
            c2=np.append(c2,(cx3,cy3))
#            print 'c111',c,circle1[2*(kk+1)-2],circle1[2*(kk+1)-1]
            ll1=1
            while ll1<=count_circle:
#               print 'cc**',c
                if circle1[2*(kk+1)-2]==c[2*ll1-2] and circle1[2*(kk+1)-1]==c[2*ll1-1]:
                    ll2=ll1
                ll1=ll1+1

            c=np.delete(c,[2*ll2-2,2*ll2-1])
            c=np.append(c,(cx3,cy3))

#            print 'c222',c
            kk=kk+1
        
        while k1<=k9:
#            print 'c2',c2,k1
#            print 'midln',midln
            k2=k1+1
            if k1==k9:
                k2=1
            object5=canvas.find_closest(midln[2*k1-2],midln[2*k1-1])
            canvas.delete(object5)
            if c2[2*k1-2] != c2[2*k2-2] and arind!=1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20
                ,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1]
                ,c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2==1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2==1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2==1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2],arrow="last")
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if c2[2*k1-2] != c2[2*k2-2] and arind==1 and k2!=1:
                p7=(c2[2*k1-1]-c2[2*k2-1])/(c2[2*k1-2]-c2[2*k2-2])
                p8=((c2[2*k1-2]-c2[2*k2-2])/math.sqrt((c2[2*k1-2]-c2[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]
                ,width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c2[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c2[2*k1-1]
                ,-(-p8)*(20/math.sqrt((p7**2)+1))+c2[2*k2-2],
                -(-p8)*p7*(20/math.sqrt((p7**2)+1))+c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-2] == c2[2*k2-2] and arind==1 and k2!=1:
                p9=((c2[2*k1-1]-c2[2*k2-1])/math.sqrt((c2[2*k1-1]-c2[2*k2-1])**2))
                canvas.create_line(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20,
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2],c2[2*k1-1]-p9*20,c2[2*k2-2],c2[2*k2-1]+p9*20))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            if k1!= 0 and k2 !=0 and c2[2*k1-1] == c2[2*k2-1] and arind==1 and k2!=1:
                p9=(c2[2*k2-2]-c2[2*k1-2])/math.sqrt((c2[2*k2-2]-c2[2*k1-2])**2)
                canvas.create_line(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1],
                width=pickWidths[2])
                midln=np.append(midln,((c2[2*k1-2]+c2[2*k2-2])/2,(c2[2*k1-1]+c2[2*k2-1])/2))
                lnr=np.append(lnr,(c2[2*k1-2]+p9*20,c2[2*k1-1],c2[2*k2-2]-p9*20,c2[2*k2-1]))
                line=np.append(line,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
                ln=np.append(ln,(c2[2*k1-2],c2[2*k1-1],c2[2*k2-2],c2[2*k2-1]))
            midln=np.delete(midln,[2*tca[tca_n-1]-2,2*tca[tca_n-1]-1])
            lnr=np.delete(lnr,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            line=np.delete(line,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])
            ln=np.delete(ln,[4*tca[tca_n-1]-1,4*tca[tca_n-1]-2,4*tca[tca_n-1]-3,4*tca[tca_n-1]-4])

            k1=k1+1
#            nn=nn+1
#    count_arrow=count_arrow+k5
#    b19.config(state="disabled")

############### initialization of the temporary list "midln" and "c2"###############################
    c2=[]
    print 'cafter',c
#    midln=[]
#    midln=midnln
############### mm => count how many times we arranged the diagram #################################
    mm=mm+1
    return

b19=Button(frame,text='Rearrange',relief=RAISED, padx=9, command=arrange,bd=4)
#b19.pack(side=TOP,anchor=S)
b19.grid(row=0,column=1)

b19.config(state="disabled")
def draw_connector():
    global circ, cap1, cap2, ln, k9,midln,tca,k5,count_arrow,j4,i
    global l,circle1,no_circ_arr,arind,lnr,line,tca_,tca_n,k16
    k13=k5
    k=1
    k1=0
    k2=0
    while k < (count_circle+1):
        d1=math.sqrt((l[0]-c[2*k-2])**2+(l[1]-c[2*k-1])**2)
        d2=math.sqrt((l[2]-c[2*k-2])**2+(l[3]-c[2*k-1])**2)
        if d1<= 20:
            k1=k
        if d2<= 20:
            k2=k
        k=k+1
    if k1==0:
        cap1=Tk()
        l1=Label(cap1,text='Please click inside the circles',bd=2,bg='yellow')
        l1.pack()
        b9=Button(cap1,text='ok',command=Exit1,bd=2)
        b9.pack(anchor=S)
    if k2==0:
        cap2=Tk()
        l2=Label(cap2,text='Please click inside the circles',bg='yellow',bd=2)
        l2.pack()  
        b10=Button(cap2,text='ok',command=Exit2,bd=2)
        b10.pack( anchor=S)
    if k1!= 0 and k2 !=0 and c[2*k1-2] != c[2*k2-2] and k13==0:
        p7=(c[2*k1-1]-c[2*k2-1])/(c[2*k1-2]-c[2*k2-2])
        p8=((c[2*k1-2]-c[2*k2-2])/math.sqrt((c[2*k1-2]-c[2*k2-2])**2))

        canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c[2*k1-2],
        -p8*p7*(20/math.sqrt((p7**2)+1))+c[2*k1-1],
        -(-p8)*(20/math.sqrt((p7**2)+1))+c[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c[2*k2-1],width=pickWidths[2])
    if k1!= 0 and k2 !=0 and c[2*k1-2] != c[2*k2-2]:
        p7=(c[2*k1-1]-c[2*k2-1])/(c[2*k1-2]-c[2*k2-2])
        p8=((c[2*k1-2]-c[2*k2-2])/math.sqrt((c[2*k1-2]-c[2*k2-2])**2))
        ln=np.append(ln,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        line=np.append(line,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
#        lnr=np.append(lnr,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c[2*k1-2],
        -p8*p7*(20/math.sqrt((p7**2)+1))+c[2*k1-1],
        -(-p8)*(20/math.sqrt((p7**2)+1))+c[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c[2*k2-1]))
        midln=np.append(midln,((c[2*k1-2]+c[2*k2-2])/2,(c[2*k1-1]+c[2*k2-1])/2))
#        midln=np.append(midln,(c[2*k1-2],c[2*k1-1]))
        count_arrow=count_arrow+1
        k5=k5+1

    if k1!= 0 and k2 !=0 and c[2*k1-2] == c[2*k2-2] and k13==0:
        p9=((c[2*k1-1]-c[2*k2-1])/math.sqrt((c[2*k1-1]-c[2*k2-1])**2))
        canvas.create_line(c[2*k1-2],c[2*k1-1]-p9*20,c[2*k2-2],c[2*k2-1]+p9*20,width=pickWidths[2])
    if k1!= 0 and k2 !=0 and c[2*k1-2] == c[2*k2-2]:

        p9=((c[2*k1-1]-c[2*k2-1])/math.sqrt((c[2*k1-1]-c[2*k2-1])**2))
        ln=np.append(ln,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        line=np.append(line,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
#        lnr=np.append(lnr,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        lnr=np.append(lnr,(c[2*k1-2],c[2*k1-1]-p9*20,c[2*k2-2],c[2*k2-1]+p9*20))
        midln=np.append(midln,((c[2*k1-2]+c[2*k2-2])/2,(c[2*k1-1]+c[2*k2-1])/2))
#        midln=np.append(midln,(c[2*k1-2],c[2*k1-1]))
        count_arrow=count_arrow+1
        k5=k5+1
    if  k1!= 0 and k2 !=0 and c[2*k1-1] == c[2*k2-1] and k13==0:
        p9=(c[2*k2-2]-c[2*k1-2])/math.sqrt((c[2*k2-2]-c[2*k1-2])**2)
        canvas.create_line(c[2*k1-2]+p9*20,c[2*k1-1],c[2*k2-2]-p9*20,c[2*k2-1],width=pickWidths[2])
    if  k1!= 0 and k2 !=0 and c[2*k1-1] == c[2*k2-1]:
        p9=(c[2*k2-2]-c[2*k1-2])/math.sqrt((c[2*k2-2]-c[2*k1-2])**2)
        ln=np.append(ln,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        line=np.append(line,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
#        lnr=np.append(lnr,(c[2*k1-2],c[2*k1-1],c[2*k2-2],c[2*k2-1]))
        lnr=np.append(lnr,(c[2*k1-2]+p9*20,c[2*k1-1],c[2*k2-2]-p9*20,c[2*k2-1]))
        midln=np.append(midln,((c[2*k1-2]+c[2*k2-2])/2,(c[2*k1-1]+c[2*k2-1])/2))
#        midln=np.append(midln,(c[2*k1-2],c[2*k1-1]))
        count_arrow=count_arrow+1
        k5=k5+1
 
#    print 'ln',circ,ln
    circ=0
    circle1=[]
    ln1=[]
    l=[]
    i=1
    j3=1
    j4=0
    j5=0
    print 'k5555555555', k5,k9
    if k5>1 and k5<=count_circle:
#    if k5>k9 and k5<=count_circle:
        while i<=k5*2-1:
#            print 'i',i
            j1=0
            j=i+1
            while j<=k5*2:
                lth1=ln[i*2-2]-ln[j*2-2]
                lth2=ln[i*2-1]-ln[j*2-1]
                if lth1==0 and lth2==0:
                    j1=j1+1
                j=j+1
            if j1==1:
                circle1=np.append(circle1,(ln[i*2-2],ln[i*2-1]))
                j5=j5+1
            ln1=np.append(ln1,j1)
            i=i+1
        while j3<=i-1:
#            print 'j3',j3,i,ln1[j3-1]
            if ln1[j3-1]>=1:
                j4=j4+1
            j3=j3+1
        if j4<=k5-1:
            if k1!= 0 and k2 !=0 and c[2*k1-2] != c[2*k2-2] :
                p7=(c[2*k1-1]-c[2*k2-1])/(c[2*k1-2]-c[2*k2-2])
                p8=((c[2*k1-2]-c[2*k2-2])/math.sqrt((c[2*k1-2]-c[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c[2*k2-1]
                ,width=pickWidths[2])
            if k1!= 0 and k2 !=0 and c[2*k1-2] == c[2*k2-2]:
                p9=((c[2*k1-1]-c[2*k2-1])/math.sqrt((c[2*k1-1]-c[2*k2-1])**2))
                canvas.create_line(c[2*k1-2],c[2*k1-1]-p9*20,c[2*k2-2],c[2*k2-1]+p9*20,width=pickWidths[2])
            if k1!= 0 and k2 !=0 and c[2*k1-1] == c[2*k2-1]:
                p9=(c[2*k2-2]-c[2*k1-2])/math.sqrt((c[2*k2-2]-c[2*k1-2])**2)
                canvas.create_line(c[2*k1-2]+p9*20,c[2*k1-1],c[2*k2-2]-p9*20,c[2*k2-1],width=pickWidths[2])
            k9=k5

        if j4>k5-1:
            if k1!= 0 and k2 !=0 and c[2*k1-2] != c[2*k2-2]:
                p7=(c[2*k1-1]-c[2*k2-1])/(c[2*k1-2]-c[2*k2-2])
                p8=((c[2*k1-2]-c[2*k2-2])/math.sqrt((c[2*k1-2]-c[2*k2-2])**2))

                canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c[2*k1-2],
                -p8*p7*(20/math.sqrt((p7**2)+1))+c[2*k1-1],
                -(-p8)*(20/math.sqrt((p7**2)+1))+c[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c[2*k2-1]
                ,width=pickWidths[2])
            if k1!= 0 and k2 !=0 and c[2*k1-2] == c[2*k2-2]:
                p9=((c[2*k1-1]-c[2*k2-1])/math.sqrt((c[2*k1-1]-c[2*k2-1])**2))
                canvas.create_line(c[2*k1-2],c[2*k1-1]-p9*20,c[2*k2-2],c[2*k2-1]+p9*20,width=pickWidths[2])
            if k1!= 0 and k2 !=0 and c[2*k1-1] == c[2*k2-1]:
                p9=(c[2*k2-2]-c[2*k1-2])/math.sqrt((c[2*k2-2]-c[2*k1-2])**2)
                canvas.create_line(c[2*k1-2]+p9*20,c[2*k1-1],c[2*k2-2]-p9*20,c[2*k2-1],width=pickWidths[2])
            no_circ_arr=k5
            k16=k16+k5
            tca=np.append(tca,k16)
            tca_n=tca_n+1
            print 'ttttt',tca_n
#            arrange()
            b19.config(state="active")
            ln=[]
            k9=k5
            k5=0
            arind=0
            
    return()
def Exit1():
    global cap1
    cap1.destroy()
    return
def Exit2(): 
    global cap2
    cap2.destroy()
    return



############## function 'dconnector()' is for drawing the arrow ###############################

def dconnector():
    canvas.bind('<Button-1>',dfirstlast)
    return
def dfirstlast(event):
    global dl, dcirc
    dl=np.append(dl,(event.x,event.y))
    dcirc=dcirc+1
    if dcirc==2:
       draw_dconnector()
       circ=0
####### arind => arrow indicator ###########################################
def draw_dconnector():
    global dcirc, dcap1, dcap2, count_arrow,j4,k9,k5,k16,no_circ_arr,ln,midln,i
    global dl,circle1,tca,arind,lnr,line,count_circle,tca_n
#    print dl
    dk=1
    dk1=0
    dk2=0
    while dk < (count_circle+1):
        dd1=math.sqrt((dl[0]-c[2*dk-2])**2+(dl[1]-c[2*dk-1])**2)
        dd2=math.sqrt((dl[2]-c[2*dk-2])**2+(dl[3]-c[2*dk-1])**2)
        if dd1<= 20:
            dk1=dk
#            print dk1
        if dd2<= 20:
            dk2=dk
#            print dk2
        dk=dk+1
    if dk1==0:
        dcap1=Tk()
        dl1=Label(dcap1,text='Please click inside the circles',bd=2,bg='yellow')
        dl1.pack()
        b11=Button(dcap1,text='ok',command=Exit3,bd=2)
        b11.pack(anchor=S)
#        return()
    if dk2==0:
        dcap2=Tk()
        dl2=Label(dcap2,text='Please click inside the circles',bg='yellow',bd=2)
        dl2.pack()  
        b12=Button(dcap2,text='ok',command=Exit4,bd=2)
        b12.pack( anchor=S)
#        return()
    if dk1!= 0 and dk2 !=0 and c[2*dk1-2] != c[2*dk2-2]:
        dp7=(c[2*dk1-1]-c[2*dk2-1])/(c[2*dk1-2]-c[2*dk2-2])
        dp8=((c[2*dk1-2]-c[2*dk2-2])/math.sqrt((c[2*dk1-2]-c[2*dk2-2])**2))
        count_arrow=count_arrow+1
        ln=np.append(ln,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        line=np.append(line,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        lnr=np.append(lnr,((-dp8*20/math.sqrt((dp7**2)+1))+c[2*dk1-2],
        -dp8*dp7*(20/math.sqrt((dp7**2)+1))+c[2*dk1-1],
        -(-dp8)*(20/math.sqrt((dp7**2)+1))+c[2*dk2-2],
        -(-dp8)*dp7*(20/math.sqrt((dp7**2)+1))+c[2*dk2-1]))
        midln=np.append(midln,((c[2*dk1-2]+c[2*dk2-2])/2,(c[2*dk1-1]+c[2*dk2-1])/2))
        k5=k5+1

    if  dk1!= 0 and dk2 !=0 and c[2*dk1-2] == c[2*dk2-2]:
        count_arrow=count_arrow+1
        dp9=(c[2*dk2-1]-c[2*dk1-1])/math.sqrt((c[2*dk2-1]-c[2*dk1-1])**2)
        ln=np.append(ln,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        line=np.append(line,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        lnr=np.append(lnr,(c[2*dk1-2],c[2*dk1-1]+dp9*20,c[2*dk2-2],c[2*dk2-1]-dp9*20))
        midln=np.append(midln,((c[2*dk1-2]+c[2*dk2-2])/2,(c[2*dk1-1]+c[2*dk2-1])/2))
        k5=k5+1
    if  dk1!= 0 and dk2 !=0 and c[2*dk1-1] == c[2*dk2-1]:
        count_arrow=count_arrow+1
        dp9=(c[2*dk2-2]-c[2*dk1-2])/math.sqrt((c[2*dk2-2]-c[2*dk1-2])**2)
        ln=np.append(ln,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        line=np.append(line,(c[2*dk1-2],c[2*dk1-1],c[2*dk2-2],c[2*dk2-1]))
        lnr=np.append(lnr,(c[2*dk1-2]+dp9*20,c[2*dk1-1],c[2*dk2-2]-dp9*20,c[2*dk2-1]))
        midln=np.append(midln,((c[2*dk1-2]+c[2*dk2-2])/2,(c[2*dk1-1]+c[2*dk2-1])/2))
        k5=k5+1

    print 'pppp',j4,k9
    circ=0
    circle1=[]
    ln1=[]
    l=[]
    i=1
    j3=1
    j4=0
    j5=0
    if k5>1 and k5<=count_circle:
        while i<=k5*2-1:
#            print 'i',i
            j1=0
            j=i+1
            while j<=k5*2:
                lth1=ln[i*2-2]-ln[j*2-2]
                lth2=ln[i*2-1]-ln[j*2-1]
                if lth1==0 and lth2==0:
                    j1=j1+1
                j=j+1
            if j1==1:
                circle1=np.append(circle1,(ln[i*2-2],ln[i*2-1]))
                j5=j5+1
            ln1=np.append(ln1,j1)
            i=i+1
        while j3<=i-1:
#            print 'j3',j3,i,ln1[j3-1]
            if ln1[j3-1]>=1:
                j4=j4+1
            j3=j3+1

        if j4>k5-1:
            print '***',j4,k9
#            k9=k9+1
            if dk1!= 0 and dk2 !=0 and c[2*dk1-2] != c[2*dk2-2]:
                dp7=(c[2*dk1-1]-c[2*dk2-1])/(c[2*dk1-2]-c[2*dk2-2])
                dp8=((c[2*dk1-2]-c[2*dk2-2])/math.sqrt((c[2*dk1-2]-c[2*dk2-2])**2))
#               print dp8

                canvas.create_line((-dp8*20/math.sqrt((dp7**2)+1))+c[2*dk1-2],
                -dp8*dp7*(20/math.sqrt((dp7**2)+1))+c[2*dk1-1],
                -(-dp8)*(20/math.sqrt((dp7**2)+1))+c[2*dk2-2],
                -(-dp8)*dp7*(20/math.sqrt((dp7**2)+1))+c[2*dk2-1]
                ,width=pickWidths[2],arrow="last")

            if  dk1!= 0 and dk2 !=0 and c[2*dk1-2] == c[2*dk2-2]:
                dp9=(c[2*dk2-1]-c[2*dk1-1])/math.sqrt((c[2*dk2-1]-c[2*dk1-1])**2)
                canvas.create_line(c[2*dk1-2],c[2*dk1-1]+dp9*20,c[2*dk2-2],c[2*dk2-1]-dp9*20,
                width=pickWidths[2],arrow="last")
            if  dk1!= 0 and dk2 !=0 and c[2*dk1-1] == c[2*dk2-1]:
                dp9=(c[2*dk2-2]-c[2*dk1-2])/math.sqrt((c[2*dk2-2]-c[2*dk1-2])**2)
                canvas.create_line(c[2*dk1-2]+dp9*20,c[2*dk1-1],c[2*dk2-2]-dp9*20,c[2*dk2-1],
                width=pickWidths[2],arrow="last")
            arind=1
            b19.config(state="active")
            no_circ_arr=k5
            k16=k16+k5
            tca=np.append(tca,k16)
            tca_n=tca_n+1
            print 'tca,tca_n',tca,tca_n
#            arrange()
            ln=[]
            k9=k5
            k5=0
 

#    print dcirc
    dcirc=0
    dl=[]
#    return()
    
def Exit3():
    global dcap1
    dcap1.destroy()
    return
def Exit4(): 
    global dcap2
    dcap2.destroy()
    return

#############################################################################################
########## this section is for drawing different shapes by clicking on the canvas ###########
#############################################################################################

def hexagon():
    global k6,count_circle,count_arrow
    k6=6
    drawfig()
    count_circle=count_circle+6
    count_arrow=count_arrow+6
def pentagon():
    global k6,count_circle,count_arrow
    k6=5
    drawfig()
    count_circle=count_circle+5
    count_arrow=count_arrow+5
def square():
    global k6,count_circle,count_arrow
    k6=4
    drawfig()
    count_circle=count_circle+4
    count_arrow=count_arrow+4
def triangle():
    global k6,count_circle,count_arrow
    k6=3
    drawfig()
    count_circle=count_circle+3
    count_arrow=count_arrow+3
def double():
    global k6,count_circle,count_arrow
    k6=2
    drawfig()
    count_circle=count_circle+2
    count_arrow=count_arrow+2


def drawfig():
    canvas.bind('<Button-1>',drawgeo)
    return
def drawgeo(event):
    global k6,ln,lnr,line,midln,c,count_circle,count_arrow
    c3=[]
    k1=1
    print count_circle, count_arrow
    cx=event.x
    cy=event.y
    diam=100
    ang=2*3.14159265359/k6
    cx1=cx
    cy1=cy-diam
    canvas.create_oval(cx1-20,cy1-20,cx1+20,cy1+20,width=pickWidths[2])
    c3=np.append(c3,(cx1,cy1))
    c=np.append(c,(cx1,cy1))
    kk=1
    while kk<=k6-1:
        cx2=(cx1-cx)*math.cos(kk*ang)-(cy1-cy)*math.sin(kk*ang)
        cy2=(cy1-cy)*math.cos(kk*ang)+(cx1-cx)*math.sin(kk*ang)
        cx3=cx2+cx
        cy3=cy2+cy
        canvas.create_oval(cx3-20,cy3-20,cx3+20,cy3+20,width=pickWidths[2])
        c3=np.append(c3,(cx3,cy3))
        c=np.append(c,(cx3,cy3))
        kk=kk+1

    while k1<=k6:
#            print 'c2',c2,k1
#            print 'midln',midln
        k2=k1+1
        if k1==k6:
            k2=1
        if c3[2*k1-2] != c3[2*k2-2] and k2!=1:
            print 'sourav1'
            p7=(c3[2*k1-1]-c3[2*k2-1])/(c3[2*k1-2]-c3[2*k2-2])
            p8=((c3[2*k1-2]-c3[2*k2-2])/math.sqrt((c3[2*k1-2]-c3[2*k2-2])**2))
            canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c3[2*k1-2],
            -p8*p7*(20/math.sqrt((p7**2)+1))+c3[2*k1-1],
            -(-p8)*(20/math.sqrt((p7**2)+1))+c3[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c3[2*k2-1]
            ,width=pickWidths[2])
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c3[2*k1-2],-p8*p7*(20/math.sqrt((p7**2)+1))+c3[2*k1-1],
            -(-p8)*(20/math.sqrt((p7**2)+1))+c3[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c3[2*k2-1]))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        if k1!= 0 and k2 !=0 and c3[2*k1-2] == c3[2*k2-2] and k2!=1:
            print 'sourav2'
            p9=((c3[2*k1-1]-c3[2*k2-1])/math.sqrt((c3[2*k1-1]-c3[2*k2-1])**2))
            canvas.create_line(c3[2*k1-2],c3[2*k1-1]-p9*20,c3[2*k2-2],c3[2*k2-1]+p9*20,
            width=pickWidths[2])
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,(c3[2*k1-2],c3[2*k1-1]-p9*20,c3[2*k2-2],c3[2*k2-1]+p9*20))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        if k1!= 0 and k2 !=0 and c3[2*k1-1] == c3[2*k2-1] and k2!=1:
            print 'sourav3'
            p9=(c3[2*k2-2]-c3[2*k1-2])/math.sqrt((c3[2*k2-2]-c3[2*k1-2])**2)
            canvas.create_line(c3[2*k1-2]+p9*20,c3[2*k1-1],c3[2*k2-2]-p9*20,c3[2*k2-1],
            width=pickWidths[2])
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,(c3[2*k1-2]+p9*20,c3[2*k1-1],c3[2*k2-2]-p9*20,c3[2*k2-1]))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        if c3[2*k1-2] != c3[2*k2-2] and k2==1:
            print 'sourav4'
            p7=(c3[2*k1-1]-c3[2*k2-1])/(c3[2*k1-2]-c3[2*k2-2])
            p8=((c3[2*k1-2]-c3[2*k2-2])/math.sqrt((c3[2*k1-2]-c3[2*k2-2])**2))
            canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+c3[2*k1-2],
            -p8*p7*(20/math.sqrt((p7**2)+1))+c3[2*k1-1],
            -(-p8)*(20/math.sqrt((p7**2)+1))+c3[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c3[2*k2-1]
            ,width=pickWidths[2],arrow="last")
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,((-p8*20/math.sqrt((p7**2)+1))+c3[2*k1-2],
            -p8*p7*(20/math.sqrt((p7**2)+1))+c3[2*k1-1],
            -(-p8)*(20/math.sqrt((p7**2)+1))+c3[2*k2-2],-(-p8)*p7*(20/math.sqrt((p7**2)+1))+c3[2*k2-1]))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        if k1!= 0 and k2 !=0 and c3[2*k1-2] == c3[2*k2-2] and k2==1:
            print 'sourav5'
            p9=((c3[2*k1-1]-c3[2*k2-1])/math.sqrt((c3[2*k1-1]-c3[2*k2-1])**2))
            canvas.create_line(c3[2*k1-2],c3[2*k1-1]-p9*20,c3[2*k2-2],c3[2*k2-1]+p9*20,
            width=pickWidths[2],arrow="last")
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,(c3[2*k1-2],c3[2*k1-1]-p9*20,c3[2*k2-2],c3[2*k2-1]+p9*20))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        if k1!= 0 and k2 !=0 and c3[2*k1-1] == c3[2*k2-1] and k2==1:
            print 'sourav6'
            p9=(c3[2*k2-2]-c3[2*k1-2])/math.sqrt((c3[2*k2-2]-c3[2*k1-2])**2)
            canvas.create_line(c3[2*k1-2]+p9*20,c3[2*k1-1],c3[2*k2-2]-p9*20,c3[2*k2-1],
            width=pickWidths[2],arrow="last")
            ln=np.append(ln,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            line=np.append(line,(c3[2*k1-2],c3[2*k1-1],c3[2*k2-2],c3[2*k2-1]))
            lnr=np.append(lnr,(c3[2*k1-2]+p9*20,c3[2*k1-1],c3[2*k2-2]-p9*20,c3[2*k2-1]))
            midln=np.append(midln,((c3[2*k1-2]+c3[2*k2-2])/2,(c3[2*k1-1]+c3[2*k2-1])/2))
        k1=k1+1
#    print 'middle ln',midln
#    print 'centre c',c

############################################################################################    
######## function popup_menu(event) create an menu list at the clicked point to delete #####
######## the geometric figure .. It can be increased by putting any jobs ###################
############################################################################################

def popup_menu(event):
    global del_eventx, del_eventy, c,cap3,lnr,lndel,cdel,midln,count_circle,count_arrow
    l1=1
    l2=1
    l3=1
    nc=0
    nl=0
    ml=0
    k=1
    kk=1
    lndel=0
    cdel=0
    k1=0
    while l1 < (count_arrow+1):
        d1=math.sqrt((event.x-c[2*l1-2])**2+(event.y-c[2*l1-1])**2)
        if d1<=20:
            nc=nc+1
        l1=l1+1
    while l2 < (count_arrow+1):
        d2=((event.x-lnr[4*l2-4])/(lnr[4*l2-4]-lnr[4*l2-2]))-((event.y-lnr[4*l2-3])/(lnr[4*l2-3]-lnr[4*l2-1]))
        if math.sqrt(d2**2)//1==0:
            nl=nl+1
        l2=l2+1 
    while l3 < (count_arrow+1):
        print 'l33333',l3
        d3=math.sqrt((lnr[4*l3-4]-lnr[4*l3-2])**2.0+(lnr[4*l3-3]-lnr[4*l3-1])**2.0)/2.0
        d4=math.sqrt((event.x-midln[2*l3-2])**2+(event.y-midln[2*l3-1])**2)
        if d4<=d3:
            ml=ml+1
            k=l3
        l3=l3+1
#    print 'nc,nl,ml',nc,nl,ml
    if nc==0 and nl!=0 and ml!=0:
        k1=k1+1
        lndel=k
        print 'inside',k
        del_eventx=event.x
        del_eventy=event.y
        popup=Menu(root,tearoff=0)
        popup.add_cascade(label='click Delete to delete the line')
#        popup.add_command(label='Enter value', command=Value)
        popup.add_command(label='Delete', command=Delete)
        popup.add_separator()
        popup.add_command(label='Exit', command=Exit)
        try:
            popup.tk_popup(event.x_root, event.y_root,0)
        finally:
            popup.grab_release()
    while kk < (count_circle+1):
        d1=math.sqrt((event.x-c[2*kk-2])**2+(event.y-c[2*kk-1])**2)
        if d1<= 20 :
            k1=k1+1
            cdel=kk
            del_eventx=event.x
            del_eventy=event.y
            popup=Menu(root,tearoff=0)
            popup.add_cascade(label='click Delete to delete the circle')
#            popup.add_command(label='Enter value', command=Value)
            popup.add_command(label='Delete', command=Delete)
            popup.add_separator()
            popup.add_command(label='Exit', command=Exit)
            try:
                popup.tk_popup(event.x_root, event.y_root,0)
            finally:
                popup.grab_release()
        kk=kk+1
    
    if k1==0:   
        cap3=Tk()
        dl6=Label(cap3,text='to delete an object please click on the figure',bg='yellow',bd=2)
        dl6.pack()  
        b16=Button(cap3,text='ok',command=Exit5,bd=2)
        b16.pack( anchor=S)
            
            
def Exit5():
    global cap3
    cap3.destroy()
    return

def Delete():
    global del_eventx, del_eventy, c,count_circle,count,e3,e4,lnr,lndel,cdel,count_arrow
    global midln, line,ln
    object = canvas.find_closest(del_eventx, del_eventy)
    canvas.delete(object)
    print 'lndel, cdel',lndel, cdel
   
    print 'midln_new', midln
    k=1
    if cdel!=0:
        while k<count_circle+1:
            d1=math.sqrt((del_eventx-c[2*k-2])**2+(del_eventy-c[2*k-1])**2)
            if d1<=20:
                k1=1
                while k1<count_circle+1:
                    x=(c[2*k-2]+c[2*k1-2])/2
                    y=(c[2*k-1]+c[2*k1-1])/2
                    k2=1
                    while k2<count_arrow+1:
                        if x==midln[2*k2-2] and y==midln[2*k2-1]:
                            object = canvas.find_closest(x,y)
                            canvas.delete(object)
                            lnr=np.delete(lnr,[4*k2-1,4*k2-2,4*k2-3,4*k2-4])
                            line=np.delete(line,[4*k2-1,4*k2-2,4*k2-3,4*k2-4])
                            ln=np.delete(ln,[4*k2-1,4*k2-2,4*k2-3,4*k2-4])
                            midln=np.delete(midln,[2*k2-2,2*k2-1])
#                            print count_arrow
                            count_arrow=count_arrow-1                            
                        k2=k2+1
                    k1=k1+1
            k=k+1

    if lndel!=0:
        lnr=np.delete(lnr,[4*lndel-1,4*lndel-2,4*lndel-3,4*lndel-4])
        line=np.delete(line,[4*lndel-1,4*lndel-2,4*lndel-3,4*lndel-4])
        ln=np.delete(ln,[4*lndel-1,4*lndel-2,4*lndel-3,4*lndel-4])
        midln=np.delete(midln,[2*lndel-1,2*lndel-2])
        count_arrow=count_arrow-1
    if cdel!=0:
        c=np.delete(c,[2*cdel-1,2*cdel-2])
        count_circle=count_circle-1


def Exit7():
    global cap5
    cap5.destroy()
    return
def Exit():
    return

######################################################################################
######### function 'select' and 'moving_object' is for moving figure on canvas #######
######################################################################################

def select(event):
    global object1, event_movex, event_movey 
    global c,count_circle,lnr,count_arrow
    global midln, cdell, lndell, line, cap13, flg2
    l1=1
    l2=1
    l3=1
    nc=0
    nl=0
    ml=0
    k=1
    flg2=1
    lndell=0
    cdell=0
    k1=0
    while l1 < (count_arrow+1):
        d1=math.sqrt((event.x-c[2*l1-2])**2+(event.y-c[2*l1-1])**2)
        if d1<=20:
            nc=nc+1
        l1=l1+1
    while l2 < (count_arrow+1):
        d2=((event.x-lnr[4*l2-4])/(lnr[4*l2-4]-lnr[4*l2-2]))-((event.y-lnr[4*l2-3])/(lnr[4*l2-3]-lnr[4*l2-1]))
        if math.sqrt(d2**2)//1==0:
            nl=nl+1
        l2=l2+1 
    while l3 < (count_arrow+1):
        d3=math.sqrt((lnr[4*l3-4]-lnr[4*l3-2])**2.0+(lnr[4*l3-3]-lnr[4*l3-1])**2.0)/2.0
        d4=math.sqrt((event.x-midln[2*l3-2])**2+(event.y-midln[2*l3-1])**2)
        if d4<=d3:
            ml=ml+1
        l3=l3+1
    print 'nc,nl,ml',nc,nl,ml
    if nc==0 and nl!=0 and ml!=0:
        k1=k1+1
        lndell=k
        print 'inside'
        event_movex = event.x
        event_movey = event.y
        object1 = canvas.find_closest(event_movex, event_movey)
    k=1
    while k < (count_circle+1):
        d1=math.sqrt((event.x-c[2*k-2])**2+(event.y-c[2*k-1])**2)
        if d1<= 20 :
            k1=k1+1
            cdell=k
#            event_movex = event.x
#            event_movey = event.y
            event_movex = c[2*k-2]
            event_movey = c[2*k-1]
            object1 = canvas.find_closest(event_movex, event_movey)
        k=k+1
    
    if k1==0:   
        flg2=0
        event_movex = event.x
        event_movey = event.y
            
    return
def moving_obj(where):
    global object1, event_movex, event_movey 
    global c,count_circle,line,lnr,count_arrow
    global midln, cdell, flg2
    flg1=0
    if flg2==0:
        diffX = event_movex - where.x
        diffY = event_movey - where.y
        canvas.move(ALL,-diffX,-diffY)
    if flg2!=0:
        diffX = event_movex - where.x
        diffY = event_movey - where.y
        canvas.move(object1,-diffX,-diffY)
        k=1
        if cdell!=0:
            while k<count_circle+1:
                d1=math.sqrt((event_movex-c[2*k-2])**2+(event_movey-c[2*k-1])**2)
                if d1<=20:
                    k1=count_arrow
                    while k1>0:
#                        print 'k1',k1
                        k2=1
                        while k2<3:
                            d2=math.sqrt((c[2*k-2]-lnr[4*k1-(4-(k2-1)*2)])**2+(c[2*k-1]-lnr[4*k1-(3-(k2-1)*2)])**2)
                            if d2<21:
                                k3=k2
                                if k3==1:
                                    flg1=1
#                                   canvas.create_line(lnr[4*k1-2],lnr[4*k1-1],where.x,where.y,width=pickWidths[2])
                                    if lnr[4*k1-1] != where.y and lnr[4*k1-2] != where.x:
                                        print 'k11',k1
                                        object2 = canvas.find_closest(midln[2*k1-2],midln[2*k1-1])
                                        canvas.delete(object2)
                                        p7=(line[4*k1-3]-where.y)/(line[4*k1-4]-where.x)
                                        p8=((line[4*k1-4]-where.x)/math.sqrt((line[4*k1-4]-where.x)**2))
                                        canvas.create_line((-p8*20/math.sqrt((p7**2)+1))+line[4*k1-2],
                                        -p8*p7*(20/math.sqrt((p7**2)+1))+line[4*k1-1],
                                        -(-p8)*(20/math.sqrt((p7**2)+1))+where.x,
                                        -(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y
                                        ,width=pickWidths[2])

                                        a=lnr[4*k1-2]
                                        b=lnr[4*k1-1]
                                        aa=line[4*k1-2]
                                        bb=line[4*k1-1]
                                    
                                        lnr=np.delete(lnr,[4*k1-1,4*k1-2,4*k1-3,4*k1-4])
                                        line=np.delete(line,[4*k1-1,4*k1-2,4*k1-3,4*k1-4])
                                        lnr=np.append(lnr,(a,b,-(-p8)*(20/math.sqrt((p7**2)+1))+where.x,
                                        -(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y))
                                        line=np.append(line,(aa,bb,where.x,where.y))
                                        midln=np.delete(midln,[2*k1-2,2*k1-1])
                                        a1=(a+(-(-p8)*(20/math.sqrt((p7**2)+1))+where.x))/2
                                        b1=(b+(-(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y))/2
                                        midln=np.append(midln,(a1,b1))


                                if k3==2 :
                                    flg1=1
#                                   canvas.create_line(lnr[4*k1-4],lnr[4*k1-3],where.x,where.y,width=pickWidths[2])
                                    if lnr[4*k1-3] != where.y and lnr[4*k1-4] != where.x:
                                        print 'k21',k1
                                        object2 = canvas.find_closest(midln[2*k1-2],midln[2*k1-1])
                                        canvas.delete(object2)
                                        p7=(line[4*k1-1]-where.y)/(line[4*k1-2]-where.x)
                                        p8=((line[4*k1-2]-where.x)/math.sqrt((line[4*k1-2]-where.x)**2))
                                        canvas.create_line(((-p8)*20/math.sqrt((p7**2)+1))+line[4*k1-4],
                                        (-p8)*p7*(20/math.sqrt((p7**2)+1))+line[4*k1-3],
                                        -(-p8)*(20/math.sqrt((p7**2)+1))+where.x,-(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y
                                        ,width=pickWidths[2])
                                        a=lnr[4*k1-4]
                                        b=lnr[4*k1-3]
                                        aa=line[4*k1-4]
                                        bb=line[4*k1-3]

                                        lnr=np.delete(lnr,[4*k1-1,4*k1-2,4*k1-3,4*k1-4])
                                        line=np.delete(line,[4*k1-1,4*k1-2,4*k1-3,4*k1-4])
                                        lnr=np.append(lnr,(-(-p8)*(20/math.sqrt((p7**2)+1))+where.x,
                                        -(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y,a,b))
                                        line=np.append(line,(where.x,where.y,aa,bb))
                                        midln=np.delete(midln,[2*k1-2,2*k1-1])
                                        a1=(a+(-(-p8)*(20/math.sqrt((p7**2)+1))+where.x))/2
                                        b1=(b+(-(-p8)*p7*(20/math.sqrt((p7**2)+1))+where.y))/2
                                        midln=np.append(midln,(a1,b1))


                            k2=k2+1
                        
                        k1=k1-1
                    c=np.delete(c,[2*k-2,2*k-1])
                    c=np.append(c,(where.x,where.y))
                k=k+1
        if flg1==0:
            c=np.delete(c,[2*cdell-2,2*cdell-1])
            c=np.append(c,(where.x,where.y))
                    
    return
canvas.bind('<Button-3>',popup_menu)
canvas.bind('<Button-2>',select)
#canvas.bind('<Control>',selectopt)
canvas.bind('<ButtonRelease-2>',moving_obj)
def quit():
    root.quit()
#t = Text(frame2, height=20, width=40)
#t.pack()
#def enter_text():
#    global count_circle, val, c,k4, vall, del_eventx, del_eventy
#    k=1
#    print "fff",event.x
#    while k < (count_circle+1):
#        d1=math.sqrt((del_eventx-c[2*k-2])**2+(del_eventy-c[2*k-1])**2)
#        if d1<= 20:
#            k4=k
#            t.insert(END,"\n event")
#            t.insert(END,['C',k4,'=',vall])
##        t.insert("end",'***')
##        t.insert("end",val[k4])
##        k4=k4+1
#        k=k+1

##########################################################################
############### gif images for the buttons ###############################
##########################################################################

image1=PhotoImage(file="circle.gif")
image5=PhotoImage(file="hexagon.gif")
image6=PhotoImage(file="connect.gif")
image8=PhotoImage(file="con_cir.gif")
image9=PhotoImage(file="pentagon.gif")
image10=PhotoImage(file="square.gif")
image11=PhotoImage(file="Triangle.gif")
image12=PhotoImage(file="Line.gif")
var=IntVar

################ Radiobutton to draw the circle ##############################

rb1=Radiobutton(frame,image=image1,indicatoron = 0,variable=var,value=0,relief=RAISED, padx=48 ,command=circle,bd=4)
rb1.grid(row=0,column=0)

###################################################################################################################
################ function 'funcn' contains all the buttons for drawing different geometric shapes #################
###################################################################################################################

def funcn():
    global flag,r1,r2,r3,r4,r5
    flag=flag+1
    if flag==2:
        destroy_button()
    if flag==1:
        NVar=IntVar
        r1=Radiobutton(frame,image=image5,indicatoron = 0,variable=NVar,value=10,relief=RAISED, padx=19,command=hexagon,bd=4)
        r1.grid(row=1,column=1)
        r2=Radiobutton(frame,image=image9,indicatoron = 0,variable=NVar,value=11,relief=RAISED, padx=19,command=pentagon,bd=4)
        r2.grid(row=2,column=1)
        r3=Radiobutton(frame,image=image10,indicatoron = 0,variable=NVar,value=12,relief=RAISED, padx=19,command=square,bd=4)
        r3.grid(row=3,column=1)
        r4=Radiobutton(frame,image=image11,indicatoron = 0,variable=NVar,value=13,relief=RAISED, padx=19,command=triangle,bd=4)
        r4.grid(row=4,column=1)
        r5=Radiobutton(frame,image=image12,indicatoron = 0,variable=NVar,value=14,relief=RAISED, padx=19,command=double,bd=4)
        r5.grid(row=5,column=1)

def destroy_button():
    global flag,r1,r2,r3,r4,r5
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    flag=0

### Function 'TOF_cal' is for calculating the Tern Over Frequency ###################### 
def TOF_cal():
    global val, vall
    print val
    print vall
    print delG

########################################################################################
##### various buttons ##################################################################
########################################################################################

rb5=Button(frame,image=image5,relief=RAISED, padx=8,command=funcn,bd=4)
rb5.grid(row=1,column=0)
b16=Button(frame2,text='Put Numbers',relief=RAISED, padx=9, command=Numbering,bd=4)
b16.pack(side=TOP,anchor=S)
b17=Button(frame2,text='TOF Cal',relief=RAISED, padx=9, bd=4,command=TOF_cal)
b17.pack(side=TOP,anchor=S)
b18=Button(frame2,text='TON Cal',relief=RAISED, padx=9, bd=4)
b18.pack(side=TOP,anchor=S)
rb7=Radiobutton(frame,image=image8,indicatoron = 0,variable=var,value=1,relief=RAISED, padx=28, command=connector,bd=4)
rb7.grid(row=2,column=0)
rb8=Radiobutton(frame,image=image6,indicatoron = 0,variable=var,value=2,relief=RAISED, padx=28, command=dconnector,bd=4)
rb8.grid(row=3,column=0)


menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="draw", menu=subMenu)
subMenu.add_command(label="Circle", command= circle)
subMenu.add_command(label="Connector", command= connector)
subMenu.add_command(label="Dconnector", command= dconnector)

editMenu=Menu(menu)
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="quit", command= quit)

################################################################################################################
########### function 'done' and 'disappear' is for disable the drawing button after clicking 'Done' button ####
########### function 'redraw' and 'appear' is for enable the drawing button after clicking 'redraw' button
################################################################################################################
def done():
    global k3
    k3=1
    canvas.bind('<Button-1>',disappear)
    return
def disappear(event):
    rb1.config(state="disabled")
    rb5.config(state="disabled")
    rb7.config(state="disabled")
    rb8.config(state="disabled")

def redraw():
    global k3
    k3=0
    canvas.bind('<Button-1>',appear)
def appear(event):
    rb1.config(state="active")
    rb5.config(state="active")
    rb7.config(state="active")
    rb8.config(state="active")

################################################################################################################
########### function 'clean' is for destroy the old canvas and recreate a new one ##############################
################################################################################################################
def clean():
    global count_circle, c,tca,mm, count_arrow, ln, lnr, line
    global canvas,centr,mm
    ln=[]
    lnr=[]
    line=[]
    c=[]
    tca=[]
    tca=np.append(tca,1)
    mm=0
    count_circle=0
    count_arrow=0
    canvas.destroy()
    canvas=Canvas(frame1, height=700, width= 700, bg='white',bd=2)
    canvas.pack()
    
var1=IntVar

###################################################################################################################
########################### Buttons ###############################################################################
###################################################################################################################

rb10=Radiobutton(frame,text='Redraw',indicatoron = 0,variable=var1,value=3,relief=RAISED, padx=7,pady=5,bd=4, command=redraw)
rb10.grid(row=7,column=0)

rb11=Radiobutton(frame,text='done',indicatoron = 0,variable=var1,value=4,relief=RAISED, padx=7,pady=5,bd=4, command=done)
rb11.pack(side=LEFT,anchor=W)
rb11.grid(row=8,column=0)
rb6=Button(frame,text='Clean',relief=RAISED, padx=7,pady=5, command=clean,bd=4)
rb6.grid(row=9,column=0)
root.mainloop()
