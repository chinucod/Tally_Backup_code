import shutil
import os
import math
import tkinter 
import sys
from tkinter import *
root=Tk()
root.title("calc")
root.geometry("800x1400")

def Calc():
    t1=int(sub1value.get())
    t2=int(sub2value.get())
    t3=int(sub3value.get())
    t4=int(sub4value.get())
    t5=int(sub5value.get())
    t6=int(sub6value.get())
    t7=int(sub7value.get())
    t8=int(sub8value.get())
    t9=int(sub9value.get())
    t10=int(sub10value.get())
    t11=int(sub11value.get())
    t12=int(sub12value.get())
    t13=int(sub13value.get())
    t14=int(sub14value.get())
    t15=int(sub15value.get())
    
    total=(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15)
    total2=total*35.48/100
    total3=total-total2
    total4=total3*25/100
    total5=total3+total4
    Label(text=f"{total}",font="arial 15 bold").place(x=200,y=770)
    Label(text="{0:.4f}".format((total2)),font="arial 15 bold").place(x=200,y=820)
    Label(text="{0:.4f}".format((total3)),font="arial 15 bold").place(x=200,y=870)
    Label(text="{0:.4f}".format((total4)),font="arial 15 bold").place(x=200,y=920)
    Label(text="{0:.4f}".format((total5)),font="arial 25 bold",foreground="red").place(x=200,y=970)
def Clear():
    sub1value.delete(0,END)
    sub2value.delete(0,END)
    sub3value.delete(0,END)
    sub4value.delete(0,END)
    sub5value.delete(0,END)
    sub6value.delete(0,END)
    sub7value.delete(0,END)
    sub8value.delete(0,END)
    sub9value.delete(0,END)
    sub10value.delete(0,END)
    sub11value.delete(0,END)
    sub12value.delete(0,END)
    sub13value.delete(0,END)
    sub14value.delete(0,END)
    sub15value.delete(0,END)
    saree1value.delete(0,END)
    saree2value.delete(0,END)
    saree3value.delete(0,END)
    saree4value.delete(0,END)
    saree5value.delete(0,END)
    saree6value.delete(0,END)
    saree7value.delete(0,END)
    saree8value.delete(0,END)
    saree9value.delete(0,END)
    saree10value.delete(0,END)
    saree11value.delete(0,END)
    saree12value.delete(0,END)
    saree13value.delete(0,END)
    saree14value.delete(0,END)
    saree15value.delete(0,END)
def Zero():
    if sub1value.get()=="":
        sub1value.insert(0,0)  
    if sub2value.get()=="":
        sub2value.insert(0,0)    
    if sub3value.get()=="":
        sub3value.insert(0,0)
    if sub4value.get()=="":
        sub4value.insert(0,0)
    if sub5value.get()=="":
        sub5value.insert(0,0)
    if sub6value.get()=="":
        sub6value.insert(0,0)
    if sub7value.get()=="":
        sub7value.insert(0,0)
    if sub8value.get()=="":
        sub8value.insert(0,0)
    if sub9value.get()=="":
        sub9value.insert(0,0)
    if sub10value.get()=="":
        sub10value.insert(0,0)
    if sub11value.get()=="":
        sub11value.insert(0,0)
    if sub12value.get()=="":
        sub12value.insert(0,0)   
    if sub13value.get()=="":
        sub13value.insert(0,0)
    if sub14value.get()=="":
        sub14value.insert(0,0)
    if sub15value.get()=="":
        sub15value.insert(0,0)
    if saree1value.get()=="":
        saree1value.insert(0,0)
    if saree2value.get()=="":
        saree2value.insert(0,0)    
    if saree3value.get()=="":
        saree3value.insert(0,0)
    if saree4value.get()=="":
        saree4value.insert(0,0)
    if saree5value.get()=="":
        saree5value.insert(0,0)
    if saree6value.get()=="":
        saree6value.insert(0,0)
    if saree7value.get()=="":
        saree7value.insert(0,0)
    if saree8value.get()=="":
        saree8value.insert(0,0)
    if saree9value.get()=="":
        saree9value.insert(0,0)
    if saree10value.get()=="":
        saree10value.insert(0,0)
    if saree11value.get()=="":
        saree11value.insert(0,0)
    if saree12value.get()=="":
        saree12value.insert(0,0)   
    if saree13value.get()=="":
        saree13value.insert(0,0)
    if saree14value.get()=="":
        saree14value.insert(0,0)
    if saree15value.get()=="":
        saree15value.insert(0,0)
                                     
            
       
