import socket
import struct
import sys
import cv2, imutils, socket
import numpy as np
import time
import base64
import threading, wave, pyaudio, time
from multiprocessing import Process
from scipy.io import wavfile
import moviepy.editor as mp
import pygame
import threading
from threading import *


def mstream():
	multicast_group ='224.0.0.1'
	mcast_port1=21516
	mcast_port2=9998
	mcast_port3=2011
	mcast_porta1=1010
	BUFF_SIZE=65536
	MCAST_IF_IP="192.168.56.1"
	host_name=socket.gethostname()
	host_ip=socket.gethostbyname(host_name)
	
	def Video1():
  
		sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock1.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_IF,socket.inet_aton(multicast_group))
		vid = cv2.VideoCapture("sm.mp4") 
		
		while True:
			WIDTH=600
			while(vid.isOpened()):
				_,frame = vid.read()
				frame = imutils.resize(frame,width=WIDTH)
				encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,60])
				message = base64.b64encode(buffer)
				sock1.sendto(message,(multicast_group,mcast_port1))
				cv2.imshow('TRANSMITTING VIDEO',frame)
				
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					sock1.close()                 
					break
				

	def Video2():
    
		sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock2.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_IF,socket.inet_aton(multicast_group))
		vid = cv2.VideoCapture("dvv.mp4") 
		
		while True:
			WIDTH=600
			while(vid.isOpened()):
				_,frame = vid.read()
				frame = imutils.resize(frame,width=WIDTH)
				encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,60])
				message = base64.b64encode(buffer)
				sock2.sendto(message,(multicast_group,mcast_port2))
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					sock2.close()
					break
				

	def Video3():
    
		sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock3.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_IF,socket.inet_aton(multicast_group))
		vid = cv2.VideoCapture("cn.mp4") 
		
		while True:
			WIDTH=600
			while(vid.isOpened()):
				_,frame = vid.read()
				frame = imutils.resize(frame,width=WIDTH)
				encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,60])
				message = base64.b64encode(buffer)
				sock3.sendto(message,(multicast_group,mcast_port3))
				cv2.imshow('TRANSMITTING VIDEO',frame)
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					sock3.close()
					break
				
	
	threading.Thread(target=Video1).start()
	threading.Thread(target=Video2).start()
	threading.Thread(target=Video3).start()

	

    
