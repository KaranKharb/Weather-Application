import tkinter as tk
from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz
root=tk.Tk()
root.title("Weather Application")
root.geometry("900x500+300+200")
root.resizable(False,False)
def getWeather():
    try:
        city=textf.get()
        geoloc=Nominatim(user_agent="geoapiExcercises")
        loc=geoloc.geocode(city)
        obj=TimezoneFinder()
        res=obj.timezone_at(lng=loc.longitude, lat=loc.latitude)
        home=pytz.timezone(res)
        localtime=datetime.now(home)
        currenttime=localtime.strftime("%I:%M %P")
        clock.config(text=currenttime)
        name.config(text="CURRENT WEATHER")
        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="
        jsondata=requests.get(api).json()
        cond=jsondata['weather'][0]['main']
        description=jsondata['weather'][0]['description']
        temp=int(jsondata['main']['tem']-273.15)
        pressure=jsondata['main']['pressure']
        humidity=jsondata['main']['humidity']
        wind=jsondata['wind']['speed']
        t.config(text=(temp,"°"))
        c.config(text=(cond,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
    except EXCEPTION as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")        
    
    
searchimg=tk.PhotoImage(file="img/search.png")
myimg=tk.Label(root,image=searchimg)
myimg.place(x=20,y=20)
textf=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textf.place(x=50,y=40)
textf.focus()
sicon=tk.PhotoImage(file="img/search_icon.png")
myicon=tk.Button(image=sicon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myicon.place(x=400,y=34)
myicon.pack()

#logo
logoimg=tk.PhotoImage(file="img/logo.png")
logo=tk.Label(root,image=logoimg)
logo.place(x=150,y=100)
#bottom box
frame=tk.PhotoImage(filr="img/box.png")
frameimg=tk.Label(root,image=frame)
frameimg.pack(padx=5,pady=5,side=BOTTOM)
#time
name=tk.Label(root,font=("arial",15,"bold"))
name.place(x=30,y=130)
clock=tk.Label(root,font=("Helvetica",15,"bold"))
clock.place(x=30,y=130)
#label
label1=tk.Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)
label2=tk.Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label2.place(x=25,y=400)
label3=tk.Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)
label4=tk.Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)
t=tk.Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=tk.Label(font=("arial",15,"bold"),fg="#ee666d")
c.place(x=400,y=250)
w=tk.Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=tk.Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=tk.Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=tk.Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)
root.mainloop()