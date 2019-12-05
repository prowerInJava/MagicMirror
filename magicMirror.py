import tkinter as tk
from tkinter import ttk
import os
import time
import datetime
import sys
import platform
import pickle
import random

class magicMirror:
      def __init__(self):
            self.title = "MagicMirror"
            self.weatherPng = 'png/rain.png'
            self.Mirror()
            return None
      #对dayLabel hourLabel miLabel实时显示时间
      def tick(self):
            self.t1 = ''
            localtime = time.strftime('%Y-%m-%d-%H-%M-%S')
            if localtime != self.t1:
                  timelist = localtime.split('-')
                  year = timelist[0]
                  mm = timelist[1]
                  day = timelist[2]
                  hour = timelist[3]
                  mi = timelist[4]
                  ss = timelist[5]
                  daystr = ('%s年%s月%s日'%(year,mm,day))
                  self.dayLabel.config(text = daystr)
                  self.hourLabel.config(text = hour)
                  self.miLabel.config(text = mi)
                  self.miLabel.after(1000,self.tick)
            return None
      #cityLabel 实时显示城市名称
      def get_city(self):
            self.c1 = ''
            #print(self.get_config())
            self.city = self.get_config()['city']
            
            if self.c1 != self.city:
                  self.cityLabel.config(text=self.city)
                  self.cityLabel.after(1000,self.get_city)
      #手动配置需要显示的城市，config/mycity.txt文件
      def get_config(self):
            with open(r'config/mycity.txt','r',1,'gbk') as file:
                  pcmap = {}
                  for f in file.readlines():
                        try:
                              a = f.split(":")
                              pcmap.fromkeys(a[0])
                              pcmap[a[0]] = a[1]
                        except Exception as e:
                              continue
            return pcmap
      #获取新浪写入的新闻资料，data/news.txt
      def get_sinaNews(self):
            first = ''
            with open('data/news.txt','r',1,'gbk') as file:
                  texts = file.readline()
            if texts != first:
                  a = texts.split('***')
                  self.newsLabelTime.config(text = a[0])
                  self.newsLabel.config(text = a[1])
                  #print(a)
            self.newsLabel.after(1000,self.get_sinaNews)
      #主体      
      def Mirror(self):
            self.mirror = tk.Tk()
            self.mirror.title(self.title)
            self.mirror.overrideredirect(True)
            w = self.mirror.winfo_screenwidth()
            h = self.mirror.winfo_screenheight()
            self.mirror.geometry("%dx%d"%(w,h))

            #定一个全局的黑色背景的Frame
            self.mainFrame = tk.Frame(width=w,height=h,bg = 'black').place(x=0,y=0)
            
            #显示日期
            self.dayLabel = tk.Label(self.mainFrame,text = ('%d年%d月%d日'%(2011,12,23)),
                                     font=('Times New Roman',30,'bold'),fg='darkgray',bg='black')
            self.dayLabel['height'] = 1
            self.dayLabel['width'] = 14
            self.dayLabel.place(x=20,y=20)

            #显示时间使用LCD字体DS-Digital
            self.hourLabel = tk.Label(self.mainFrame,font=('DS-Digital',100),fg='white',bg='black')
            self.sLabel = tk.Label(self.mainFrame,text=':',font=('DS-Digital',100),fg='white',bg='black')
            self.miLabel = tk.Label(self.mainFrame,font=('DS-Digital',100),fg='white',bg='black')
            self.hourLabel['height'] = 1
            self.hourLabel['width'] = 2
            self.sLabel['height'] = 1
            self.miLabel['height'] = 1
            self.miLabel['width'] = 2
            self.hourLabel.place(x=38,y=85)
            self.sLabel.place(x=168,y=85)
            self.miLabel.place(x=193,y=85)
            
            self.tick()

            #TODO 从天气信息中获取第一天的星期几信息
            #显示星期几 
            self.todayLabel = tk.Label(self.mainFrame,text = '星期五',background='black',
                                       foreground='darkgray',font=('宋体',30,'bold'))
            self.todayLabel['height'] = 1
            self.todayLabel.place(x=600,y=20)

            #显示当前配置的城市
            self.cityLabel = tk.Label(self.mainFrame,text='海门',font=('宋体',30,'bold'),fg='darkgray',bg = 'black')
            self.cityLabel['height'] = 1
            self.cityLabel.place(x=450,y=20)
            
            self.get_city()

            #TODO 获取当日天气与未来天气信息

            #新浪实时新闻显示
            self.newsLabelTime = tk.Label(self.mainFrame,text='新浪消息:10:27:37',font = ('宋体',18,'bold'),fg = 'white',bg='black')
            self.newsLabelTime.place(x=34,y=1095)
            self.newsLabel = tk.Label(self.mainFrame,text='【最高检：检察机关依法对鲁炜、莫建成、张杰辉三案提起公诉】',
                                      font = ('宋体',14,'bold'),fg = 'white',bg='black',width = 63,height=9,
                                      wraplength = 690,anchor = 'nw',justify = 'left',pady=3)
            self.newsLabel.place(x=34,y=800)
            self.get_sinaNews()

            self.mirror.mainloop()
            

magicMirror()

            
            
            
      
            
