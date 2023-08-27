import socket
import struct
import sys
import cv2, imutils, socket
import numpy as np
import time
import base64
import socket, cv2, pickle,struct,time
import pyshine as ps
import threading, wave, pyaudio, time
from multiprocessing import Process
from scipy.io import wavfile
import moviepy.editor as mp
import pygame
def livstream():
	
		multicast_group = '224.0.0.1'
		mcast_port1 = 3021
		BUFF_SIZE = 65536
		MCAST_IF_IP="192.168.56.1"
		host_name = socket.gethostname()
		host_ip =socket.gethostbyname(host_name)


  
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
		sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_IF,socket.inet_aton(multicast_group))
		vid = cv2.VideoCapture(0) 
		
		while True:
			WIDTH=600
			while(vid.isOpened()):
				_,frame = vid.read()
				frame = imutils.resize(frame,width=WIDTH)
				encoded,buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,60])
				message = base64.b64encode(buffer)
				sock.sendto(message,(multicast_group,mcast_port1))
				
				cv2.imshow('TRANSMITTING VIDEO',frame)
				key = cv2.waitKey(1) & 0xFF
				if key == ord('q'):
					sock1.close()                 
					break
			

