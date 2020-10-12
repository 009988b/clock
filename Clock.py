#!/usr/bin/python3
# Clock.py
# 3/26/2019
from tkinter import *
from math import sin,cos,pi
from datetime import *
from sys import *
class Clock(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		self.size=500
		self.title('Clock')
		self.w = Canvas(self, width=500, height=500, bg="#3b66aa")
		self.w.create_oval( 20, 20, 480, 480, outline="black", fill="white", tags="face" )
		self.w.pack()
		self.w.create_line(0,0,0,0, fill="#7f7f7f", tags="hour")
		self.w.create_line(0,0,0,0, fill="black", tags="minute")
		self.w.create_line(0,0,0,0, fill="red", tags="second")
		labels = [Label(text="12"),Label(text="3"),Label(text="6"),Label(text="9")]
		coords = [[self.size/2,50],[450,self.size/2],[self.size/2,450],[50,self.size/2]]
		for l in labels:
			idx = labels.index(l)
			l.place(x=coords[idx][0],y=coords[idx][1])
		self.clk()
	def clk(self):
		def point(ang):
			x = 250 + (175 * cos(ang))
			y = 250 - (175 * sin(ang))
			return [x,y]
		def sec_pos(): 
			s = datetime.now().second
			if s == 0:
				deg = 90
			else:
				deg = -6*s + 90
			ang = deg*pi*2/360
			return point(ang)
		def min_pos():
			m = datetime.now().minute
			if m == 0:
				deg = 90
			else:
				deg = -6*m + 90
			ang = deg*pi*2/360
			return point(ang)
		def hour_pos():
			h = datetime.now().hour
			if h >= 12:
				deg = (h - 12)*-30 + 90
			else:
				deg = -30*h+90
			ang = deg*pi*2/360
			return point(ang)
		s = sec_pos()
		m = min_pos()
		h = hour_pos()
		self.w.coords("second", (250, 250, s[0],s[1]))
		self.w.coords("minute", (250, 250, m[0],m[1]))
		self.w.coords("hour", (250, 250, h[0],h[1]))
		self.after(1000, self.clk)
app = Clock()
app.mainloop()
