from tkinter import *
from tkinter import messagebox
import requests
import json
from tkinter import *
from tkinter import messagebox
import requests
import socket
import struct
import threading
from threading import *
import tkinter as tk
import sys
import cv2, imutils, socket
import numpy as np
import time
import base64
from PIL import Image, ImageTk
import pyaudio

from multiprocessing import Process
import tkinter.font as tkFont



def multicastingvideo():

	top = tk.Toplevel()
	top.title('channel selection')
	top.geometry("300x200")

	multicast_group ='224.0.0.1'
	mcast_port1 = 21516
	mcast_port2=9998
	mcast_port3=2011
	mcast_porta1=1010
	BUFF_SIZE = 65536
	host_name = socket.gethostname()
	host_ip =socket.gethostbyname(host_name)

	def StarsMovies():

		sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
		sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		group = socket.inet_aton(multicast_group)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		sock1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		sock1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock1.bind(('',mcast_port1))
		
		while True:
			WIDTH=1000
			HEIGHT=1000
			packet = sock1.recv(BUFF_SIZE)
			data = base64.b64decode(packet,' /')
			npdata = np.fromstring(data,dtype=np.uint8)
			frame = cv2.imdecode(npdata,1)
			
			cv2.imshow("RECEIVING VIDEO",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord('q'):
				sock1.close()
				cv2.destroyAllWindows()	
				break
			

	def Discovery():
    
		sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
		sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		group = socket.inet_aton(multicast_group)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		sock2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		sock2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock2.bind(('',mcast_port2))
		
		while True:
			WIDTH=1000
			HEIGHT=1000
			packet = sock2.recv(BUFF_SIZE)
			data = base64.b64decode(packet,' /')
			npdata = np.fromstring(data,dtype=np.uint8)
			frame = cv2.imdecode(npdata,1)
			
			cv2.imshow("RECEIVING VIDEO",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord('q'):
				sock2.close()
				cv2.destroyAllWindows()
				break
			

	def CartoonNetwork():
    
		sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
		sock3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		group = socket.inet_aton(multicast_group)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		sock3.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		sock3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock3.bind(('',mcast_port3))
		
		while True:
			WIDTH=1000
			HEIGHT=1000
			packet = sock3.recv(BUFF_SIZE)
			data = base64.b64decode(packet,' /')
			npdata = np.fromstring(data,dtype=np.uint8)
			frame = cv2.imdecode(npdata,1)
			
			cv2.imshow("RECEIVING VIDEO",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord('q'):
				sock3.close()
				cv2.destroyAllWindows()
				break
			

	fontStyle = tkFont.Font(family="Lucida Grande", size=20)
	lb = Label(top,text = "Select the channel you want to watch: ",font=fontStyle).place(x=375,y=10)
	sm = ImageTk.PhotoImage(file='smr.PNG')
	b1 = Button(top,image=sm,command = StarsMovies,activeforeground = "red",activebackground = "pink",pady=10)
	cn= ImageTk.PhotoImage(file='cartoon.PNG')
	b2 = Button(top,text = "Cartoon Network",image=cn,command=CartoonNetwork,activeforeground = "blue",activebackground = "pink",pady=10)
	dv= ImageTk.PhotoImage(file='discovery.PNG')
	b3 = Button(top,image=dv,command=Discovery,activeforeground = "green",activebackground = "pink",pady = 10)
	b1.place(x=425,y=50)
	b2.place(x=425,y=250)
	b3.place(x=425,y=450)
	top.configure(bg='red')
	top.mainloop()



def livestreaming():

		multicast_group = '224.0.0.1'
		mcast_port1 =3021
		mcast_port2=9999
		mcast_port3=2010
		mcast_porta1=1010
		BUFF_SIZE = 65536
		host_name = socket.gethostname()
		host_ip =socket.gethostbyname(host_name)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		group = socket.inet_aton(multicast_group)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		sock.bind(('',mcast_port1))
		
		while True:
			WIDTH=1000
			HEIGHT=1000
			packet = sock.recv(BUFF_SIZE)
			data = base64.b64decode(packet,' /')
			npdata = np.fromstring(data,dtype=np.uint8)
			frame = cv2.imdecode(npdata,1)
			
			cv2.imshow("RECEIVING VIDEO",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord('q'):
				sock.close()
				cv2.destroyAllWindows()	
				break
gui = Tk()
gui.title('Multicasting ')
gui.geometry("1350x700+0+0")
gui.configure(bg='black')
lbl = Label(gui,text = "select what you want to do",fg= "red").place(x=425,y=10)
lbl= ("times new roman", 100, "bold")
vms= ImageTk.PhotoImage(file='vs.PNG')
la1 = Label(gui,image=vms)
la1.pack(side=TOP, anchor=NW)
lvs1= ImageTk.PhotoImage(file='lvvs.PNG')
la2 = Label(gui,image=lvs1)
la2.place(relx = 0.0,rely = 1.0,anchor ='sw')

unn= ImageTk.PhotoImage(file='ung.PNG')
la4 = Label(gui,image=unn)                                                  
la4.pack(side=BOTTOM, anchor=SE)    
bt = Button(gui,text="video multicasting",command=multicastingvideo,font=("times new roman", 30, "bold"),activeforeground = "red",activebackground = "pink",pady=10,height=3, width=18)    
bt1 = Button(gui,text="Live videostreaming",command=livestreaming,font=("times new roman", 30, "bold"),activeforeground = "red",activebackground = "pink",pady=10,height=3, width=18)
bt.place(x=425,y=50)
bt1.place(x=425,y=200)
gui.mainloop()