def Remove():
    t16=saree1value.get()
    t17=saree2value.get()
    t18=saree3value.get()
    t19=saree4value.get()
    t20=saree5value.get()
    t21=saree6value.get()
    t22=saree7value.get()
    t23=saree8value.get()
    t24=saree9value.get()
    t25=saree10value.get()
    t26=saree11value.get()
    t27=saree12value.get()
    t28=saree13value.get()
    t29=saree14value.get()
    t30=saree15value.get()
    remove_items=[]
    remove_items.append(t16+".jpg")
    remove_items.append(t17+".jpg")
    remove_items.append(t18+".jpg")
    remove_items.append(t19+".jpg")
    remove_items.append(t20+".jpg")
    remove_items.append(t21+".jpg")
    remove_items.append(t22+".jpg")
    remove_items.append(t23+".jpg")
    remove_items.append(t24+".jpg")
    remove_items.append(t25+".jpg")
    remove_items.append(t26+".jpg")
    remove_items.append(t27+".jpg")
    #k='0'
    #remove_items.remove('0')
    from_dir=""
    to_dir="H:/My Drive/backup_saree_soldout"
    a = [i for i in remove_items if i != '0.jpg']
    print(a)
    #print(a)
    for i in a:
        for files in os.listdir('H:/My Drive/random sarees'):
            #print("current folder")
            for file in os.listdir('H:/My Drive/random sarees/'+files):
                #print(file)
                if i in file:
                    print('found in '+files+" "+file)
                    print(file)
                    from_dir='H:/My Drive/random sarees/'+files
                    shutil.copy(from_dir,to_dir)
                    sys.stdout.write("copied")
                else:
                    pass
        #if os.path.exists('H:/My Drive/random sarees/'+i):
            
            #print(i.split('-'))

    #print(remove_items)

sub1=Label(root,text="num1",font="arial 10")
sub2=Label(root,text="num2",font="arial 10")
sub3=Label(root,text="num3",font="arial 10")
sub4=Label(root,text="num4",font="arial 10")
sub5=Label(root,text="num5",font="arial 10")
sub6=Label(root,text="num6",font="arial 10")
sub7=Label(root,text="num7",font="arial 10")
sub8=Label(root,text="num8",font="arial 10")
sub9=Label(root,text="num9",font="arial 10")
sub10=Label(root,text="num10",font="arial 10")
sub11=Label(root,text="num11",font="arial 10")
sub12=Label(root,text="num12",font="arial 10")
sub13=Label(root,text="num13",font="arial 10")
sub14=Label(root,text="num14",font="arial 10")
sub15=Label(root,text="num15",font="arial 10")
saree1=Label(root,text="Saree Number 1",font="arial 10")
saree2=Label(root,text="Saree Number 2",font="arial 10")
saree3=Label(root,text="Saree Number 3",font="arial 10")
saree4=Label(root,text="Saree Number 4",font="arial 10")
saree5=Label(root,text="Saree Number 5",font="arial 10")
saree6=Label(root,text="Saree Number 6",font="arial 10")
saree7=Label(root,text="Saree Number 7",font="arial 10")
saree8=Label(root,text="Saree Number 8",font="arial 10")
saree9=Label(root,text="Saree Number 9",font="arial 10")
saree10=Label(root,text="Saree Number 10",font="arial 10")
saree11=Label(root,text="Saree Number 11",font="arial 10")
saree12=Label(root,text="Saree Number 12",font="arial 10")
saree13=Label(root,text="Saree Number 13",font="arial 10")
saree14=Label(root,text="Saree Number 14",font="arial 10")
saree15=Label(root,text="Saree Number 15",font="arial 10")
tot1=Label(root,text="TOTAL",font="arial 10 bold")
tot2=Label(root,text="35.48%",font="arial 10 bold")
tot3=Label(root,text="TOTAL 2",font="arial 10 bold")
tot4=Label(root,text="25% PROFIT",font="arial 10 bold")
tot5=Label(root,text="FINAL",font="arial 25 bold",foreground="red")

sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
sub4.place(x=50,y=170)
sub5.place(x=50,y=220)
sub6.place(x=50,y=270)
sub7.place(x=50,y=320)
sub8.place(x=50,y=370)
sub9.place(x=50,y=420)
sub10.place(x=50,y=470)
sub11.place(x=50,y=520)
sub12.place(x=50,y=570)
sub13.place(x=50,y=620)
sub14.place(x=50,y=670)
sub15.place(x=50,y=720)
saree1.place(x=350,y=20)
saree2.place(x=350,y=70)
saree3.place(x=350,y=120)
saree4.place(x=350,y=170)
saree5.place(x=350,y=220)
saree6.place(x=350,y=270)
saree7.place(x=350,y=320)
saree8.place(x=350,y=370)
saree9.place(x=350,y=420)
saree10.place(x=350,y=470)
saree11.place(x=350,y=520)
saree12.place(x=350,y=570)
saree13.place(x=350,y=620)
saree14.place(x=350,y=670)
saree15.place(x=350,y=720)
tot1.place(x=50,y=770)
tot2.place(x=50,y=820)
tot3.place(x=50,y=870)
tot4.place(x=50,y=920)
tot5.place(x=50,y=970)

