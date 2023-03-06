__author__ = 'shafengfeng'
# -*- coding: utf-8 -*-
from City_info import City_info
from  Tkinter import *
import tkFont
import json
import urllib,string
import sys,os
reload(sys)
sys.setdefaultencoding( "utf-8" )
class App:
    def __init__(self,master):
        frame=[Frame() for i in range(6)]
        for i in range(6):
            frame[i]=Frame(master)
            frame[i].pack()
        self.label=Label(frame[0],text="请输入需要城市名称",fg="red",font=tkFont.Font(family="微软雅黑",size=20),width=20)
        self.label.pack(side=LEFT)
        self.text=Text(frame[1],width=50,height=20)
        self.text.pack(side=LEFT)
        self.button1=Button(frame[2],text="查询",fg="red",font=tkFont.Font(family="微软雅黑",size=20),width=20,command=self.Search)
        self.button1.pack(side=LEFT)

        self.text_1=Text(frame[3],width=50,height=20)
        self.text_1.pack(side=LEFT)



    def Search(self):
        cityname=self.text.get(1.0,END)
        cityname=str(cityname).strip()
        citycode=City_info.get(cityname)
        #print(citycode)
        #url='http://www.weather.com.cn/data/cityinfo/%s.html' %citycode
        url = 'http://m.weather.com.cn/data/%s.html'%citycode
        data=urllib.urlopen(url).read()
        print(data)
        result=json.loads(data)
        weather=result["weatherinfo"]
        #str_temp=('%s %s %s~%s\n')%(weather['city'],weather['weather'],weather['temp2'],weather['temp1'])
        str_temp=('%s %s %s %s %s %s %s %s\n\n')%(weather['city'],weather['date_y'],weather['week'],weather['temp1'],weather['weather1'],weather['wind1'],weather['index'],weather['index_d'])
        str_temp1=('%s %s %s \n%s %s %s \n%s %s %s \n')%(weather['temp2'],weather['weather2'],weather['wind2'],weather['temp3'],weather['weather3'],weather['wind3'],weather['temp4'],weather['weather4'],weather['wind4'])
        self.text_1.insert(1.0,str_temp1)
        self.text_1.insert(1.0,"未来三天的天气情况:\n")
        self.text_1.insert(1.0,str_temp)


root=Tk()
app=App(root)
root.title("天气查询系统")
root.mainloop()
