# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:55:56 2018

@author: Cheng
"""
import Tkinter as tk
import numpy as np
from visual import *
from visual.graph import *
import matplotlib.pylab as plt

#h=1.9
#theta=52.5
#F=18.3
   
basket_height=3.0#籃框離地高度(m)
basket_radius=0.2#籃框半徑(m)
basket_board_height=1.05#籃板寬(m)
basket_board_width=1.8#籃板長(m)
basketball_radius=0.75/(2*np.pi)#籃球半徑(m)
field_width=2#場地寬(m)
field_length=6.4#場地長(三分線)
m=0.65#籃球質量(kg)
    
contact_length=0.15#籃框邊緣和籃板間距
E=0.85#消耗係數
k=0.47#空氣阻力常數

def animation():#動畫模擬定義
    global basket_height,basket_radius,basket_board_height,basket_board_width,basketball_radius,field_width,field_length,m,contact_length,E,k#引用定義外的常數
    
    h=float(entry1.get())#引用entry1內的數字
    theta=float(entry2.get())#引用entry2內的數字
    F=float(entry3.get())#引用entry3內的數字
    
    scene = display(width=1000,height=1000,background=(0.5,0.6,0.5))#建立一個視窗
    scene.autoscale=False
    ball=sphere(material=materials.earth,radius=basketball_radius)#建立一顆球
    board=box(length=0.01,height=basket_board_height,width=basket_board_width,material=materials.silver)#利用box建立籃板
    contact=box(length=0.15,height=0.01,width=0.05,material=materials.silver)#籃框邊緣和籃板間的板子
    basket=ring(pos=(field_length*1.25/2-basket_radius-contact_length,basket_height-basket_height/2,0), axis=(0,1,0), radius=basket_radius, thickness=0.02)#籃框位置與大小
    bottom = box(length=field_length*1.25,height=0.01,width=field_width,material=materials.silver)#利用box建立地板
        
    ball.pos=(bottom.length/2.0-field_length,-basket_height/2+h,0)#球之位置
    board.pos=(field_length*1.25/2,basket_height+0.37-basket_height/2,0)#籃板之位置
    contact.pos=(basket.pos.x+basket_radius+contact_length/2,basket.pos.y,basket.pos.z)#籃框邊緣和籃板間的板子位置
    bottom.pos = (0,-basket_height/2,0)#地板位置
    
    theta=theta*np.pi/180.0#角度單位換算
    v=F*0.3/m#出手速度
    start=vector(v*np.cos(theta),v*np.sin(theta),0)
    ball.velocity=start#球的速度方向大小
    
    grap_velocity=gdisplay(x=0,y=0,xtitle="time(s)",ytitle="velocity(m/s)", width=600, height=400,title="velocity")#建立畫圖視窗
    grap=gcurve(gdisplay=grap_velocity,color=color.red)#在指定視窗內畫線
    
    grap_total_energy=gdisplay(x=0,y=0,xtitle="time(s)",ytitle="energy(J)", width=600, height=400,title="total_energy")
    grap1=gcurve(gdisplay=grap_total_energy,color=color.red)
    
    grap_energy=gdisplay(x=0,y=0,xtitle="time(s)",ytitle="energy(J)", width=600, height=400,title="red of U energy and green of K energy")
    grap_U=gcurve(gdisplay=grap_energy,color=color.red)
    grap_K=gcurve(gdisplay=grap_energy,color=color.green)
       
    t=0
    times=0
    while (1==1):#動畫開始
        rate=100000
        dt=5*10**(-5)
        ball.velocity=ball.velocity-vector(0,9.8*dt,0)-((k*ball.velocity)*dt/m)#球之及時速度
        ball.pos=ball.pos+ball.velocity*dt#球之及時位置
        i=0
        j=0
        k=0
        while abs(ball.pos-(basket.pos-vector(basket_radius,0,0)))<basketball_radius:#擋卡牆或卡框程式
            if i==0:#碰撞籃框程式
                a=ball.velocity
                b=(basket.pos-vector(basket_radius,0,0))-ball.pos
                c=np.dot(a,b)*b/(abs(b))**2
                ball.velocity=ball.velocity-2*c*E
                i=1
            ball.velocity=ball.velocity-vector(0,9.8*dt,0)-((k*ball.velocity)*dt/m)
            ball.pos=ball.pos+ball.velocity*dt
        
        while abs(ball.pos-(basket.pos+vector(basket_radius,0,0)))<basketball_radius:#擋卡牆或卡框程式
            if j==0:#碰撞籃框程式
                a=ball.velocity
                b=(basket.pos+vector(basket_radius,0,0))-ball.pos
                c=np.dot(a,b)*b/(abs(b))**2
                ball.velocity=ball.velocity-2*c*E
                j=1
            ball.velocity=ball.velocity-vector(0,9.8*dt,0)-((k*ball.velocity)*dt/m)
            ball.pos=ball.pos+ball.velocity*dt
            
        while abs(ball.pos.y-bottom.pos.y)<basketball_radius:#擋卡牆或卡框程式
            times=times+1
            if k==0:#碰撞地板程式
                ball.velocity.y=-ball.velocity.y*E
                k=1
            ball.velocity=ball.velocity-vector(0,9.8*dt,0)-((k*ball.velocity)*dt/m)
            ball.pos=ball.pos+ball.velocity*dt
    
        while (abs(ball.pos.x-board.pos.x)<basketball_radius and abs(ball.pos.y-board.pos.y)<basket_board_height/2.0):#擋卡牆或卡框程式
            if k==0:#碰撞籃板程式
                ball.velocity.x=-ball.velocity.x*E
                k=1
            ball.velocity=ball.velocity-vector(0,9.8*dt,0)-((k*ball.velocity)*dt/m)#*(ball.velocity/abs(ball.velocity))
            ball.pos=ball.pos+ball.velocity*dt    
            
        if ball.pos.x>board.pos.x+bottom.length/5.0 or ball.pos.x<-bottom.length/2.0-bottom.length/5.0 or times==2:#彈地兩下或超出一定距離動畫重新開始
            ball.pos=(bottom.length/2.0-field_length,-basket_height/2+h,0)
            ball.velocity=start
            times=0
               
        grap.plot(pos=(t,abs(ball.velocity)))#動畫運行及時繪圖
        grap1.plot(pos=(t,m*9.8*(ball.pos.y+basket_height/2.0)+m*((abs(ball.velocity))**2)/2.0))
        grap_U.plot(pos=(t,m*9.8*(ball.pos.y+basket_height/2.0)))
        grap_K.plot(pos=(t,m*((abs(ball.velocity))**2)/2.0))
               
        t=t+dt
        

def animation_ensure():#點選動畫後之確認程式
       
    def close1():        
        try:
            window2.destroy()
        except:        
            window1.destroy()
  
    if entry1.get()!="" and entry2.get()!="" and entry3.get()!="" and float(entry1.get())>0.2:
        
        window2=tk.Tk()
        window2.title("警告")
        window2.geometry("300x200")
        label=tk.Label(window2,text="建議先點選提示觀看",font=(None,20))
        end=tk.Button(window2,text="關閉",command=close1,width=18)
        confirm=tk.Button(window2,text="仍要觀看動畫",command=animation,width=18)
        label.grid(row=1,column=1,columnspan=2,padx=5,pady=30)
        confirm.grid(row=2,column=1,columnspan=1,padx=5,pady=30)
        end.grid(row=2,column=2,columnspan=1,padx=5,pady=30)
        window1.mainloop()
    else:
        window1=tk.Tk()
        window1.title("警告")
        window1.geometry("300x200")
        label=tk.Label(window1,text="請輸入正確且完整的資訊",font=(None,15))
        end=tk.Button(window1,text="關閉",command=close1,width=25)
        label.grid(row=1,column=2,columnspan=2,padx=35,pady=30)
        end.grid(row=2,column=2,columnspan=2,padx=35,pady=30)
        window1.mainloop()

def clean():#清除entry內之內容物
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    entry3.delete(0,tk.END)
    
def f(x,h):#利用出手高度以及出手角度估算出手所需之速度
    global field_length,basket_radius,contact_length
    x=x*np.pi/180.0
    y=field_length-basket_radius-contact_length
    v=((9.8*y**2)/(2*(np.cos(x))**2)/(y*np.tan(x)-(3-h)))**0.5
    return v   

def hint():#提示按鈕程式
    global m,basket_radius
   
    def close2():
        window3.destroy()
   
    if entry1.get()!="":
        h=float(entry1.get())

        if h<=basket_radius:#球與地板距離不可小於藍球半徑
            window3=tk.Tk()
            window3.title("警告")
            window3.geometry("300x200")
            label=tk.Label(window3,text="請輸入正確的出手高度",font=(None,15))
            end=tk.Button(window3,text="關閉",command=close2,width=25)
            label.grid(row=1,column=2,columnspan=2,padx=45,pady=30)
            end.grid(row=2,column=2,columnspan=2,padx=45,pady=30)
            window3.mainloop()

        High=(3-h)+basket_radius

        try:#判斷角度有內容物有機會進球、有內容物沒機會進球和無內容物
            ang=float(entry2.get())
            if (((f(ang,h)*np.sin(ang*np.pi/180.0))**2)/2.0/9.8)>High:
                a1=0
            else:
                a1=1                
        except:
            a1=2       
        
        if a1==0:
            theta=float(entry2.get())
            s="%.2f"%(f(theta,h)*m/0.3)
            label5=tk.Label(window,text="hint:"+str(s),font=(None,15))
            label5.grid(row=5,column=4,columnspan=1)
            
            a=np.linspace(30,75,46)
            b=[]
            for i in a:
                b.append(f(i,h)*m/0.3)
                       
            plt.title("Function of scoring")
            plt.xlabel('angle(degree)')
            plt.ylabel('force(N)')
            plt.plot(a,b,"-o")
            plt.legend(loc=2)
            plt.show()
            
        elif a1==1:
            theta=float(entry2.get())
            s="%.2f"%(f(theta,h)*m/0.3)
            label5=tk.Label(window,text="無法進球",font=(None,15))
            label5.grid(row=5,column=4,columnspan=1)
            
        elif a1==2:

            label5=tk.Label(window,text="                      ",font=(None,15))
            label5.grid(row=5,column=4,columnspan=1)
            a=np.linspace(30,75,46)
            b=[]
            for i in a:
                b.append(f(i,h)*m/0.3)
                       
            plt.title("Function of scoring")
            plt.xlabel('angle(degree)')
            plt.ylabel('force(N)')
            plt.plot(a,b,"-o")
            plt.legend(loc=2)
            plt.show()            
           
    else:
       
        window3=tk.Tk()
        window3.title("警告")
        window3.geometry("300x200")
        label=tk.Label(window3,text="請輸入正確的出手高度",font=(None,15))
        end=tk.Button(window3,text="關閉",command=close2,width=25)
        label.grid(row=1,column=2,columnspan=2,padx=45,pady=30)
        end.grid(row=2,column=2,columnspan=2,padx=45,pady=30)
        window3.mainloop()
    
def close():
    window.destroy()

window=tk.Tk()
window.title("籃球投籃模擬")
start=tk.Button(window,text="動畫",command=animation_ensure,width=25)
hin=tk.Button(window,text="提示",command=hint,width=25)
picture=tk.Button(window,text="清除",command=clean,width=25)
end=tk.Button(window,text="關閉",command=close,width=25)
label1=tk.Label(window,text="籃球投籃模擬",font=(None,15))
label2=tk.Label(window,text="出手高度(m) :",font=(None,15))
label3=tk.Label(window,text="出手仰角(度) :",font=(None,15))
label4=tk.Label(window,text="出手力道(N) :",font=(None,15))
entry1=tk.Entry(window,width=43,font=(None,15))
entry2=tk.Entry(window,width=43,font=(None,15))
entry3=tk.Entry(window,width=43,font=(None,15))

label1.grid(row=2,column=1,columnspan=4,padx=5,pady=20)
label2.grid(row=3,column=1,padx=5,pady=20)
label3.grid(row=4,column=1,padx=5,pady=20)
label4.grid(row=5,column=1,padx=5,pady=20)
entry1.grid(row=3,column=2,columnspan=2)
entry2.grid(row=4,column=2,columnspan=2)
entry3.grid(row=5,column=2,columnspan=2)
start.grid(row=6,column=1,padx=5,pady=20)
hin.grid(row=6,column=2,padx=5,pady=20)
picture.grid(row=6,column=3,padx=5,pady=20)
end.grid(row=6,column=4,padx=5,pady=20)
window.mainloop()




