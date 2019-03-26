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
		twelve = Label(text="12")
		twelve.place(x=self.size/2, y=50)
		three = Label(text="3")
		three.place(x=450, y=self.size/2)
		six = Label(text="6")
		six.place(x=self.size/2, y=450)
		nine = Label(text="9")
		nine.place(x=50, y= self.size/2)
		self.clk()
	def clk(self):
		def pointX(ang):
			x = 250 + (175 * cos(ang))
			return x
		def pointY(ang):
			y = 250 - (175 * sin(ang))
			return y
		s = datetime.now().second
		if s == 0:
			sDegrees = 90
		else:
			sDegrees = -6*s + 90
		sAng = sDegrees*pi*2/360
		sx = pointX(sAng)
		sy = pointY(sAng)
		m=datetime.now().minute
		if m == 0:
			mDegrees = 90
		else:
			mDegrees = -6*m + 90
		mAng = mDegrees*pi*2/360
		mx = pointX(mAng)
		my = pointY(mAng)
		h = datetime.now().hour
		if h >= 12:
			hDegrees = 0
			hDegrees = (h - 12)*-30 + 90
		else:
			hDegrees = -30*h
		hAng = hDegrees*pi*2/360
		hx = pointX(hAng)
		hy = pointY(hAng)
		self.w.coords("hour", (250, 250, hx, hy))
		self.w.coords("minute", (250, 250, mx, my))
		self.w.coords("second", (250, 250, sx, sy))
		print(hDegrees, mDegrees, sDegrees)
		self.after(1000, self.clk)
app = Clock()
app.mainloop()