sub1value=StringVar()
sub2value=StringVar()
sub3value=StringVar()
sub4value=StringVar()
sub5value=StringVar()
sub6value=StringVar()
sub7value=StringVar()
sub8value=StringVar()
sub9value=StringVar()
sub10value=StringVar()
sub11value=StringVar()
sub12value=StringVar()
sub13value=StringVar()
sub14value=StringVar()
sub15value=StringVar()
saree1value=StringVar()
saree2value=StringVar()
saree3value=StringVar()
saree4value=StringVar()
saree5value=StringVar()
saree6value=StringVar()
saree7value=StringVar()
saree8value=StringVar()
saree9value=StringVar()
saree10value=StringVar()
saree11value=StringVar()
saree12value=StringVar()
saree13value=StringVar()
saree14value=StringVar()
saree15value=StringVar()

sub1value=Entry(root,textvariable=sub1value,font="arial 15",width=15)
sub2value=Entry(root,textvariable=sub2value,font="arial 15",width=15)
sub3value=Entry(root,textvariable=sub3value,font="arial 15",width=15)
sub4value=Entry(root,textvariable=sub4value,font="arial 15",width=15)
sub5value=Entry(root,textvariable=sub5value,font="arial 15",width=15)
sub6value=Entry(root,textvariable=sub6value,font="arial 15",width=15)
sub7value=Entry(root,textvariable=sub7value,font="arial 15",width=15)
sub8value=Entry(root,textvariable=sub8value,font="arial 15",width=15)
sub9value=Entry(root,textvariable=sub9value,font="arial 15",width=15)
sub10value=Entry(root,textvariable=sub10value,font="arial 15",width=15)
sub11value=Entry(root,textvariable=sub11value,font="arial 15",width=15)
sub12value=Entry(root,textvariable=sub12value,font="arial 15",width=15)
sub13value=Entry(root,textvariable=sub13value,font="arial 15",width=15)
sub14value=Entry(root,textvariable=sub14value,font="arial 15",width=15)
sub15value=Entry(root,textvariable=sub15value,font="arial 15",width=15)
saree1value=Entry(root,textvariable=saree1value,font="arial 15",width=15)
saree2value=Entry(root,textvariable=saree2value,font="arial 15",width=15)
saree3value=Entry(root,textvariable=saree3value,font="arial 15",width=15)
saree4value=Entry(root,textvariable=saree4value,font="arial 15",width=15)
saree5value=Entry(root,textvariable=saree5value,font="arial 15",width=15)
saree6value=Entry(root,textvariable=saree6value,font="arial 15",width=15)
saree7value=Entry(root,textvariable=saree7value,font="arial 15",width=15)
saree8value=Entry(root,textvariable=saree8value,font="arial 15",width=15)
saree9value=Entry(root,textvariable=saree9value,font="arial 15",width=15)
saree10value=Entry(root,textvariable=saree10value,font="arial 15",width=15)
saree11value=Entry(root,textvariable=saree11value,font="arial 15",width=15)
saree12value=Entry(root,textvariable=saree12value,font="arial 15",width=15)
saree13value=Entry(root,textvariable=saree13value,font="arial 15",width=15)
saree14value=Entry(root,textvariable=saree14value,font="arial 15",width=15)
saree15value=Entry(root,textvariable=saree15value,font="arial 15",width=15)

sub1value.place(x=150,y=20)
sub2value.place(x=150,y=70)
sub3value.place(x=150,y=120)
sub4value.place(x=150,y=170)
sub5value.place(x=150,y=220)
sub6value.place(x=150,y=270)
sub7value.place(x=150,y=320)
sub8value.place(x=150,y=370)
sub9value.place(x=150,y=420)
sub10value.place(x=150,y=470)
sub11value.place(x=150,y=520)
sub12value.place(x=150,y=570)
sub13value.place(x=150,y=620)
sub14value.place(x=150,y=670)
sub15value.place(x=150,y=720)
saree1value.place(x=480,y=20)
saree2value.place(x=480,y=70)
saree3value.place(x=480,y=120)
saree4value.place(x=480,y=170)
saree5value.place(x=480,y=220)
saree6value.place(x=480,y=270)
saree7value.place(x=480,y=320)
saree8value.place(x=480,y=370)
saree9value.place(x=480,y=420)
saree10value.place(x=480,y=470)
saree11value.place(x=480,y=520)
saree12value.place(x=480,y=570)
saree13value.place(x=480,y=620)
saree14value.place(x=480,y=670)
saree15value.place(x=480,y=720)

Button(text="Calculate",font="arial 15",bg="blue",bd=10,command=Calc).place(x=400,y=900)
Button(text="Clear",font="arial 15",bg="red",bd=10,command=Clear).place(x=530,y=900)
Button(text="zero",font="arial 15",bg="white",bd=10,command=Zero).place(x=630,y=900)
Button(text="Remove",font="arial 15",bg="yellow",bd=10,command=Remove).place(x=530,y=800)
root.mainloop()