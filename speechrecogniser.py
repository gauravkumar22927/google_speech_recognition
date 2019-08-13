# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 00:56:16 2019

@author: gaura
"""
import speech_recognition as sr
r = sr.Recognizer()
while(True):
	with sr.Microphone() as source:
		print('speak Anything')
		audio = r.listen(source)
		
		try:
			text = r.recognize_google(audio)
			print('You Said: {} '.format(text))
		except:
			print('sorry nothing listened')